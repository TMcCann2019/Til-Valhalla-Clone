import React, {useState} from 'react'
import {useHistory} from 'react-router-dom'
import styled from "styled-components";
import { useFormik } from "formik"
import * as yup from "yup"

function Authentication({updateUser}) {
    const [signUp, setSignUp] = useState(false)
    const history = useHistory()

    const handleClick = () => setSignUp((signUp) => !signUp)
        const formSchema = yup.object.shape({
            username: yup.string().required("Username is required"),
            email: yup.string().required("Email is required"),
            password: yup.string().required("<PASSWORD>")
        })
    
    const formik = useFormik({
        initialValues: {
            username: "",
            email: "",
            password: ""
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            fetch(signUp ? '/signup' : '/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values, null, 2)
            })
            .then((resp) => {
                if (resp.ok){
                    resp.json().then(user => {
                        updateUser(user)
                        history.push('/')
                    })
                } else {
                    updateUser(null)
                    history.push('/authentication')
                }
            })        
        }
    })

    return (
        <>
        {formik.errors && Object.values(formik.errors).map((error) => <h2 style = {{color: 'red'}}>{error}</h2>)}
        <h2>Please Log in or Sign Up!</h2>
        <h2>{signUp?'Already a member?' : 'Not a member?'}</h2>
        <button onClick={handleClick}>{signUp?'Log In!' : 'Register now!'}</button>
        <Form onSubmit={formik.handleSubmit}>
            <label>
                Username:
                <input type="text" name="username" value={formik.values.username} onChange={formik.handleChange} />
            </label>
            <label>
                Password:
                <input type="password" name="password" value={formik.values.password} onChange={formik.handleChange} />
                {signUp && (
                    <>
                    <label>
                        Email
                        <input type="text" name="email" value={formik.values.email} onChange={formik.handleChange} />
                    </label>
                    </>
                )}
            </label>
            <input type = 'submit' value={signUp ? 'Sign Up!' : 'Log In!'} />
        </Form>
        </>
    )
}

export default Authentication

export const Form = styled.form`
display:flex;
flex-direction:column;
width: 400px;
margin:auto;
font-family:Arial;
font-size:30px;
input[type=submit]{
  background-color:#42ddf5;
  color: white;
  height:40px;
  font-family:Arial;
  font-size:30px;
  margin-top:10px;
  margin-bottom:10px;
}
`