import "./App.css";
import { Routes, Route } from "react-router-dom";
import SearchForm from "./components/SearchForm";
import React from "react";
import Home from "./pages/Home";
import People from "./pages/People";
import Planets from "./pages/Planets";

function App() {
  return (
    <div>
      <SearchForm />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/people/:id" element={<People />} />
        <Route path="/planets/:id" element={<Planets />} />
      </Routes>
    </div>
  );
}

export default App;
