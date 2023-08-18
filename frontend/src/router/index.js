// frontend\src\router\index.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/) 
import Vue from 'vue'
import VueRouter from 'vue-router'
// @ts-ignore
import Home from '../views/Home.vue'
import store from '../store/index.js'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/home',
    name: 'homeview',
    component: () => import('../views/HomeView.vue'),
    meta: {requiresAuth: true}
  },
  {
    path: '/notloggedin',
    name: 'notLoggedIn',
    component: () => import('../views/NotLoggedIn.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/RegisterView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  // @ts-ignore
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.getIsUserLoggedIn) {
      next()
      return
    }
    next('/notLoggedIn')
  } else {
    next()
  }
})

export default router
