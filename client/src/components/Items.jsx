import React, { useState } from 'react';
import Comments from './Comments';

function Items({ product }) {
    const [comments, setComments] = useState([]);
    const [showDetails, setShowDetails] = useState(true);

    const fetchComments = () => {
        fetch(`/api/items/${product.id}/comments`)
            .then(res => res.json())
            .then(data => setComments(data))
            .catch(error => console.error('Error fetching comments:', error));
    };

    const toggleDetails = () => {
        if (!showDetails) {
            fetchComments();
        }
        setShowDetails(prevState => !prevState);
    };

    return (
        <div style={{ width: 400, display: "flex", flexDirection: "column", alignItems: "center" }} id="listing_window" className="window">
            <div style={{ width: 390, height: 27, color: 'white' }} className="title-bar">
                <h4>{showDetails ? product.item_name : 'Comments'}</h4>
                <div className="title-bar-controls">
                    <button aria-label="Minimize" />
                    <button aria-label="Maximize" />
                    <button aria-label="Close" />
                </div>
            </div>
            <div style={{ textAlign: "center" }}>
                <br />
                {showDetails ? (
                    <>
                        <img style={{ margin: "0 auto" }} width='250px' src={product.item_img} alt={product.item_name} />
                        <h5>{product.description}</h5>
                        <p>{product.category} - Inventory: {product.inventory}</p>
                        <p>{product.created_at}</p>
                    </>
                ) : (
                    <>
                        <h3>Comments:</h3>
                        {comments.map(comment => <Comments key={comment.id} comment={comment} />)}
                    </>
                )}
            </div>
            <div className="buttons">
                <button onClick={() => console.log('Buy clicked for item:', product.id)}>Buy Item</button>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <button onClick={toggleDetails}>{showDetails ? 'Show Comments' : 'Show Details'}</button>
                <br /><br />
            </div>
        </div>
    );
}

export default Items;

/*
function Items({product, comments, showComments, toggleComments}) {

    const mappedComments = comments.map(comment => <Comments key={comment.id} comment={comment} />);

    return (
        
            <div  style={{ width: 400, display: "flex", flexDirection: "column", alignItems: "center" }} id="listing_window" className="window">
                <div style={{ width:390, height: 27, color:'white'}} className="title-bar">
                    <h4>{product.item_name}</h4>
                    <div className="title-bar-controls">
                        <button aria-label="Minimize" />
                        <button aria-label="Maximize" />
                        <button aria-label="Close" />
                    </div>
                </div>
                <div style={{ textAlign: "center" }}>
                    <br></br>
                    <img style={{ margin: "0 auto" }} width='250px' src={product.item_img}/>
                    <h5>{product.description}</h5>
                    <p>{product.category} - Inventory: 1</p>
                    <p>{product.created_at}</p>
                </div>
                <div className="buttons">
                    <button onClick={() => console.log('Buy clicked for item:', product.id)}>Buy Item</button>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <button onClick={toggleComments}>{showComments ? 'Show Details' : 'Show Comments'}</button>
                    <br /><br />
                    {showComments && <div>{mappedComments}</div>}
                </div>
            </div>
    )
}
*/