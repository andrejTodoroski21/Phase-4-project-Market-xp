import React, {useEffect, useState} from "react";
import Items from "./Items"
//import "xp.css/dist/XP.css";

function Listings() {
    
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('/api/items')
            .then(res => res.json())
            .then(data => setProducts(data));
    }, []);

    return (
        <div>
            <br />
            <div className="content-container">
                {products.map(product => (
                    <Items key={product.id} product={product} />
                ))}
            </div>
        </div>
    );
}
/*
    const [products, setProducts] = useState([])
    const [comments, setComments] = useState([])
    const [showCommentsMap, setShowCommentsMap] = useState({});

    const toggleComments = (itemId) => {
        setShowCommentsMap(prevState => ({
            ...prevState,
            [itemId]: !prevState[itemId]
        }));
    };

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

    const mappedProducts = products.map(p => <Items key={p.id} product={p} comments={comments}/>)
    const mappedComments = comments.map(p => <Comments key={c.id} comment={c}/>)

    return (
        <div>
            <br></br>
            <div className="content-container">
                {mappedProducts}
                <div>
                    {mappedComments}
                </div>
            </div>
        </div>

    )
}
*/

export default Listings