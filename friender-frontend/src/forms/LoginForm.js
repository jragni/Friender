import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import "./LoginForm.css";
// import { useHistory } from "react-router-dom"

/** LoginForm
 * Form for user to log into app.
 *
 * Props:
 *  - login  --- function to log user
 *
 * States:
 * - currentUser  --- user info
 *     {firstName, lastName, email, description, bio}
 *
 * Routes -> LoginForm
 */
function LoginForm({ login }) {
  let history = useHistory();
  const currUserObj = useContext(UserContext);

  if (currUserObj) history.push("/");

  const [loginInfo, setLoginInfo] = useState({
    email: "",
    password: "",
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setLoginInfo((loginInfo) => ({
      ...loginInfo,
      [name]: value,
    }));
  }
  // Sends search back to parent component
  function handleSubmit(evt) {
    evt.preventDefault();
    //login(loginInfo);
    history.push("/");
  }
  // TODO: validate if this works

  return (
<<<<<<< HEAD
    <div className="LoginForm" style={{ padding: "8px" }}>
      <form className="login-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <input
            type="text"
            style={{ width: "400px" }}
            id="email"
<<<<<<< HEAD
            name="image"
            className="form-control"
            placeholder="iamge"
=======
            name="email"
            className="form-control form-input"
            placeholder="Email"
>>>>>>> d653f69265c8e6975073ad6a7e9f20141ff93e84
            onChange={handleChange}
            value={loginInfo.image}
          />
        </div>
        <div className="form-group">
          <input
            type="text"
            style={{ width: "400px" }}
            id="login-password"
            name="password"
            className="form-control form-input"
            placeholder="Password"
            onChange={handleChange}
            value={loginInfo.password}
          />
        </div>
=======
    <div className="LoginForm">
      <form className="container login-form" onSubmit={handleSubmit}>
        <h1> Login </h1>
        <input
          type="text"
          style={{ width: "400px" }}
          id="email"
          name="email"
          className="form-control form-input"
          placeholder="Email"
          onChange={handleChange}
          value={loginInfo.email}
        />
        <input
          type="text"
          style={{ width: "400px" }}
          id="login-password"
          name="password"
          className="form-control form-input"
          placeholder="Password"
          onChange={handleChange}
          value={loginInfo.password}
        />
>>>>>>> be357a1d759c3272b9ba96c3e03a3bb1d0a48639
        <button className="btn-primary btn">Log In</button>
      </form>
    </div>
  );
}

export default LoginForm;
