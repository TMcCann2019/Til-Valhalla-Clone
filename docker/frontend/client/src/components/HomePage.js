import styled from 'styled-components'
import ProductContainer from './ProductContainer'

function HomePage({products}){
    return (
        <div>
            <Image />
            <h1>Welcome to Til Valhalla!</h1>
            <h2>We are on a mission to help support our veterans, first responders, and law enforcement personnel</h2>
            <ProductContainer products = {products} />
        </div>
    )
}

export default HomePage

const Image = styled.img.attrs(() => ({
    src : 'https://th.bing.com/th/id/OIP.Qb0ElUSf99DeESZ8pXqLkgAAAA?rs=1&pid=ImgDetMain',
}))`
    postion: absolute;
    z-index: 1;`