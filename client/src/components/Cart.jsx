import { useState, useEffect } from 'react';

function Cart() {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    fetch('/api/cart')
      .then(response => response.json())
      .then(data => setCartItems(data));
  }, []);

  function handleRemove(item_id) {
    fetch(`/api/cart/${item_id}`, { method: 'DELETE' })
      .then(response => {
        if (response.ok) {
          setCartItems(cartItems.filter(item => item.item_id !== item_id));
        } else {
          alert('Error removing item from cart');
        }
      });
  }

  return (
    <div>
      <h2>Your Cart</h2>
      {cartItems.map(item => (
        <div key={item.id}>
          <h3>{item.item.name}</h3>
          <p>Quantity: {item.quantity}</p>
          <button onClick={() => handleRemove(item.item_id)}>Remove</button>
        </div>
      ))}
    </div>
  );
}

export default Cart;