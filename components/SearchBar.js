import React, { Fragment } from "react";
import { StyleSheet, View, TextInput } from "react-native";

import { AntDesign } from "@expo/vector-icons";

export default function SearchBar(props) {
  return !props.favourites ? (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        onChangeText={val => props.setSearchString(val)}
        value={props.searchString}
        type="text"
      />
      <AntDesign name="search1" style={styles.icon} size={32} />
    </View>
  ) : (
    <Fragment></Fragment>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    backgroundColor: "#602320",
    alignItems: "center",
    justifyContent: "center",
    width: "100%",
    padding: "1.25rem"
  },
  input: {
    flex: 9,
    backgroundColor: "#f0f8ff",
    borderRadius: 5,
    height: "3rem",
    padding: "1rem",
    fontSize: 15,
    fontFamily: "montserrat"
  },
  icon: {
    marginLeft: "1rem",
    flex: 1,
    color: "#eb8c00"
  }
});
