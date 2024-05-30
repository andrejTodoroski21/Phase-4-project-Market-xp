import React, {useEffect, useState} from "react";
import { Link, useOutletContext } from 'react-router-dom'
function Profile() {

    const{currentUser}=useOutletContext()
    const {setCurrentUser}=useOutletContext()

    const [items, setItems] = useState([]);
    const [cart, setCart] = useState([]);

    useEffect(() => {
      fetch('/api/get-session')
      .then(response => {
        if (response.status === 200) {
          response.json()
          .then(loggedInUser => setCurrentUser(loggedInUser))
        }
      })
    }, []);

    useEffect(() => {
        fetch('/api/items')
            .then(res => res.json())
            .then(data => setItems(data));
    }, []);

    useEffect(() => {
      fetch('/api/cart')
          .then(res => res.json())
          .then(data => setCart(data));
  }, []);

  console.log(cart)

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
    <div>
      <br />
      {currentUser && (
          <div>
            <h3>My Listings:</h3>
            {items
              .filter(items => items.seller_id === currentUser.id) 
              .map(item => (
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
                  <div className="my-listing">
                    <h4>{item.item_name}</h4>
                    <img width='250px' src={item.item_img} alt={item.item_name} />
                    <h5>{item.description}</h5>
                    <p>{item.category}</p>
                  </div>
                  <br></br>
                </div>
              ))}
          </div>

          
        )}
              <br />
      {currentUser && (
          <div>
            <h3>My Orders:</h3>
            {cart
              .filter(cart => cart.user_id === currentUser.id) 
              .map(cart => (
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
                  <div className="my-listing">
                    <h4>{cart.item.item_name}</h4>
                    <img width='250px' src={cart.item.item_img} alt={cart.item.item_name} />
                  </div>
                  <br></br>
                </div>
              ))}
          </div>
          

        )}
            </div>
                    </div>

                </div>
            </div>
        </>
    )
}

export default Profile