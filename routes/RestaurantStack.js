import React, { useState } from "react";

import { createStackNavigator } from "react-navigation-stack";
import { createAppContainer } from "react-navigation";

import Main from "../components/Main.js";
import Restaurant from "../components/Restaurant.js";
import TopBar from "../components/TopBar.js";

const screens = {
  Main: {
    screen: Main,
    navigationOptions: {
      headerTitle: () => <TopBar title="KasPietums?" />
    }
  },
  Restaurant: {
    screen: Restaurant,
    navigationOptions: ({ navigation }) => {
      return {
        headerTitle: () => <TopBar title={navigation.getParam("name")} />
      };
    }
  }
};

const RestaurantStack = createStackNavigator(screens);

export default createAppContainer(RestaurantStack);
