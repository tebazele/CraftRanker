<script setup>
import LiteYouTubeEmbed from 'vue-lite-youtube-embed'
import 'vue-lite-youtube-embed/style.css'
import CheckList from '../components/Check-list.vue'
import PurchaseButton from '../components/Purchase-button.vue';


const offerText = [{
  bullet: "More than 90 in-depth instructional videos",
  text: "that enhance book learning and help you apply what we've learned about starting a successful Etsy shop."
},
{
  bullet: "Advice you can trust.",
  text: "We created these classes as a way to help friends and family who asked for help with their shops but had trouble digesting some of the concepts in book format."
},
{
  bullet: "Straightforward, fun video instruction.",
  text: "(It's like we're sitting right next to you by the computer, taking you step by step through creating a successful Etsy shop!)",
},
{
  bullet: "Extra tips and strategies not found in the book!",
  text: "Extra advice, stories, and insights to help you get your shop in shape."
},
{
  bullet: "Full walkthrough",
  text: "of titles, descriptions, keywords, audience targeting, listing photos, branding, SEO, marketing, scaling, and more."
},
{
  bullet: "One-time, flat fee.",
  text: "No subscriptions, no re-bills, no hidden fees. Seriously."
}
]

</script>

<template>
  <div class="container-fluid">
    <section class="row justify-content-center pos-rel">
      <div class="col-12 text-center">
        <h1>Video Coursework Companion:</h1>

        <h2 class="fst-italic">
          The Ultimate Guide to Selling on Etsy
        </h2>


      </div>
      <!-- <div class="blammie text-end me-5 mt-3">
        <h6 class="me-5">Don't have our book?</h6>
        <button class="btn btn-outline-dark border border-warning ms-3"><a href="https://a.co/d/gP6RLVm"
            target="_blank"><i class="mdi mdi-book-arrow-right"></i> Get it on Amazon Now!</a></button>
      </div> -->
    </section>
    <hr class="m-4" />
    <section class="row justify-content-center text-secondary text-center">
      <h4>Get 90+ Recorded Video Lessons to Accompany Your Book Learning
      </h4>
      <div class="col-md-4">

        <!-- <button class="btn btn-info text-light bg-turquoise my-3 fs-4">Get University of Etsy Now</button> -->
        <PurchaseButton />
      </div>
    </section>
    <section class="row justify-content-around">
      <div class="col-md-7 mt-5 ">
        <div class="elevation p-0 mx-5">
          <LiteYouTubeEmbed id="Osaww1kn-tc" title="5 Strategies to Sell on Etsy" rel="prefetch" />

        </div>
        <div class="mx-5 my-2">
          <p class="text-secondary">Wondering what video learning with Noelle and Jeanne is like? Enjoy this recorded
            webinar that takes you through 5 of our best tips for new sellers!</p>
        </div>
        <div class="mt-5 ms-5">
          <h3><span class="text-turquoise">A Love Letter</span> to Our Fellow Etsy Sellers</h3>
        </div>
        <div class="mx-5 my-3">
          <p>In our first month on Etsy, we made exactly one sale 😬</p>
          <p>We've learned a lot since then (like, a LOT). Over the past 9 years, our hobby has become a full-time job,
            and our Etsy shop (Fourth Wave Apparel) now ranks in the top 1% of all Etsy shops and has more than 25,000
            sales.</p>
          <p><span class="fw-bold text-turquoise">The University of Etsy</span> (our video masterclass series for Etsy
            sellers!) includes foundational work called "Etsy Essentials" and advanced learning called "Etsy Expert." Both
            masterclasses series are our love letter to Etsy sellers. We believe that a rising tide lifts all ships, and
            we love teaching other sellers how to learn from our success (and our mistakes). </p>
        </div>

      </div>
      <div class="col-md-5 mt-5">
        <div class="text-center">
          <h2><span class="text-orange text-uppercase">University of Etsy </span>Masterclasses</h2>
          <h6 class="text-turquoise">Exclusive Offer: $19.99 <span class="text-dark">(Regularly $297)</span></h6>
        </div>
        <hr class="mx-4" />
        <div v-for="(t, index) in offerText" :key="index" class="pt-2">
          <CheckList :text="t" />

        </div>
      </div>
    </section>
    <hr class="mx-4" />
    <section class="row">
      <div class="col-12">
        <h1 class="text-orange text-center">Course Preview & Syllabus</h1>
      </div>
      <div class="col-md-5">
        <div class="ms-5 mt-5">
          <p>Take a quick peek inside the masterclasses:</p>
          <p><span class="fw-bold">The content is yours forever</span> (and we'll update it to reflect the latest
            best-practices in Etsy as we go!) No subscriptions, no re-bills, no hidden fees. Just helpful content to help
            you grow.</p>
          <p>Click <a class="text-turquoise" href="../../public/worksheets/Masterclass_Syllabi.pdf"
              target="_blank">HERE</a> to download the Course Syllabus!</p>

        </div>

      </div>
      <div class="col-md-7">
        <div class="m-5 elevation">
          <LiteYouTubeEmbed id="OI5BA60PhQI" title="Introduction to Etsy Essentials" />
        </div>
      </div>
    </section>
  </div>
</template>




<style scoped>
.pos-rel {
  position: relative;
}

.blammie {
  position: absolute;
}

@media only screen and (max-width: 768px) {
  .blammie {
    display: none;
  }

}
</style>