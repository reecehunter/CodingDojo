import React, { useState } from "react";
import AuthorForm from "../components/AuthorForm";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const CreateAuthorPage = () => {
  const [errors, setErrors] = useState([]);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post(`http://localhost:8080/api/authors`, {
        name: e.target[0].value,
      })
      .then((res) => navigate(`/`))
      .catch((err) => {
        const errorRes = err.response.data.error.errors;
        const errorMessageArray = [];
        for (const key in errorRes) errorMessageArray.push(errorRes[key].message);
        setErrors(errorMessageArray);
      });
  };

  return (
    <>
      <p>Add a New Author</p>
      {errors.map((error, index) => (
        <p key={index} className="text-danger">
          {error}
        </p>
      ))}
      <AuthorForm submitCallback={handleSubmit} />
    </>
  );
};

export default CreateAuthorPage;
