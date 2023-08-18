// frontend\src\main.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/) import Vue from 'vue'
import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import vuetify from './plugins/vuetify';


Vue.config.productionTip = false;

import store from './store'


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
