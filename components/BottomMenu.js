import React from "react";
import { StyleSheet, View, Text, TouchableOpacity } from "react-native";

export default function BottomMenu(props) {
  return (
    <View style={styles.container}>
      <TouchableOpacity
        style={props.favourites ? styles.button : styles.buttonPressed}
        onPress={() => {
          props.setFavourites(false);
          props.setSearchString("");
        }}
      >
        <Text style={styles.text}>Visi</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={props.favourites ? styles.buttonPressed : styles.button}
        onPress={() => {
          props.setFavourites(true);
          props.setSearchString("");
        }}
      >
        <Text style={styles.text}>Mėgstamiausi</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#133337",
    flexDirection: "row",
    width: "100%",
    justifyContent: "center"
  },
  button: {
    width: "50%",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#133337"
  },
  buttonPressed: {
    width: "50%",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#eb8c00"
  },
  text: {
    fontSize: 15,
    color: "#f0f8ff",
    fontFamily: "montserrat"
  }
});
