import React, {useEffect, useState} from "react";
import { useOutletContext } from 'react-router-dom'
import Items from "./Items"
//import "xp.css/dist/XP.css";

function Listings() {
    const{currentUser} =useOutletContext()
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
                    <Items key={product.id} product={product} currentUser={currentUser} />
                ))}
            </div>
        </div>
    );
}

export default Listings