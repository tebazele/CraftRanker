import { defineStore } from 'pinia'
import api from '../services/axiosService.js'


export const useVideoStore = defineStore('video', {
  state: () => ({
    videos: [],

  }),
  getters: {
    // NOTE accessing the state like this acts like a computed
    videosDB(state) {
     
      return state.videos
    }
    // TODO write getters that filter videos by module
  },
  actions: {
    async getVideos() {
      try {
        const res = await api.get('/videos')
        console.log(res.data)
        this.videos = res.data
      } catch (error) {
        console.error(error)
      }
    }
  }
})
  

