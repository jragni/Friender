import React, { useState, useContext } from "react";
import { useHistory } from "react-router-dom";
import UserContext from "../UserContext";
import "./SignupForm.css";

/**EditProfileForm
 * form for users to edit their profile. In order to edit profile, user
 * must enter correct password.
 *
 * Props:
 * - update --- function to update the current user profile.
 * States:
 *  - userInfo  --- form fields {firstName, lastName, email, password}
 *
 * Routes -> EditProfileForm
 */
function EditProfileForm({ update }) {
  console.log("EditProfileForm: rendering");
  const history = useHistory();
  const currentUser = useContext(UserContext);
  console.log("EditProfileForm, currentUser: ", currentUser);
  if (!currentUser) history.push("/");

  // STATES
  const [userInfo, setUserInfo] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  function handleChange(evt) {
    const { name, value } = evt.target;
    setUserInfo((SignUpData) => ({
      ...SignUpData,
      [name]: value,
    }));
  }
  // Sends search back to parent component
  function handleSubmit(evt) {
    evt.preventDefault();
    update(userInfo);
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
          value={userInfo.firstName}
        />
        <input
          id="signup-last-name"
          name="lastName"
          className="form-control form-input"
          placeholder="Last Name"
          onChange={handleChange}
          value={userInfo.lastName}
        />
        <input
          id="signup-email"
          name="email"
          className="form-control form-input"
          placeholder="Email"
          onChange={handleChange}
          value={userInfo.email}
        />
        <input
          id="signup-password"
          name="password"
          className="form-control form-input"
          placeholder="Password"
          onChange={handleChange}
          value={userInfo.password}
        />
        <button className="btn btn-primary">Register</button>
      </form>
    </div>
  );
}

export default EditProfileForm;
