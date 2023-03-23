import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import AuthorForm from "../components/AuthorForm";

const EditPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    axios
      .get(`http://localhost:8080/api/authors/${id}`)
      .then((res) => {
        setName(res.data.author.name);
      })
      .catch((err) => console.log(err));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    const updateData = {
      name: e.target[0].value,
    };

    axios
      .put(`http://localhost:8080/api/authors/${id}`, updateData)
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
      <div>
        <h1>Update Author</h1>
        {errors.map((error, index) => (
          <p key={index} className="text-danger">
            {error}
          </p>
        ))}
        <AuthorForm submitCallback={handleSubmit} name={name} />
      </div>
    </>
  );
};

export default EditPage;
