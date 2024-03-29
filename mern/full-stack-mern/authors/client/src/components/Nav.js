import React from "react";
import { Link } from "react-router-dom";

const Nav = () => {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/new">Add an author</Link>
    </nav>
  );
};

export default Nav;
