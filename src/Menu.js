import React, { Component } from "react";

import Chart from "./Chart.js";

import "./Menu.scss";

class Menu extends Component {
  constructor(props) {
    super();
    this.state = {
      showToken: false,
      apiToken:
        "7vDOXcfVOrgNHjyGOaR0BFC0YTz6PRWKxrGTdbcHmDeQJdE5xlp2VE9U8O6VGU7NGdCpL60wNC3sJAt2eRCQtu4egb4mJnSF0Ui9sRMedZxW6gDkHNrLcPdaVwebfFESRmU8p70K2fRIPpszWKxyeIn9HIAd6jOf0DAC1TAS2R2PB2BcY12HW1X1E7dYNruSJNm4dngF",
      tokenTextareaValue: "*".repeat(200),
      handleScreeningSelect: props.handleScreeningSelect
    };

    this.showHideToken = this.showHideToken.bind(this);
    this.handleShowHide = this.handleShowHide.bind(this);
    this.copyTokenApi = this.copyTokenApi.bind(this);
  }

  showHideToken() {
    if (this.state.showToken) {
      this.setState({ tokenTextareaValue: this.state.apiToken });
    } else {
      this.setState({ tokenTextareaValue: "*".repeat(200) });
    }
  }

  handleShowHide() {
    this.setState({ showToken: !this.state.showToken }, () => {
      this.showHideToken();
    });
  }

  copyTokenApi() {
    let tokenTextareaElement = document.getElementById("api-token");

    this.setState({ showToken: true }, () => {
      this.showHideToken();
      setTimeout(() => {
        tokenTextareaElement.select();
        document.execCommand("copy");
      }, 250);
    });
  }

  render() {
    return (
      <div className="Menu">
        <div id="row-1">
          <div id="daily-reports-choice" className="box">
            <i className="fas fa-file-alt"></i>
            <h2>Daily reports</h2>
          </div>
          <div id="your-api-token-choice" className="box">
            <h2>Your API token:</h2>
            <textarea
              readOnly
              id="api-token"
              value={this.state.tokenTextareaValue}
            ></textarea>
            <div id="api-buttons">
              <i
                id="show-hide-btn"
                className={
                  this.state.showToken ? "fas fa-eye-slash" : "fas fa-eye"
                }
                onClick={this.handleShowHide}
              ></i>
              <i
                id="copy-btn"
                className="fas fa-copy"
                onClick={this.copyTokenApi}
              ></i>
            </div>
          </div>
        </div>
        <div id="row-2">
          <div id="your-requests-choice" className="box">
            <h2>Your requests:</h2>
            <Chart />
          </div>
          <div
            id="manual-reverse-image-search-choice"
            className="box"
            onClick={this.state.handleScreeningSelect}
          >
            <i className="fas fa-search"></i>
            <h2>Manual image screening</h2>
          </div>
        </div>
      </div>
    );
  }
}

export default Menu;
