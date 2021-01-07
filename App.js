import React, { useState } from "react";
import { AppLoading } from "expo";
import * as Font from "expo-font";

import Navigator from "./routes/RestaurantStack.js";
import Loading from "./components/Loading.js";

export default function App() {
  const [appLoaded, setAppLoaded] = useState(false);

  async function loadApp() {
    await Font.loadAsync({
      montserrat: require("./assets/Montserrat-Regular.ttf")
    });
  }

  if (appLoaded) {
    return <Navigator />;
  } else {
    return <Loading loadApp={loadApp} setAppLoaded={setAppLoaded} />;
  }
}
