import "./App.css";
import FormPage from "./pages/FormPage";
import { Routes, Route } from "react-router-dom";
import OneProductPage from "./pages/OneProductPage";
import Nav from "./components/Nav";
import EditPage from "./pages/EditPage";

function App() {
  return (
    <>
      <Nav />
      <Routes>
        <Route path="/" element={<FormPage />} />
        <Route path="/:id" element={<OneProductPage />} />
        <Route path="/:id/edit" element={<EditPage />} />
      </Routes>
    </>
  );
}

export default App;
