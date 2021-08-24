import './App.css';
import Nav from "./Nav";
import Routes from "./Routes";
import { useHistory } from "react-router-dom";
import React, { useEffect, useState } from "react";
import Api from "./api";
import UserContext from "./UserContext";
import jwt from "jsonwebtoken";
function App() {
  return (
    <UserContext.Provider value={{}}>

      <div className="App">
        <Nav />
        <Routes />
      </div>
    </UserContext.Provider>
  );
}

export default App;
