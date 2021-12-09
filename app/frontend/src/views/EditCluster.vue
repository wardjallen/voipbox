<template>
  <section>
    <h1>Edit cluster</h1>
    <hr/><br/>

    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="clusterName" class="form-label">Cluster Name:</label>
        <input type="text" name="clusterName" v-model="form.clusterName" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="clusterAxlUsername" class="form-label">Axl Username:</label>
        <input type="text" name="clusterAxlUsername" v-model="form.clusterAxlUsername" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="clusterAxlPassword" class="form-label">Axl Password:</label>
        <input type="text" name="clusterAxlPassword" v-model="form.clusterAxlPassword" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'EditCluster',
  props: ['id'],
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
    this.GetCluster();
  },
  computed: {
    ...mapGetters({ cluster: 'stateCluster' }),
  },
  methods: {
    ...mapActions(['updateCluster', 'viewCluster']),
    async submit() {
    try {
      let cluster = {
        id: this.id,
        form: this.form,
      };
      await this.updateCluster(cluster);
      this.$router.push({name: 'Cluster', params:{id: this.cluster.id}});
    } catch (error) {
      console.log(error);
    }
    },
    async GetCluster() {
      try {
        await this.viewCluster(this.id);
        this.form.title = this.cluster.title;
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    }
  },
};
</script>
