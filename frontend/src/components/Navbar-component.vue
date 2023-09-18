<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary bg-header p-md-5 py-3 px-1">
    <div class="d-flex flex-column">
      <router-link :to="{ name: 'home' }">
        <img alt="logo" src="../assets/img/crLogoSquare.svg" height="120" />
      </router-link>
    </div>
    <button class="navbar-toggler bg-transparent ms-auto" type="button" data-bs-toggle="collapse"
      data-bs-target="#linksdropdown" aria-controls="linksdropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="linksdropdown">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 text-end text-shadow">
        <li class="nav-item mx-3 d-lg-none d-block">
          <router-link class="text-uppercase text-primary fw-bold link" :to="{ name: 'plans' }">
            SHOW ME HOW
          </router-link>
        </li>
        <li class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link"
            :to="{ name: 'courseContent', query: { series: 'Essentials', module: 1 } }">
            Etsy Courses
          </router-link>
        </li>
        <li class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'about' }">
            About Us
          </router-link>
        </li>
        <li
          :class="route.path.includes('plans') || route.path.includes('coursecontent') || route.path.includes('register') ? 'd-none' : ''"
          class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'contact' }">
            Contact
          </router-link>
        </li>
        <!-- <li class="nav-item mx-3">
          <router-link class="text-uppercase text-dark link" :to="{ name: 'register' }">
            Register
          </router-link>
        </li> -->
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
    <div v-if="route.path.includes('plans') || route.path.includes('coursecontent') || route.path.includes('register')">
      <button @click="goToContact()" class="btn bg-turquoise btn-info text-light d-none d-lg-block elevation"><i class="mdi
          mdi-email"> </i> Contact
        Us</button>
    </div>
    <div v-else>
      <button @click="goToPlans()" class="btn bg-turquoise btn-info text-light d-none d-lg-block elevation">Show Me
        How!</button>
    </div>
  </nav>
</template>


<script>
import { useRouter, useRoute } from 'vue-router';

import { useAuthStore } from '../stores/auth.js';
import { computed } from 'vue';
export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    const route = useRoute();
    return {
      authStore,
      route,
      async logout() {
        try {
          await authStore.logout()
          router.push({ name: 'login' })
        } catch (error) {
          console.log(error);
        }
      },
      isToken: computed(() => authStore.getIsUserLoggedIn),
      goToPlans() {
        router.push({ name: 'plans' })
      },
      goToContact() {
        router.push({ name: 'contact' })
      }

    }
  }
};
</script>


<style lang="scss" scoped>
.bg-header {
  background-image: url('../assets/img/header_long7.jpg');
  background-position: top;
  background-size: cover;
}

// @media only screen and (max-width: 768px) {
//   .bg-header {
//     background-image: url('../assets/img/header_long3.svg');
//     background-position: top;
//     background-size: cover;

//   }
// }

.bg-transparent {
  background-color: #d9c7af92 !important;
}

.bg-transparent-2 {
  background-color: rgba(255, 255, 255, 0.325) !important;
  border-radius: 10px;
}

.text-shadow {
  text-shadow: -1px 1px rgba(250, 235, 215, 0.714);
}

.link {
  text-decoration: none !important;
}
</style>