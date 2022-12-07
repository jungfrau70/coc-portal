import Vue from 'vue'
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.snow.css'
// import { quillEditor } from 'vue-quill-editor'
import { Button, Input, Select } from 'view-design'
// import Error from './Error.vue'

Vue.use(VueQuillEditor, Button, Input, Select, Error)
