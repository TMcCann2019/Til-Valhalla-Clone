import  {useParams, useHistory } from 'react-router-dom'
import {useEffect, useState} from 'react'
import styled from 'styled-components'

function ProductDetail({deleteProduct, productEdit}) {
  const [product, setProduct] = useState()
  const [error, setError] = useState(null)
  
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
      <button >Buy</button>
      <button onClick={() => deleteProduct(product)}>Delete</button>
      <button onClick={() => productEdit(product)}>Edit</button>
      </CardDetail>
    )
  }
  
  export default ProductDetail
  const CardDetail = styled.li`
    display:flex;
    flex-direction:column;
    justify-content:start;
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