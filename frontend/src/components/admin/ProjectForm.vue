<template>
  <div class="form-wrap">
    <!-- Header -->
    <div class="form-header">
      <div>
        <p class="form-label">{{ isEdit ? 'EDIT PROJECT' : 'NEW PROJECT' }}</p>
        <h2 class="form-title">{{ isEdit ? form.title || 'Untitled' : 'Add project' }}</h2>
      </div>
      <button class="close-btn" @click="$emit('cancel')" aria-label="Close">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
          <path d="M3 3l12 12M15 3L3 15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </button>
    </div>

    <form class="form-body" @submit.prevent="save">

      <!-- Title + Slug -->
      <div class="field-row">
        <div class="field">
          <label>Title <span class="req">*</span></label>
          <input v-model="form.title" @input="autoSlug" placeholder="Homepedia" required />
        </div>
        <div class="field">
          <label>Slug <span class="req">*</span></label>
          <input v-model="form.slug" placeholder="homepedia" required />
          <span class="field-hint">URL-friendly, unique</span>
        </div>
      </div>

      <!-- Category + Type + Year + Team -->
      <div class="field-row">
        <div class="field">
          <label>Category <span class="req">*</span></label>
          <select v-model="form.category" required>
            <option value="">— pick one —</option>
            <option value="WEB">Web Dev</option>
            <option value="BIGDATA">Big Data</option>
            <option value="AI">AI / ML</option>
            <option value="DEVOPS">DevOps</option>
          </select>
        </div>
        <div class="field">
          <label>Project type</label>
          <select v-model="form.project_type">
            <option value="PERSONAL">Personal</option>
            <option value="SCHOOL">School</option>
            <option value="PROFESSIONAL">Professional</option>
          </select>
        </div>
        <div class="field field--sm">
          <label>Year</label>
          <input v-model="form.year" placeholder="2025" maxlength="4" />
        </div>
        <div class="field field--sm">
          <label>Team size</label>
          <input v-model.number="form.team_size" type="number" min="1" placeholder="1" />
        </div>
        <div class="field field--sm">
          <label>Order</label>
          <input v-model.number="form.order" type="number" placeholder="1" />
        </div>
      </div>

      <!-- Short description -->
      <div class="field">
        <label>Short description <span class="req">*</span></label>
        <textarea v-model="form.description" rows="2" placeholder="One-sentence summary shown on the card." required />
      </div>

      <!-- Long description -->
      <div class="field">
        <label>Long description</label>
        <textarea v-model="form.long_description" rows="5" placeholder="Full detail shown in the project modal." />
      </div>

      <!-- Tech stack -->
      <div class="field">
        <label>Tech stack</label>
        <div class="tag-input-wrap">
          <div class="tag-list">
            <span v-for="(t, i) in form.tech_stack" :key="i" class="tag-chip">
              {{ t }}
              <button type="button" @click="removeTag('tech_stack', i)">×</button>
            </span>
          </div>
          <input
            v-model="techInput"
            placeholder="Type and press Enter or comma"
            @keydown.enter.prevent="addTag('tech_stack', techInput)"
            @keydown.188.prevent="addTag('tech_stack', techInput)"
          />
        </div>
      </div>

      <!-- Topics / tags -->
      <div class="field">
        <label>Topics</label>
        <div class="tag-input-wrap">
          <div class="tag-list">
            <span v-for="(t, i) in form.tags" :key="i" class="tag-chip">
              {{ t }}
              <button type="button" @click="removeTag('tags', i)">×</button>
            </span>
          </div>
          <input
            v-model="tagInput"
            placeholder="e.g. ETL, NLP, Microservices"
            @keydown.enter.prevent="addTag('tags', tagInput)"
            @keydown.188.prevent="addTag('tags', tagInput)"
          />
        </div>
      </div>

      <!-- Thumbnail -->
      <div class="field">
        <label>Thumbnail</label>
        <div class="upload-area" :class="{ 'has-img': form.thumbnail }">
          <img v-if="form.thumbnail" :src="form.thumbnail" class="thumb-preview" alt="thumbnail" />
          <label class="upload-btn" :class="{ 'upload-btn--overlay': form.thumbnail }">
            <input type="file" accept="image/*" @change="uploadFile($event, 'thumbnail')" />
            {{ form.thumbnail ? 'Replace image' : 'Upload image' }}
          </label>
          <button v-if="form.thumbnail" type="button" class="clear-thumb" @click="form.thumbnail = ''">Remove</button>
        </div>
        <span class="field-hint">Or paste a URL:</span>
        <input v-model="form.thumbnail" placeholder="https://... or /uploads/..." />
      </div>

      <!-- Video URL -->
      <div class="field">
        <label>Video URL</label>
        <input v-model="form.video_url" placeholder="YouTube (youtube.com/watch?v=…) or Loom (loom.com/share/…)" />
      </div>

      <!-- Architecture diagram -->
      <div class="field">
        <label>Architecture Diagram</label>
        <div class="upload-area" :class="{ 'has-img': form.arch_diagram }">
          <img v-if="form.arch_diagram" :src="form.arch_diagram" class="thumb-preview" alt="diagram" />
          <label class="upload-btn" :class="{ 'upload-btn--overlay': form.arch_diagram }">
            <input type="file" accept="image/*" @change="uploadFile($event, 'arch_diagram')" />
            {{ form.arch_diagram ? 'Replace' : 'Upload diagram' }}
          </label>
          <button v-if="form.arch_diagram" type="button" class="clear-thumb" @click="form.arch_diagram = ''">Remove</button>
        </div>
        <span class="field-hint">Or paste a URL:</span>
        <input v-model="form.arch_diagram" placeholder="https://... or /uploads/..." />
      </div>

      <!-- Links -->
      <div class="field-row">
        <div class="field">
          <label>GitHub URL</label>
          <input v-model="form.github_url" placeholder="https://github.com/..." />
        </div>
        <div class="field">
          <label>Demo URL</label>
          <input v-model="form.demo_url" placeholder="https://..." />
        </div>
      </div>

      <!-- Save -->
      <div class="form-footer">
        <span v-if="saveError" class="save-error">{{ saveError }}</span>
        <button type="button" class="btn-ghost" @click="$emit('cancel')">Cancel</button>
        <button type="submit" class="btn-primary" :disabled="saving">
          {{ saving ? 'Saving…' : isEdit ? 'Save changes' : 'Add project' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import axios from 'axios'

const props = defineProps({ project: Object })
const emit = defineEmits(['saved', 'cancel'])

const isEdit = computed(() => !!props.project?.id)

const blank = () => ({
  title: '', slug: '', category: '', description: '', long_description: '',
  tech_stack: [], tags: [], thumbnail: '', video_url: '', arch_diagram: '',
  github_url: '', demo_url: '', year: '', team_size: null, order: 0, project_type: 'PERSONAL',
})

const form = ref(blank())
const techInput = ref('')
const tagInput = ref('')
const saving = ref(false)
const saveError = ref('')

watch(() => props.project, p => {
  form.value = p ? { ...blank(), ...p } : blank()
  techInput.value = ''
  tagInput.value = ''
  saveError.value = ''
}, { immediate: true })

function autoSlug() {
  if (!isEdit.value) {
    form.value.slug = form.value.title
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, '')
  }
}

function addTag(field, val) {
  const v = val.trim().replace(/,$/, '')
  if (v && !form.value[field].includes(v)) {
    form.value[field].push(v)
  }
  if (field === 'tech_stack') techInput.value = ''
  else tagInput.value = ''
}

function removeTag(field, i) {
  form.value[field].splice(i, 1)
}

async function uploadFile(e, field) {
  const file = e.target.files[0]
  if (!file) return
  const fd = new FormData()
  fd.append('file', file)
  const { data } = await axios.post('/api/upload', fd)
  form.value[field] = data.url
}

async function save() {
  saving.value = true
  saveError.value = ''
  try {
    const payload = { ...form.value }
    if (isEdit.value) {
      await axios.put(`/api/projects/${props.project.id}`, payload)
    } else {
      await axios.post('/api/projects', payload)
    }
    emit('saved')
  } catch (e) {
    saveError.value = e.response?.data?.detail ?? e.message
  } finally {
    saving.value = false
  }
}
</script>

<style scoped>
.form-wrap { display: flex; flex-direction: column; height: 100%; }

/* Header */
.form-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 28px 32px 20px;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  background: var(--bg);
  z-index: 10;
}

.form-label {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-light);
  margin-bottom: 4px;
}

.form-title { font-size: 22px; font-weight: 700; letter-spacing: -0.02em; }

.close-btn {
  background: none;
  border: 1px solid var(--border);
  border-radius: 50%;
  width: 36px; height: 36px;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; color: var(--ink);
  transition: background 0.2s, color 0.2s;
  flex-shrink: 0;
}
.close-btn:hover { background: var(--ink); color: var(--bg); }

/* Body */
.form-body {
  flex: 1;
  padding: 28px 32px 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.field { display: flex; flex-direction: column; gap: 6px; flex: 1; }
.field--sm { flex: 0 0 100px; }

.field-row { display: flex; gap: 16px; flex-wrap: wrap; }

label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-mid);
}

.req { color: #c0392b; }

input, select, textarea {
  font-family: var(--font-sans);
  font-size: 14px;
  color: var(--ink);
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 9px 12px;
  outline: none;
  transition: border-color 0.2s;
  width: 100%;
}
input:focus, select:focus, textarea:focus { border-color: var(--ink); }
textarea { resize: vertical; }

.field-hint { font-size: 11px; color: var(--ink-light); margin-top: -2px; }

/* Tag input */
.tag-input-wrap {
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 8px 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: border-color 0.2s;
}
.tag-input-wrap:focus-within { border-color: var(--ink); }

.tag-list { display: flex; flex-wrap: wrap; gap: 6px; }

.tag-chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-family: var(--font-mono);
  background: #F0F0F0;
  padding: 3px 8px;
  border-radius: 2px;
}
.tag-chip button {
  background: none;
  border: none;
  font-size: 14px;
  cursor: pointer;
  color: var(--ink-light);
  padding: 0;
  line-height: 1;
  width: auto;
  transition: color 0.15s;
}
.tag-chip button:hover { color: #c0392b; }

.tag-input-wrap input {
  border: none;
  padding: 0;
  font-size: 13px;
}
.tag-input-wrap input:focus { border: none; }

/* Upload */
.upload-area {
  border: 1px dashed var(--border);
  border-radius: 2px;
  padding: 16px;
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
  min-height: 72px;
}
.upload-area.has-img { padding: 8px; }

.thumb-preview {
  width: 80px;
  height: 50px;
  object-fit: cover;
  border-radius: 2px;
  flex-shrink: 0;
}

.upload-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.04em;
  border: 1px solid var(--ink);
  border-radius: 2px;
  padding: 7px 14px;
  cursor: pointer;
  text-transform: none;
  color: var(--ink);
  transition: background 0.2s, color 0.2s;
}
.upload-btn:hover { background: var(--ink); color: var(--bg); }
.upload-btn input { display: none; }

.clear-thumb {
  font-size: 12px;
  background: none;
  border: none;
  color: var(--ink-light);
  cursor: pointer;
  text-decoration: underline;
  padding: 0;
  width: auto;
}
.clear-thumb:hover { color: #c0392b; }

/* Footer */
.form-footer {
  display: flex;
  align-items: center;
  gap: 12px;
  justify-content: flex-end;
  padding: 20px 32px 28px;
  border-top: 1px solid var(--border);
  margin-top: 8px;
  background: var(--bg);
}

.save-error {
  font-size: 12px;
  color: #c0392b;
  margin-right: auto;
}

.btn-primary {
  background: var(--ink);
  color: var(--bg);
  border: none;
  border-radius: 2px;
  padding: 10px 22px;
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font-sans);
  cursor: pointer;
  transition: opacity 0.2s;
}
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
.btn-primary:hover:not(:disabled) { opacity: 0.8; }

.btn-ghost {
  background: transparent;
  color: var(--ink);
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font-sans);
  cursor: pointer;
  transition: border-color 0.2s;
}
.btn-ghost:hover { border-color: var(--ink); }
</style>
