import React from "react";

import "./Variables.scss";
import "./Navbar.scss";

class Navbar extends React.Component {
  constructor(props) {
    super();
    this.handleChange = this.handleChange.bind(this);

    this.state = {
      lang: props.lang,
      changeLang: props.changeLang,
      strings: {
        en: {
          about: "About us",
          governance: "Governance",
          projects: "Projects"
        },
        lt: {
          about: "Apie mus",
          governance: "Valdymas",
          projects: "Projektai"
        },
        no: {
          about: "Om oss",
          governance: "Styresett",
          projects: "Prosjekter"
        }
      }
    };
  }

  handleChange(e) {
    this.setState({ lang: e.target.value });
    this.state.changeLang(e.target.value);
  }

  render() {
    const lang = this.state.lang;

    return (
      <div className="Navbar">
        <div id="navbar-contents">
          <div id="logo-div">
            <a href="#navbar">
              <img src="/logo.png" alt="logo" />
            </a>
          </div>
          <div id="menu-div">
            <div id="menu">
              <ul>
                <a href="#about">
                  <li>{this.state.strings[lang]["about"]}</li>
                </a>
                <a href="#governance">
                  <li>{this.state.strings[lang]["governance"]}</li>
                </a>
                <a href="#projects">
                  <li>{this.state.strings[lang]["projects"]}</li>
                </a>
              </ul>
            </div>
            <div id="lang">
              <select value={lang} onChange={this.handleChange}>
                <option value="en">EN</option>
                <option value="lt">LT</option>
                <option value="no">NO</option>
              </select>
              <img src={`/flags/${lang}.png`} alt="language icon" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Navbar;
