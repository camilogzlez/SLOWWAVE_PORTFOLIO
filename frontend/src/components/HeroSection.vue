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
        <h1 id="hero-name">
          <span id="hero-first-name" class="text-outline">Camilo</span><br />
          <span>González</span>
        </h1>
        <p class="hero-sub">
          From raw data to real products. <br /> I engineer the intelligence behind the interface.
        </p>
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
  color: var(--ink-mid);
}

.scroll-line {
  width: 1.5px;
  height: 40px;
  background: linear-gradient(to bottom, var(--ink-mid), transparent);
  animation: scrollPulse 2s ease-in-out infinite;
}

@keyframes scrollPulse {
  0%, 100% { opacity: 0.6; transform: scaleY(1); }
  50% { opacity: 1; transform: scaleY(0.6); }
}

@media (max-width: 1100px) {
  .hero-inner {
    grid-template-columns: 1fr;
    padding-top: 100px;
  }
  .hero-tags { flex-direction: row; flex-wrap: wrap; }
}

@media (max-width: 700px) {
  /* no room beside the text for the wave illustration on narrow screens --
     go fully solid so it doesn't show through and clash with the heading */
  .hero {
    background: var(--bg);
  }
}
</style>
