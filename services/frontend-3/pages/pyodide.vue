<template>
  <div>
    <p id="title">My first Pyodide app</p>
  </div>
</template>

<script>
// import { loadPyodide } from 'pyodide.mjs'

export default {
  async mounted() {
    await this.pyo()
  },
  methods: {
    async pyo() {
      const pyodide = await loadPyodide()

      pyodide.runPython(`
          print('Hello world, from the browser!')

          import js
          js.document.title = "Hello from Python"

          js.document.getElementById("title").innerText = "Replaced by Python"
        `)
    },
  },
}
</script>