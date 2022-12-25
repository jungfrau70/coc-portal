<template>
  <v-container>
    <UserSignup />
  </v-container>
</template>

<script>
import UserSignup from '~/components/UserSignup.vue'

export default {
  name: 'InspirePage',
  components: {
    UserSignup,
  },
}
</script>