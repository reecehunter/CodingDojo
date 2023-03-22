import React from "react";
import axios from "axios";

const DeleteButton = (props) => {
  const { id, onDelete } = props;

  const handleClick = () => {
    axios
      .delete(`http://localhost:8080/api/products/${id}`)
      .then((res) => onDelete())
      .catch((err) => console.log(err));
  };

  return <button onClick={handleClick}>Delete</button>;
};

export default DeleteButton;
