import React from "react";
import { Link } from "react-router-dom";

const AuthorForm = (props) => {
  const { submitCallback, name = "" } = props;

  return (
    <form onSubmit={(e) => submitCallback(e)}>
      <input type="text" name="name" id="name" placeholder="Authors Name" defaultValue={name} />
      <Link to="/">
        <button className="btn btn-secondary">Cancel</button>
      </Link>
      <input type="submit" value="Submit" className="btn btn-primary" />
    </form>
  );
};

export default AuthorForm;
