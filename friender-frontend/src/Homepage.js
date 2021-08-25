import React from "react";

function Homepage({currentUser}) {
  
  return(
    <div className="Homepage">
      {true ?  /* set true for if logged in for now */
          (<h1> Welcome {currentUser.firstName} </h1>)
            :
      }
       
    </div>
  );
}

Homepage.defaultProps = {
  currentUser: {firstName: 'testFN', lastName: 'testLN'},

}

export default Homepage;
