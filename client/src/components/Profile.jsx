
function Profile() {
    return (
        <>
            <br></br>
            <br></br>
            <div style={{marginLeft: '30px'}}>
                    <div style={{width: '30%'}} id="title-window" className="window">
                    <div style={{height: '30px'}} className="title-bar">
                    <h3 class="title-bar-text">Profile</h3>

                    <div class="title-bar-controls">
                        <button aria-label="Minimize"></button>
                        <button aria-label="Maximize"></button>
                        <button aria-label="Close"></button>
                    </div>

                    </div>
                    <div class="window-body">
                        <p>Your listings</p>
                        <p>Your Orders</p>
                    </div>

                </div>
            </div>
        </>
    )
}

export default Profile