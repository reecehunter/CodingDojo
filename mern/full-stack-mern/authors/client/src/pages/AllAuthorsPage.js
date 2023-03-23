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

  return (
    <div>
      <h2>All Authors</h2>
      <p>We have quotes by:</p>
      <AuthorList authors={authors} setAuthors={setAuthors} />
    </div>
  );
};

export default AllAuthorsPage;
