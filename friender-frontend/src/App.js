import "./App.css";
import Nav from "./nav-routes/Nav";
import Routes from "./nav-routes/Routes";
import React from "react";
import {BrowserRouter} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Nav />
        <Routes />
      </BrowserRouter>
    </div>
  );
}

export default App;
