import React from 'react'
import { useState} from 'react'
import {useNavigate} from 'react-router-dom'
import {ACCESS_TOKEN, REFRESH_TOKEN} from '../constants'
import "../styles/form.css"

const Form = ({route , method}) => {
    const navigate = useNavigate()
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [Loading, setLoading] = useState(false) 
    const handleSubmit = async (e) => {
        setLoading(true)
        e.preventDefault()
        try{
            const res = await api.post(route , {username , password} )
            if(method == 'login'){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
                navigate('/')
               } else{
                navigate('/login')
               }}catch(error) {
                alert(error)
               }finally{
                setLoading(false)
               }
    }
  return (
    <div>
    <form onSubmit={handleSubmit} className="form-container">
        <h1>{method == 'login' ? 'Login' : 'Register'} </h1>
        <input type="text" className='form-input' value={username} onChange={(e) => setUsername(e.target.value)} placeholder='Enter Username' />
        <input type="password" className='form-input' value={password} onChange={(e) => setPassword(e.target.value)} placeholder='Enter Password' />
        <button className='form-button' type='submit'>{method == 'login' ? 'Login' : 'Register'}</button>

    </form>
    </div>
  )
  } 
export default Form
