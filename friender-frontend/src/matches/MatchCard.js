import React from "react";
import { Link } from "react-router-dom";
import "./MatchCard.css";

/**MatchCard
 * Component that renders the current user's match's details.
 *
 * Props:
 *  - FirstName
 *  - LastName
 *  - Description
 *
 * State:
 *  None
 *
 * MatchList -> MatchCard
 */
function MatchCard({ match }) {
  console.log("MatchCard rendering...");
  const { firstName, lastName, description, id, image_url } = match;
  const fullName = `${firstName} ${lastName}`;
  // TODO: BUILD OUT UNMATCH features on API
  return (
    <div className="MatchCard card">
      <img className="card-img-top" src={image_url} alt={fullName} />
      <div className="card-body">
        <h5 className="card-title">{firstName}</h5>
        <p className="card-text">{description}</p>
        <Link href="/" className="btn btn-primary btn-sm card-btn">
          Chat
        </Link>
        <Link href="/" className="btn btn-danger btn-sm card-btn">
          Unmatch
        </Link>
      </div>
    </div>
  );
}

export default MatchCard;
