import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/evenness',
    name: 'evenness',
    component: () => import('../views/EvennessView.vue')
  },
  {
    path: '/crack',
    name: 'crack',
    component: () => import('../views/CrackView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
