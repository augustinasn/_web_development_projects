import React, { Fragment } from "react";
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  TouchableWithoutFeedback,
  Keyboard
} from "react-native";

import SearchBar from "./SearchBar.js";

import { FontAwesome } from "@expo/vector-icons";

const isIn = (strOne, strTwo) => {
  let strTwoParsed = strTwo.toLowerCase().replace(/\s/g, "");

  let ltChars = [
    ["ą", "a"],
    ["č", "c"],
    ["ę", "e"],
    ["ė", "e"],
    ["į", "i"],
    ["š", "s"],
    ["ų", "u"],
    ["ū", "u"],
    ["ž", "z"]
  ];

  ltChars.forEach(charPair => {
    while (strTwoParsed.indexOf(charPair[0]) !== -1) {
      strTwoParsed = strTwoParsed.replace(charPair[0], charPair[1]);
    }
  });

  if (strOne.indexOf(strTwoParsed) !== -1) {
    return true;
  } else {
    return false;
  }
};

export default function RestaurantList({
  searchString,
  setSearchString,
  restaurants,
  favourites,
  openRestaurant
}) {
  let restaurantNames = Object.keys(restaurants);

  return (
    <TouchableWithoutFeedback onPress={() => Keyboard.dismiss()}>
      <View style={styles.container}>
        <SearchBar
          favourites={favourites}
          searchString={searchString}
          setSearchString={setSearchString}
        />
        <ScrollView style={styles.list}>
          {restaurantNames.map(item => {
            return isIn(restaurants[item]["search_string"], searchString) ||
              searchString == "" ? (
              <TouchableOpacity
                key={restaurants[item]["key"]}
                style={
                  favourites && restaurants[item]["favourite"] == 0
                    ? styles.itemInvisible
                    : styles.itemVisible
                }
                onPress={() => {
                  openRestaurant(restaurants[item]);
                }}
              >
                <Text style={styles.text}>{restaurants[item]["name"]}</Text>
                <FontAwesome
                  name="star"
                  size={25}
                  style={
                    restaurants[item]["favourite"] == 1
                      ? styles.iconVisible
                      : styles.iconInvisible
                  }
                />
              </TouchableOpacity>
            ) : (
              <Fragment key={restaurants[item]["key"]}></Fragment>
            );
          })}
        </ScrollView>
      </View>
    </TouchableWithoutFeedback>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 9,
    alignItems: "center",
    backgroundColor: "#a32020",
    width: "100%"
  },
  list: {
    padding: "1.25rem",
    width: "100%"
  },
  itemVisible: {
    backgroundColor: "#e0301e",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    width: "100%",
    height: "5rem",
    marginBottom: "1.25rem",
    borderRadius: 10,
    padding: "1rem"
  },
  itemInvisible: {
    display: "none"
  },
  text: {
    color: "#f0f8ff",
    fontSize: 18,
    fontFamily: "montserrat"
  },
  iconVisible: {
    color: "#eb8c00"
  },
  iconInvisible: {
    color: "#eb8c00",
    opacity: 0
  }
});
