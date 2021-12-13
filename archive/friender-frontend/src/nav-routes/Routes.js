import React from "react";
import { Switch, Route } from "react-router-dom";
import Homepage from "../homepage/Homepage";
import EditProfile from "../profile/EditProfile";
import Matches from "../matches/Matches";
export default function Routes(props) {

  return (
    <Switch>

      <Route exact path="/">
        <Homepage />
      </Route>

      <Route exact path="/profile">
        <EditProfile />
      </Route>

      <Route to="/matches">
        <Matches/>
      </Route>
    </Switch>
  );
}
