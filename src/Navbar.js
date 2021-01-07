import React, { Component, Fragment } from "react";
import { Link, withRouter } from "react-router-dom";

import "./Navbar.scss";

class Navbar extends Component {
  constructor(props) {
    super();
    this.state = {
      loggedIn: props.loggedIn,
      handleLogout: props.handleLogout,
      showContent: true,
      landing: props.landing
    };
  }

  logOut = () => {
    this.state.handleLogout();
    this.props.history.push("/login");

    setTimeout(() => {
      alert("Succesfully logged out!");
    }, 200);
  };

  render() {
    return (
      <div className="Navbar">
        <div id="navbar-content">
          <div id="left-side">
            <div id="logo-div">
              {this.state.landing ? (
                <Fragment>
                  <img src="/logo-alt.png" alt="logo"></img>
                  <span className="emphasised-text">Fox</span>
                  <span>Trapper</span>
                  <span>&trade;</span>
                </Fragment>
              ) : (
                <Fragment />
              )}
            </div>
          </div>
          <div id="right-side">
            {this.state.loggedIn && this.state.showContent ? (
              <button href="#" onClick={this.logOut} className="btn-regular">
                Log out
              </button>
            ) : (
              <Link
                className="btn-regular"
                to={{
                  pathname: "/login"
                }}
              >
                Log in
              </Link>
            )}
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(Navbar);
