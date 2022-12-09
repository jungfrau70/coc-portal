<!--UI-->
<template>
  <div id="app">
    <div class="container">
      <button
        class="btn btn-info"
        data-toggle="modal"
        data-target="#exampleModal"
      >
        show modal
      </button>
      <example-modal></example-modal>
    </div>
  </div>
</template>

<!--Script-->
<script>
export default {
  methods: {
    showModal() {
      const element = this.$refs.modal.$el
      document.$(element).modal('show')
    },
  },
}
</script>

<!--CSS-->
<style></style>
