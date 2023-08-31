<template>
  <section class="row justify-content-center">
    <div class="col-11 pt-5">
      <div class="m-2 p-4 card elevation-3">
        <h1>Register</h1>
        <form @submit.prevent="register()">
          <div class="d-flex align-items-baseline p-3">
            <i class="mdi mdi-account-circle pe-2 fs-3"> </i>
            <input v-model="formData.email" placeholder="Email" />
          </div>
          <div class="d-flex align-items-baseline">
            <i class="mdi mdi-lock pe-2 fs-3 p-3"> </i>
            <input v-model="formData.password" placeholder="Password" />
          </div>
          <div class="d-flex align-items-baseline">
            <i class="mdi mdi-rename pe-2 fs-3 p-3"> </i>
            <input v-model="formData.fullName" placeholder="Name" />
          </div>
          <div class="d-flex justify-content-end">
            <button class="btn btn-secondary">Register</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>


<script>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth.js';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const formData = ref({});
    const authStore = useAuthStore();
    const router = useRouter();
    return {
      formData,
      async register() {
        try {
          const registerData = {
            ...formData.value
          }
          await authStore.registerNewUser(registerData)
          formData.value = {}
          router.push({ name: 'courseContent', query: { series: 'Essentials', module: 1 } })
        } catch (error) {
          console.error(error)
        }
      }
    }
  }
};
</script>


<style lang="scss" scoped>
.elevation-3 {
  box-shadow: 2px 2px 8px gray;
}

input {
  width: 100%;
  border: none;
  border-bottom: 1px solid gray;
  padding: 6px;
}
</style>