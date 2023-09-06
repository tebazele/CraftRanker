<template>
  <section class="row justify-content-center">
    <div class="col-11 pt-5">
      <div class="m-2 p-4 card elevation-3">
        <h1>Reset Your Password</h1>
        <form @submit.prevent="resetPassword()">
          <div class="d-flex align-items-baseline p-3">
            <i class="mdi mdi-account-circle pe-2 fs-3"> </i>
            <input v-model="formData.email" placeholder="Email" required />
          </div>

          <div class="d-flex justify-content-end">
            <button class="btn btn-secondary">Submit</button>
          </div>
        </form>
      </div>

    </div>
  </section>
</template>


<script>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth.js';
// import { useRouter } from 'vue-router';


export default {
  setup() {
    const formData = ref({})
    const authStore = useAuthStore();
    // const router = useRouter();
    return {
      formData,
      async resetPassword() {
        try {
          const body = {
            ...formData.value
          }
          await authStore.resetPassword(body)
          // router.push({ name: 'resetPassword', params: { token: 4 } })
        } catch (error) {
          console.error(error)
        }
      }
    }
  }
};
</script>


<style scoped>
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