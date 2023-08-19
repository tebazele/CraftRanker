<template>
  <div>
    This is the home view for people who are logged in
    <hello-world />

  </div>
</template>

<script>
import HelloWorld from '../components/HelloWorld.vue'

export default {
  name: 'CourseContent',

  components: {
    HelloWorld,
  },
}
</script>
