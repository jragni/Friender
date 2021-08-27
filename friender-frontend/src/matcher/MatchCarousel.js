import React, { useState } from "react";

/** MatchCarousel
 * Component that shows the user other potential matches
 * that haven't been seen yet. The user can like or unlike
 * from this component.
 *
 * Hompage -> MatchCarousel -> UserCard
 */

function MatchCarousel({ like, unlike }) {
  console.log("rendering MatchCarousel");
  return (
    <div className="MatchCarousel">
      <h1> MATCH TIME </h1>
    </div>
  );
}

export default MatchCarousel;
