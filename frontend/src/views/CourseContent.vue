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
          <div class="col-md-4">
            <div class="m-3">

              <button class="btn btn-secondary btn-w mt-4 mb-1" type="button" data-bs-toggle="collapse"
                data-bs-target="#essentials" aria-expanded="false" aria-controls="essentials">
                Etsy Essentials
              </button>
              <div class="collapse mb-3" id="essentials">

                <!-- FIXME figure out how to set aria-current to true dynamically -->
                <ul class="list-group">
                  <li @click="goToModule('Essentials', 1)" class="list-group-item clickable"
                    :class="whichModActive == 'Essentials1' ? 'active' : ''" aria-current="true">Module 1: Setting Up
                    Your Shop</li>
                  <li @click="goToModule('Essentials', 2)" class="list-group-item clickable"
                    :class="whichModActive == 'Essentials2' ? 'active' : ''">Module 2: Listings
                  </li>
                  <li @click="goToModule('Essentials', 3)" class="list-group-item clickable"
                    :class="whichModActive == 'Essentials3' ? 'active' : ''">Module 3: Product
                    Photography & Shop Images</li>
                  <li @click="goToModule('Essentials', 4)" class="list-group-item clickable"
                    :class="whichModActive == 'Essentials4' ? 'active' : ''">Module 4: Pricing,
                    Product Fulfillment, & Shipping</li>
                  <li @click="goToModule('Essentials', 5)" class="list-group-item clickable"
                    :class="whichModActive == 'Essentials5' ? 'active' : ''">Module 5: Customer
                    Service</li>
                  <li @click="goToModule('Essentials', 6)" class="list-group-item clickable"
                    :class="whichModActive == 'Essentials6' ? 'active' : ''">Module 6: Bonus -
                    Stats & Marketing</li>
                </ul>

              </div>
              <button class="btn btn-secondary btn-w mt-3 mb-1" type="button" data-bs-toggle="collapse"
                data-bs-target="#expert" aria-expanded="false" aria-controls="expert">
                Etsy Expert
              </button>
              <div class="collapse" id="expert">

                <ul class="list-group">
                  <li @click="goToModule('Expert', 1)" class="list-group-item clickable"
                    :class="whichModActive == 'Expert1' ? 'active' : ''">Module 1:
                    Marketing,
                    Advertising, Sales, & Promotional Strategies</li>
                  <li @click="goToModule('Expert', 2)" class="list-group-item clickable"
                    :class="whichModActive == 'Expert2' ? 'active' : ''">Module 2: Advanced
                    Branding & Marketing Tactics</li>
                  <li @click="goToModule('Expert', 3)" class="list-group-item clickable"
                    :class="whichModActive == 'Expert3' ? 'active' : ''">Module 3: Data
                    Analytics, Keeping Sales High, & Moving Off Etsy's Platform
                  </li>
                  <li @click="goToModule('Expert', 4)" class="list-group-item clickable"
                    :class="whichModActive == 'Expert4' ? 'active' : ''">Module 4: Profit
                    Margins & Scaling</li>
                  <li @click="goToModule('Expert', 5)" class="list-group-item clickable"
                    :class="whichModActive == 'Expert5' ? 'active' : ''">Module 5:
                    Troubleshooting All Things Etsy</li>

                </ul>

              </div>
              <div v-if="whichModActive == 'Essentials1'" class="mt-4">
                <a class="btn btn-light bg-light-orange btn-w mt-3 mb-1"
                  href="../../public/worksheets/Etsy101_Worksheet.pdf">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Essentials2'" class="mt-4">
                <a class="btn btn-light bg-lime btn-w mt-3 mb-1" href="../../public/worksheets/Etsy102_Worksheet.pdf"
                  target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Essentials3'" class="mt-4">
                <a class="btn btn-light bg-pink btn-w mt-3 mb-1" href="../../public/worksheets/Etsy103+104_Worksheet.pdf"
                  target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Essentials4'" class="mt-4">
                <a class="btn btn-light bg-light-blue btn-w mt-3 mb-1"
                  href="../../public/worksheets/Etsy105_Worksheet.pdf" target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Essentials5'" class="mt-4">
                <a class="btn btn-light bg-light-purple btn-w mt-3 mb-1"
                  href="../../public/worksheets/Etsy106_Worksheet.pdf" target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Essentials6'" class="mt-4">
                <a class="btn btn-light bg-bonus btn-w mt-3 mb-1" href="../../public/worksheets/Etsy107_Worksheet.pdf"
                  target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Expert1'" class="mt-4">
                <a class="btn btn-dark bg-orange btn-w mt-3 mb-1" href="../../public/worksheets/Etsy201_Worksheet.pdf"
                  target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Expert2'" class="mt-4">
                <a class="btn btn-dark bg-dark-blue btn-w mt-3 mb-1" href="../../public/worksheets/Etsy202_Worksheet.pdf"
                  target="_blank">Download Worksheet</a>
              </div>
              <div v-else-if="whichModActive == 'Expert4'" class="mt-4">
                <a class="btn btn-dark bg-dark-green btn-w mt-3 mb-1" href="../../public/worksheets/Etsy204_Worksheet.pdf"
                  target="_blank">Download Worksheet</a>
              </div>

            </div>

          </div>
          <div class="col-md-7 p-3 ">
            <div v-for="v in whichMod" :key="v.id" class="m-3">
              <VideoCard :video="v" />

            </div>
          </div>
        </section>
      </div>
    </section>

  </div>
</template>


<script>
import { onMounted, computed, ref } from 'vue';
import { useVideoStore } from '../stores/video.js';
import VideoCard from '../components/Video-card.vue';
import { useRoute, useRouter } from 'vue-router';


export default {
  components: { VideoCard },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const whichModActive = ref(route.query.series + route.query.module)
    const videoStore = useVideoStore();
    onMounted(() => {
      videoStore.getVideos()
    })

    return {
      // TODO when a series and module is selected, add params to route; then, use ref to reactively store the params; use a v-bind that checks the current module and series against the ref and sets the proper list item to active
      route,
      whichModActive,
      whichMod: computed(() => {
        // console.log(whichModActive.value);
        let filteredVideos = videoStore.videos.filter(v => v.module == route.query.module && v.series == 'Etsy ' + route.query.series)

        return filteredVideos
      }),
      goToModule(series, module) {
        router.push({ path: 'coursecontent', query: { series: series, module: module } })
        whichModActive.value = series + module
      }
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

.clickable {
  cursor: pointer;
}
</style>