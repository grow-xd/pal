import { createRouter, createWebHistory } from 'vue-router'
import BaseView from '../views/AppView.vue'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import FriendsView from '../views/FriendsView.vue'
import CommView from '../views/CommView.vue'
import LogoutView from '../views/LogoutView.vue'
import ProfileView from '../views/ProfileView.vue'

const guard = function(to, from, next) {
  if(localStorage.getItem('token')){
    next()
  }else{
    next('/')
  }
}

const guard1 = function(to, from, next) {
  if(!localStorage.getItem('token')){
    next()
  }else{
    next('/home')
  }
}

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
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      beforeEnter: (to, from, next) => {
        guard(to, from, next)
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      beforeEnter: (to, from, next) => {
        guard(to, from, next)
      }
    },
    {
      path: '/friends',
      name: 'friends',
      component: FriendsView,
      beforeEnter: (to, from, next) => {
        guard(to, from, next)
      }
    },
    {
      path: '/communities',
      name: 'Communities',
      component: CommView,
      beforeEnter: (to, from, next) => {
        guard(to, from, next)
      }
    },
  ]
})

export default router
