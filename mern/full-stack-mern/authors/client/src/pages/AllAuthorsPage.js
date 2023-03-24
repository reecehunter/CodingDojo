import React, { useState, useEffect } from "react";
import AuthorList from "../components/AuthorList";
import axios from "axios";

const AllAuthorsPage = () => {
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8080/api/authors")
      .then((res) => setAuthors(res.data.authors))
      .catch((err) => console.log(err));
  }, []);

  const filterList = (id) => {
    const filteredList = authors.filter((author) => author._id !== id);
    setAuthors(filteredList);
  };

  return (
    <div>
      <h2>All Authors</h2>
      <p>We have quotes by:</p>
      <AuthorList authors={authors} onDelete={filterList} />
    </div>
  );
};

export default AllAuthorsPage;
