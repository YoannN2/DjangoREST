import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/auth/Login.vue'
import Signup from '../views/auth/Signup.vue'
//import Article from '../views/article/article.vue'
import Articles from '../views/article/articles.vue'

Vue.use(VueRouter)

const routes = [
  /* HOME */
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  /* AUTH */
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },

  /* ARTICLE */
  {
    path: "/articles",
    name: "Articles",
    component: Articles,
    meta: {
      requireLogin: true,
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
