<template>
  <header :class="['site-header', { scrolled }]">
    <div class="container header-inner">
      <router-link :to="`/${locale}`" class="logo" aria-label="Slowwave — home">
        <img src="../assets/slowwave-logo.png" alt="Slowwave" class="logo-img" />
      </router-link>

      <nav class="nav">
        <a href="#projects" class="nav-link">{{ t('nav.work') }}</a>
        <a href="#about" class="nav-link">{{ t('nav.about') }}</a>
        <a href="#contact" class="nav-link">{{ t('nav.contact') }}</a>
        <button type="button" class="lang-switch" @click="switchLocale">{{ otherLocale }}</button>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRoute, useRouter } from 'vue-router'

const scrolled = ref(false)

function onScroll() {
  scrolled.value = window.scrollY > 40
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))

const { t, locale } = useI18n()
const route = useRoute()
const router = useRouter()

const otherLocale = computed(() => (locale.value === 'fr' ? 'EN' : 'FR'))

function switchLocale() {
  const next = locale.value === 'fr' ? 'en' : 'fr'
  router.push({ path: `/${next}`, hash: route.hash })
}
</script>

<style scoped>
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 20px 0;
  transition: padding 0.3s ease, background 0.3s ease, border-color 0.3s ease;
  border-bottom: 1px solid transparent;
}

.site-header.scrolled {
  padding: 12px 0;
  background: rgba(250, 250, 250, 0.92);
  backdrop-filter: blur(12px);
  border-bottom-color: var(--border);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  transition: opacity 0.2s;
}
.logo:hover { opacity: 0.7; }

.logo-img {
  height: 56px;
  width: auto;
  display: block;
}

.nav { display: flex; gap: 32px; }

.nav-link {
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--ink-mid);
  transition: color 0.2s;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 1px;
  background: var(--ink);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.25s ease;
}

.nav-link:hover { color: var(--ink); }
.nav-link:hover::after { transform: scaleX(1); }

.lang-switch {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--ink-mid);
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 4px 8px;
  transition: color 0.2s, border-color 0.2s;
}
.lang-switch:hover { color: var(--ink); border-color: var(--ink); }
</style>
