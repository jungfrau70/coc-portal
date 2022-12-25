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
      <div v-if="isLoggedIn">
        <nuxt-link to="/auth/logout">Logout</nuxt-link>
      </div>
      <div v-else>
        <nuxt-link to="/auth/login">LogIn</nuxt-link>
        <span> or </span>
        <nuxt-link to="/auth/signup">SignUp</nuxt-link>
      </div>

      <!-- <v-container>
          <div v-if="isLoggedIn" id="logout">
          <nuxt-link to="/logout">Logout</nuxt-link>
        </div>
        <p v-else>
          <nuxt-link to="/register">Sign-in</nuxt-link>
          <span> or </span>
          <nuxt-link to="/login">Log In</nuxt-link>
        </p>
        </v-container> -->

      <!-- <div class="navbar-end">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link"> My Account </a>
          <div class="navbar-dropdown">
            <nuxt-link class="navbar-item" to="/profile">My Profile</nuxt-link>
            <hr class="navbar-divider" />
            <a class="navbar-item">Logout</a>
          </div>
        </div>
        <template>
          <nuxt-link class="navbar-item" to="/register">Register</nuxt-link>
          <nuxt-link class="navbar-item" to="/login">Log In</nuxt-link>
        </template>
      </div> -->
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
// import HomeView from '../views/HomeView.vue'

export default {
  name: 'DefaultLayout',
  components: {
    // HomeView,
  },
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
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: '이슈관리',
        //   to: '/issue/list',
        // },
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: '장애관리',
        //   to: '/problem/list',
        // },
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: '변경관리',
        //   to: '/change/list',
        // },
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: '요청관리',
        //   to: '/request/list',
        // },
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: '..,',
        //   to: '/',
        // },
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: '보고서',
        //   to: '/jupyterlite',
        // },
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
      return null
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logOut')
      this.$router.push('/auth/login')
    },
  },
}
</script>
