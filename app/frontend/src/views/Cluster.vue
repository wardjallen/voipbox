<template>
  <div v-if="cluster">
    <p><strong>Cluster Name:</strong> {{ cluster.clusterName }}</p>
      <p><router-link :to="{name: 'EditCluster', params:{id: cluster.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeCluster()" class="btn btn-secondary">Delete</button></p>
  </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Cluster',
  props: ['id'],
  async created() {
    try {
      await this.viewCluster(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ cluster: 'stateCluster', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewCluster', 'deleteCluster']),
    async removeCluster() {
      try {
        await this.deleteCluster(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    }
  },
};
</script>
