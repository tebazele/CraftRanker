<template>
  <div>
    <section class="row justify-content-center">
      <div class="col-md-10 col-12 p-4">
        <h1>Welcome to the University of Etsy</h1>
      </div>
    </section>

    <section class="row justify-content-center">
      <div class="col-md-10 col-12 card">

        <section class="row">
          <div class="col-3">
            <div class="m-3">
              This is the navigation area based on module
              Two dropdowns, one for each series
              with module numbers.
            </div>
          </div>
          <div class="col-9 p-3">
            <div v-for="v in videoStore.videosDB" :key="v.id">
              <VideoCard :video="v" />

            </div>
          </div>
        </section>
      </div>
    </section>

  </div>
</template>


<script>
import { onMounted } from 'vue';
import { useVideoStore } from '../stores/video.js';

import VideoCard from '../components/Video-card.vue';

export default {
  components: { VideoCard, VideoCard },
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