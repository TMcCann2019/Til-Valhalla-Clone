import { Route, Switch, useHistory } from 'react-router-dom'
import {useEffect, useState} from 'react'
import {createGlobalStyle} from 'styled-components'
import Navigation from './Navigation'
import HomePage from './HomePage'
import About from './About'
import ProductDetail from './ProductDetails'
import ShoppingCart from './ShoppingCart'
import Authentication from './Authentication'
import NotFound from './NotFound'
import ProductForm from './ProductForm'

function App() {
  const [productEdit, setProductEdit] = useState([])
  const [products, setProducts] = useState([])
  const [user, setUser] = useState(null)
  const history = useHistory()

  useEffect(() => {
    fetchUser()
    fetchProducts()
  }, [])

  const fetchProducts = () => (
    fetch('/products')
    .then(resp => resp.json())
    .then(setProducts)
  )

  const fetchUser = () => {
    fetch('/users')
    .then (resp => {
      if (resp.ok){
        resp.json().then(setUser)
      } else {
        setUser(null)
      }
    })
  }
  
  const updateProduct = (updated_product) => setProducts(products => products.map(product => product.id == updated_product.id ? updated_product : product))
  const deleteProduct = (deleted_product) => setProducts(products => products.filter((product) => product.id !== deleted_product.id))
  const addProduct = (product) => setProducts(current => [...current,product])
  const handleEdit = (product) => {
    setProductEdit(product)
    history.push('/cart')
  }

  const updateUser = (user) => setUser(user)

  if (!user) return (
    <>
      <GlobalStyle />
      <Navigation />
      <Authentication updateUser={updateUser}/>
    </>
  )

  return (
    <>
    <GlobalStyle />
    <Navigation updateUser={updateUser} />
      <Switch>
        <Route exact path='/authentication'>
          <Authentication updateUser={updateUser}/>
        </Route>
        <Route exact path='/about'>
          <About />
        </Route>
        <Route path = '/cart' updateProduct = {updateProduct} productEdit = {handleEdit} deleteProduct = {deleteProduct}>
          <ShoppingCart />
        </Route>
        <Route path='/products'>
          <ProductDetail deleteProduct = {deleteProduct} productEdit = {handleEdit}/>
        </Route>
        <Route path = '/products/new'>
          <ProductForm addProduct = {addProduct} />
        </Route>
        <Route exact path='/'>
          <HomePage />
        </Route>
        <Route>
          <NotFound />
        </Route>
      </Switch>
    </>
  )
}

export default App;

const GlobalStyle = createGlobalStyle`
    body{
      background-color: black; 
      color:white;
    }
    `