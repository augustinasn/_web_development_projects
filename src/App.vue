<template>
  <div id="app">
    <transition name="router-anim" enter-active-class="animated fadeIn">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  name: "app",
  created() {
    if (firebase.auth().currentUser) {
      this.$store.commit("refresh", firebase.auth().currentUser.email);
    }
  }
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

$main-font: "Montserrat", sans-serif;
$black-text-color: #133337;
$black-text-color-alt: #2c4c50;
$black-text-color-alt-2: #242f3e;
$white-text-color: #f5f5f5;
$emphasis-color: #ffd700;
$emphasis-color-alt: #ffa500;

html,
body {
  background: $black-text-color-alt !important;
  color: $white-text-color !important;
  font-family: $main-font;
  scroll-behavior: smooth;
}
</style>
