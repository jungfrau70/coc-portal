<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title ma-0 pa-0 auto>{{
              item.title
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>mdi-application</v-icon>
      </v-btn>
      <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>mdi-minus</v-icon>
      </v-btn>

      <v-toolbar-title>{{ title }}</v-toolbar-title>
      <v-spacer />
      <!-- <v-tabs color="deep-purple accent-4" left flat>
        <v-tab nuxt>리스트</v-tab>
        <v-tab nuxt>챠트</v-tab>
      </v-tabs> -->
      <!-- <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn> -->
      <section>
        <div v-if="isLoggedIn" id="logout">
          <p id="logout">
            Click <a href="/dashboard">here</a> to view all notes.
          </p>
        </div>
        <p v-else>
          <span><a href="/register">Register</a></span>
          <span> or </span>
          <span><a href="/login">Log In</a></span>
        </p>
      </section>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light> mdi-repeat </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Home',
          to: '/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '인시던트핸들링',
          to: '/incident/list',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '이슈관리',
          to: '/issue/list',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '장애관리',
          to: '/problem/list',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '변경관리',
          to: '/change/list',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '요청관리',
          to: '/request/list',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '..,',
          to: '/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: '보고서',
          to: '/jupyterlite',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Spark Lenz',
    }
  },
  computed: {
    isLoggedIn: function () {
      // return this.$store.getters.isAuthenticated
      return null;
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logOut')
      this.$router.push('/login')
    },
  },
}
</script>
