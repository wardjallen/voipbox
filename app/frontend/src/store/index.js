import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import users from './modules/users';
import clusters from './modules/clusters';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    users,
    clusters,
  },
  plugins: [createPersistedState()]
});
