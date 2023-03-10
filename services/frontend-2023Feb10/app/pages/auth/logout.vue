<template>
  <v-container>
    <UserLogout />
  </v-container>
</template>

<script>
import UserLogout from '~/components/UserLogout.vue'

export default {
  name: 'InspirePage',
  components: {
    UserLogout,
  },
}
</script>