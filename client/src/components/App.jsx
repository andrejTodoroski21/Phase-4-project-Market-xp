import { Outlet } from 'react-router-dom'
import React from 'react'
import Navbar from '../Navbar.jsx'

function App() {

  return (
    <div className='App'>
      <Navbar />
      <h3>"Website Title"</h3>

      <div>
        <Outlet />
      </div>

    </div>
  )

}

export default App
