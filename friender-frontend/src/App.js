import "bootswatch/dist/quartz/bootstrap.min.css";
import "./App.css";
import Nav from "./nav-routes/Nav";
import Routes from "./nav-routes/Routes";
import { useHistory } from "react-router-dom";
import React, { useEffect, useState } from "react";
import Api from "./api/api";
import UserContext from "./UserContext";

/** Friender
 * An app that allows the user to meet adults in their area
 */
function App() {
  /** FOR DEV **/
  const _testuser = {
    email: "test@test.com",
    firstName: "testFN",
    lastName: "testLN",
    userId: 1,
  };
  /** END DEV **/

  // TODO: have user persist throughout screen refresh and same browser

  const [currentUser, setCurrentUser] = useState(_testuser);
  const [isLoaded, setIsLoaded] = useState(true); // SET TO false for DEV

  function login() {}

  function unmatch() {}

  function updateProfile() {}

  function signup() {}

  function logout() {
    setCurrentUser(null);
  }

  function getMatches() {}

  if (!isLoaded) return <i> LOADING... lonely? </i>;
  return (
    <UserContext.Provider value={currentUser}>
      {/* FOR DEV-- change later*/}
      <div className="App">
        <Nav logout={logout} />
        <Routes
          update={updateProfile}
          unmatch={unmatch}
          getMatches={getMatches}
          login={login}
          signup={signup}
        />
      </div>
    </UserContext.Provider>
  );
}

export default App;
