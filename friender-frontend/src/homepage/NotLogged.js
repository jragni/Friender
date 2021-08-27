import "./Homepage.css";
import React from "react";
import { Link } from "react-router-dom";

function NotLogged() {
  console.log("rendering not logged");
  return (
    <div className="NotLogged container homepage-jumbotron">
      <main className="card container">
        <div className="card-body">
          <h1> Friendster </h1>
          <h4 className="card-subtitle text-muted">
            ~Meet lonely adults in your area~
          </h4>
          <div className="card-body">
            <Link className="btn btn-login btn-lg" to="/login">
              Log In
            </Link>
            <Link className="btn btn-signup btn-lg" to="/signup">
              Sign Up
            </Link>
          </div>
        </div>
      </main>
    </div>
  );
}
export default NotLogged;
