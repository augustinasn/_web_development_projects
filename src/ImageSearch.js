import React, { Component, Fragment } from "react";
import { Helmet } from "react-helmet";
import axios from "axios";

import "./ImageSearch.scss";

class ImageSearch extends Component {
  constructor(props) {
    super();
    this.state = {
      file: null,
      imgUrl: "",
      handleGoBackToMenu: props.handleGoBackToMenu,
      loading: false
    };

    this.handleOnChange = this.handleOnChange.bind(this);
    this.handleOnSubmit = this.handleOnSubmit.bind(this);
    this.handleRunScreening = this.handleRunScreening.bind(this);
  }

  handleOnChange(e) {
    this.setState({ file: e.target.files[0] });
    const imgUrl = URL.createObjectURL(e.target.files[0]);
    this.setState({ imgUrl: imgUrl });
  }

  handleOnSubmit(e) {
    e.preventDefault();

    document.getElementById("image-select").click();
  }

  handleRunScreening() {
    this.setState({ loading: true });
    this.printToConsole("Attempting a reverse image search...");

    let searchUrl = "https://foxtrapper-api.herokuapp.com/web_search";

    let formData = new FormData();
    formData.append("file", this.state.file);
    let config = {
      headers: {
        "content-type": "multipart/form-data"
      }
    };

    axios.post(searchUrl, formData, config).then(res => {
      res.data.forEach(i => {
        let key = Object.keys(i)[0];
        let val = i[key];

        this.printToConsole(key + " " + val);
      });

      this.setState({ loading: false });
    });
  }

  getTimestamp() {
    let now = new Date(Date.now());

    let hour = now.getHours();
    let min = now.getMinutes();
    let sec = now.getSeconds();

    let timestamp = hour + ":" + min + ":" + sec;

    return timestamp;
  }

  printToConsole(content) {
    let node = document.createElement("span");
    let timestamp = this.getTimestamp();
    let textNode = document.createTextNode("[" + timestamp + "]: " + content);

    node.appendChild(textNode);
    document.getElementById("console-content").appendChild(node);
  }

  componentDidMount() {
    this.printToConsole("Checking server status...");

    let serverStatus = "Server is not responding.";

    axios.get("https://foxtrapper-api.herokuapp.com/").then(res => {
      serverStatus = res.data;
      this.printToConsole(serverStatus);
    });
  }

  render() {
    return (
      <div className="ImageSearch box">
        <Helmet>
          <title>Image Screening | FoxTrapper&trade;</title>
        </Helmet>

        <div id="col-1">
          <div id="img-upload-div">
            <div
              id="img-div"
              style={{
                backgroundImage: "url(" + this.state.imgUrl + ")"
              }}
            >
              {this.state.imgUrl === "" ? (
                <div id="no-image">
                  <i className="fas fa-image"></i>
                  <span>No image is selected.</span>
                </div>
              ) : (
                <Fragment></Fragment>
              )}
            </div>
            <div id="file-input-div">
              <form onSubmit={this.handleOnSubmit}>
                <input
                  type="file"
                  name="image-select"
                  id="image-select"
                  onChange={this.handleOnChange}
                />
                <input
                  type="submit"
                  name="image-upload"
                  id="image-upload"
                  className="btn-regular"
                  value="Browse"
                />
              </form>
            </div>
          </div>
          <div id="buttons-div">
            <button
              id="run-screening"
              className="btn-regular"
              onClick={
                this.state.imgUrl === ""
                  ? console.log("Image not selected")
                  : this.handleRunScreening
              }
              style={
                this.state.imgUrl === "" || this.state.loading
                  ? { background: "grey", cursor: "not-allowed" }
                  : {}
              }
            >
              {this.state.loading ? "Loading..." : "Run screening"}
            </button>
            <button
              id="go-back"
              className="btn-regular"
              onClick={this.props.handleGoBackToMenu}
            >
              Go back
            </button>
          </div>
        </div>
        <div id="col-2">
          <div id="console">
            <div id="console-content"></div>
          </div>
        </div>
      </div>
    );
  }
}

export default ImageSearch;
