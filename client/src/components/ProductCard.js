import {Link} from 'react-router-dom'
import styled from 'styled-components'


function ProductCard({product}) {
    const {id, name, description, image, price, size, color} = product

    return (
      <Card id={id}>
        <Link to={`/products/${id}`}> 
          <div>
            <h2>{name}</h2>
            <p>$ {price}</p>
            <p>{size}</p>
            <p>{color}</p>
            <p>{description}</p>
          </div>
          <img src={image} alt = {name}/>
        </Link>
      </Card>
     
    )
  }
  
  export default ProductCard


  const Card = styled.li`
    display:flex;
    flex-direction:row;
    justify-content:start;
    font-family:Arial, sans-serif;
    margin:5px;
    &:hover {
      transform: scale(1.15);
      transform-origin: top left;
    }
    a{
      text-decoration:none;
      color:red;
    }
    img{
      width: 180px;
      margin-left:50%;
      mask-image: linear-gradient(to left, rgba(0, 0, 0, .9) 80%, transparent 100%);
    }
    position:relative;
    div{
     position:float-left;
    }
  `