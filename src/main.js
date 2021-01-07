import Vue from "vue";
import VueRouter from "vue-router";
import firebase from "firebase";

import store from "./store/store.js";

import App from "./App.vue";
import Landing from "./Landing.vue";
import Login from "./Login.vue";
import Dashboard from "./Dashboard.vue";
import VmiEds from "./templates/VmiEds.vue";
import EmployeeHiring from "./templates/EmployeeHiring.vue";

Vue.use(VueRouter);

const routes = [
  {
    name: "landing",
    path: "/",
    component: Landing
    //  meta: {
    //    requiresGuest: true
    //   }
  },
  {
    name: "login",
    path: "/login",
    component: Login,
    meta: {
      requiresGuest: true
    }
  },
  {
    name: "dashboard",
    path: "/dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: "VmiEds",
    path: "/VmiEds",
    component: VmiEds,
    meta: {
      requiresAuth: true
    }
  },
  {
    name: "EmployeeHiring",
    path: "/EmployeeHiring",
    component: EmployeeHiring,
    meta: {
      requiresAuth: true
    }
  }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

// Nav Guard
router.beforeEach((to, from, next) => {
  // Check for requiresAuth guard
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Check if NO logged user
    if (!firebase.auth().currentUser) {
      // Go to login
      next({
        path: "/login",
        query: {
          redirect: to.fullPath
        }
      });
    } else {
      // Proceed to route
      next();
    }
  } else if (to.matched.some(record => record.meta.requiresGuest)) {
    // Check if NO logged user
    if (firebase.auth().currentUser) {
      // Go to login
      next({
        path: "/dashboard",
        query: {
          redirect: to.fullPath
        }
      });
    } else {
      // Proceed to route
      next();
    }
  } else {
    // Proceed to route
    next();
  }
});

let app;

firebase.auth().onAuthStateChanged(user => {
  if (!app) {
    app = new Vue({
      el: "#app",
      router,
      store,
      render: h => h(App)
    });
  }
});
