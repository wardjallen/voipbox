import axios from 'axios';

const state = {
  sites: null,
  site: null
};

const getters = {
  stateSites: state => state.sites,
  stateSite: state => state.site,
};

const actions = {
  async createSite({dispatch}, site) {
    await axios.post('sites', site);
    await dispatch('getSites');
  },
  async getSites({commit}) {
    let {data} = await axios.get('sites');
    commit('setSites', data);
  },
  async viewSite({commit}, id) {
    let {data} = await axios.get(`sites/${id}`);
    commit('setSite', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateSite({}, site) {
    await axios.patch(`sites/${site.id}`, site.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteSite({}, id) {
    await axios.delete(`sites/${id}`);
  }
};

const mutations = {
  setSites(state, sites){
    state.sites = sites;
  },
  setSite(state, site){
    state.site = site;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
