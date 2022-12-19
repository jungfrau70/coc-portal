<template>
  <!-- <div v-highlight v-html="$md.render(convertedText)"></div> -->
  <div v-html="$md.render(convertedText)"></div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      model: '# Hello World!',
      convertedText: '',
    }
  },
  mounted() {
    this.getMarkdown()
  },
  methods: {
    getMarkdown() {
      const url = 'hello.md'
      axios.get(url).then((response) => {
        this.rawText = response.data
        // this.convertedText = this.changeMarkdown(response.data)
        this.convertedText = response.data
        // console.log(this.convertedText)
      })
    },
  },
}
</script>
