import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home";
import Word from "./components/Word";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/:word/:color1/:color2" element={<Word />} />
      </Routes>
      <p></p>
    </div>
  );
}

export default App;
