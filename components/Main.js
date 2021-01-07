import React, { useState } from "react";
import { StyleSheet, View } from "react-native";

import RestaurantList from "./RestaurantList.js";
import BottomMenu from "./BottomMenu.js";
import Loading from "./Loading.js";

import axios from "axios";

export default function Main({ navigation }) {
  const [favourites, setFavourites] = useState(false);
  const [searchString, setSearchString] = useState("");
  const [appLoaded, setAppLoaded] = useState(false);
  const [restaurants, setRestaurants] = useState({});

  const URL = "https://kur-pietaut.herokuapp.com/restaurants";

  async function loadApp() {
    await axios.get(URL).then(res => {
      setRestaurants(res.data);
    });
  }

  const openRestaurant = restaurant => {
    navigation.navigate("Restaurant", restaurant);
  };

  if (appLoaded) {
    return (
      <View style={styles.container}>
        {/* <TopBar /> */}
        <RestaurantList
          searchString={searchString}
          setSearchString={setSearchString}
          restaurants={restaurants}
          favourites={favourites}
          openRestaurant={openRestaurant}
        />
        <BottomMenu
          favourites={favourites}
          setFavourites={setFavourites}
          setSearchString={setSearchString}
        />
      </View>
    );
  } else {
    return <Loading loadApp={loadApp} setAppLoaded={setAppLoaded} />;
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#a32020"
  }
});
