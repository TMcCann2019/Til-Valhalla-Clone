import styled from 'styled-components'

function About () {
    return(
        <div>
            <Image />
            <h1>About Til Valhalla!</h1>
            <h2>“We do not seek peace in order to be at war, but we go to war that we may have peace. Be peaceful, therefore, in warring, so that you may vanquish those whom you war against, and bring them to the prosperity of peace.– St. Augustine</h2>
            <h4>This project is just a tribute to the Til Valhalla Project website that has a larger and more robust mission than just selling apparel. If you are interested in helping out and supporting this cause check out their website at https://tilvalhallaproject.com/ </h4>
        </div>
    )
}

export default About

const Image = styled.img.attrs(() => ({
    src : 'https://wallpaperaccess.com/full/303000.jpg',
}))`
    postion: absolute;
    z-index: 1;`