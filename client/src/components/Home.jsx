import { Link, useOutletContext } from 'react-router-dom'
import myComputer from '../assets/High-Res_XP_Icons/My Computer.ico'
import myProfile from '../assets/High-Res_XP_Icons/My Profile Folder.ico'
import aboutIcon from '../assets/High-Res_XP_Icons/Internet Properties.ico'

function Home () {
    const{currentUser} =useOutletContext()
    return (
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
    )
}

export default Home
