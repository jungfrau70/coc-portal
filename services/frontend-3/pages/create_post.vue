<template>
  <div class="rteditor" background-color: ivory>
    <h1>Blog Post Creator</h1>
    <quill-editor ref="myQuillEditor"></quill-editor>
  </div>
</template>

<script>
// import BlogPostCreator from './components/BlogPostCreator.vue'
export default {
  name: 'CreatePost',
  // components: {
  //   BlogPostCreator
  // }
}
</script>

<style scoped>
h1 {
  margin-left: 20px;
  margin-top: 10px;
}
.rteditor {
  margin-left: 1px;
  margin-right: 1px;
  background-color: white;
  color: black;
}
</style>
