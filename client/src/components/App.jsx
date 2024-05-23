import { Outlet } from 'react-router-dom'
import React, {useState, useEffect} from 'react'
import Navbar from '../Navbar.jsx'
import icon from '../assets/icon-revised.png'

function App() {

  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className='App'>
      <Navbar />
      <h3>"Website Title"</h3>

      <div>
        <Outlet />
      </div>

      <div className="start-menu-bar">
        <img height='31px' src={icon}/>
      </div>
      <div className="right-taskbar">
        <div className="clock">
          {currentTime.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' })}
        </div>
      </div>
    </div>
  )

}

export default App
