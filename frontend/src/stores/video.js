import { defineStore } from 'pinia'
import api from '../services/axiosService.js'


export const useVideoStore = defineStore('video', {
  state: () => ({
    videos: [],

  }),
  getters: {
    videosDB(state) {
      return state.videos
    }
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
  

