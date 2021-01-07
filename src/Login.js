import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import { Helmet } from "react-helmet";

import "./Login.scss";

class Login extends Component {
  constructor(props) {
    super();
    this.state = {
      toDashboard: false,
      loggedIn: props.loggedIn,
      handleLogin: props.handleLogin
    };
  }

  logIn = () => {
    this.state.handleLogin();
    this.setState({
      toDashboard: true
    });
  };

  render() {
    if (this.state.toDashboard || this.state.loggedIn) {
      return <Redirect to="/dashboard" />;
    }

    return (
      <div className="Login">
        <Helmet>
          <title>Login | FoxTrapper&trade;</title>
        </Helmet>
        <div id="login-window" className="box">
          <h2>
            <span>
              <span className="emphasised-text">Fox</span>Trapper&trade;
            </span>{" "}
            user zone
          </h2>
          <form
            onSubmit={e => {
              e.preventDefault();
            }}
          >
            <input
              type="text"
              name="user-name"
              id="login-user-name"
              placeholder="User name"
              required
            />
            <input
              type="password"
              name="user-password"
              id="login-user-password"
              placeholder="Password"
              autoComplete="on"
              required
            />
            <input
              type="submit"
              name="user-login"
              id="user-login"
              className="btn-regular"
              value="Log in"
              onClick={this.logIn}
            />
          </form>
        </div>
      </div>
    );
  }
}

export default Login;
