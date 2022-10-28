import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _410d206c = () => interopDefault(import('..\\pages\\backup\\index.vue' /* webpackChunkName: "pages/backup/index" */))
const _4eca21be = () => interopDefault(import('..\\pages\\change\\index.vue' /* webpackChunkName: "pages/change/index" */))
const _30411613 = () => interopDefault(import('..\\pages\\database\\index.vue' /* webpackChunkName: "pages/database/index" */))
const _31679348 = () => interopDefault(import('..\\pages\\incident\\index.vue' /* webpackChunkName: "pages/incident/index" */))
const _5943028e = () => interopDefault(import('..\\pages\\instance\\index.vue' /* webpackChunkName: "pages/instance/index" */))
const _59498f6d = () => interopDefault(import('..\\pages\\issue\\index.vue' /* webpackChunkName: "pages/issue/index" */))
const _215e0e68 = () => interopDefault(import('..\\pages\\kubernetes\\index.vue' /* webpackChunkName: "pages/kubernetes/index" */))
const _17468edd = () => interopDefault(import('..\\pages\\login\\index.vue' /* webpackChunkName: "pages/login/index" */))
const _695558b8 = () => interopDefault(import('..\\pages\\logout\\index.vue' /* webpackChunkName: "pages/logout/index" */))
const _28b1eee7 = () => interopDefault(import('..\\pages\\problem\\index.vue' /* webpackChunkName: "pages/problem/index" */))
const _bb0b03fc = () => interopDefault(import('..\\pages\\regularcheck\\index.vue' /* webpackChunkName: "pages/regularcheck/index" */))
const _1b9768f7 = () => interopDefault(import('..\\pages\\request\\index.vue' /* webpackChunkName: "pages/request/index" */))
const _6eaa59a4 = () => interopDefault(import('..\\pages\\security\\index.vue' /* webpackChunkName: "pages/security/index" */))
const _942a5954 = () => interopDefault(import('..\\pages\\signup\\index.vue' /* webpackChunkName: "pages/signup/index" */))
const _00db42ee = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/backup",
    component: _410d206c,
    name: "backup"
  }, {
    path: "/change",
    component: _4eca21be,
    name: "change"
  }, {
    path: "/database",
    component: _30411613,
    name: "database"
  }, {
    path: "/incident",
    component: _31679348,
    name: "incident"
  }, {
    path: "/instance",
    component: _5943028e,
    name: "instance"
  }, {
    path: "/issue",
    component: _59498f6d,
    name: "issue"
  }, {
    path: "/kubernetes",
    component: _215e0e68,
    name: "kubernetes"
  }, {
    path: "/login",
    component: _17468edd,
    name: "login"
  }, {
    path: "/logout",
    component: _695558b8,
    name: "logout"
  }, {
    path: "/problem",
    component: _28b1eee7,
    name: "problem"
  }, {
    path: "/regularcheck",
    component: _bb0b03fc,
    name: "regularcheck"
  }, {
    path: "/request",
    component: _1b9768f7,
    name: "request"
  }, {
    path: "/security",
    component: _6eaa59a4,
    name: "security"
  }, {
    path: "/signup",
    component: _942a5954,
    name: "signup"
  }, {
    path: "/",
    component: _00db42ee,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
