export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "Spark Lenz",
    htmlAttrs: {
      lang: "kr",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: "클라우드 운영/관리",
      },
    ],
    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
      {
        rel: "stylesheet",
        href: "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css",
        integrity: "sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N",
        crossorigin: "anonymous"
      },
      {
        rel: "stylesheet",
        href: "https://pyscript.net/latest/pyscript.css",
      },
    ],
    script: [
      {
        defer: "",
        src: "https://use.fontawesome.com/releases/v5.15.4/js/all.js",
      },
      // {
      //   defer: "",
      //   src: "https://pyscript.net/latest/pyscript.js",
      // },
    ],
  },


  // Customize the progress-bar color
  loading: { color: "#fff" },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    // "~/node_modules/bootstrap/dist/css/bootstrap.css",
    // "~/node_modules/datatables.net-bs4/css/dataTables.bootstrap4.css",
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: ["@nuxtjs/vuetify"],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    "@nuxtjs/auth-next",
    "@nuxtjs/axios",
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/bootstrap
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: "http://localhost:8000",
  },

  auth: {
    strategies: {
      local: {
        scheme: "refresh",
        localStorage: {
          prefix: "auth.",
        },
        token: {
          prefix: "access_token.",
          property: "access_token",
          maxAge: 86400,
          type: "Bearer",
        },
        refreshToken: {
          prefix: "refresh_token.",
          property: "refresh_token",
          data: "refresh_token",
          maxAge: 60 * 60 * 24 * 15,
        },
        user: {
          property: "user",
          autoFetch: true,
        },
        endpoints: {
          login: { url: "/account/login", method: "post" },
          // refresh: { url: '/token/refresh/', method: 'post' },
          user: { url: "/account/user", method: "get" },
          // logout: { url: '/logout', method: 'post'}
        },
      },
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  
  publicRuntimeConfig: {
    apiURL: process.env.API_URL
  }
};
