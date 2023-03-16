import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Planets = () => {
  const { id } = useParams();
  const [data, setData] = useState();
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get(`https://swapi.dev/api/planets/${id}`)
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
              <p>Climate: {entry.climate}</p>
              <p>Terrain: {entry.terrain}</p>
              <p>Surface Water: {entry.surface_water ? "true" : "false"}</p>
              <p>Population: {entry.population}</p>
            </div>
          ))
        : ""}
    </div>
  );
};

export default Planets;
