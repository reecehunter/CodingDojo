import React from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const ProductForm = (props) => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post(`http://localhost:8080/api/products`, {
        title: e.target[0].value,
        price: e.target[1].value,
        description: e.target[2].value,
      })
      .then((res) => {
        console.log(res.data.product._id);
        navigate(`/${res.data.product._id}`);
      })
      .catch((err) => console.log(err));
  };

  return (
    <form className="container" onSubmit={(e) => handleSubmit(e)}>
      <input type="text" name="title" id="title" placeholder="Title" />
      <input type="number" name="price" id="price" placeholder="1" />
      <input
        type="text"
        name="description"
        id="description"
        placeholder="Description"
      />
      <input type="submit" value="Add Product" />
    </form>
  );
};

export default ProductForm;
