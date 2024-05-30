import { useState } from 'react'
import { useOutletContext } from 'react-router-dom'
import { useNavigate } from 'react-router-dom';


function NewListing() {
  const { currentUser, setCurrentUser } = useOutletContext()
  // STATE //

  const [item_name, setItemName] = useState('')
  const [price, setPrice] = useState('')
  const [item_img, setImage] = useState('')
  const [category, setCategory] = useState('')
  const [description, setDescription] = useState('')
  const [inventory, setInventory] = useState('')
  const navigate = useNavigate();



  // EVENTS //

  function handleSubmit(e) {
    e.preventDefault()

    const seller_id = currentUser.id;

    fetch('/api/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ item_name, price, item_img, category, description, inventory, seller_id})
    })
    .then(response => {
      if (response.ok) {
        response.json()
        .then( newItem => {
          setCurrentUser(newItem) 
          navigate('/profile');
        });
      } else {
        alert("adding item unsuccessful")
      }
    })
  }

  // RENDER //

  return (

    <div className="window" style={{ marginLeft: '5em', width: 300 }}>
    <div className="title-bar">
      <div className="title-bar-text">Sign up</div>
      <div className="title-bar-controls">
            <button aria-label="Minimize" />
            <button aria-label="Maximize" />
            <button aria-label="Close" />
        </div>
    </div>
    <div className="window-body">
    <form className='user-form' onSubmit={handleSubmit}>

      <h2>New Items</h2>


    <div class="field-row">
        <label for="item_name">Item Name</label>
        <input id="item_name" type="text" onChange={e => setItemName(e.target.value)}
      value={item_name}/>
    </div>

    <div class="field-row">
        <label for="price">Price</label>
        <input id="price" type="text" onChange={e => setPrice(e.target.value)}
      value={price}/>
    </div>

    <div class="field-row">
        <label for="item_img">Image</label>
        <input id="item_img" type="text" onChange={e => setImage(e.target.value)}
      value={item_img}/>
    </div>

    <div class="field-row">
        <label for="category">Category</label>
        <input id="category" type="text" onChange={e => setCategory(e.target.value)}
      value={category}/>
    </div>

    <div class="field-row">
        <label for="description">Description</label>
        <input id="description" type="text" onChange={e => setDescription(e.target.value)}
      value={description}/>
    </div>

    <div class="field-row">
        <label for="inventory">Inventory</label>
        <input id="inventory" type="text" onChange={e => setInventory(e.target.value)}
      value={inventory}/>
    </div>



   {/* ({ item_name, price, item_img, category, description, inventory}) */}


    <input type="submit"
      value='Add item'
    />

    </form>


  </div>
  </div>
  )

}

export default NewListing