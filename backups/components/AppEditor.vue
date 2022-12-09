<template>
  <section>
    <client-only>
      <quill-editor
        ref="editor"
        v-model.lazy="editedContent"
        :options="editorOption"
        class="editor--border relative"
        @change="debounceTextChange"
      />
    </client-only>
  </section>
</template>

<script>
import { debounce } from 'vue-debounce'
export default {
  // 如果是編輯文章，則會從parent收到文章當前的content
  props: {
    content: {
      type: String,
      default: () => '',
    },
  },
  data() {
    return {
      editedContent: this.content,
      // 所有文本編輯器功能設定均寫在editorOption
      editorOption: {
        theme: 'snow', // 可換
        modules: {
          toolbar: {
            // container這裡是個大坑，[]表分群
            container: [
              ['bold', 'italic', 'underline', 'strike', 'code'],
              ['blockquote', 'code-block'],
              [{ header: [1, 2, 3, 4, 5, 6, false] }],
              [{ list: 'ordered' }, { list: 'bullet' }],
              [{ script: 'sub' }, { script: 'super' }],
              [{ indent: '-1' }, { indent: '+1' }],
              [{ size: ['small', false, 'large', 'huge'] }],
              [{ color: [] }, { background: [] }],
              [{ align: [] }],
              ['clean'],
              ['link', 'image', 'video'],
            ],
            // 客製化圖片上傳功能用的
            handlers: {
              image: this.uploadImage,
            },
          },
        },
      },
    }
  },
  methods: {
    debounceTextChange: debounce(function () {
      //don't use arrow function
      this.$emit('text-change', this.editedContent)
    }, 3000),

    // 後面再補上uploadImage說明如何客製化圖片上傳功能
  },
}
</script>