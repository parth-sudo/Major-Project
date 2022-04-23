import React from "react";
import '../styles/HomeStyle.css';
import Login from './Login.js';
import {Link} from "react-router-dom";

function Home() {

  return (
        <div className="header">
            <h1 style={{textAlign : 'center'}}>Maladie Prediction</h1>
            <Link to='/login'>
              <button> Login/Sign-up </button>
            </Link>
        </div>
  );
}

export default Home;
