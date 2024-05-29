import React from 'react';

function Comments({ comment }) {
    return (
            <div className='comment-container'>
                <div className='comment-info'>
                    <p>{comment.content}</p>
                    <p style={{fontWeight:'bold'}}>By: {comment.user.username}</p>
                    <button id='comment-delete'>Delete</button>
                </div>
            </div>
    );
}

export default Comments;