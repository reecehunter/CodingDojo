import React, { useState, useEffect } from "react";
import ProductForm from "../components/ProductForm";
import axios from "axios";

const FormPage = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8080/api/products")
      .then((res) => setProducts(res.data.products))
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <ProductForm />
      <hr />

      <div className="container">
        <h1>All Products</h1>
        <hr />
        {products.map((product, index) => (
          <a key={index} href={`/${product._id}`}>
            {product.title}
          </a>
        ))}
      </div>
    </>
  );
};

export default FormPage;
