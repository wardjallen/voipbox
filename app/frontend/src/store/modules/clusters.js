import axios from 'axios';

const state = {
  clusters: null,
  cluster: null
};

const getters = {
  stateClusters: state => state.clusters,
  stateCluster: state => state.cluster,
};

const actions = {
  async createCluster({dispatch}, cluster) {
    await axios.post('clusters', cluster);
    await dispatch('getClusters');
  },
  async getClusters({commit}) {
    let {data} = await axios.get('clusters');
    commit('setClusters', data);
  },
  async viewCluster({commit}, id) {
    let {data} = await axios.get(`clusters/${id}`);
    commit('setCluster', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateCluster({}, cluster) {
    await axios.patch(`clusters/${cluster.id}`, cluster.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteCluster({}, id) {
    await axios.delete(`clusters/${id}`);
  }
};

const mutations = {
  setClusters(state, clusters){
    state.clusters = clusters;
  },
  setCluster(state, cluster){
    state.cluster = cluster;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
