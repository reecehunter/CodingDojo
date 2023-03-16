import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const People = () => {
  const { id } = useParams();
  const [data, setData] = useState();
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get(`https://swapi.dev/api/people/${id}`)
      .then((res) => {
        setData([res.data]);
        setError("");
      })
      .catch((err) => {
        setError("These aren't the droids you're looking for");
        setData([]);
      });
  }, [id]);

  return (
    <div>
      <p style={{ color: "red" }}>{error}</p>

      {data
        ? data.map((entry, idx) => (
            <div key={idx}>
              <h2>{entry.name}</h2>
              <p>Height: {entry.height}</p>
              <p>Mass: {entry.mass}</p>
              <p>Hair Color: {entry.hair_color}</p>
              <p>Skin Color: {entry.skin_color}</p>
            </div>
          ))
        : ""}
    </div>
  );
};

export default People;
