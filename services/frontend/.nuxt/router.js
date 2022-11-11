import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _41188956 = () => interopDefault(import('..\\pages\\backup\\index.vue' /* webpackChunkName: "pages/backup/index" */))
const _aaa73214 = () => interopDefault(import('..\\pages\\blog\\index.vue' /* webpackChunkName: "pages/blog/index" */))
const _4ed58aa8 = () => interopDefault(import('..\\pages\\change\\index.vue' /* webpackChunkName: "pages/change/index" */))
const _5b15ec7d = () => interopDefault(import('..\\pages\\database\\index.vue' /* webpackChunkName: "pages/database/index" */))
const _12210cc6 = () => interopDefault(import('..\\pages\\incident\\index.vue' /* webpackChunkName: "pages/incident/index" */))
const _039955ba = () => interopDefault(import('..\\pages\\instance\\index.vue' /* webpackChunkName: "pages/instance/index" */))
const _d9cf3d7a = () => interopDefault(import('..\\pages\\issue\\index.vue' /* webpackChunkName: "pages/issue/index" */))
const _2b521b5c = () => interopDefault(import('..\\pages\\kubernetes\\index.vue' /* webpackChunkName: "pages/kubernetes/index" */))
const _511560b3 = () => interopDefault(import('..\\pages\\login\\index.vue' /* webpackChunkName: "pages/login/index" */))
const _2a13a33d = () => interopDefault(import('..\\pages\\problem\\index.vue' /* webpackChunkName: "pages/problem/index" */))
const _96fef356 = () => interopDefault(import('..\\pages\\register\\index.vue' /* webpackChunkName: "pages/register/index" */))
const _10ca0f6c = () => interopDefault(import('..\\pages\\regularcheck\\index.vue' /* webpackChunkName: "pages/regularcheck/index" */))
const _1cf91d4d = () => interopDefault(import('..\\pages\\request\\index.vue' /* webpackChunkName: "pages/request/index" */))
const _1900acd0 = () => interopDefault(import('..\\pages\\security\\index.vue' /* webpackChunkName: "pages/security/index" */))
const _6f299450 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _41188956,
    name: "backup"
  }, {
    path: "/blog",
    component: _aaa73214,
    name: "blog"
  }, {
    path: "/change",
    component: _4ed58aa8,
    name: "change"
  }, {
    path: "/database",
    component: _5b15ec7d,
    name: "database"
  }, {
    path: "/incident",
    component: _12210cc6,
    name: "incident"
  }, {
    path: "/instance",
    component: _039955ba,
    name: "instance"
  }, {
    path: "/issue",
    component: _d9cf3d7a,
    name: "issue"
  }, {
    path: "/kubernetes",
    component: _2b521b5c,
    name: "kubernetes"
  }, {
    path: "/login",
    component: _511560b3,
    name: "login"
  }, {
    path: "/problem",
    component: _2a13a33d,
    name: "problem"
  }, {
    path: "/register",
    component: _96fef356,
    name: "register"
  }, {
    path: "/regularcheck",
    component: _10ca0f6c,
    name: "regularcheck"
  }, {
    path: "/request",
    component: _1cf91d4d,
    name: "request"
  }, {
    path: "/security",
    component: _1900acd0,
    name: "security"
  }, {
    path: "/",
    component: _6f299450,
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
