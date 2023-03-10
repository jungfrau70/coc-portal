<template>
  <v-container>
    <UserLogin />
  </v-container>
</template>

<script>
import UserLogin from '~/components/UserLogin.vue'

export default {
  name: 'InspirePage',
  components: {
    UserLogin,
  },
}
</script>

