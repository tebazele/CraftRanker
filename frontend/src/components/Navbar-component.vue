<template>
  <nav class="bg-header p-5">
    <div class="d-flex flex-column">
      <img alt="logo" src="../assets/img/crLogoSquare.svg" height="120" />
    </div>
  </nav>
</template>


<script>
// import { computed, reactive, onMounted } from 'vue';
export default {
  setup() {
    return {}
  }
};
</script>


<style lang="scss" scoped>
.bg-header {
  background-image: url('../assets/img/headerLongDarker.jpg');
  background-position: center;
  background-size: cover;
}
</style>