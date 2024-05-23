import React, {useEffect, useState} from "react";
//const [product, setProduct] = useState('')

function Items() {

    /* useEffect(()=> {
        fetch('')
        .then(response => {
            if (response.status === 200) {
                response.json()
                .then(data => setProduct(data))
        }
        })
    }, []) */

    return (
        <div>
            <h2>Item Name</h2>
            <img src={'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Nintendo_64.jpg/640px-Nintendo_64.jpg'}/>
            <h3>Description: test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test</h3>
            <p>*Category* - Inventory: 5 - Page Views: 5</p>
            <p>*time posted*</p>

            
        </div>
    )
}

export default Items