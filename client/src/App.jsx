import { useState } from 'react'
import './App.css'

function App() {
  const [loginEmail, setLoginEmail] = useState('')
  const [loginPassword, setLoginPassword] = useState('')

  const [registerEmail, setRegisterEmail] = useState('')
  const [registerPassword, setRegisterPassword] = useState('')

  const [username, setUsername] = useState('')
  const [location, setLocation] = useState('')

  async function handleLogin() {
    const response = await fetch('http://127.0.0.1:5000/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: loginEmail,
        password: loginPassword
      })
    })

    const data = await response.json()

    if (response.ok) {
      // Login was successful
      console.log('Logged in:', data)
    } else {
      // Something went wrong
      console.log('Error:', data)
    }
  }

  async function handleRegister() {
    const response = await fetch('http://127.0.0.1:5000/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: registerEmail,
        password: registerPassword,
        username: username,
        location_id: location
      })
    })

    const data = await response.json()

    if (response.ok) {
      // Login was successful
      console.log('Logged in:', data)
    } else {
      // Something went wrong
      console.log('Error:', data)
    }
  }
  
  return (
    <>
      <div className="container">
        <div className="login-fields">
          <label htmlFor="" className="login-email">Email: </label>
          <input type="text" value={loginEmail} onChange={(e) => setLoginEmail(e.target.value)} />
          <br></br>
          <label htmlFor="" className="password-login">Password: </label>
          <input type="text" value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)} />
          <button onClick={handleLogin}>Login</button>
        </div>
        <div className="register-fields">
          <label htmlFor="" className="register-email">Email: </label>
          <input type="text" value={registerEmail} onChange={(e) => setRegisterEmail(e.target.value)} />
          <br />
          <label htmlFor="" className="register-username">Username: </label>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
          <br></br>
          <label htmlFor="" className="register-location">Location: </label>
          <input type="text" value={location} onChange={(e) => setLocation(e.target.value)} />
          <br></br>
          <label htmlFor="" className="register-password">Password: </label>
          <input type="text" value={registerPassword} onChange={(e) => setRegisterPassword(e.target.value)} />
          <button onClick={handleRegister}>Register</button>
        </div>
      </div>
    </>
  )
}

export default App
