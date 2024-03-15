import { createWebHistory, createRouter } from "vue-router";

import Home from "../pages/Home.vue";
import Play from "../pages/Play.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/play",
    component: Play,
  },
];

const router = createRouter({
  // https://router.vuejs.org/guide/
  history: createWebHistory(),
  routes,
});

export default router;
