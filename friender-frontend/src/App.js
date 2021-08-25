import "bootswatch/dist/quartz/bootstrap.min.css";
import "./App.css";
import Nav from "./nav-routes/Nav";
import Routes from "./nav-routes/Routes";
import { useHistory } from "react-router-dom";
import React, { useEffect, useState } from "react";
import Api from "./api/api";
import UserContext from "./UserContext";
function App() {
  function login() {}

  function register() {}

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
