<template>
  <section id="projects" class="projects-section">
    <div class="container">
      <!-- Section header -->
      <div class="section-header">
        <p class="section-label">SELECTED WORK</p>
        <h2 class="section-title">
          <span class="text-outline">My</span> Projects
        </h2>
      </div>

      <!-- Category filter bar -->
      <div class="filter-bar" role="tablist" aria-label="Filter projects by category">
        <button
          v-for="cat in categories"
          :key="cat.value"
          class="pill"
          :class="{ active: activeCategory === cat.value }"
          role="tab"
          :aria-selected="activeCategory === cat.value"
          @click="setCategory(cat.value)"
        >{{ cat.label }}</button>
      </div>

      <!-- Grid -->
      <TransitionGroup name="grid" tag="div" class="projects-grid">
        <ProjectCard
          v-for="project in filtered"
          :key="project.id"
          :project="project"
          @open="(p, section) => $emit('open', p, section)"
        />
      </TransitionGroup>

      <!-- Empty state -->
      <div v-if="!filtered.length && !loading" class="empty-state">
        <p>No projects in this category yet.</p>
      </div>

      <!-- Skeleton loading -->
      <div v-if="loading" class="projects-grid">
        <div v-for="i in 4" :key="i" class="skeleton-card"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import ProjectCard from './ProjectCard.vue'

const props = defineProps({
  projects: { type: Array, default: () => [] },
  loading: Boolean,
  filterCategory: { type: String, default: 'ALL' },
})
const emit = defineEmits(['open', 'category-change'])

const categories = [
  { label: 'All', value: 'ALL' },
  { label: 'Web Dev', value: 'WEB' },
  { label: 'Big Data', value: 'BIGDATA' },
  { label: 'AI / ML', value: 'AI' },
  { label: 'DevOps', value: 'DEVOPS' },
]

const activeCategory = ref(props.filterCategory)

watch(() => props.filterCategory, val => { activeCategory.value = val })

function setCategory(val) {
  activeCategory.value = val
  emit('category-change', val)
}

const filtered = computed(() =>
  activeCategory.value === 'ALL'
    ? props.projects
    : props.projects.filter(p => p.category === activeCategory.value)
)
</script>

<style scoped>
.projects-section {
  padding: 100px 0;
  position: relative;
  z-index: 1;
  background: linear-gradient(to right, var(--bg) 0%, var(--bg) 48%, transparent 56%);
}

.section-header { margin-bottom: 48px; }

.section-label {
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-light);
  margin-bottom: 12px;
}

.section-title {
  font-size: clamp(36px, 5vw, 64px);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1;
}

/* Filter bar */
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 48px;
}

/* Grid — masonry-inspired responsive columns */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

/* TransitionGroup animations */
.grid-enter-active { transition: opacity 0.35s ease, transform 0.35s ease; }
.grid-leave-active { transition: opacity 0.2s ease; position: absolute; }
.grid-enter-from { opacity: 0; transform: translateY(16px); }
.grid-leave-to   { opacity: 0; }

/* Skeleton */
.skeleton-card {
  aspect-ratio: 3/2;
  border-radius: var(--radius);
  background: linear-gradient(90deg, #F0F0F0 25%, #E4E4E4 50%, #F0F0F0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.empty-state {
  text-align: center;
  padding: 80px 0;
  color: var(--ink-light);
  font-size: 15px;
}
</style>
