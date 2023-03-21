import "./App.css";
import FormPage from "./pages/FormPage";
import { Routes, Route } from "react-router-dom";
import OneProductPage from "./pages/OneProductPage";
import Nav from "./components/Nav";

function App() {
  return (
    <>
      <Nav />
      <Routes>
        <Route path="/" element={<FormPage />} />
        <Route path="/:id" element={<OneProductPage />} />
      </Routes>
    </>
  );
}

export default App;
