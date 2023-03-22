import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import DeleteButton from "../components/DeleteButton";

const OneProductPage = () => {
  const { id } = useParams();
  const [product, setProduct] = useState({
    title: "",
    price: 0,
    description: "",
  });
  const navigate = useNavigate();

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
      <DeleteButton id={id} onDelete={() => navigate("/")} />
    </div>
  );
};

export default OneProductPage;
