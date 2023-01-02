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
        <!-- <nav-footer />         -->
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
    <!-- <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer> -->
  </v-app>
</template>

<script>
// import NavFooter from './NavFooter.vue'

export default {
  components: {
    // NavFooter,
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
          icon: 'mdi-account-multiple',
          title: 'Discussion(Summary)',
          to: '/discussion/list',
        },
        {
          icon: 'mdi-alert-octagon',
          title: 'Incident Handling',
          to: '/management-incident/list',
        },
        {
          icon: 'mdi-alert-outline',
          title: 'Issue',
          to: '/management-issue/list',
        },
        {
          icon: 'mdi-ambulance',
          title: 'Problem',
          to: '/management-problem/list',
        },
        {
          icon: 'mdi-key-change',
          title: 'Change',
          to: '/management-change/list',
        },
        {
          icon: 'mdi-import',
          title: 'Request',
          to: '/management-request/list',
        },
        {
          icon: 'mdi-magnify-plus',
          title: 'Capacity',
          to: '/management-capacity/list',
        },
        {
          icon: 'mdi-content-save-all',
          title: 'Backup',
          to: '/management-backup/list',
        },
        {
          icon: 'mdi-numeric-1-box-multiple-outline',
          title: 'Instance',
          to: '/inventory-instance/list',
        },
        {
          icon: 'mdi-numeric-2-box-multiple-outline',
          title: 'Kubernetes',
          to: '/inventory-kubernetes/list',
        },
        {
          icon: 'mdi-numeric-3-box-multiple-outline',
          title: 'Database',
          to: '/inventory-database/list',
        },
        {
          icon: 'mdi-numeric-4-box-multiple-outline',
          title: 'License',
          to: '/inventory-license/list',
        },
        {
          icon: 'mdi-lock-plus',
          title: 'Vulnerability(Security)',
          to: '/vulnerability/list',
        },
        {
          icon: 'mdi-wrench',
          title: 'Preventive(PM)',
          to: '/preventive/list',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Lenz Portal',
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
