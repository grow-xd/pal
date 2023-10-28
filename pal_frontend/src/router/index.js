import { createRouter, createWebHistory } from 'vue-router'
import BaseView from '../views/AppView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'base',
      component: BaseView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView,
      // beforeEnter: (to, from, next) => {
      //   guard(to, from, next)
      // }
    },
    {
      path: '/signup',
      name: 'Signup',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: SignupView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      
    },
  ]
})

export default router
