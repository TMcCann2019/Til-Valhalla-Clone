import { useState, useEffect } from 'react'
import {Link} from 'react-router-dom'
import styled from 'styled-components'
import { useHistory } from 'react-router-dom'
import { GiHamburgerMenu } from 'react-icons/gi'

function Navigation({updateUser}) {
  const [menu, setMenu] = useState(false)
  const history = useHistory()
  const [cartItemsCount, setCartItemsCount] = useState(0)

  useEffect(() => {
    fetchUserData()
  }, [])

  const fetchUserData = () => {
    fetch('/authorized')
    .then(resp => {
      if (resp.ok){
        resp.json().then(user => {
          updateUser(user)
          if (user.orders && user.order.length > 0){
            const cart = user.orders.find(order => order.status === 'In Cart')
            if (cart){
              setCartItemsCount(cart.order_items.length)
            }
          }
        })
      } else {
        updateUser(null)
        setCartItemsCount(0)
      }
    })
  }
  
  const handleLogout = () => {
    fetch("/logout", {
      method: "DELETE",
      }).then(res => {
        if(res.ok){
          updateUser(null)
          history.push('/authentication')
        }
      })
  }

    return (
      <Nav> 
        <NavH1>Til Valhalla</NavH1>
        <Menu>
          {!menu?
          <div onClick={() => setMenu(!menu)}>
            <GiHamburgerMenu size={30}/> 
          </div>:
          <ul>
            <li onClick={() => setMenu(!menu)}>x</li>
            <li><Link to='/'> Home</Link></li>
            <li><Link to= '/about'>About</Link></li>
            <li><Link to='/cart'> Cart ({cartItemsCount})</Link></li>
            <li><Link to='/products'> New Product</Link></li>
            <li><Link to='/authentication'> Login/Signup</Link></li>
            <li onClick={handleLogout}> Logout </li>
          </ul>
          }
        </Menu>
      </Nav>
    )
}

export default Navigation

const NavH1 = styled.h1`
font-family: 'Splash', cursive;
`
const Nav = styled.div`
  display: flex;
  justify-content:space-between;
`;

const Menu = styled.div`
  display: flex;
  align-items: center;
  a{
    text-decoration: none;
    color:white;
    font-family:Arial;
  }
  a:hover{
    color:green
  }
  ul{
    list-style:none;
  }
`;