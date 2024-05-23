function Items({product}) {

    return (
        <div className="content-container">
            <div  style={{ width: 300, display: "flex", flexDirection: "column", alignItems: "center" }} className="window">
                <div style={{ width: 290, height: 27, color:'white'}} className="title-bar">
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
                    <p>{product.category} - Inventory: 5 - Page Views: 5</p>
                    <p>{product.created_at}</p>
                </div>
                <div className="buttons">
                    <button onClick={console.log('clicked')}>Add to Cart</button>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <button onClick={console.log('clicked')}>Show Comments</button>
                    <br></br>
                    <br></br>
                </div>
            </div>
            <br></br>
            <br></br>
        </div>
    )
}

export default Items