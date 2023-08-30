<template>
  <div>
    This is the video card
    <p>{{ video?.name }}</p>
  </div>
</template>


<script>

export default {
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  setup() {
    return {}
  }
};
</script>


<style lang="scss" scoped></style>