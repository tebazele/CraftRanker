// import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import api from '../services/axiosService.js';
import { useToast } from 'vue-toastification'

const toast = useToast();



export const useAuthStore = defineStore('auth', {
  state: () => ({
    isUserLoggedIn: false,
    isRegistrationProcessSucceed: false,
    registrationProcessMessage: '',
    isProcessing: false,
    loginToken: '',
    loginProcessMessage: ''
  }),
  getters: {
    getRegistrationProcessSuccess: (state) => {
      if (state.registrationProcessMessage == '') {
        return null;
      } else {
        return state.isRegistrationProcessSucceed;
      }
    },
    // NOTE don't need these in Pinia, can access any state directly from the store instance
    // getRegistrationProcessMessage: (state) => state.registrationProcessMessage,
    // getLoginProcessMessage: (state) => state.loginProcessMessage,
    // isProcessing: (state) => state.isProcessing,
    getIsUserLoggedIn: (state) => {
      if (!state.isUserLoggedIn) {
        if (sessionStorage.loginToken) {
          return true
        }
        return false
      }
      return true

    }
  },
  actions: {
    // SECTION test actions to see how this shit works
    // logSomething(string) {
    //   console.log(string)
    // },
    // SECTION These actions set the state (used to be mutations in Vuex)
// FIXME these mutations may be better off refactored by assigning them directly to the store within each component, eg. authStore.isUserLogginIn = res.data.success;
    setLogged(loginResult) {
      this.isUserLoggedIn = loginResult.success;
      this.loginToken = loginResult.token;
      this.loginProcessMessage = loginResult.message;
      if (loginResult.success) {
        sessionStorage.loginToken = loginResult.token;
      } else {
        sessionStorage.removeItem("loginToken");
      }
    },
    setRegistrationStatus(result) {
      this.isRegistrationProcessSucceed = result.success;
      // FIXME are we not storing a token on registration? 
      sessionStorage.isRegistrationProcessSucceed = result.success;
      this.registrationProcessMessage = result.message;
    },
    // FIXME We may be able to refactor this away too
    setIsProcessing(isProcessing) {
      this.isProcessing = isProcessing
    },
    setLogout() {
      sessionStorage.removeItem('loginToken');
      this.isUserLoggedIn = false;
    },
    // SECTION These actions make api calls
    async registerNewUser(payload) {
      try {
        this.isProcessing = true;
        const response = await api.post('register', payload); 
        console.log(response.data);
        toast.success("Registration successful!")
        this.isProcessing = false;
        this.setRegistrationStatus({
          success: true,
          message: response.data.message
        }); 
           
      } catch (error) {
        this.isProcessing = false;
        if (typeof error != 'undefined' && typeof error.response != 'undefined') {
          this.setRegistrationStatus({
            success: false,
            message: error.response.data.message
            
          });
        } else {
          this.setRegistrationStatus({
            success: false,
            message: error.message
          })
        }
        toast.error("Something went wrong. Please try again.")
        // console.error(error);
        }
    },
    async authenticateUserAndSetToken(payload) {
      try {
        // console.log("this is the payload on the authenticateUserAndSetToken function", payload);
        this.isProcessing = true;
        const res = await api.post('token', payload);
        console.log(res.data);
        this.isProcessing = false;
        this.setLogged({
          success: true,
          token: res.data.token,
          message: "Credentials accepted"         
        })
        api.defaults.headers.common['Authorization'] = res.data.token;
        toast.success("You are logged in")
      } catch (error) {
        this.isProcessing = false;
        if (typeof error != 'undefined' && typeof error.response != 'undefined') {
          this.setRegistrationStatus({
            success: false,
            message: error.response.data.message
          });
        } else {
          this.setRegistrationStatus({
            success: false,
            message: error.message
          })
        }
        toast.error("Password incorrect")
        // console.error(error);
        // console.error(error);
      }
    },
    async resetPassword(body) {
      try {
        const res = await api.post('reset', body)
        console.log(res.data)
      } catch (error) {
        console.error(error)
      }
    },
    async logout() {
      try {
        await api.post('logout');
        this.setIsProcessing(false)
        this.setLogout()
        toast.success("You are logged out.")
      } catch (error) {
        this.setIsProcessing(false)
        if (typeof error != 'undefined' && typeof error.response != 'undefined') {
           this.setLogout();
        } else {
          this.setLogout();
                        }
        // console.error(error)
        toast.error("Not logged out. Something went wrong.")
      }
    }
  }
})

