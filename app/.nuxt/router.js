import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _1c4ce983 = () => interopDefault(import('..\\pages\\backup\\index.vue' /* webpackChunkName: "pages/backup/index" */))
const _2a09ead5 = () => interopDefault(import('..\\pages\\change\\index.vue' /* webpackChunkName: "pages/change/index" */))
const _3ab2f56a = () => interopDefault(import('..\\pages\\database\\index.vue' /* webpackChunkName: "pages/database/index" */))
const _1c83d49a = () => interopDefault(import('..\\pages\\incident\\index.vue' /* webpackChunkName: "pages/incident/index" */))
const _445f43e0 = () => interopDefault(import('..\\pages\\instance\\index.vue' /* webpackChunkName: "pages/instance/index" */))
const _9a1e7114 = () => interopDefault(import('..\\pages\\issue\\index.vue' /* webpackChunkName: "pages/issue/index" */))
const _56d573ff = () => interopDefault(import('..\\pages\\kubernetes\\index.vue' /* webpackChunkName: "pages/kubernetes/index" */))
const _70edc6e6 = () => interopDefault(import('..\\pages\\login\\index.vue' /* webpackChunkName: "pages/login/index" */))
const _b2d5c68a = () => interopDefault(import('..\\pages\\logout\\index.vue' /* webpackChunkName: "pages/logout/index" */))
const _95296ea0 = () => interopDefault(import('..\\pages\\problem\\index.vue' /* webpackChunkName: "pages/problem/index" */))
const _57aed9d9 = () => interopDefault(import('..\\pages\\regularcheck\\index.vue' /* webpackChunkName: "pages/regularcheck/index" */))
const _af5e7a80 = () => interopDefault(import('..\\pages\\request\\index.vue' /* webpackChunkName: "pages/request/index" */))
const _59c69af6 = () => interopDefault(import('..\\pages\\security\\index.vue' /* webpackChunkName: "pages/security/index" */))
const _ddaac726 = () => interopDefault(import('..\\pages\\signup\\index.vue' /* webpackChunkName: "pages/signup/index" */))
const _021203e4 = () => interopDefault(import('..\\pages\\upload\\index.vue' /* webpackChunkName: "pages/upload/index" */))
const _2e75d9f6 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _1c4ce983,
    name: "backup"
  }, {
    path: "/change",
    component: _2a09ead5,
    name: "change"
  }, {
    path: "/database",
    component: _3ab2f56a,
    name: "database"
  }, {
    path: "/incident",
    component: _1c83d49a,
    name: "incident"
  }, {
    path: "/instance",
    component: _445f43e0,
    name: "instance"
  }, {
    path: "/issue",
    component: _9a1e7114,
    name: "issue"
  }, {
    path: "/kubernetes",
    component: _56d573ff,
    name: "kubernetes"
  }, {
    path: "/login",
    component: _70edc6e6,
    name: "login"
  }, {
    path: "/logout",
    component: _b2d5c68a,
    name: "logout"
  }, {
    path: "/problem",
    component: _95296ea0,
    name: "problem"
  }, {
    path: "/regularcheck",
    component: _57aed9d9,
    name: "regularcheck"
  }, {
    path: "/request",
    component: _af5e7a80,
    name: "request"
  }, {
    path: "/security",
    component: _59c69af6,
    name: "security"
  }, {
    path: "/signup",
    component: _ddaac726,
    name: "signup"
  }, {
    path: "/upload",
    component: _021203e4,
    name: "upload"
  }, {
    path: "/",
    component: _2e75d9f6,
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
