import Vue from "vue";
import Vuex from "vuex";

import firebase from "firebase";
import db from "../firebase/firebase.js";

Vue.use(Vuex);

let storage = firebase.storage();
let thumbsRef = storage.ref().child("thumbnails");

let thumbnails = {};

// thumbsRef.listAll().then(res => {
//     res.items.forEach(itemRef => {
//         thumbsRef.child(itemRef.name).getDownloadURL().then(url => {
//             thumbnails[itemRef.name] = url
//         });
//     })
// });

export default new Vuex.Store({
  state: {
    loggedIn: false,
    currentUser: "",
    currentUserReports: [],
    lang: "en",
    reportSent: false
  },
  getters: {
    isLoggedIn: state => {
      return state.loggedIn;
    },
    getCurrentUser: state => {
      return state.currentUser;
    },
    getCurrentUserReports: state => {
      return state.currentUserReports;
    },
    getLang: state => {
      return state.lang;
    },
    getReportSent: state => {
      return state.reportSent;
    }
  },
  mutations: {
    reportSentSwitch: state => {
      state.reportSent = !state.reportSent;
    },
    langChange: (state, lang) => {
      state.lang = lang;
    },
    logIn: (state, user) => {
      state.loggedIn = true;
      state.currentUser = user.user.email;
    },
    logOut: state => {
      state.loggedIn = false;
      state.currentUser = "";
    },
    refresh: (state, currentUser) => {
      state.loggedIn = true;
      state.currentUser = currentUser;
    },
    fetchReports: (state, currentUser) => {
      state.currentUserReports = [];

      db.collection("reports")
        .where("users", "array-contains", state.currentUser)
        .orderBy("name")
        .get()
        .then(qS =>
          qS.forEach(doc => {
            state.currentUserReports.push({
              component: doc.data().component,
              name: doc.data().name,
              id: doc.id,
              description: doc.data().description,
              thumbUrl: doc.data().thumbUrl,
              ready: doc.data().ready
            });
          })
        );
    }
  }
});
