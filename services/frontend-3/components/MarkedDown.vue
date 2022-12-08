<template>
  <div>
    <div>{{ rawText }}</div>
    <div v-html="convertedText"></div>

  </div>
</template>

<script>
import axios from 'axios'
import { marked } from 'marked'

export default {
  name: 'ShowMdPage',
  data() {
    return {
      rawText: '',
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
        this.convertedText = this.changeMarkdown(response.data)
      })
    },
    changeMarkdown(text) {
      marked.setOptions({
        renderer: new marked.Renderer(),
        gfm: true,
        headerIds: false,
        tables: true,
        breaks: true,
        pedantic: false,
        sanitize: true,
        smartLists: true,
        smartypants: false,
      })
      return marked(text)
    },
  },
}
</script>