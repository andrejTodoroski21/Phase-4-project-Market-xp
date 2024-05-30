import { Outlet } from 'react-router-dom'
import React, {useState, useEffect} from 'react'
import Navbar from '../Navbar.jsx'
import icon from '../assets/icon-revised.png'

function App() {

  // STATE //

  const [currentUser, setCurrentUser] = useState(null);
  const [currentTime, setCurrentTime] = useState(new Date());

  // FETCH SESSION FOR LOGIN

  useEffect(() => {
    fetch('/api/get-session')
    .then(response => {
      if (response.status === 200) {
        response.json()
        .then(loggedInUser => setCurrentUser(loggedInUser))
      }
    })
  }, []);

  // SET DATE USE EFFECT 

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className='App'>
      <span className='header'>
        <div style={{width: '30%'}} id="title-window" className="window">
            <div style={{height: '30px'}} class="title-bar">
            <h3 class="title-bar-text">Market XP</h3>

              <div class="title-bar-controls">
                <button aria-label="Minimize"></button>
                <button aria-label="Maximize"></button>
                <button aria-label="Close"></button>
              </div>

            </div>

          <div class="window-body">
            <Navbar />
          </div>
          
        </div>
        </span>
      <div>
        <Outlet context={{currentUser, setCurrentUser}}/>
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
