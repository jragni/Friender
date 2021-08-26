import { useContext } from "react";
import "bootswatch/dist/quartz/bootstrap.min.css";
import { Switch, Route, Redirect } from "react-router-dom";
import SignupForm from "../forms/SignupForm";
import LoginForm from "../forms/LoginForm";
import UserContext from "../UserContext";
import Homepage from "../homepage/Homepage";
import Matches from "../matches/Matches";
import TestForm from "../forms/TestForm"; // FOR DEV

/**Routes
 * Routes for the web application
 *
 * Props;
 *  - signup  --- function that handles signup requests
 *  - login  --- funciton that handles login requests
 *
 * States:
 *  None
 *
 * App -> Routes -> { SignupForm, LoginForm, Homepage, Matches }
 */

function Routes({ signup, login, getMatches }) {
  //private route -> usercontext {props.childre}
  // const { currentUser } = useContext(UserContext);
  // const token = localStorage.getItem("jobly-token");
  return (
    <div className="Routes">
      {
        <Switch>
          <Route exact path="/signup">
            <SignupForm signup={signup} />
          </Route>

          <Route exact path="/login">
            <LoginForm login={login} />
          </Route>

          <Route exact path="/matches">
            <Matches getMatches={getMatches} />
          </Route>

          {/* DEV TESTING */}
          <Route exact path="/upload">
            <TestForm />
          </Route>
          {/*END DEV TESTING */}

          <Route exact path="/">
            <Homepage />
          </Route>

          <Redirect to="/" />
        </Switch>
      }
    </div>
  );
}

export default Routes;
