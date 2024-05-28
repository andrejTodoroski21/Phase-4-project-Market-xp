import React, {useEffect, useState} from "react";
import Items from "./Items"
import Comments from './Comments'
//import "xp.css/dist/XP.css";

function Listings() {

    const [products, setProducts] = useState([])
    const [comments, setComments] = useState([])

    useEffect(()=> {
        fetch('/api/items')
        .then(res => res.json())
        .then(data => setProducts(data))
        }, [])

    useEffect(()=> {
        fetch('/api/comments')
        .then(res => res.json())
        .then(data => setComments(data))
        }, [])
    
    console.log(products)

    const mappedProducts = products.map(p => <Items key={p.id} product={p}/>)
    const mappedComments = products.map(p => <Comments key={p.id} comment={p}/>)

    return (
        <div>
            <br></br>
            <div className="content-container">
                {mappedProducts}
                    {mappedComments}
            </div>
        </div>
    )
}

export default Listings