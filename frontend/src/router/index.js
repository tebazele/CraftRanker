import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// FIXME why can't I access the store from my router?
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
