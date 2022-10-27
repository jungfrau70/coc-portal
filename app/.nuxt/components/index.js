export { default as Backup } from '../..\\components\\Backup.vue'
export { default as Change } from '../..\\components\\Change.vue'
export { default as Database } from '../..\\components\\Database.vue'
export { default as Incident } from '../..\\components\\Incident.vue'
export { default as Instance } from '../..\\components\\Instance.vue'
export { default as Issue } from '../..\\components\\Issue.vue'
export { default as Kubernetes } from '../..\\components\\Kubernetes.vue'
export { default as Login } from '../..\\components\\Login.vue'
export { default as Logout } from '../..\\components\\Logout.vue'
export { default as Problem } from '../..\\components\\Problem.vue'
export { default as Regularcheck } from '../..\\components\\Regularcheck.vue'
export { default as Request } from '../..\\components\\Request.vue'
export { default as Security } from '../..\\components\\Security.vue'
export { default as Signup } from '../..\\components\\Signup.vue'
export { default as Upload } from '../..\\components\\Upload.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
