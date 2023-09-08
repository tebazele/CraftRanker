<template>
  <div class="video-thumbnail">

    <h3>{{ video?.name }}</h3>
    <hr />
    <LiteYouTubeEmbed :id="video?.youtubeId" :title="video?.name" rel="prefetch" />

  </div>
</template>


<script setup>
import LiteYouTubeEmbed from 'vue-lite-youtube-embed'
import 'vue-lite-youtube-embed/style.css'


const props = defineProps({
  video: Object
})
</script>


<style lang="scss" scoped>
.video-thumbnail {
  max-width: 500px;

}
</style>