import React from "react";
import { Link } from "react-router-dom";
import DeleteButton from "./DeleteButton";
import Table from "react-bootstrap/Table";

const AuthorList = (props) => {
  const { authors, setAuthors } = props;

  const filterList = (id) => {
    const filteredList = authors.filter((author) => author._id !== id);
    setAuthors(filteredList);
  };

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Author</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {authors.map((author, index) => (
          <tr key={index}>
            <td>{author.name}</td>
            <td className="d-flex">
              <Link to={`/edit/${author._id}`}>
                <button className="btn btn-primary">Edit</button>
              </Link>
              <DeleteButton id={author._id} onDelete={() => filterList(author._id)} />
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default AuthorList;
