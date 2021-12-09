<template>
  <div>
    <section>
  <div v-if="cluster">
    <p><strong>Cluster Name:</strong> {{ cluster.clusterName }}</p>
      <p><router-link :to="{name: 'EditCluster', params:{id: cluster.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeCluster()" class="btn btn-secondary">Delete</button></p>
  </div>
  </section>
  <br/><br/>

      <section>
      <h1>Sites</h1>
      <hr/><br/>

      <!-- <div v-if="sites.length">
        <div v-for="site in sites" :key="site.id" class="sites">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Site Name:</strong> {{ site.siteName }}</li>
                <li><router-link :to="{name: 'Site', params:{id: site.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div> -->
    </section>
  <br/><br/>

      <section>
      <h1>Add new site</h1>
      <hr/><br/>
      </section>

  

 </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Cluster',
  props: ['id'],
  data() {
    return {
      form: {
        siteName: '',
      },
    };
  },
  async created() {
    try {
      await this.viewCluster(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ cluster: 'stateCluster', user: 'stateUser', sites: 'stateSites'}),
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
