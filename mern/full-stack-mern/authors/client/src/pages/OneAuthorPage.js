import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";
import AuthorForm from "../components/AuthorForm";

const OneAuthorPage = () => {
  const { id } = useParams();
  const [author, setProduct] = useState("");

  useEffect(() => {
    axios
      .get(`http://localhost:8080/api/authors/${id}`)
      .then((res) => setProduct(res.data.author))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h2>Edit Author</h2>
      {/* <AuthorForm submitCallback={} /> */}
    </div>
  );
};

export default OneAuthorPage;
