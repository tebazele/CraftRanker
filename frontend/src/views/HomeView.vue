<template>
  <!-- SECTION router-push to a page to purchase the video courses -->
  <div>
    <section class="row">
      <div class="col-12 text-center ">
        <h1 class="text-dark text-uppercase mt-md-3">Learn from real top-1% etsy sellers</h1>
        <h4 class="text-secondary">No guesswork. No BS. Just proven strategies for success on Etsy</h4>
      </div>
    </section>
    <section class="row justify-content-center">
      <div class="col-12 col-md-4 text-center">

      </div>
    </section>
    <section class="row justify-content-center">
      <div class="col-12 col-md-7 mt-md-5 mt-1 p-3">
        <h3 class="text-center">We Love Helping Other Etsy Sellers Succeed</h3>
        <p class="text-center text-orange">Good advice can be hard to find:<br />We learned that the hard way.
        </p>
        <div class="text-max">
          <p>Our success on Etsy wasn't overnight. And it wasn't an accident, or "good luck."" It was the
            result of meticulous
            testing, research, mistakes (lots of mistakes) and doing more of what worked (and less of what didn't!). </p>
          <p>
            That's why, after years of hard work (and success in becoming a top-1% Etsy shop!) we love sending the
            elevator
            back down to other Etsy sellers who are in the same place we were at years ago. Because a rising tide lifts
            all
            ships. And when Etsy gets stronger as a platform with sellers who know the ropes, we all benefit.
          </p>
          <p>
            Our success is replicable. Which means that you can do it in your shop too. And we'd love to teach you how.
          </p>

        </div>

      </div>
      <div class="col-12 col-md-4 p-md-3 d-flex d-md-block justify-content-center">
        <img src="../assets/img/craftranker_main.jpg" class="img-fluid rounded img-height mt-md-5 m-3" />

      </div>
    </section>
    <hr class="m-3" />
    <section class="row justify-content-center">
      <div class="col-12">
        <h2 class="text-center">What Other Etsy Sellers Are Saying:</h2>
      </div>
    </section>
    <!-- SECTION reviews -->
    <!-- STUB 1 -->
    <section v-for="t in testimonials" :key="t.id" class="row justify-content-center">
      <TestimonialCard :testimonial="t" />

    </section>
    <!-- {{ myList }} -->





  </div>
</template>

<script>
// import { computed } from 'vue';
// import { ref } from 'vue';
import TestimonialCard from '../components/Testimonial-card.vue';
import { testimonials } from '../stores/testimonialData.js';
export default {

  setup() {
    // const myList = ref(testimonials)

    return {
      testimonials
    }
  },
  components: { TestimonialCard }
}

</script>

<style scoped lang="scss">
.text-max {
  margin: auto;
  max-width: 500px;
}

@media only screen and (max-width: 768px) {
  .text-max {
    margin-top: 12px;
    margin-left: 12px;
    margin-right: 12px;
    text-align: justify;
  }
}


.img-height {
  max-height: 500px;
  width: 400px;
  object-fit: cover;
  object-position: center;
}

@media only screen and (max-width: 768px) {
  .img-height {
    max-height: 400px;
    width: 350px;
    margin: auto auto;
  }
}

.pos-rel {
  position: relative;
}
</style>