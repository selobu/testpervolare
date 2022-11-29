<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
  </div>

  <p>
    Check out
    <a href="https://hv.gestionhseq.com" target="_blank">my cv </a>, for details
    and explanations
  </p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
