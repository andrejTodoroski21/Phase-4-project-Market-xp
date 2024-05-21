import { Link } from 'react-router-dom'

function Navbar () {

    return (
        <div>
            <Link className='navbar' to="/">Home</Link>
            &nbsp; &nbsp;
            <Link className='navbar' to="/listings">Listings</Link>
            &nbsp; &nbsp;
            <Link className='navbar' to="/profile">Profile</Link>
            &nbsp; &nbsp;
            <Link className='navbar' to="/about">About</Link>
            
        </div>
    )
}

export default Navbar