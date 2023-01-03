<template>
  <v-app>
    <JwtLogin />
  </v-app>
</template>

<script>
import JwtLogin from '@/components/JwtLogin.vue'
export default {
  components: {
    JwtLogin,
  },
}
</script>
