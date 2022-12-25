<template>
  <v-container>
    <HomeView />
    <!-- <Navbar /> -->
  </v-container>
</template>

<script>
// import Navbar from '../components/Navbar.vue'
import HomeView from '~/components/HomeView.vue'

export default {
  name: 'InspirePage',
  components: {
    HomeView,
    // Navbar,
  },
}
</script>