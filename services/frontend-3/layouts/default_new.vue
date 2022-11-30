<template>
  <v-container>
    <v-tabs
      v-model="active_tab"
      grow
      background-color="white"
      color="cyan darken-1"
    >
      <v-tab
        v-for="tab of tabs"
        :key="tab.id"
        v-show="tab.enable === 'Y'"
        @click="movePage(tab.id)"
      >
        {{ tab.name }}
      </v-tab>
    </v-tabs>
    <component :is="currentView" :mainId="mainId" :keyId="keyId" />
  </v-container>
</template>

<script>
export default {
  name: 'DefaultLayout',
  // components: {
  //   problemList,
  //   requestList,
  // },

  data() {
    return {
      currentView: 0,
      active_tab: 0,
      tabs: [
        { id: 0, name: '문제관리' },
        { id: 1, name: '요청관리' },
        { id: 2, name: '이슈관리' },
      ],

      // clipped: false,
      // drawer: false,
      // fixed: false,

      // items: [
      //   {
      //     icon: 'mdi-apps',
      //     title: 'Home',
      //     to: '/',
      //   },
      //   {
      //     icon: 'mdi-chart-bubble',
      //     title: '문제관리',
      //     to: '/problemlist',
      //     toPlot: '/problemlist/plot',
      //   },
      //   {
      //     icon: 'mdi-chart-bubble',
      //     title: '요청관리',
      //     to: '/requestlist',
      //   },
      // ],

      // tabs: [
      //   { name: 'table', icon: 'list', path: '/table' },
      //   { name: 'plots', icon: 'playlist_add', path: '/plots' },
      // ],
      // miniVariant: false,
      // right: true,
      // rightDrawer: false,
      // title: 'Lenz Dashboard',

      mainId: '',
      keyId: '',
      selectedTab: 0,
    }
  },
  computed: {
    tab: {
      set(tab) {
        this.$router.replace({ query: { ...this.$route.query, tab } })
      },
      get() {
        return this.$route.query.tab
      },
    },
  },

  created() {
    this.currentView = 0
  },

  mounted() {
    this.active_tab = 0
  },

  methods: {
    movePage(id) {
      this.currentView = id
    },
  },
}
</script>
