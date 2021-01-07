import React, { useState } from "react";
import {
  StyleSheet,
  View,
  Text,
  Image,
  ScrollView,
  TouchableOpacity
} from "react-native";
import { Linking } from "expo";

import axios from "axios";

import Loading from "./Loading.js";

export default function Restaurant({ navigation }) {
  const [appLoaded, setAppLoaded] = useState(false);
  const [restaurantDetails, setRestaurantDetails] = useState({});

  const URL = navigation.getParam("url");

  async function loadApp() {
    await axios.get(URL).then(res => {
      setRestaurantDetails(res.data);
    });
  }

  if (appLoaded) {
    return (
      <View style={styles.container}>
        <TouchableOpacity
          style={styles.imageContainer}
          onPress={() => {
            Linking.openURL(restaurantDetails["image"]);
          }}
        >
          <Image
            style={styles.image}
            source={{ uri: restaurantDetails["image"] }}
          />
        </TouchableOpacity>
        <View style={styles.textBox}>
          <ScrollView>
            <Text style={styles.text}>{restaurantDetails["time"]}:</Text>
            <br />
            <Text style={styles.text}>{restaurantDetails["text"]}</Text>
          </ScrollView>
        </View>
      </View>
    );
  } else {
    return <Loading loadApp={loadApp} setAppLoaded={setAppLoaded} />;
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#a32020",
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
    height: "100%",
    padding: "1.25rem"
  },
  textBox: {
    backgroundColor: "#133337",
    width: "100%",
    borderRadius: 10,
    marginTop: "1.25rem",
    maxHeight: "50%",
    padding: "1rem",
    borderColor: "black",
    borderStyle: "solid",
    borderWidth: 2
  },
  text: {
    color: "#f0f8ff",
    fontFamily: "montserrat"
  },
  imageContainer: {
    borderColor: "#eb8c00",
    borderStyle: "solid",
    borderWidth: 2,
    borderRadius: 10,
    width: "100%",
    height: "50%"
  },
  image: {
    backgroundColor: "#f0f8ff",
    widht: "100%",
    height: "100%",
    borderRadius: 10
  }
});
