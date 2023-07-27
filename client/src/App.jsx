import { useState } from 'react';
import './App.css'

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  async function handleLogin() {
    const response = await fetch('http://127.0.0.1:5000/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    });

    const data = await response.json();

    if (response.ok) {
      // Login was successful
      console.log('Logged in:', data);
    } else {
      // Something went wrong
      console.log('Error:', data);
    }
  }
  
  return (
    <>
      <div className="container">
        <div className="login-fields">
          <label htmlFor="" className="login-email">Email: </label>
          <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
          <br></br>
          <label htmlFor="" className="password-login">Password: </label>
          <input type="text" value={password} onChange={(e) => setPassword(e.target.value)} />
          <button onClick={handleLogin}>Login</button>
        </div>
      </div>
    </>
  )
}

export default App;
