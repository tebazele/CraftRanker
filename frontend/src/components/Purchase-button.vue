<!-- eslint-disable no-undef -->
<template>
  <div>
    <button @click="redirect()" class="btn btn-info text-light bg-turquoise my-3 fs-4">Get University of Etsy Now</button>
  </div>
</template>


<script>
// NOTE Stripe brought into project with CDN link
// FIXME in production, make sure to change to live mode in env and use live product instead of test
import { onMounted } from 'vue';
import { stripeTestModeKey } from "../env.js";
import { useToast } from "vue-toastification";

export default {
  setup() {
    let stripe = null;
    const toast = useToast();

    onMounted(async () => {
      try {

        // eslint-disable-next-line no-undef
        stripe = await Stripe(stripeTestModeKey);

      } catch (error) {
        toast.error("Something went wrong when we tried to redirect to Stripe")
      }
    })
    function redirect() {
      stripe.redirectToCheckout({
        successUrl: "http://127.0.0.1:5173/success",
        cancelUrl: "http://127.0.0.1:5173/plans",
        lineItems: [
          {
            // FIXME this is the test product, replace with the real one in production
            price: "price_1NpaPiHCtKGyoq0UKwu614bT",
            quantity: 1
          }
        ],
        mode: "payment"
      });
    }
    return { redirect }
  }
};
</script>


<style lang="scss" scoped></style>