import React, { Component } from "react";
import "./Splash.scss";

class Splash extends Component {
  render() {
    return (
      <div className="Splash">
        <div id="splash-content">
          <div id="left">
            <h1>AI based insurance claims fraud prevention</h1>
            <p>
              FoxTrapper&trade; is a computer vision enabled service that
              screens any given image for dublicates within search engine
              results and a variety of custom datasets.
            </p>
            <h3>Our partners:</h3>
            <div id="parners">
              <a href="http://www.gjensidige.lt" target="_blank">
                <img
                  className="partner"
                  src="gjensidige-logo.png"
                  alt="Gjensidige logo"
                />
              </a>
            </div>
          </div>
          <div id="right">
            <img src="/hiker.png" alt="hiker" />
          </div>
        </div>
      </div>
    );
  }
}

export default Splash;
