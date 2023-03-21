import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const OneProductPage = () => {
  const { id } = useParams();
  const [product, setProduct] = useState({
    title: "",
    price: 0,
    description: "",
  });

  useEffect(() => {
    axios
      .get(`http://localhost:8080/api/products/${id}`)
      .then((res) => setProduct(res.data.product))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="container">
      <h1>Single Product</h1>
      <hr />
      <h2>
        <strong>{product.title}</strong>
      </h2>
      <p>Price: ${product.price}</p>
      <p>Description: {product.description}</p>
    </div>
  );
};

export default OneProductPage;
