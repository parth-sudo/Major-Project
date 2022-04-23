import './App.css';
import Home from './pages/Home.js';
import Login from './pages/Login.js';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

function App() {
  return (
    <Router>
    <Routes>
      <Route exact path="/" element={<Home/>} />
      <Route path="/login" element={<Login/>} />
    </Routes>
  </Router>
  );
}

export default App;
