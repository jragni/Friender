import "bootswatch/dist/quartz/bootstrap.min.css";
import "./App.css";
import Nav from "./nav-routes/Nav";
import Routes from "./nav-routes/Routes";
import React, { useHistory, useEffect, useState } from "react";
import FrienderApi from "./api/FrienderApi";
import UserContext from "./UserContext";
import axios from "axios";

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

  const [currentUser, setCurrentUser] = useState(null);
  const [isLoaded, setIsLoaded] = useState(true); // SET TO false for DEV

  async function login(loginData) {
    console.log("Logging in App.js....");
    const res = await FrienderApi.login(loginData);
    console.log("Response of login: ", res);
    if (res !== null) {
      FrienderApi.setCurrentUser = res;
      setCurrentUser(res);
      localStorage.setItem("currentUser", JSON.stringify(res));
    } else {
      setCurrentUser(null);
    }
  }

  useEffect(function geCurrentUserLocalStorage() {
    const currentUser = JSON.parse(localStorage.getItem("currentUser"));
    if (currentUser !== "null") {
      setCurrentUser(currentUser);
    }
  }, []);

  function unmatch() {}

  //DEV TESTING ------------------
  //
  async function updateProfile(userInfo) {
    console.log("updating profile");
    // TODO: add this to the API instead
    const response = await axios.post("http://localhost:5000/upload", {
      data: userInfo,
    });
    console.log("response", response);
  }

  async function signup(signupData) {
    console.log("signup----------------signing user up");
    const res = await FrienderApi.signup(signupData);
    console.log("res for signup in APP.js:", res);
    FrienderApi.currentUser = res;
    setCurrentUser(res);
    localStorage.setItem("currentUser", JSON.stringify(res));
  }
  // END DEV TESTING =================

  function logout() {
    setCurrentUser(null);
    localStorage.setItem("currentUser", null);
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
