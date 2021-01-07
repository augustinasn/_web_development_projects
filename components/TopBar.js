import React from "react";
import { StyleSheet, Text, View } from "react-native";

import { MaterialCommunityIcons } from "@expo/vector-icons";

export default function TopBar(props) {
  return (
    <View style={styles.container}>
      <MaterialCommunityIcons
        name="silverware-fork-knife"
        style={styles.icon}
        size={20}
      />
      <Text style={styles.text}>{props.title}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: "row"
  },
  text: {
    fontSize: 20,
    color: "#133337",
    fontFamily: "montserrat"
  },
  icon: { marginRight: "0.5rem", color: "#602320" }
});
