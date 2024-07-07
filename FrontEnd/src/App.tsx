import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./pages/Home";
import EventDetailPage from "./pages/EventDetailPage";
import UserProfilePage from "./pages/UserProfilePage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/events/:id" component={EventDetailPage} />
        <Route path="/profile" component={UserProfilePage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
      </Switch>
    </Router>
  );
};

export default App;
