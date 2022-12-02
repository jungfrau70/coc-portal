<template>
  <v-dialog v-model="editBoardDialog" purple eager>
    <v-card>
      <!-- HERE -->
      <iframe ref="formFrame" :src="url" @load="afterLoad()" ></iframe> =
    </v-card>
  </v-dialog>
</template>
<script>
export default {


  data() {
    return {
      url: 'public/iframe.html',
      editBoardDialog: '',
      title: 'Hello Nuxters!',
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
