import React, { Component } from "react";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Landing from "./Landing.js";
import Login from "./Login.js";
import Dashboard from "./Dashboard.js";

import "./App.scss";

class App extends Component {
  constructor(props) {
    super();
    this.state = {
      loggedIn: false
    };
  }

  handleLogin = () => {
    this.setState({ loggedIn: true });
  };

  handleLogout = () => {
    this.setState({ loggedIn: false });
  };

  render() {
    return (
      <Router>
        <div className="App">
          <Switch>
            <Route
              exact
              path="/"
              render={props => (
                <Landing
                  {...props}
                  loggedIn={this.state.loggedIn}
                  handleLogout={this.handleLogout}
                />
              )}
            />
            <Route
              exact
              path="/login"
              render={props => (
                <Login
                  {...props}
                  loggedIn={this.state.loggedIn}
                  handleLogin={this.handleLogin}
                />
              )}
            />
            <Route
              exact
              path="/dashboard"
              render={props => (
                <Dashboard
                  {...props}
                  loggedIn={this.state.loggedIn}
                  handleLogout={this.handleLogout}
                />
              )}
            />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
