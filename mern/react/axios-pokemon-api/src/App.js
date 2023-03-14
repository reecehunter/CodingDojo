import "./App.css";
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [pokemon, setPokemon] = useState([]);

  const fetchPokemon = () => {
    axios
      .get("https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20")
      .then((response) => {
        return response.data;
      })
      .then((jsonResponse) => {
        setPokemon([...jsonResponse.results]);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="container">
      <button onClick={fetchPokemon}>Fetch Pokemon</button>
      <ul>
        {pokemon.map((p, i) => (
          <li key={i}>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
