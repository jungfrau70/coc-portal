<template>
  <v-dialog v-model="editBoardDialog" eager >
    <v-card>
      <!-- HERE -->
      <iframe id="ifrm" src="test.html" width="500" height="500"></iframe>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  data() {
    return {
      editBoardDialog: '',
      title: 'Hello Nuxters!',
    }
  },
  methods: {
    // opens the dialog
    openEditor() {
      this.editBoardDialog = true
      this.sendImageToIframe()
    },
    // passing data to iframe
    sendImageToIframe() {
      const iframe = document.getElementById('ifrm').contentWindow // return NULL... why?
      // sends the image to the iframe
      iframe.postMessage({
        action: 'updateAll',
        data: this.board.editorDetails,
      })
    },
  },
}
</script>
