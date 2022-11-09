import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _16e8834d = () => interopDefault(import('..\\pages\\backup\\index.vue' /* webpackChunkName: "pages/backup/index" */))
const _cd5f1aa6 = () => interopDefault(import('..\\pages\\blog\\index.vue' /* webpackChunkName: "pages/blog/index" */))
const _24a5849f = () => interopDefault(import('..\\pages\\change\\index.vue' /* webpackChunkName: "pages/change/index" */))
const _06617698 = () => interopDefault(import('..\\pages\\database\\index.vue' /* webpackChunkName: "pages/database/index" */))
const _984b3606 = () => interopDefault(import('..\\pages\\incident\\index.vue' /* webpackChunkName: "pages/incident/index" */))
const _c026a54c = () => interopDefault(import('..\\pages\\instance\\index.vue' /* webpackChunkName: "pages/instance/index" */))
const _78f5cc6c = () => interopDefault(import('..\\pages\\issue\\index.vue' /* webpackChunkName: "pages/issue/index" */))
const _031b18c9 = () => interopDefault(import('..\\pages\\kubernetes\\index.vue' /* webpackChunkName: "pages/kubernetes/index" */))
const _36f2cbdc = () => interopDefault(import('..\\pages\\login\\index.vue' /* webpackChunkName: "pages/login/index" */))
const _0e42e826 = () => interopDefault(import('..\\pages\\problem\\index.vue' /* webpackChunkName: "pages/problem/index" */))
const _5639de8c = () => interopDefault(import('..\\pages\\register\\index.vue' /* webpackChunkName: "pages/register/index" */))
const _091e7423 = () => interopDefault(import('..\\pages\\regularcheck\\index.vue' /* webpackChunkName: "pages/regularcheck/index" */))
const _01286236 = () => interopDefault(import('..\\pages\\request\\index.vue' /* webpackChunkName: "pages/request/index" */))
const _d58dfc62 = () => interopDefault(import('..\\pages\\security\\index.vue' /* webpackChunkName: "pages/security/index" */))
const _51d7d262 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

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
    component: _16e8834d,
    name: "backup"
  }, {
    path: "/blog",
    component: _cd5f1aa6,
    name: "blog"
  }, {
    path: "/change",
    component: _24a5849f,
    name: "change"
  }, {
    path: "/database",
    component: _06617698,
    name: "database"
  }, {
    path: "/incident",
    component: _984b3606,
    name: "incident"
  }, {
    path: "/instance",
    component: _c026a54c,
    name: "instance"
  }, {
    path: "/issue",
    component: _78f5cc6c,
    name: "issue"
  }, {
    path: "/kubernetes",
    component: _031b18c9,
    name: "kubernetes"
  }, {
    path: "/login",
    component: _36f2cbdc,
    name: "login"
  }, {
    path: "/problem",
    component: _0e42e826,
    name: "problem"
  }, {
    path: "/register",
    component: _5639de8c,
    name: "register"
  }, {
    path: "/regularcheck",
    component: _091e7423,
    name: "regularcheck"
  }, {
    path: "/request",
    component: _01286236,
    name: "request"
  }, {
    path: "/security",
    component: _d58dfc62,
    name: "security"
  }, {
    path: "/",
    component: _51d7d262,
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
