import LoginPanel from "./components/Login/Login"
import RegisterPanel from "./components/Register/Register"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/Register" element={<RegisterPanel />} />
      <Route path="/fetchReviews" element={<fetchReviews />} />
    </Routes>
  );
}
export default App;
