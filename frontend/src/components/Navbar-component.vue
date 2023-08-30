<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary bg-header p-5">
    <div class="d-flex flex-column">
      <router-link :to="{ name: 'home' }">
        <img alt="logo" src="../assets/img/crLogoSquare.svg" height="120" />
      </router-link>
    </div>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'courseContent' }">
            Etsy Courses
          </router-link>
        </li>
        <li class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'about' }">
            About Us
          </router-link>
        </li>
        <li class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'contact' }">
            Contact
          </router-link>
        </li>
        <li v-if="!isToken" class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'login' }">
            Login
          </router-link>
        </li>
        <li v-else class="nav-item mx-3">
          <a class="text-dark text-uppercase link" href="#" @click="logout()">Logout</a>
        </li>
      </ul>
      <!-- TODO make purchase page and connect stripe, set up register page to be accessible only after payment confirmed -->
      <!-- <button class="btn btn-info">GET MASTERCLASSES NOW!</button> -->
    </div>
  </nav>
</template>


<script>
import { useRouter } from 'vue-router';

import { useAuthStore } from '../stores/auth.js';
import { computed } from 'vue';
export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    return {
      authStore,
      async logout() {
        try {
          await authStore.logout()
          router.push({ name: 'login' })
        } catch (error) {
          console.log(error);
        }
      },
      isToken: computed(() => authStore.getIsUserLoggedIn)

    }
  }
};
</script>


<style lang="scss" scoped>
.bg-header {
  background-image: url('../assets/img/headerLongDarker.jpg');
  background-position: center;
  background-size: cover;
}

.link {
  text-decoration: none !important;
}
</style>