<template>
  <div class="col-md-10 mb-2 mb-md-0">
    <div class="my-md-2 mx-md-5 mx-2 px-md-5 py-md-3 border rounded bg-white row align-items-baseline elevation">
      <img src="../assets/img/doubleQuote.svg" class="quote-art col-md-4" />
      <div class="col-md-10">
        <p class="mb-2">{{ testimonial.body }}</p>
        <h6 class="text-turquoise mt-0 text-end">~ {{ testimonial.author }}</h6>
      </div>
    </div>
  </div>
</template>


<script>

export default {
  props: {
    testimonial: {
      type: Object,
      required: true
    }
  },
  setup() {
    return {}
  }
};
</script>


<style scoped>
.quote-art {
  height: 80px;
  width: 120px;
}
</style>