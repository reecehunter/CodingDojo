import React from "react";
import { useNavigate } from "react-router-dom";

const SearchForm = () => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate(`/${e.target[0].value}/${e.target[1].value}`);
  };

  return (
    <form onSubmit={(e) => handleSubmit(e)}>
      <select name="type" id="type">
        <option value="people">People</option>
        <option value="planets">Planets</option>
      </select>

      <label htmlFor="id">ID:</label>
      <input type="number" name="id" id="id" />

      <input type="submit" value="Search" />
    </form>
  );
};

export default SearchForm;
