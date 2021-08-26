import React from "react";
import { Link } from "react-router-dom";
import "./MatchCard.css";
import defaulImg from "./blank-profile-picture-973460_1280.png";

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
function MatchCard({ unmatch, match }) {
  console.log("MatchCard rendering...");
  const { firstName, lastName, description, id, image_url } = match;
  const fullName = `${firstName} ${lastName}`;
  // TODO: BUILD OUT UNMATCH features on API
  return (
    <div className="MatchCard card">
      <img
        className="card-img-top"
        src={image_url ? image_url : defaulImg}
        alt={fullName}
      />
      <div className="card-body">
        <h5 className="card-title">{firstName}</h5>
        <p className="card-text">{description}</p>
        <Link href="/" className="btn btn-primary btn-sm card-btn">
          Chat
        </Link>
        <button onClick={unmatch} className="btn btn-danger btn-sm card-btn">
          Unmatch
        </button>
      </div>
    </div>
  );
}

export default MatchCard;
