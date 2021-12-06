import Vue from 'vue';
import VueRouter from 'vue-router';

import store from '@/store'

import Dashboard from '@/views/Dashboard';
import EditCluster from '@/views/EditCluster';
import Home from '@/views/Home.vue';
import Login from '@/views/Login';
import Cluster from '@/views/Cluster';
import Profile from '@/views/Profile';
import Register from '@/views/Register';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {requiresAuth: true},
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {requiresAuth: true},
  },
  {
    path: '/clusters/:id',
    name: 'Cluster',
    component: Cluster,
    meta: {requiresAuth: true},
    props: true,
  },
  {
    path: '/clusters/:id',
    name: 'EditCluster',
    component: EditCluster,
    meta: {requiresAuth: true},
    props: true,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;


