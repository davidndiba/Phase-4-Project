// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// const ProductList = ({ addToCart }) => {
//   const [products, setProducts] = useState([]);

//   useEffect(() => {
//     axios.get('/api/products').then((response) => {
//       setProducts(response.data);
//     });
//   }, []);

//   return (
//     <>
//       <div>
//         <h2>Product List</h2>
//         <div className="products">
//           {products.map((product) => (
//             <div className="product-card" key={product.id}>
//               <div>
//                 {/* You can use an image here if you have an 'image' property in your product */}
//                 <img src={product.image} alt="product" className="product-image" />
//               </div>
//               <div className="product-details">
//                 <h1 className="product-title">{product.name}</h1>
//                 <p className="product-description">{/* Add a description if available */}</p>
//                 <p className="product-price">${product.price}</p>
//                 <button onClick={() => addToCart(product.id)} className="btn">
//                   Add to Cart
//                 </button>
//               </div>
//             </div>
//           ))}
//         </div>
//       </div>
//     </>
//   );
// };

// export default ProductList;
import { useEffect, useState } from "react";
import { Axios } from "axios";
import { Link } from "react-router-dom";

// function Products() {
//   const [products, setProducts] = useState([]);

//   useEffect(() => {
//     fetch("/")
//       .then((res) => res.json())
//       .then((data) => setProducts(data));
//   }, []);
function Products ({ addToCart })  {
     const [products, setProducts] = useState([]);
  
     useEffect(() => {
       Axios.get('/api/products').then((response) => {
         setProducts(response.data);
       });
     }, []);
  return (
    <>
      <div>
        <div className="banner_container page_banner_container">
          <div className="site_tagline">
            <h1 className="tagline">Products</h1>
          </div>
          <img
            src="https://images.unsplash.com/photo-1604654894611-6973b376cbde?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
            alt="Banner"
            className="banner page_banner"
          />
        </div>
        <div>
         <h2>Product List</h2>
         <div className="products">
           {products.map((product) => (
             <div className="product-card" key={product.id}>
               <div>
                {/* You can use an image here if you have an 'image' property in your product */}
                 <img src={product.image} alt="product" className="product-image" />
               </div>
               <div className="product-details">
                 <h1 className="product-title">{product.name}</h1>
                 <p className="product-description">{/* Add a description if available */}</p>
                 <p className="product-price">${product.price}</p>
                 <button onClick={() => addToCart(product.id)} className="btn">
                   Add to Cart
                 </button>
               </div>
             </div>
           ))}
         </div>
       </div>

       
      </div>
    </>
  );
}

export default Products;

// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// const ProductList = ({ addToCart }) => {
//   const [products, setProducts] = useState([]);

//   useEffect(() => {
//     axios.get('/api/products').then((response) => {
//       setProducts(response.data);
//     });
//   }, []);

//   return (
//     <div>
//       <h2>Product List</h2>
//       <ul>
//         {products.map((product) => (
//           <li key={product.id}>
//             {product.name} - ${product.price}
//             <button onClick={() => addToCart(product.id)}>Add to Cart</button>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default ProductList;

