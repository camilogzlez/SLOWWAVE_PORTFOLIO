import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import HomeView from './views/HomeView.vue'
import AdminView from './views/AdminView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/admin', component: AdminView },
  ],
  scrollBehavior: () => ({ top: 0 }),
})

createApp(App).use(router).mount('#app')
