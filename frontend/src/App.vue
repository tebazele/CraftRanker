<template>
  <header class="sticky-top">
    <NavbarComponent />
  </header>
  <main>
    <router-view />
  </main>
  <footer>

    <section class="row justify-content-center">
      <div class="col-12 col-md-5 text-center pt-5">

        <img src="./assets/img/crLogoSquare.svg" height="120" />
      </div>

    </section>
    <section class="row justify-content-center">

      <div class="col-12 text-center">

        <h6 class="text-uppercase">
          <router-link :to="{ name: 'home' }">
            <span>
              terms of service
            </span>
          </router-link> |
          <router-link :to="{ name: 'home' }">
            <span>
              Privacy policy
            </span>
          </router-link>
        </h6>
      </div>
      <div class="col-6 col-md-4 text-center">
        <p>
          Disclaimer: Etsy is a trademark of Etsy, Inc.
          This content is not created or endorsed by Etsy, Inc.
          All Rights Reserved 2022 © Copyright CraftRanker
        </p>
      </div>
    </section>
  </footer>
</template>


<script>
// import { computed, reactive, onMounted } from 'vue';
import NavbarComponent from './components/Navbar-component.vue';
export default {
  setup() {
    return {}
  },
  components: { NavbarComponent }
};
</script>


<style lang="scss" scoped>
main {
  min-height: 40vh;
}

// footer {}
</style>