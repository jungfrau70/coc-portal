<template>
  <quill-editor></quill-editor>
</template>

<script setup>
import { quillEditor } from 'vue-quill-editor'
// import { Button, Input, Select } from 'iview'

export default {
  name: 'Creator',
  components: {
    Button,
    Input,
    Select,
    quillEditor,
  },

  data() {
    return {
      content: '',
      editorOption: {
        debug: 'info',
        placeholder: 'Type your post...',
        readOnly: true,
        theme: 'snow',
      },
    }
  },

  methods: {},
}
</script>
