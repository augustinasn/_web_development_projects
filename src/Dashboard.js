import React, { Component, Fragment } from "react";
import { Helmet } from "react-helmet";
import { Redirect } from "react-router-dom";

import Navbar from "./Navbar.js";
import Menu from "./Menu.js";
import ImageSearch from "./ImageSearch.js";

import "./Dashboard.scss";

class Dashboard extends Component {
  constructor(props) {
    super();
    this.state = {
      loggedIn: props.loggedIn,
      handleLogout: props.handleLogout,
      showMenu: true,
      showImageScreening: false
    };

    this.handleScreeningSelect = this.handleScreeningSelect.bind(this);
    this.handleGoBackToMenu = this.handleGoBackToMenu.bind(this);
  }

  componentWillUnmount() {
    this.setState({ showMenu: true, showImageScreening: false });
  }

  handleScreeningSelect() {
    this.setState({ showMenu: false, showImageScreening: true });
  }

  handleGoBackToMenu() {
    this.setState({ showMenu: true, showImageScreening: false });
  }

  render() {
    if (!this.state.loggedIn) {
      return <Redirect to="/login" />;
    }

    return (
      <div className="Dashboard">
        <Helmet>
          <title>Dashboard | FoxTrapper&trade;</title>
        </Helmet>

        <Navbar
          landing={false}
          loggedIn={this.state.loggedIn}
          handleLogout={this.state.handleLogout}
        />

        <div id="dashboard-contents">
          {this.state.showMenu ? (
            <Menu handleScreeningSelect={this.handleScreeningSelect} />
          ) : (
            <Fragment></Fragment>
          )}

          {this.state.showImageScreening ? (
            <ImageSearch handleGoBackToMenu={this.handleGoBackToMenu} />
          ) : (
            <Fragment></Fragment>
          )}
        </div>
      </div>
    );
  }
}

export default Dashboard;
