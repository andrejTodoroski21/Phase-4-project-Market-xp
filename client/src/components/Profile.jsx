import React, { useEffect, useState } from "react";
import { Link, useOutletContext } from 'react-router-dom';

function Profile() {
    const { currentUser } = useOutletContext();
    const { setCurrentUser } = useOutletContext();

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

    return (
        <>
            <br />
            <br />
            <div style={{ display: 'flex', justifyContent: 'space-around', marginLeft: '30px' }}>
                <div style={{ width: '30%' }}>
                    <div style={{ width: '100%' }} id="listing-window" className="window">
                        <div style={{ height: '30px' }} className="title-bar">
                            <h3 class="title-bar-text">My Listings</h3>
                            <div class="title-bar-controls">
                                <button aria-label="Minimize"></button>
                                <button aria-label="Maximize"></button>
                                <button aria-label="Close"></button>
                            </div>
                        </div>
                        <div class="window-body">
                            {currentUser && items.filter(item => item.seller_id === currentUser.id).length > 0 ? (
                                <div>
                                    {items
                                        .filter(item => item.seller_id === currentUser.id)
                                        .map(item => (
                                            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                                                <div className="my-listing">
                                                    <h4>{item.item_name}</h4>
                                                    <img width='250px' src={item.item_img} alt={item.item_name} />
                                                    <h5>{item.description}</h5>
                                                    <p>{item.category}</p>
                                                    <p>Price:{item.price}</p>
                                                </div>
                                                <br />
                                            </div>
                                        ))}
                                </div>
                            ) : (
                                <h3>No listings found</h3>
                            )}
                        </div>
                    </div>
                </div>
                <div style={{ width: '30%' }}>
                    <div style={{ width: '100%' }} id="orders-window" className="window">
                        <div style={{ height: '30px' }} className="title-bar">
                            <h3 class="title-bar-text">My Orders</h3>
                            <div class="title-bar-controls">
                                <button aria-label="Minimize"></button>
                                <button aria-label="Maximize"></button>
                                <button aria-label="Close"></button>
                            </div>
                        </div>
                        <div class="window-body">
                            {currentUser && cart.filter(item => item.user_id === currentUser.id).length > 0 ? (
                                <div>
                                    {cart
                                        .filter(item => item.user_id === currentUser.id)
                                        .map(item => (
                                            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                                                <div className="my-listing">
                                                    <h4>{item.item.item_name}</h4>
                                                    <img width='250px' src={item.item.item_img} alt={item.item.item_name} />
                                                    <solid><p>Price:{item.item.price}</p></solid>
                                                </div>
                                                <br />
                                            </div>
                                        ))}
                                </div>
                            ) : (
                                <h3>No orders found</h3>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Profile;

