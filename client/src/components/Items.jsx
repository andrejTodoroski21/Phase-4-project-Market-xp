import React, { useState, useEffect } from 'react';
import Comments from './Comments';

function Items({ product, currentUser }) {

    // STATE AND CONTEXT
    const [comments, setComments] = useState([]);
    const [showDetails, setShowDetails] = useState(true);
    const [commentText, setCommentText] = useState('');
    const [showCommentForm, setShowCommentForm] = useState(false);

    // FETCH COMMENTS

    const fetchComments = () => {
        fetch(`/api/items/${product.id}/comments`)
            .then(res => res.json())
            .then(data => setComments(data))
            .catch(error => console.error('Error fetching comments:', error));
    };

    useEffect(() => {
        fetchComments();
    }, []); 

    // TOGGLE BUTTON 
    const toggleDetails = () => {
        setShowDetails(prevShowDetails => !prevShowDetails);
    };

    const handleCommentChange = (e) => {
        setCommentText(e.target.value);
    };

    //POST REQUEST FOR COMMENTS

    const handleCommentSubmit = () => {
        fetch('/api/comments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content: commentText,
                item_id: product.id,
            }),
        })
        .then(res => res.json())
        .then(newComment => {
            setComments([...comments, newComment]);
            setCommentText('');
            setShowCommentForm(false);
        })
        .catch(error => console.error('Error adding comment:', error));
    };

    const toggleCommentForm = () => {
        setShowCommentForm(prev => !prev);
    };
    

    //DELETE REQUEST FOR COMMENTS
    const deleteComment = (commentId) => {
        fetch(`/api/comments/${commentId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                setComments(comments.filter(comment => comment.id !== commentId));
            } else {
                alert("Error deleting comment");
            }
        })
        .catch(error => {
            console.error('Error deleting comment:', error);
            alert("Error deleting comment");
        });
    };

    const handleBuy = () => {
            fetch(`/api/items/${product.id}/buy`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    item_id: product.id,
                    buyer_id: currentUser.id
                }),
            })
            .then(res => res.json())

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
                        {comments.map(comment => (<Comments key={comment.id} comment={comment} currentUser={currentUser} onDelete={deleteComment}/>))}
                        <div className='comment-buttons'>
                            <button onClick={showCommentForm ? handleCommentSubmit : toggleCommentForm}>
                                {showCommentForm ? 'Submit' : 'Add a Comment'}
                            </button>
                            {showCommentForm && (
                                <div>
                                    <textarea className="comment-box" value={commentText} onChange={handleCommentChange} />
                                </div>
                            )}
                        </div>
                        <br></br>
                    </>
                )}
            </div>
            <div className="buttons">
                <button onClick={handleBuy}>Buy Item</button>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <button onClick={toggleDetails}>{showDetails ? 'Show Comments' : 'Show Details'}</button>
                <br /><br />
            </div>
        </div>
    );
}

export default Items;
