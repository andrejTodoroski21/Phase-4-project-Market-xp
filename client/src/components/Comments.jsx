import React from 'react';

function Comments({ comment }) {
    return (
        <div>
            <p>{comment.content}</p>
            {<p>By: {comment.user.name}</p>}
            {<p>Created At: {comment.created_at}</p>}
        </div>
    );
}

export default Comments;