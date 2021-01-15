import React from "react";

import "./Variables.scss";
import "./App.scss";

import Navbar from "./Navbar.js";
import Splash from "./Splash.js";

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      lang: "en",
      running: true
    };
  }

  changeLang = val => {
    this.setState({ lang: val });
    this.setState({ running: false });
    setTimeout(() => {
      this.setState({ running: true });
    }, 10);
  };

  render() {
    const lang = this.state.lang;

    return (
      <div className="App">
        <Navbar lang={this.state.lang} changeLang={this.changeLang} />
        {this.state.running ? (
          <Splash lang={this.state.lang} />
        ) : (
          <React.Fragment></React.Fragment>
        )}
      </div>
    );
  }
}

export default App;
