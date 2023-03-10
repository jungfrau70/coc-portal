<template>
  <v-app>
    <v-card>
      <v-tabs>
        <v-tab to="/discussion/list">리스트</v-tab>
        <v-tab to="/discussion/graph">그래프</v-tab>
        <v-tab to="/discussion/dashboard">대시보드</v-tab>
        <v-tab to="/discussion/analyzer">분석기</v-tab>
      </v-tabs>
      <nuxt-child />
    </v-card>
    <v-card>
      <vegaEmbed />
    </v-card>
  </v-app>
</template>

<script>
import vegaEmbed from '~/components/HelloAltair.vue'

export default {
  components: { vegaEmbed },
}
</script>