import "./App.css";
import FormPage from "./pages/CreateAuthorPage";
import { Routes, Route } from "react-router-dom";
import OneAuthorPage from "./pages/OneAuthorPage";
import Nav from "./components/Nav";
import EditPage from "./pages/EditPage";
import AllAuthorsPage from "./pages/AllAuthorsPage";

function App() {
  return (
    <div className="container">
      <h1>Favorite Authors</h1>
      <Nav />
      <hr />

      <Routes>
        <Route path="/" element={<AllAuthorsPage />} />
        <Route path="/new" element={<FormPage />} />
        <Route path="/:id" element={<OneAuthorPage />} />
        <Route path="edit/:id" element={<EditPage />} />
      </Routes>
    </div>
  );
}

export default App;
