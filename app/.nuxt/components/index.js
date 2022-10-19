export { default as DeleteModal } from '../..\\components\\DeleteModal.vue'
export { default as Input } from '../..\\components\\Input.vue'
export { default as Item } from '../..\\components\\Item.vue'
export { default as List } from '../..\\components\\List.vue'
export { default as Login } from '../..\\components\\Login.vue'
export { default as Logo } from '../..\\components\\Logo.vue'
export { default as Modal } from '../..\\components\\Modal.vue'
export { default as Navbar } from '../..\\components\\Navbar.vue'
export { default as Pagination } from '../..\\components\\Pagination.vue'
export { default as Signup } from '../..\\components\\Signup.vue'
export { default as Table } from '../..\\components\\Table.vue'
export { default as Toast } from '../..\\components\\Toast.vue'
export { default as TodoForm } from '../..\\components\\TodoForm.vue'
export { default as TodoList } from '../..\\components\\TodoList.vue'
export { default as TodoSimpleForm } from '../..\\components\\TodoSimpleForm.vue'

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
