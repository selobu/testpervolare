// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Products from '@/views/Products.vue'
import Signin from '@/views/signin.vue'
import Signup from '@/views/signup.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/products',
    name: 'Products',
    component: Products
  },
  {
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  }
]

const router = createRouter({ history: createWebHistory(), routes })
export default router
