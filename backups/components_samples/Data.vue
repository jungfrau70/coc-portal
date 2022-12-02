<template>
  <div>
    <div v-html="htmlFileText">
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from "vue";
  import htmlFileContent from '../compositions/data'
  
  const htmlFileText = ref('')
  
  onMounted(() => {
    htmlFileText.value = htmlFileContent
  })
</script>
