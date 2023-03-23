import React from "react";
import axios from "axios";

const DeleteButton = (props) => {
  const { id, onDelete } = props;

  const handleClick = () => {
    axios
      .delete(`http://localhost:8080/api/authors/${id}`)
      .then((res) => onDelete())
      .catch((err) => console.log(err));
  };

  return (
    <button onClick={handleClick} className="btn btn-danger">
      Delete
    </button>
  );
};

export default DeleteButton;
