import { Link, useOutletContext } from 'react-router-dom'

function Home () {
    const{currentUser} =useOutletContext()
    return (
        <>
            <img src='' />
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
