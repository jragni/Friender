import { useContext } from "react";
import "bootswatch/dist/quartz/bootstrap.min.css";
import { Switch, Route, Redirect } from "react-router-dom";
import SignupForm from "../forms/SignupForm";
import LoginForm from "../forms/LoginForm";
import UserContext from "../UserContext";
import Homepage from "../Homepage";
import TestForm from "../forms/TestForm";

function Routes() {
  //private route -> usercontext {props.childre}
  // const { currentUser } = useContext(UserContext);
  // const token = localStorage.getItem("jobly-token");
  return (
    <div className="Routes">
      {
        <Switch>
          <Route exact path="/signup">
            <SignupForm />
          </Route>

          <Route exact path="/login">
            <LoginForm />
          </Route>

          <Route exact path="/upload">
            {/* used for DEV TESTING */}
            <TestForm />
          </Route>

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
