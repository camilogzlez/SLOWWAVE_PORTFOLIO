import { ref } from 'vue'
import axios from 'axios'

export function useProjects() {
  const projects = ref([])
  const loading = ref(false)
  const error = ref(null)

  async function fetchProjects() {
    loading.value = true
    error.value = null
    try {
      const { data } = await axios.get('/api/projects')
      projects.value = data
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { projects, loading, error, fetchProjects }
}
