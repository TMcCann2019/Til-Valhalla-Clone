import styled from 'styled-components'
import ProductCard from './ProductCard'


function ProductContainer({products}) {

    return (
     <div>
         <Title>Til Valhalla</Title>
         <CardContainer>
             {products.map(product => <ProductCard  key={product.id} product={product}  />)}
         </CardContainer>
     </div>
    )
  }
  
export default ProductContainer

const Title = styled.h1`
    text-transform: uppercase;
    font-family:Arial, sans-serif;
    width:70px;
    font-size: 70px;
    line-height: .8;
    transform: scale(.7, 1.4);
`


const CardContainer = styled.ul`
    display:flex;
    flex-direction:column;
`