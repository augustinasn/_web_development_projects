import React, { Component } from "react";
import { Helmet } from "react-helmet";

import Navbar from "./Navbar.js";
import Splash from "./Splash.js";

import "./Landing.scss";

class Landing extends Component {
  constructor(props) {
    super();
    this.state = {
      loggedIn: props.loggedIn,
      handleLogout: props.handleLogout
    };
  }

  render() {
    return (
      <div className="Landing">
        <Helmet>
          <title>Main | FoxTrapper&trade;</title>
        </Helmet>

        <Navbar
          loggedIn={this.state.loggedIn}
          handleLogout={this.state.handleLogout}
          landing={true}
        />

        <Splash />
      </div>
    );
  }
}

export default Landing;
