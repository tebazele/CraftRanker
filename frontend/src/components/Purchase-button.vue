<!-- eslint-disable no-undef -->
<template>
  <div>
    <button @click="redirect()" class="btn btn-info text-light bg-turquoise my-3 fs-4">Get University of Etsy Now</button>
  </div>
</template>


<script>
// NOTE Stripe brought into project with CDN link
// FIXME in production, make sure to change to live mode in env and use live product instead of test
// import { onMounted } from 'vue';

import { useToast } from "vue-toastification";
import api from '../services/axiosService.js';
// import { useAuthStore } from '../stores/auth.js';

export default {
  setup() {
    // eslint-disable-next-line no-unused-vars
    // let stripe = null;
    const toast = useToast();
    // const authStore = useAuthStore();

    // onMounted(async () => {
    //   try {
    //     // NOTE go get publishable key and init an instance of Stripe
    //     // const res = await api.get('public-keys')
    //     await console.log("hello")
    //     // eslint-disable-next-line no-undef
    //     // stripe = await Stripe(res.data.key);
    //     // console.log(stripe)

    //   } catch (error) {
    //     toast.error("Something went wrong")
    //   }
    // })
    async function redirect() {
      try {
        const res = await api.post('create-checkout-session')

        // console.log(res.data)


        window.location.href = res.data.sessionURL
      } catch (error) {
        toast.error("Something went wrong when redirecting to Stripe")
      }
      // FIXME ? this seems like how we connect to stripe in client-only interface
      // Instead, make a call to the backend route /stripecheckout
      // stripe.redirectToCheckout({
      //   successUrl: "http://127.0.0.1:5173/success",
      //   cancelUrl: "http://127.0.0.1:5173/plans",
      //   lineItems: [
      //     {
      //       // FIXME this is the test product, replace with the real one in production
      //       price: "price_1NpaPiHCtKGyoq0UKwu614bT",
      //       quantity: 1
      //     }
      //   ],
      //   mode: "payment"
      // });
    }
    return { redirect }
  }
};
</script>


<style lang="scss" scoped></style>