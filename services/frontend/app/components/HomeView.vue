<template>
  <div class="container">
    <header class="jumbotron">
      <h3>{{ content }}</h3>
    </header>
    <CompanyIntro />
  </div>
</template>
  
<script>
// import Tutorial from './Tutorial.vue'
import CompanyIntro from './CompanyIntro.vue'
// import UserService from '~/services/user.service'

export default {
  name: 'HomeView',
  components: {
    CompanyIntro
  },
  data() {
    return {
      content: '',
    }
  },
  mounted() {
    // UserService.getPublicContent().then(
    //   (response) => {
    //     this.content = response.data
    //   },
    //   (error) => {
    //     this.content =
    //       (error.response && error.response.data) ||
    //       error.message ||
    //       error.toString()
    //   }
    // )
  },
}
</script>