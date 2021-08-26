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
        <div>
          <Link className="btn" to="/login">
            Log In{" "}
          </Link>
          <Link className="btn" to="/signup">
            {" "}
            Sign Up{" "}
          </Link>
        </div>
      )}
    </div>
  );
}

Homepage.defaultProps = {
  currentUser: { firstName: "testFN", lastName: "testLN" },
};

export default Homepage;
