import { Link, useOutletContext } from 'react-router-dom'
import myComputer from '../assets/High-Res_XP_Icons/My Computer.ico'
import myProfile from '../assets/High-Res_XP_Icons/My Profile Folder.ico'
import aboutIcon from '../assets/High-Res_XP_Icons/Internet Properties.ico'

function Home () {
    const{currentUser} =useOutletContext()
    const{setCurrentUser} =useOutletContext()

    function handleLogout() {
        setCurrentUser(null)
        fetch('/api/logout', { method: 'DELETE' })
    }

    return (

    <div>
        <div className='icon-container'>
            <Link to="/listings"><img className='app-icon' src={myComputer} /></Link>
            <p className='icon-text'>Listings</p>
        
            <br/>

            <Link to="/profile"><img className='app-icon' src={myProfile} /></Link>
            <p className='icon-text'>My Profile</p>

            <br/>

            <Link to="/about"><img className='app-icon' src={aboutIcon} /></Link>
            <p className='icon-text' >About</p>
        </div>
            <div style={{marginLeft:'70px'}}>
                <div style={{width: '30%'}} id="title-window" className="window">
                    <div style={{height: '30px'}} class="title-bar">
                    <h3 style={{color: 'white'}}>Welcome, {currentUser ? currentUser.username : 'Guest'}!</h3>

                    <div class="title-bar-controls">
                        <button aria-label="Minimize"></button>
                        <button aria-label="Maximize"></button>
                        <button aria-label="Close"></button>
                    </div>

                    </div>

                <div class="window-body">
                    <p>Enjoy browsing, selling, and discussing your old crap!</p>
                    {currentUser && <button onClick={handleLogout}>Logout</button>}
                </div>
                
                </div>
        </div>
    </div>
    )
}

export default Home
