import React, {useEffect, useState} from "react";
import { Link, useOutletContext } from 'react-router-dom'
function Profile() {

    const{currentUser} =useOutletContext()

    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch('/api/items')
            .then(res => res.json())
            .then(data => setItems(data));
    }, []);

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
      <div>
        {items
          .filter(items => items.seller_id === currentUser.id) // Filter products by current user's ID
          .map(item => (
            <div key={item.id} className="product-item">
              <h3>{item.item_name}</h3>
              <img src={item.item_img} alt={item.item_name} />
            </div>
          ))}
      </div>
    </div>
                    </div>

                </div>
            </div>
        </>
    )
}

export default Profile