<template>
  <!-- SECTION router-push to a page to purchase the video courses -->
  <section class="row">
    <div class="col-12 text-center ">
      <h1 class="text-dark text-uppercase">Learn from real top-1% etsy sellers</h1>
      <h4 class="text-secondary">No guesswork. No BW. Just proven strategies for success on Etsy</h4>
    </div>
  </section>
  <section class="row justify-content-center">
    <div class="col-12 col-md-4 text-center">

    </div>
  </section>
  <section class="row justify-content-center">
    <div class="col-12 col-md-7 mt-5 p-3">
      <h3 class="text-center">We Love Helping Other Etsy Sellers Succeed</h3>
      <p class="text-info text-center">Good advice can be hard to find:<br />We learned that the hard way.</p>
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
    <div class="col-12 col-md-4 p-3 ">
      <img src="../assets/img/craftranker_main.jpg" class="img-fluid rounded img-height mt-5" />

    </div>
  </section>
  <hr />
  <section class="row justify-content-center">
    <div class="col-12">
      <h2 class="text-center">What Other Etsy Sellers Are Saying:</h2>
    </div>
    <!-- SECTION reviews -->
    <!-- STUB 1 -->
    <div class="col-10">
      <div class="my-2 mx-5 px-5 py-3 border rounded bg-white row align-items-baseline">
        <img src="../assets/img/doubleQuote.svg" class="quote-art col-4" />
        <div class="col-10 ">
          <p class="mb-2">My shop improved immediately.A highly recommended resource!</p>
          <h6 class="text-info mt-0 text-end">~ WoodenGiftCo</h6>
        </div>
      </div>

    </div>
    <!-- STUB 2 -->
    <div class="col-10">
      <div class="my-2 mx-5 px-5 py-3 border rounded bg-white row align-items-baseline">
        <img src="../assets/img/doubleQuote.svg" class="quote-art col-4" />
        <div class="col-8 ">
          <p class="mb-2">I've been away from selling on Etsy for over seven years, and I knew coming back, I was
            walking
            into a completely different selling experience. I had no desire to overwhelm myself with internet rabbit
            holes
            and google searches trying to figure out what changed and what that meant for me ... I highly recommend this
            to any new sellers or anyone coming back to Etsy after a few years away. I wish I would have had it years
            ago
            when I tried to sell the first time.</p>
          <h6 class="text-info mt-0 text-end">~ Sue S.</h6>
        </div>
      </div>

    </div>
    <!-- STUB 3 -->
    <div class="col-10">
      <div class="my-2 mx-5 px-5 py-3 border rounded bg-white row align-items-baseline">
        <img src="../assets/img/doubleQuote.svg" class="quote-art col-4" />
        <div class="col-8 ">
          <p class="mb-2">Like a friend sitting across the table; honest, straight-forward,
            and lots of great info! I HIGHLY recommend.</p>
          <h6 class="text-info mt-0 text-end">~ Summer D.</h6>
        </div>
      </div>

    </div>
    <!-- STUB 4 -->
    <div class="col-10">
      <div class="my-2 mx-5 px-5 py-3 border rounded bg-white row align-items-end">
        <img src="../assets/img/doubleQuote.svg" class="quote-art col-4" />
        <div class="col-8 ">
          <p class="mb-2">Whether you have sold on Etsy for 5 years or are just getting started,
            this is like getting a mini degree in Etsy.</p>
          <h6 class="text-info mt-0">~ Elyse G.</h6>
        </div>
      </div>

    </div>
    <!-- STUB 5 -->
    <div class="col-10">
      <div class="my-2 mx-5 px-5 py-3 border rounded bg-white row align-items-end">
        <img src="../assets/img/doubleQuote.svg" class="quote-art col-4" />
        <div class="col-8 ">
          <p class="mb-2">My shop improved immediately.A highly recommended resource!</p>
          <h6 class="text-info mt-0">~ WoodenGiftCo</h6>
        </div>
      </div>

    </div>
    <div class="col-12">
      <div class="m-5 px-5 py-3 border rounded bg-white row align-items-end">
        <img src="../assets/img/doubleQuote.svg" class="quote-art col-4" />
        <div class="col-8 ">
          <p class="mb-2">My shop improved immediately.A highly recommended resource!</p>
          <h6 class="text-info mt-0">~ WoodenGiftCo</h6>
        </div>
      </div>

    </div>

  </section>
</template>

<script>
// import { onMounted } from 'vue';
// import { useCounterStore } from '../stores/counter.js';
export default {
  setup() {
    // const counterStore = useCounterStore();
    // onMounted(() => {
    //   counterStore.getMovies()
    // })
    // const store = useCounterStore()
    return {
      // store
    }
  }
}
// import TheWelcome from '../components/TheWelcome.vue'
</script>

<style scoped lang="scss">
.text-max {
  margin: auto;
  max-width: 500px;
}


.img-height {
  max-height: 500px;
  width: 400px;
  object-fit: cover;
  object-position: center;
}

.pos-rel {
  position: relative;
}

.quote-art {
  height: 80px;
  width: 120px;

}
</style>