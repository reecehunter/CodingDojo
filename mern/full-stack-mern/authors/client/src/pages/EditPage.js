import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import ProductForm from "../components/ProductForm";

const EditPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    axios
      .get(`http://localhost:8080/api/products/${id}`)
      .then((res) => {
        setTitle(res.data.product.title);
        setPrice(res.data.product.price);
        setDescription(res.data.product.description);
      })
      .catch((err) => console.log(err));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    const updateData = {
      title: e.target[0].value,
      price: e.target[1].value,
      description: e.target[2].value,
    };

    axios
      .put(`http://localhost:8080/api/products/${id}`, updateData)
      .then((res) => navigate(`/${id}`))
      .catch((err) => console.log(err));
  };

  return (
    <>
      <div className="container">
        <h1>Update Product</h1>
        <hr />
        <ProductForm
          submitCallback={handleSubmit}
          title={title}
          price={price}
          description={description}
        />
      </div>
    </>
  );
};

export default EditPage;
