<template>
  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-tags">
        <span
          v-for="tag in tags"
          :key="tag"
          class="pill"
          :class="{ active: activeTag === tag }"
          @click="$emit('filter', tag)"
        >{{ tag }}</span>
      </div>

      <div class="hero-heading">
        <h1>
          <span class="text-outline">Camilo</span><br />
          <span>González</span>
        </h1>
        <p class="hero-sub">
          From raw data to real products. <br /> I engineer the intelligence behind the interface.
        </p>
        <a href="#projects" class="hero-cta">
          See my work
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
            <path d="M1 7h12M7 1l6 6-6 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </div>
    </div>

    <div class="scroll-indicator">
      <span class="scroll-label">scroll</span>
      <div class="scroll-line"></div>
    </div>
  </section>
</template>

<script setup>
defineProps({ tags: Array, activeTag: String })
defineEmits(['filter'])
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-top: 80px;
  position: relative;
  z-index: 1;
  /* left side solid so text is readable; right side transparent so animation shows through */
  background: linear-gradient(to right, var(--bg) 0%, var(--bg) 42%, transparent 58%);
}

.hero-inner {
  display: grid;
  grid-template-columns: 180px 1fr;
  align-items: center;
  gap: 48px;
  min-height: calc(100vh - 80px);
  padding-top: 40px;
  padding-bottom: 80px;
}

.hero-tags {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.hero-heading h1 {
  font-size: clamp(52px, 7vw, 96px);
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.03em;
  margin-bottom: 28px;
}

.hero-sub {
  font-size: 16px;
  color: var(--ink-mid);
  line-height: 1.7;
  max-width: 380px;
  margin-bottom: 40px;
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border-bottom: 1.5px solid var(--ink);
  padding-bottom: 4px;
  transition: gap 0.25s ease, opacity 0.2s;
}
.hero-cta:hover { gap: 16px; opacity: 0.7; }

.scroll-indicator {
  position: absolute;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.scroll-label {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-light);
}

.scroll-line {
  width: 1px;
  height: 40px;
  background: linear-gradient(to bottom, var(--ink-light), transparent);
  animation: scrollPulse 2s ease-in-out infinite;
}

@keyframes scrollPulse {
  0%, 100% { opacity: 0.4; transform: scaleY(1); }
  50% { opacity: 1; transform: scaleY(0.6); }
}

@media (max-width: 1100px) {
  .hero-inner {
    grid-template-columns: 1fr;
    padding-top: 100px;
  }
  .hero-tags { flex-direction: row; flex-wrap: wrap; }
}
</style>
