import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import users from './modules/users';
import clusters from './modules/clusters';
import sites from './modules/sites';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    users,
    clusters,
    sites,
  },
  plugins: [createPersistedState()]
});
