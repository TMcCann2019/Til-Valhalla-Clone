import { Route, Switch, useHistory } from 'react-router-dom'
import {useEffect, useState} from 'react'
import Navigation from './components/navigation'
import HomePage from './components/HomePage'
import About from './components/About'
import Products from './components/Products'
import ShoppingCart from './components/ShoppingCart'
import Authentication from './components/Authentication'
import NotFound from './components/NotFound'

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
      <Navigation />
      <Authentication updateUser={updateUser}/>
    </>
  )

  return (
    <>
    <Navigation updateUser={updateUser}  handleEdit={handleEdit}/>
      <Switch>
        <Route exact path='/authentication'>
          <Authentication updateUser={updateUser}/>
        </Route>
        <Route exact path='/about'>
          <About />
        </Route>
        <Route exact path = '/cart' updateProduct = {updateProduct} productEdit = {productEdit} deleteProduct = {deleteProduct}>
          <ShoppingCart />
        </Route>
        <Route exact path='/products'>
          <Products products={products} addProduct = {addProduct}/>
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
