import React, { useContext } from "react";
import "./Nav.css";
import { NavLink } from "react-router-dom";
import UserContext from "../UserContext";

/** Nav
 * Navbar for each page
 *
 * Props:
 *  - logout --- function that handles user logout
 *
 * App -> NavBar
 *
 */
function Nav({ logout }) {
  //TODO pass logout function through the nav props
  // and add it as an onclick event on the logout button
  const currentUser = useContext(UserContext);
  console.log(currentUser);
  return (
    <div className="Navbar">
      <nav className="Nav navbar navbar-expand-md navbar-dark bg-primary">
        <NavLink exact to="/" className="nav-brand me-auto ">
          <i className="logo"> Friender </i>
        </NavLink>
        {!currentUser ? (
          <ul className="navbar-nav ms-auto ">
            <li className="navbar-nav mr-4">
              <NavLink exact to="/login" className="nav-link">
                Login
              </NavLink>
            </li>
            <li className="navbar-nav mr-4">
              <NavLink exact to="/signup" className="nav-link">
                Sign Up
              </NavLink>
            </li>
          </ul>
        ) : (
          <NavLink to="/" className="nav-link" onClick={logout}>
            Log out as {currentUser.firstName}
          </NavLink>
        )}
      </nav>
    </div>
  );
}

export default Nav;
