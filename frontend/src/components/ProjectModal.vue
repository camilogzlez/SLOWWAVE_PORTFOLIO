<template>
  <Teleport to="body">
    <Transition name="overlay">
      <div v-if="project" class="modal-overlay" @click.self="$emit('close')" />
    </Transition>

    <Transition name="modal">
      <div v-if="project" class="modal-panel" role="dialog" :aria-label="project.title" aria-modal="true">
        <button class="modal-close" @click="$emit('close')" :aria-label="t('modal.close')">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M4 4l12 12M16 4L4 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </button>

        <div class="modal-scroll" ref="modalScroll">
          <!-- Video (YouTube or Loom) or thumbnail -->
          <div class="modal-media">
            <div v-if="videoEmbed" class="video-wrapper">
              <iframe
                :src="videoEmbed"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              />
            </div>
            <div v-else-if="project.thumbnail" class="media-img">
              <img :src="project.thumbnail" :alt="project.title" />
            </div>
            <div v-else class="media-placeholder">
              <CategoryIcon :category="project.category" :size="64" />
            </div>
          </div>

          <div class="modal-body">
            <!-- Meta row -->
            <div class="modal-meta">
              <span class="pill">{{ categoryLabel }}</span>
              <span v-if="project.project_type" class="meta-type">{{ typeLabel }}</span>
              <span v-if="project.year" class="meta-item">{{ project.year }}</span>
              <span v-if="project.team_size" class="meta-item">
                {{ project.team_size === 1 ? t('modal.solo') : t('modal.teamOf', { count: project.team_size }) }}
              </span>
            </div>

            <h2 class="modal-title">{{ project.title }}</h2>

            <p class="modal-desc">{{ localizedProject.long_description || localizedProject.description }}</p>

            <!-- Tech stack -->
            <div class="modal-section">
              <h4 class="modal-section-label">{{ t('modal.techStack') }}</h4>
              <div class="tag-list">
                <span v-for="tech in project.tech_stack" :key="tech" class="tech-tag">{{ tech }}</span>
              </div>
            </div>

            <!-- Topics -->
            <div v-if="project.tags?.length" class="modal-section">
              <h4 class="modal-section-label">{{ t('modal.topics') }}</h4>
              <div class="tag-list">
                <span v-for="tag in project.tags" :key="tag" class="pill" style="cursor:default">{{ tag }}</span>
              </div>
            </div>

            <!-- Architecture diagram -->
            <div v-if="project.arch_diagram" class="modal-section" ref="archRef">
              <h4 class="modal-section-label">{{ t('modal.architecture') }}</h4>
              <a :href="project.arch_diagram" target="_blank" rel="noopener" class="arch-diagram-wrap">
                <img :src="project.arch_diagram" alt="Architecture diagram" class="arch-diagram" />
                <span class="arch-diagram-overlay">
                  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
                    <path d="M7 3H3v12h12v-4M10 3h5v5M15 3L8 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  {{ t('modal.openFullSize') }}
                </span>
              </a>
            </div>

            <!-- Links -->
            <div class="modal-links">
              <a v-if="project.github_url" :href="project.github_url" target="_blank" rel="noopener" class="modal-link">
                <!-- GitHub icon -->
                <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
                  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                {{ t('modal.github') }}
              </a>
              <a v-if="project.video_url && !videoEmbed" :href="project.video_url" target="_blank" rel="noopener" class="modal-link">
                <!-- Play icon -->
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.4"/>
                  <path d="M6.5 5.5l4 2.5-4 2.5V5.5z" fill="currentColor"/>
                </svg>
                {{ t('modal.watchDemo') }}
              </a>
              <a v-if="project.demo_url" :href="project.demo_url" target="_blank" rel="noopener" class="modal-link modal-link--primary">
                <svg width="14" height="14" viewBox="-1 0 12 12" fill="currentColor">
                  <path d="M2 1.5l9 4.5-9 4.5V1.5z"/>
                </svg>
                {{ t('modal.liveDemo') }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { computed, watch, ref, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'
import CategoryIcon from './CategoryIcon.vue'
import { localizeProject } from '../i18n/projectTranslations'

const props = defineProps({ project: Object, scrollTo: String })
defineEmits(['close'])

const { t, locale } = useI18n()

const archRef = ref(null)
const modalScroll = ref(null)

const localizedProject = computed(() => localizeProject(props.project, locale.value) ?? {})

// category/project-type badges stay in English in both locales by design
const labels = { WEB: 'Web Dev', BIGDATA: 'Big Data', AI: 'AI / ML', DEVOPS: 'DevOps' }
const categoryLabel = computed(() => labels[props.project?.category] ?? props.project?.category)

const typeLabels = { SCHOOL: 'Epitech project', PERSONAL: 'Personal project', PROFESSIONAL: 'Professional' }
const typeLabel = computed(() => typeLabels[props.project?.project_type] ?? props.project?.project_type)

const videoEmbed = computed(() => {
  const url = props.project?.video_url
  if (!url) return null
  const autoplay = props.scrollTo === 'video' ? 1 : 0
  const yt = url.match(/(?:v=|youtu\.be\/)([A-Za-z0-9_-]{11})/)
  if (yt) return `https://www.youtube.com/embed/${yt[1]}?rel=0&mute=1&autoplay=${autoplay}`
  const loom = url.match(/loom\.com\/(?:share|embed)\/([a-zA-Z0-9]+)/)
  if (loom) return `https://www.loom.com/embed/${loom[1]}?muted=1&autoplay=${autoplay}`
  return null
})

watch([() => props.project, () => props.scrollTo], async ([proj, section]) => {
  document.body.style.overflow = proj ? 'hidden' : ''
  if (proj && section === 'arch') {
    await nextTick()
    setTimeout(() => {
      archRef.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }, 320) // wait for the modal open transition
  }
})
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10,10,10,0.55);
  backdrop-filter: blur(4px);
  z-index: 200;
}

.modal-panel {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: 201;
  width: min(680px, 100vw);
  background: var(--bg);
  display: flex;
  flex-direction: column;
  box-shadow: -24px 0 80px rgba(0,0,0,0.12);
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 10;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--ink);
  transition: background 0.2s, border-color 0.2s;
}
.modal-close:hover { background: var(--ink); color: var(--bg); border-color: var(--ink); }

.modal-scroll { overflow-y: auto; flex: 1; overscroll-behavior: contain; }

/* Media */
.modal-media { width: 100%; aspect-ratio: 16/9; background: #F0F0F0; overflow: hidden; }

.video-wrapper { position: relative; width: 100%; height: 100%; }
.video-wrapper iframe { position: absolute; inset: 0; width: 100%; height: 100%; }

.media-img img { width: 100%; height: 100%; object-fit: cover; }

.media-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #F5F5F5, #E8E8E8);
}

/* Body */
.modal-body { padding: 32px; }

.modal-meta { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 16px; }

.meta-item { font-size: 12px; color: var(--ink-light); letter-spacing: 0.04em; }

.meta-type {
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-light);
  background: #F0F0F0;
  border-radius: 2px;
  padding: 2px 7px;
}

.modal-title {
  font-size: clamp(24px, 4vw, 36px);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin-bottom: 20px;
}

.modal-desc { font-size: 15px; line-height: 1.75; color: var(--ink-mid); margin-bottom: 32px; }

.modal-section { margin-bottom: 28px; }

.modal-section-label {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink-light);
  margin-bottom: 12px;
}

.tag-list { display: flex; flex-wrap: wrap; gap: 8px; }

.tech-tag { font-size: 12px; font-family: var(--font-mono); background: #F0F0F0; padding: 5px 10px; border-radius: 2px; }

/* Architecture diagram */
.arch-diagram-wrap {
  display: block;
  position: relative;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  cursor: pointer;
}
.arch-diagram {
  width: 100%;
  height: auto;
  display: block;
  transition: filter 0.25s;
}
.arch-diagram-overlay {
  position: absolute;
  inset: 0;
  background: rgba(10,10,10,0.5);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  opacity: 0;
  transition: opacity 0.2s;
}
.arch-diagram-wrap:hover .arch-diagram-overlay { opacity: 1; }

/* Links */
.modal-links {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  margin-top: 32px;
}

.modal-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border: 1px solid var(--ink);
  border-radius: var(--radius);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  transition: background 0.2s, color 0.2s;
}
.modal-link:hover { background: var(--ink); color: var(--bg); }

.modal-link--primary { background: var(--ink); color: var(--bg); }
.modal-link--primary:hover { background: #3A3A3A; border-color: #3A3A3A; }
</style>
