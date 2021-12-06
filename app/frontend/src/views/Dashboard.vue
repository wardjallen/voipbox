<template>
  <div>
    <section>
      <h1>Add new cluster</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="clusterName" class="form-label">Cluster Name:</label>
          <input type="text" name="clusterName" v-model="form.clusterName" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="clusterAxlUsername" class="form-label">Axl User Name:</label>
          <input type="text" name="clusterAxlUsername" v-model="form.clusterAxlUsername" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="clusterAxlPassword" class="form-label">Axl Password:</label>
          <input type="password" name="clusterAxlPassword" v-model="form.clusterAxlPassword" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Clusters</h1>
      <hr/><br/>

      <div v-if="clusters.length">
        <div v-for="cluster in clusters" :key="cluster.id" class="clusters">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Cluster Name:</strong> {{ cluster.clusterName }}</li>
                <li><router-link :to="{name: 'Cluster', params:{id: cluster.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Dashboard',
  data() {
    return {
      form: {
        clusterName: '',
        clusterAxlUsername: '',
        clusterAxlPassword: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getClusters');
  },
  computed: {
    ...mapGetters({ clusters: 'stateClusters'}),
  },
  methods: {
    ...mapActions(['createCluster']),
    async submit() {
      await this.createCluster(this.form);
    },
  },
};
</script>
