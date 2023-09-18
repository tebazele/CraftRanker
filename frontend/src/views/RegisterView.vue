<template>
  <section class="row justify-content-center">
    <div class="col-12 text-center">
      <h1><i class="mdi mdi-party-popper"></i>Thank you for your purchase!</h1>
    </div>
    <div class="col-11 pt-3">
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
import { useToast } from "vue-toastification";

export default {
  setup() {
    const formData = ref({});
    const authStore = useAuthStore();
    const router = useRouter();
    const toast = useToast();

    // onMounted(() => {
    //   console.log(authStore.customerSessionID, authStore.customerSessionURL)
    // })
    return {
      toast,
      formData,
      async register() {
        try {
          const registerData = {
            ...formData.value
          }

          await authStore.registerNewUser(registerData)
          toast.success("Thanks for registering! Please log in to view course content.", {
            position: "top-right",
            timeout: 5000,
            closeOnClick: true,
            pauseOnFocusLoss: true,
            pauseOnHover: true,
            draggable: true,
            draggablePercent: 0.6,
            showCloseButtonOnHover: false,
            hideProgressBar: true,
            closeButton: "button",
            icon: "fas fa-rocket",
            rtl: false
          });

          formData.value = {}

          router.push({ name: 'login' })
        } catch (error) {
          // console.error(error)
          toast.error("Something went wrong")
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