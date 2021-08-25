import React from "react";
import "bootswatch/dist/quartz/bootstrap.min.css";

function Homepage({ currentUser }) {
  return (
    <div className="Homepage">
      {true /* set true for if logged in for now */ ? (
        <h1> Welcome {currentUser.firstName} </h1>
      ) : (
        <h2> Unauthorized Access </h2>
      )}
    </div>
  );
}

Homepage.defaultProps = {
  currentUser: { firstName: "testFN", lastName: "testLN" },
};

export default Homepage;
