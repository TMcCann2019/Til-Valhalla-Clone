import { Route, Switch, useHistory } from 'react-router-dom'
import {useEffect, useState} from 'react'
import {createGlobalStyle} from 'styled-components'
import Navigation from './Navigation'
import HomePage from './HomePage'
import About from './About'
import ProductDetail from './ProductDetails'
import ProductForm from './ProductForm'
import Authentication from './Authentication'
import NotFound from './NotFound'
import Cart from './Cart'

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

  const fetchUser = () => (
    fetch('/authorized')
    .then(resp => {
      if (resp.ok){
        resp.json()
        .then(data => {
          setUser(data)
        })
      } else {
        setUser(null)
      }
    })
  )

  function handleDelete (product) {
    fetch(`/products/${product.id}`, {
      method: 'DELETE',
    }).then(resp => {
      if(resp.ok){
        deleteProduct(product)
        history.push('/')
      }
    })
  }

  function addProductToCart(product){
    fetch(`/cart`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(product, null, 2)
    }).then(resp => {
      if(resp.ok){
        resp.json().then(product => {
          addProduct(product)
          history.push(`/products/${product.id}`)
        })
      }
    })
  }
  
  const updateProduct = (updated_product) => setProducts(products => products.map(product => product.id == updated_product.id ? updated_product : product))
  const deleteProduct = (deleted_product) => setProducts(products => products.filter((product) => product.id !== deleted_product.id))
  const addProduct = (product) => setProducts(current => [...current,product])
  const handleEdit = (product) => {
    setProductEdit(product)
    history.push(`/products/edit/${product.id}`)
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
        <Route path='/products/edit/:id'>
          <ProductForm updateProduct = {updateProduct} editProduct = {productEdit} />
        </Route>
        <Route path='/products/:id'>
          <ProductDetail deleteProduct = {deleteProduct} onHandleDelete = {handleDelete} productUpdate = {handleEdit} addProductToCart={addProductToCart}/>
        </Route>
        <Route path = '/products'>
          <ProductForm addProduct = {addProduct} />
        </Route>
        <Route exact path='/'>
          <HomePage products = {products}/>
        </Route>
        <Route>
          <Cart />
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
      color:green;
    }
    `