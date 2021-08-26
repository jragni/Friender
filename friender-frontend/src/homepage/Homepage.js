import "./Homepage.css";
import React, { useContext } from "react";
import MatchCarousel from "../matcher/MatchCarousel";
import UserContext from "../UserContext";
import { Link } from "react-router-dom";

function Homepage() {
  const currentUser = useContext(UserContext);
  return (
    <div className="Homepage">
      {currentUser /* set true for if logged in for now */ ? (
        <MatchCarousel />
      ) : (
        <div className="container homepage-jumbotron">
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
      )}
    </div>
  );
}

Homepage.defaultProps = {
  currentUser: { firstName: "testFN", lastName: "testLN" },
};

export default Homepage;
