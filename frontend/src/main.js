import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import HomeView from './views/HomeView.vue'
import AdminView from './views/AdminView.vue'
import { i18n, SUPPORTED_LOCALES, DEFAULT_LOCALE, detectLocale, persistLocale } from './i18n'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: () => `/${detectLocale()}` },
    { path: '/:locale(en|fr)', component: HomeView },
    { path: '/admin', component: AdminView },
    { path: '/:pathMatch(.*)*', redirect: () => `/${DEFAULT_LOCALE}` },
  ],
  // a pure language switch (/en <-> /fr) keeps the scroll position; any
  // other navigation (e.g. into/out of /admin, or the initial redirect
  // from "/") resets to the top.
  scrollBehavior: (to, from) =>
    to.params.locale && from.params.locale && to.params.locale !== from.params.locale
      ? false
      : { top: 0 },
})

router.beforeEach((to) => {
  const locale = to.params.locale
  if (locale && SUPPORTED_LOCALES.includes(locale)) {
    i18n.global.locale.value = locale
    document.documentElement.lang = locale
    persistLocale(locale)
  }
})

createApp(App).use(router).use(i18n).mount('#app')
