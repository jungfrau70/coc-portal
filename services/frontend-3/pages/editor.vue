<template>
  <div class="blog-post-creator">
    <quill-editor
      v-model="content"
      ref="myQuillEditor"
      :options="editorOption"
    ></quill-editor>
  </div>
</template>

