import React, { useState } from "react";
import { StyleSheet, View, Text, Image } from "react-native";
import { AppLoading } from "expo";

export default function Loading({ loadApp, setAppLoaded }) {
  return (
    <View style={styles.container}>
      <View style={styles.loading}>
        <AppLoading startAsync={loadApp} onFinish={() => setAppLoaded(true)} />
        <Image
          style={styles.loading}
          source={require("../assets/loading.gif")}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    height: "100%",
    width: "100%",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#a32020"
  },
  loading: {
    width: 100,
    height: 100
  }
});
