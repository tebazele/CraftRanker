<template>
  <div class="d-flex">
    <i class="mdi mdi-star text-orange"></i>
    <p class="mx-2"><span class="fw-bold">{{ text.bullet }} </span> {{ text.text }}</p>
  </div>
</template>


<script>

export default {
  props: {
    text: Object
  },
  setup() {
    return {}
  }
};
</script>


<style scoped></style>