import React, { useState, useEffect } from "react";
import ProductForm from "../components/ProductForm";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import ProductList from "../components/ProductList";

const FormPage = () => {
  const [products, setProducts] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get("http://localhost:8080/api/products")
      .then((res) => setProducts(res.data.products))
      .catch((err) => console.log(err));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post(`http://localhost:8080/api/products`, {
        title: e.target[0].value,
        price: e.target[1].value,
        description: e.target[2].value,
      })
      .then((res) => navigate(`/${res.data.product._id}`))
      .catch((err) => console.log(err));
  };

  return (
    <>
      <ProductForm submitCallback={handleSubmit} />
      <hr />

      <div className="container">
        <h1>All Products</h1>
        <hr />
        <ProductList products={products} setProducts={setProducts} />
      </div>
    </>
  );
};

export default FormPage;
