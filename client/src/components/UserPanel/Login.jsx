import { useState } from 'react'

function Login({ setCurrentUser }) {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

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


  <div className="window" style={{width: 300 }}>
  <div className="title-bar">
    <div className="title-bar-text">Login</div>
    <div className="title-bar-controls">
          <button aria-label="Minimize" />
          <button aria-label="Maximize" />
          <button aria-label="Close" />
      </div>
  </div>
  <div className="window-body">

    <form className='user-form' onSubmit={handleSubmit}>

      <h2>Login</h2>

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