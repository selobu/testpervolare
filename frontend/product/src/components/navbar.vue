<script>
export default {
    props: { title: { type: String, required: true } },
};
</script>
<template>
    <v-toolbar density="comfortable" :title="title"></v-toolbar>
</template>
