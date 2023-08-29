import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

// defineStore takes two arguments -- and Id and either a setup function OR and options object with state: callback function, getters: obj, actions: functions
export const useCounterStore = defineStore('counter', () => {
// state
  const count = ref(0)
  /* movies = [];
  isLoading = false;
  */
  
  // getters
  const doubleCount = computed(() => count.value * 2)
  /*
  go get the movies when app is loaded instead of onMounted
  */
  // actions
  
  /*
  async getMovies() {
    try/catch
    this.isLoading = true
    const res = await fetch('http://localhost:8000/movies')
    const response = await result.json();
    this.movies = response;
    this.isLoading = false
  }
  */
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
