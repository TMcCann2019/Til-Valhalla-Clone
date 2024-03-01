import styled from 'styled-components'

function HomePage(){
    return (
        <div>
            <Image />
            <h1>Welcome to Til Valhalla!</h1>
            <h2>We are on a mission to help support our veterans, first responders, and law enforcement personnel</h2>
            <h2>Sign In or Sign Up to peruse our products that we offer! If you can't find a product you want, let us know and we can add it into our catalogue!</h2>
        </div>
    )
}

export default HomePage

const Image = styled.img.attrs(() => ({
    src : 'https://th.bing.com/th/id/OIP.Qb0ElUSf99DeESZ8pXqLkgAAAA?rs=1&pid=ImgDetMain',
}))`
    postion: absolute;
    z-index: 1;`