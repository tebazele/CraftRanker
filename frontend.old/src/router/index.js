// frontend\src\router\index.js
// Author: Author : Andre Baldo (http://github.com/andrebaldo/) 
import Vue from 'vue'
import VueRouter from 'vue-router'

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
    path: '/coursecontent',
    name: 'CourseContent',
    component: () => import('../views/CourseContent.vue'),
    meta: {requiresAuth: true}
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
    next('/login')
  } else {
    next()
  }
})

export default router
