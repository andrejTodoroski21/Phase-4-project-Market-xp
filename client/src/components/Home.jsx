import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import UserPanel from './UserPanel'


function Home () {

    const [currentUser, setCurrentUser] = useState(null)


  // EFFECTS //

  useEffect(() => {
    fetch('/api/check-session')
    .then(response => {
      if (response.status === 200) {
        response.json()
        .then(loggedInUser => setCurrentUser(loggedInUser))
      }
    })
  }, [])

    
    return (
        <>
            <h2>Welcome to our website</h2>

            <br/>
            <br/>

            <h3 id="site-directory">Site Directory:</h3>
            <Link to="/listings"><h3>Current Listings</h3></Link>
                <div>
                    <p>**This p-tag text is currently inside a div that will display the top-5 recent listings</p>
                </div>
            
            <br/>

            <Link to="/profile"><h3>Profile</h3></Link>
                <div>
                    <p>this p tag lives inside a div that will show a preview of the user's profile?</p>
                </div>

            <br/>

            <Link to="/about"><h3>About</h3></Link>
                <div>
                    <p>inside div with preview of about section? ...or maybe we just keep this as a link</p>
                </div>
        </>
    )
}

export default Home