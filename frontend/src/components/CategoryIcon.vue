<template>
  <svg :width="size" :height="size" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- WEB -->
    <template v-if="category === 'WEB'">
      <rect x="6" y="10" width="36" height="28" rx="2" stroke="#0A0A0A" stroke-width="1.5"/>
      <line x1="6" y1="18" x2="42" y2="18" stroke="#0A0A0A" stroke-width="1.5"/>
      <circle cx="11" cy="14" r="1.5" fill="#0A0A0A"/>
      <circle cx="16" cy="14" r="1.5" fill="#0A0A0A"/>
      <line x1="13" y1="24" x2="35" y2="24" stroke="#0A0A0A" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="13" y1="30" x2="27" y2="30" stroke="#0A0A0A" stroke-width="1.5" stroke-linecap="round"/>
    </template>
    <!-- BIGDATA -->
    <template v-else-if="category === 'BIGDATA'">
      <ellipse cx="24" cy="14" rx="14" ry="5" stroke="#0A0A0A" stroke-width="1.5"/>
      <path d="M10 14v8c0 2.76 6.27 5 14 5s14-2.24 14-5v-8" stroke="#0A0A0A" stroke-width="1.5"/>
      <path d="M10 22v8c0 2.76 6.27 5 14 5s14-2.24 14-5v-8" stroke="#0A0A0A" stroke-width="1.5"/>
    </template>
    <!-- AI -->
    <template v-else-if="category === 'AI'">
      <circle cx="24" cy="24" r="6" stroke="#0A0A0A" stroke-width="1.5"/>
      <circle cx="24" cy="8" r="3" stroke="#0A0A0A" stroke-width="1.5"/>
      <circle cx="24" cy="40" r="3" stroke="#0A0A0A" stroke-width="1.5"/>
      <circle cx="8" cy="24" r="3" stroke="#0A0A0A" stroke-width="1.5"/>
      <circle cx="40" cy="24" r="3" stroke="#0A0A0A" stroke-width="1.5"/>
      <line x1="24" y1="11" x2="24" y2="18" stroke="#0A0A0A" stroke-width="1.5"/>
      <line x1="24" y1="30" x2="24" y2="37" stroke="#0A0A0A" stroke-width="1.5"/>
      <line x1="11" y1="24" x2="18" y2="24" stroke="#0A0A0A" stroke-width="1.5"/>
      <line x1="30" y1="24" x2="37" y2="24" stroke="#0A0A0A" stroke-width="1.5"/>
    </template>
    <!-- DEVOPS -->
    <template v-else>
      <path d="M24 6 L40 16 L40 32 L24 42 L8 32 L8 16 Z" stroke="#0A0A0A" stroke-width="1.5" fill="none"/>
      <path d="M24 14 L32 19 L32 29 L24 34 L16 29 L16 19 Z" stroke="#0A0A0A" stroke-width="1.5" fill="none"/>
    </template>
  </svg>
</template>

<script setup>
defineProps({
  category: { type: String, default: 'WEB' },
  size: { type: Number, default: 48 },
})
</script>
