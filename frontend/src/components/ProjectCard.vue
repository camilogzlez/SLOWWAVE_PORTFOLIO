<template>
  <article class="project-card" @click="$emit('open', project)" tabindex="0" @keydown.enter="$emit('open', project)">
    <div class="card-thumb">
      <img v-if="project.thumbnail" :src="project.thumbnail" :alt="project.title" loading="lazy" />
      <div v-else class="card-thumb-placeholder">
        <CategoryIcon :category="project.category" />
      </div>
      <span class="card-category pill">{{ categoryLabel }}</span>
    </div>

    <div class="card-body">
      <h3 class="card-title">{{ project.title }}</h3>
      <p class="card-desc">{{ localizedProject.description }}</p>
      <div class="card-stack">
        <span v-for="tech in project.tech_stack.slice(0, 4)" :key="tech" class="stack-tag">{{ tech }}</span>
        <span v-if="project.tech_stack.length > 4" class="stack-tag stack-more">
          +{{ project.tech_stack.length - 4 }}
        </span>
      </div>
    </div>

    <!-- Direct-action link icons — click without opening modal -->
    <div v-if="project.github_url || project.demo_url || project.video_url || project.arch_diagram" class="card-icons" @click.stop>
      <a v-if="project.github_url" :href="project.github_url" target="_blank" rel="noopener" class="card-icon" :title="t('projects.iconGithub')">
        <svg width="15" height="15" viewBox="0 0 16 16" fill="currentColor">
          <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
        </svg>
      </a>
      <a v-if="project.demo_url" :href="project.demo_url" target="_blank" rel="noopener" class="card-icon" :title="t('projects.iconLiveDemo')">
        <svg width="13" height="13" viewBox="-1 0 12 12" fill="currentColor">
          <path d="M2 1.5l9 4.5-9 4.5V1.5z"/>
        </svg>
      </a>
      <button v-if="project.video_url" class="card-icon" :title="t('projects.iconWatchDemo')" @click.stop="$emit('open', project, 'video')">
        <svg width="13" height="13" viewBox="-1 0 12 12" fill="currentColor">
          <path d="M2 1.5l9 4.5-9 4.5V1.5z"/>
        </svg>
      </button>
      <button v-if="project.arch_diagram" class="card-icon" :title="t('projects.iconArchDiagram')" @click.stop="$emit('open', project, 'arch')">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">
          <rect x="1" y="4" width="4" height="3" rx="0.5"/>
          <rect x="9" y="1" width="4" height="3" rx="0.5"/>
          <rect x="9" y="10" width="4" height="3" rx="0.5"/>
          <path d="M5 5.5h2.5V2.5H9M5 5.5h2.5v6H9"/>
        </svg>
      </button>
    </div>

    <span v-if="project.project_type" class="card-type">{{ typeLabel }}</span>

    <div class="card-hover-cta">
      <span>{{ t('projects.viewProject') }}</span>
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <path d="M1 6h10M6 1l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
  </article>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import CategoryIcon from './CategoryIcon.vue'
import { localizeProject } from '../i18n/projectTranslations'

const props = defineProps({ project: Object })
defineEmits(['open'])  // open(project, section?) — section: 'video' | 'arch' | undefined

const { t, locale } = useI18n()

const localizedProject = computed(() => localizeProject(props.project, locale.value))

// category/project-type badges stay in English in both locales by design
const labels = { WEB: 'Web Dev', BIGDATA: 'Big Data', AI: 'AI / ML', DEVOPS: 'DevOps' }
const categoryLabel = labels[props.project.category] ?? props.project.category

const typeLabels = { SCHOOL: 'Epitech', PERSONAL: 'Personal', PROFESSIONAL: 'Pro' }
const typeLabel = typeLabels[props.project.project_type] ?? props.project.project_type
</script>

<style scoped>
.project-card {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  background: var(--bg);
  transition: border-color 0.25s, transform 0.25s, box-shadow 0.25s;
  position: relative;
  outline: none;
}

.project-card:hover, .project-card:focus {
  border-color: var(--ink);
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.08);
}

/* Thumbnail */
.card-thumb {
  aspect-ratio: 16 / 10;
  background: #F0F0F0;
  position: relative;
  overflow: hidden;
}

.card-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-card:hover .card-thumb img { transform: scale(1.04); }

.card-thumb-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #F5F5F5 0%, #EBEBEB 100%);
}

.card-category {
  position: absolute;
  top: 12px;
  left: 12px;
  background: var(--bg);
  color: var(--ink);
  border-color: var(--ink);
  cursor: default;
}

/* Body */
.card-body { padding: 20px 20px 16px; flex: 1; }

.card-title {
  font-size: 18px;
  font-weight: 600;
  letter-spacing: -0.02em;
  margin-bottom: 8px;
}

.card-desc {
  font-size: 13px;
  color: var(--ink-mid);
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin-bottom: 14px;
}

.card-stack { display: flex; flex-wrap: wrap; gap: 6px; }

.stack-tag {
  font-size: 10px;
  font-family: var(--font-mono);
  letter-spacing: 0.04em;
  background: #F0F0F0;
  color: var(--ink-mid);
  padding: 3px 8px;
  border-radius: 2px;
}

.stack-more { color: var(--ink-light); }

/* Link icons strip */
.card-icons {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0 20px 14px;
}

.card-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border: 1px solid var(--border);
  border-radius: 50%;
  color: var(--ink-light);
  transition: border-color 0.2s, color 0.2s, background 0.2s;
  flex-shrink: 0;
}
.card-icon:hover { border-color: var(--ink); color: var(--ink); background: var(--ink); color: var(--bg); }


/* Hover CTA */
.card-hover-cta {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-top: 1px solid var(--border);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-light);
  transition: color 0.2s;
}

.project-card:hover .card-hover-cta,
.project-card:focus .card-hover-cta { color: var(--ink); }

.card-type {
  position: absolute;
  bottom: 50px;
  right: 16px;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-light);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0.65;
}
</style>
