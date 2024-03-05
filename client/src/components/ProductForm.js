import React, {useState} from 'react'
import styled from 'styled-components'
import { useHistory } from 'react-router-dom'
import { useFormik } from "formik"
import * as yup from "yup"

function ProductForm({addProduct, updateProduct, editProduct }) {
  const history = useHistory()
  const formSchema = yup.object().shape({
    name: yup.string().required("Must enter a name"),
    description: yup.string().required("Must enter a description"),
    image: yup.string().required("Must enter an image"),
    price: yup.number().positive().required("Must enter a price"),
    size: yup.string().required("Must enter a size"),
    color: yup.string().required("Must enter a color"),
  })

  const editForm = !!editProduct

  const editValues = {
      description: editProduct.description,
      image: editProduct.image,
      price: editProduct.price,
      size: editProduct.size,
      color: editProduct.color,
  }

  const addValues = {
      name: '',
      description: '',
      image: '',
      price: '',
      size: '',
      color: '',
  }

  const formik = useFormik({
    initialValues: editForm ? editValues : addValues,
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch(editForm ? `/products/${editProduct.id}` : "/products", {
        method: editForm ? "PATCH" : "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then((res) => {
        if(res.ok) {
          res.json().then(product => {
            editForm ? updateProduct(product) : addProduct(product)
            history.push(`/products/${product.id}`)
          })
        }
      })
    },
  })

    return (
      <div className='App'>

      <Form onSubmit={formik.handleSubmit}>
        {editForm ? null : <label>Name: </label>}
        {editForm ? null : <input type='text' name='name' value={formik.values.name} onChange={formik.handleChange} />}
        
        <label>Description: </label>
        <textarea type='text' rows='4' cols='30' name='description' value={formik.values.description} onChange={formik.handleChange} />
      
        <label>Price: </label>
        <input type='number' name='price' value={formik.values.price} onChange={formik.handleChange} />
      
        <label>Image: </label>
        <input type='text' name='image' value={formik.values.image} onChange={formik.handleChange} />
      
        <label>Size: </label>
        <input type='text' name='size' value={formik.values.size} onChange={formik.handleChange} />
      
        <label>Color: </label>
        <input type='text' name='color' value={formik.values.color} onChange={formik.handleChange} />
      
        <input type='submit' />
        {console.log(formik.handleSubmit)}
      </Form> 
      </div>
    )
  }
  
  export default ProductForm

  const Form = styled.form`
    display:flex;
    flex-direction:column;
    width: 400px;
    margin:auto;
    font-family:Arial;
    font-size:30px;
    input[type=submit]{
      background-color:blue;
      color: white;
      height:40px;
      font-family:Arial;
      font-size:30px;
      margin-top:10px;
      margin-bottom:10px;
    }
  `