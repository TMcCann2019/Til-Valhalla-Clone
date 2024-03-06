import  {useParams, useHistory } from 'react-router-dom'
import {useEffect, useState} from 'react'
import styled from 'styled-components'

function ProductDetail({deleteProduct, productUpdate, onHandleDelete, addProductToCart}) {
  const [product, setProduct] = useState({order_items:[]})
  const [error, setError] = useState(null)
  const [showBuyForm, setShowBuyForm] = useState(false)
  const [quantity, setQuantity] = useState(1)
  const [subtotal, setSubtotal] = useState(0)
  
  const params = useParams()
  const history = useHistory()
  useEffect(()=>{
    fetch(`/products/${params.id}`)
    .then(res => { 
      if(res.ok){
        res.json().then(data => setProduct(data))
      } else {
        res.json().then(data => setError(data.error))
      }
    })
  },[])
  
  const {id, name, description, image, price, size, color} = product
  if(error) return <h2>{error}</h2>

  const handleBuyClick = () => {
    setShowBuyForm(true);
    setSubtotal(price * quantity)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    addProductToCart({...product, quantity})
    setShowBuyForm(false)
  }

  const handleQuantityChange = (e) => {
    const newQuantity = parseInt(e.target.value)
    setQuantity(newQuantity)
    setSubtotal(price * newQuantity)
  }

  return (
      <CardDetail id={id}>
        <h1>{name}</h1>
          <div className='wrapper'>
            <div>
              <h3>Description:</h3>
              <p>{description}</p>
              <h3>Price:</h3>
              <p>{price}</p>
              <h3>Size:</h3>
              <p>{size}</p>
              <h3>Color:</h3>
              <p>{color}</p>
            </div>
            <img src={image} alt = {name}/>
          </div>
          {showBuyForm ? (
            <form onSubmit = {handleSubmit}>
              <label>
                Quantity:
                <input type="number" value={quantity} onChange={handleQuantityChange} />
              </label>
              <p>Subtotal: {subtotal}</p>
              <button type="submit">Add to Cart</button>
            </form>
          ) : (<button onClick= {handleBuyClick}>Buy</button>)
          }
      <button onClick={() => productUpdate(product)}>Edit</button>
      <button onClick={() => onHandleDelete(product)}>Delete</button>
      </CardDetail>
    )
  }
  
  export default ProductDetail
  
  const CardDetail = styled.li`
    display:flex;
    flex-direction:column;
    justify-content:center;
    font-family:Arial, sans-serif;
    margin:5px;
    h1{
      font-size:30px;
      border-bottom:solid;
      border-color:#42ddf5;
    }
    .wrapper{
      display:flex;
      div{
        margin:10px;
      }
    }
    img{
      width: 300px;
    }
    button{
      background-color:#42ddf5;
      color: white;
      height:40px;
      font-family:Arial;
      font-size:30px;
      margin-top:10px;
    }
  `