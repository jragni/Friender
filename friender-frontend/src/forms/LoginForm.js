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
 *     {firstName, lastName, email, description, bio}
 outes -> LoginForm
 */

/** NOTE:
 * HOW TO HANDLE improper redirects
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
  function handleSubmit(evt) {
    evt.preventDefault();
    login(loginInfo);
    history.push("/login");
  }
  // TODO: validate if this works

  return (
    <div className="LoginForm">
      <form className="container login-form" onSubmit={handleSubmit}>
        <h1> Login </h1>
        <input
          type="text"
          id="email"
          name="email"
          className="form-control form-input"
          placeholder="Email"
          onChange={handleChange}
          value={loginInfo.email}
        />
        <input
          type="text"
          id="login-password"
          name="password"
          className="form-control form-input"
          placeholder="Password"
          onChange={handleChange}
          value={loginInfo.password}
        />
        <button className="btn-primary btn">Log In</button>
      </form>
    </div>
  );
}

export default LoginForm;
