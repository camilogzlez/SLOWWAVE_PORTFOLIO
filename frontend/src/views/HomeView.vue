<template>
  <div class="home">
    <!-- Fixed full-page background: animates based on total page scroll progress -->
    <WaveScrollAnimation />

    <HeroSection
      :tags="heroTags"
      :active-tag="activeHeroTag"
      @filter="onHeroFilter"
    />

    <ProjectsGrid
      :projects="projects"
      :loading="loading"
      :filter-category="activeCategory"
      @open="openModal"
      @category-change="activeCategory = $event"
    />

    <AboutSection />

    <ProjectModal :project="activeProject" :scroll-to="activeSection" @close="closeModal" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const tagToCategory = {
  'Web Dev': 'WEB',
  'Big Data': 'BIGDATA',
  'AI / ML': 'AI',
  'DevOps': 'DEVOPS',
}
import WaveScrollAnimation from '../components/WaveScrollAnimation.vue'
import HeroSection from '../components/HeroSection.vue'
import ProjectsGrid from '../components/ProjectsGrid.vue'
import AboutSection from '../components/AboutSection.vue'
import ProjectModal from '../components/ProjectModal.vue'
import { useProjects } from '../composables/useProjects'

const { projects, loading, fetchProjects } = useProjects()
const activeProject = ref(null)
const activeSection = ref(null)
const activeCategory = ref('ALL')
const activeHeroTag = ref(null)

const heroTags = ['Web Dev', 'Big Data', 'AI / ML', 'DevOps']

onMounted(fetchProjects)

function openModal(project, section = null) {
  activeProject.value = project
  activeSection.value = section
}

function closeModal() {
  activeProject.value = null
  activeSection.value = null
}

function onHeroFilter(tag) {
  const cat = tagToCategory[tag]
  if (activeCategory.value === cat) {
    // clicking the same tag again resets to ALL
    activeCategory.value = 'ALL'
    activeHeroTag.value = null
  } else {
    activeCategory.value = cat
    activeHeroTag.value = tag
  }
  document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
.home { padding-top: 0; }
</style>
