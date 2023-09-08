import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { useAuthStore } from '../stores/auth.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue'),
    },
    {
      path: '/plans',
      name: 'plans',
      component: () => import('../views/PricingView.vue')

    },
    {
      path: '/coursecontent',
      name: 'courseContent',
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
    {
      path: '/reset',
      name: 'reset',
      component: () => import('../views/ResetView.vue')
    },
    {
      path: '/reset_password',
      name: 'resetPassword',
      // beforeEnter: (to, from, next) => {
        
      // }
      component: () => import('../views/ResetTokenView.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})
// const loggedIn = false


router.beforeEach((to) => {
  // NOTE must declare instance of store after router has been set up
  const authStore = useAuthStore();
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!authStore.getIsUserLoggedIn)  
    {
      return {name: 'login'}
    }
  return true
  }
})


export default router
