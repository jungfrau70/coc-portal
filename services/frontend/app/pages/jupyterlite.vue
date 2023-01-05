<template>
  <v-app>
    <v-card>
      <!-- HERE -->
      <iframe
        ref="formFrame"
        :src="url"
        @load="afterLoad()"
        width="100%"
        height="500"
      ></iframe>
    </v-card>
  </v-app>
</template>


<script>
export default {
  data() {
    return {
      url: 'https://jupyterlite.github.io/demo/repl/index.html?kernel=python',
      editBoardDialog: '',
      title: 'JupyterLab',
    }
  },
  methods: {
    afterLoad() {
      // passing data to iframe
      window.onmessage = function (e) {
        // inside the iframe
        if (e.data === 'hello world') {
          alert('It works!')
        }
      }
    },
  },
}
</script>
