import { Outlet } from 'react-router-dom'
import React from 'react'
import Navbar from '../Navbar.jsx'
import icon from '../assets/starticon.png'

function App() {

  return (
    <div className='App'>
      <Navbar />
      <h3>"Website Title"</h3>

      <div>
        <Outlet />
      </div>

      <div className="start-menu-bar">
        <img height='30px' src={icon}/>
      </div>
    </div>
  )

}

export default App
