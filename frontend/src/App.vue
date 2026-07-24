<template>
  <template v-if="!isAdmin">
    <AppHeader />
    <main>
      <RouterView />
    </main>
    <AppFooter />
  </template>
  <template v-else>
    <RouterView />
  </template>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'

const route = useRoute()
const isAdmin = computed(() => route.path.startsWith('/admin'))
</script>
