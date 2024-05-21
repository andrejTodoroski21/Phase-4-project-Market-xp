import { Outlet } from 'react-router-dom'
import React from 'react'
import Navbar from '../Navbar.jsx'

function App() {

  return (
    <div className='App'>
      <Navbar />
      <h1>"Website Title"</h1>

      <div>
        <Outlet />
      </div>

    </div>
  )

}

export default App
