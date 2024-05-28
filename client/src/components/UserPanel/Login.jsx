import { useState } from 'react'
import {useOutletContext} from 'react-router-dom'

function Login() {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const {setCurrentUser} = useOutletContext()

  // SUBMIT EVENT

  function handleSubmit(e) {
    e.preventDefault()

    fetch('/api/login', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json', 
        'Accept': 'application/json' 
      },
      body: JSON.stringify({username, password})
    }).then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      } else {
        alert('Invalid username or password')
      }
    })
  }

  // RENDER //

  return (

    <div className ="window" style={{width: 300}}>
  <div className="title-bar">
    <div className="title-bar-text">Login</div>
    <div className="title-bar-controls">
      <button aria-label="Minimize"></button>
      <button aria-label="Maximize"></button>
      <button aria-label="Close"></button>
    </div>
  </div>
  <div class="window-body">

    <form className='user-form' onSubmit={handleSubmit}>

      <h4>Login</h4>

      <input type="text"
      onChange={e => setUsername(e.target.value)}
      value={username}
      placeholder='username'
      />

      <input type="text"
      onChange={e => setPassword(e.target.value)}
      value={password}
      placeholder='password'
      />

      <input type="submit"
      value='Login'
      />

    </form>

    </div>

    </div>
  )

}

export default Login
