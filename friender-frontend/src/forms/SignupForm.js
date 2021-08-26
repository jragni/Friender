import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import "./SignupForm.css";

/**SignUpForm
 * form for users to sign up
 *
 * Props:
 *  - signup  --
 * States:
 *  - signupInfo  --- form fields {firstName, lastName, email, password}
 *
 * Routes -> SignUpForm
 */
function SignUpForm({ signup }) {
  const history = useHistory();

  const currentUser = useContext(UserContext);
  if (currentUser) history.push("/");

  // STATES
  const [signUpInfo, setSignUpInfo] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setSignUpInfo((SignUpData) => ({
      ...SignUpData,
      [name]: value,
    }));
  }
  // Sends search back to parent component
  function handleSubmit(evt) {
    evt.preventDefault();
    //signup(signUpInfo); // TODO: will add this later
    // if(currentUser) history.push("/companies")
    history.push("/");
  }

  return (
    <div className="SignupForm">
      <form className="container signup-form" onSubmit={handleSubmit}>
        <h1> Sign Up </h1>
        <input
          id="signup-first-name"
          name="firstName"
          className="form-control form-input"
          placeholder="First Name"
          onChange={handleChange}
          value={signUpInfo.firstName}
        />
        <input
          id="signup-last-name"
          name="lastName"
          className="form-control form-input"
          placeholder="Last Name"
          onChange={handleChange}
          value={signUpInfo.lastName}
        />
        <input
          id="signup-email"
          name="email"
          className="form-control form-input"
          placeholder="Email"
          onChange={handleChange}
          value={signUpInfo.email}
        />
        <input
          id="signup-password"
          name="password"
          className="form-control form-input"
          placeholder="Password"
          onChange={handleChange}
          value={signUpInfo.password}
        />
        <button className="btn btn-primary">Register</button>
      </form>
    </div>
  );
}

export default SignUpForm;
