import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _70edc6e6 = () => interopDefault(import('..\\pages\\login\\index.vue' /* webpackChunkName: "pages/login/index" */))
const _ddaac726 = () => interopDefault(import('..\\pages\\signup\\index.vue' /* webpackChunkName: "pages/signup/index" */))
const _d5248a3c = () => interopDefault(import('..\\pages\\todos\\index.vue' /* webpackChunkName: "pages/todos/index" */))
const _2db3d0e6 = () => interopDefault(import('..\\pages\\todos\\create\\index.vue' /* webpackChunkName: "pages/todos/create/index" */))
const _4f08efde = () => interopDefault(import('..\\pages\\todos\\table.vue' /* webpackChunkName: "pages/todos/table" */))
const _f4dde46c = () => interopDefault(import('..\\pages\\todos\\_id.vue' /* webpackChunkName: "pages/todos/_id" */))
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
    path: "/login",
    component: _70edc6e6,
    name: "login"
  }, {
    path: "/signup",
    component: _ddaac726,
    name: "signup"
  }, {
    path: "/todos",
    component: _d5248a3c,
    name: "todos"
  }, {
    path: "/todos/create",
    component: _2db3d0e6,
    name: "todos-create"
  }, {
    path: "/todos/table",
    component: _4f08efde,
    name: "todos-table"
  }, {
    path: "/todos/:id",
    component: _f4dde46c,
    name: "todos-id"
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
