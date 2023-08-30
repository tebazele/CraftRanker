<template>
  <div>
    {{ videoStore.videos }}

  </div>
</template>


<script>
import { onMounted } from 'vue';
import { useVideoStore } from '../stores/video.js';
import { computed } from 'vue'

export default {
  setup() {
    const videoStore = useVideoStore();
    onMounted(() => {
      videoStore.getVideos()
    })

    return {
      videoStore
    }
  }
};
</script>


<style lang="scss" scoped></style>