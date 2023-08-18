<!-- 
frontend\src\views\Home.vue
Author: Author : Andre Baldo (http://github.com/andrebaldo/) -->
<template>
  <div class="home">
    <navbar />
    <h1>Home -- This is the unlogged in view</h1>
    <hello-world />
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import HelloWorld from '../components/HelloWorld.vue'


export default {
  name: 'home',
  components: {
    HelloWorld,
    Navbar
  }
}
</script>
