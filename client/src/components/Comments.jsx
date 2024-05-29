import React from 'react';

function Comments({ comment, currentUser, onDelete }) {
    const handleDelete = () => {
        onDelete(comment.id);
    };

    return (
        <div className='comment-container'>
            <div className='comment-info'>
                <p>{comment.content}</p>
                <p style={{fontWeight:'bold'}}>By: {comment.user.username}</p>
                {currentUser && currentUser.id === comment.user.id && (
    <button id='comment-delete' onClick={handleDelete}>Delete</button>
)}
            </div>
        </div>
    );
}

export default Comments;

