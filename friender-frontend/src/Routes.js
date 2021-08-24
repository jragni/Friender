import { useContext } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import SignupForm from "./SignupForm";
import UserContext from "./UserContext";

function Routes() {
  //private route -> usercontext {props.childre}
  // const { currentUser } = useContext(UserContext);
  // const token = localStorage.getItem("jobly-token");
  return (
    <div className="Routes">
      {
        <Switch>
          <Route exact path="/signup">
            <SignupForm/>
          </Route>
          <Redirect to="/" />
        </Switch>
      
      }

    </div>
  );
}

export default Routes;
