<template>
  <div>
    <section class="row justify-content-center">
      <div class="col-md-10 col-12 p-4">
        <h1>Welcome to the University of Etsy</h1>
      </div>
    </section>

    <section class="row justify-content-center">
      <div class="col-md-10 col-12 card">

        <section class="row justify-content-around">
          <div class="col-4">
            <div class="m-3">
              This is the navigation area based on module
              Two dropdowns, one for each series
              with module numbers.
              <button class="btn btn-secondary btn-w mb-1" type="button" data-bs-toggle="collapse"
                data-bs-target="#essentials" aria-expanded="false" aria-controls="essentials">
                Etsy Essentials
              </button>
              <div class="collapse mb-3" id="essentials">

                <ul class="list-group">
                  <li class="list-group-item" :class="isActive ? 'active' : ''" aria-current="true">Module 1: Setting Up
                    Your Shop</li>
                  <li class="list-group-item">Module 2: Listings</li>
                  <li class="list-group-item">Module 3: Product Photography & Shop Images</li>
                  <li class="list-group-item">Module 4: Pricing, Product Fulfillment, & Shipping</li>
                  <li class="list-group-item">Module 5: Customer Service</li>
                  <li class="list-group-item">Module 6: Bonus - Stats & Marketing</li>
                </ul>

              </div>
              <button class="btn btn-secondary btn-w mt-3 mb-1" type="button" data-bs-toggle="collapse"
                data-bs-target="#expert" aria-expanded="false" aria-controls="expert">
                Etsy Expert
              </button>
              <div class="collapse" id="expert">

                <ul class="list-group">
                  <li class="list-group-item" aria-current="true">Module 1: Marketing,
                    Advertising, Sales, & Promotional Strategies</li>
                  <li class="list-group-item">Module 2: Advanced Branding & Marketing Tactics</li>
                  <li class="list-group-item">Module 3: Data Analytics, Keeping Sales High, & Moving Off Etsy's Platform
                  </li>
                  <li class="list-group-item">Module 4: Profit Margins & Scaling</li>
                  <li class="list-group-item">Module 5: Troubleshooting All Things Etsy</li>

                </ul>

              </div>
            </div>
          </div>
          <div class="col-7 p-3 ">
            <div v-for="v in mod1Videos" :key="v.id" class="m-3">
              <VideoCard :video="v" />

            </div>
          </div>
        </section>
      </div>
    </section>

  </div>
</template>


<script>
import { onMounted, computed } from 'vue';
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
      // TODO when a series and module is selected, add params to route; then, use ref to reactively store the params; use a v-bind that checks the current module and series against the ref and sets the proper list item to active
      mod1Videos: computed(() => {
        let filteredVideos = videoStore.videos.filter(v => v.module == 1 && v.series == 'Etsy Essentials')
        return filteredVideos
      }),

      isActive: true
    }
  }
};
</script>


<style lang="scss" scoped>
.active {
  background-color: rgb(255, 149, 0);
}

.btn-w {
  min-width: 100%;
}
</style>