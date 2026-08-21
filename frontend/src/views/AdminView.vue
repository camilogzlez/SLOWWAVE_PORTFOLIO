<template>
  <!-- PIN gate -->
  <div v-if="!authed" class="pin-gate">
    <div class="pin-box">
      <p class="pin-label">ADMIN ACCESS</p>
      <h2 class="pin-title">Enter PIN</h2>
      <input
        ref="pinInput"
        v-model="pinEntry"
        type="password"
        class="pin-input"
        placeholder="••••"
        maxlength="64"
        @keydown.enter="checkPin"
        autocomplete="current-password"
      />
      <p v-if="pinError" class="pin-error">Wrong PIN. Try again.</p>
      <button class="btn-primary" :disabled="pinChecking" @click="checkPin">{{ pinChecking ? 'Checking…' : 'Enter' }}</button>
    </div>
  </div>

  <!-- Admin panel -->
  <div v-else class="admin-wrap">
    <!-- Sidebar -->
    <aside class="admin-sidebar">
      <a href="/" class="sidebar-logo" aria-label="Slowwave home">
        <img src="../assets/slowwave-logo.png" alt="Slowwave" style="height:44px;width:auto;display:block" />
      </a>
      <nav class="sidebar-nav">
        <span class="sidebar-section">Portfolio</span>
        <a href="/" class="sidebar-link" target="_blank">View site ↗</a>
      </nav>
      <button class="sidebar-logout" @click="logout">Log out</button>
    </aside>

    <!-- Main content -->
    <main class="admin-main">
      <!-- Header -->
      <div class="admin-header">
        <div>
          <p class="admin-label">BACKOFFICE</p>
          <h1 class="admin-title">Projects</h1>
        </div>
        <button class="btn-primary" @click="openForm(null)">
          + Add project
        </button>
      </div>

      <!-- Stats bar -->
      <div class="stats-bar">
        <div v-for="s in stats" :key="s.label" class="stat-item">
          <span class="stat-num">{{ s.count }}</span>
          <span class="stat-label">{{ s.label }}</span>
        </div>
      </div>

      <!-- Project table -->
      <div class="table-wrap">
        <table class="project-table">
          <thead>
            <tr>
              <th class="th-handle"></th>
              <th>Title</th>
              <th>Category</th>
              <th>Year</th>
              <th>Tech stack</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody v-if="loading">
            <tr><td colspan="6" class="table-loading">Loading…</td></tr>
          </tbody>
          <draggable
            v-else
            v-model="projects"
            tag="tbody"
            item-key="id"
            handle=".drag-handle"
            animation="180"
            ghost-class="row-ghost"
            @end="saveOrder"
          >
            <template #item="{ element: p }">
              <tr class="table-row">
                <td class="cell-drag">
                  <span class="drag-handle" title="Drag to reorder">
                    <svg width="10" height="14" viewBox="0 0 10 14" fill="currentColor">
                      <circle cx="3" cy="2.5" r="1.2"/><circle cx="7" cy="2.5" r="1.2"/>
                      <circle cx="3" cy="7"   r="1.2"/><circle cx="7" cy="7"   r="1.2"/>
                      <circle cx="3" cy="11.5" r="1.2"/><circle cx="7" cy="11.5" r="1.2"/>
                    </svg>
                  </span>
                </td>
                <td class="cell-title">
                  <span class="project-name">{{ p.title }}</span>
                  <span class="project-slug">{{ p.slug }}</span>
                </td>
                <td>
                  <span class="category-badge" :class="`cat-${p.category.toLowerCase()}`">
                    {{ p.category }}
                  </span>
                </td>
                <td class="cell-year">{{ p.year || '—' }}</td>
                <td class="cell-stack">
                  <span v-for="t in p.tech_stack.slice(0,3)" :key="t" class="mini-tag">{{ t }}</span>
                  <span v-if="p.tech_stack.length > 3" class="mini-tag mini-more">
                    +{{ p.tech_stack.length - 3 }}
                  </span>
                </td>
                <td class="cell-actions">
                  <button class="action-btn" @click="openForm(p)" title="Edit">
                    <EditIcon />
                  </button>
                  <button class="action-btn action-btn--danger" @click="confirmDelete(p)" title="Delete">
                    <TrashIcon />
                  </button>
                </td>
              </tr>
            </template>
          </draggable>
        </table>
        <div v-if="saving" class="save-toast">Saving order…</div>
      </div>
    </main>

    <!-- Add / Edit form panel -->
    <Transition name="panel">
      <div v-if="formOpen" class="form-overlay" @click.self="closeForm">
        <div class="form-panel">
          <ProjectForm
            :project="editing"
            @saved="onSaved"
            @cancel="closeForm"
          />
        </div>
      </div>
    </Transition>

    <!-- Delete confirm -->
    <Transition name="overlay">
      <div v-if="deleteTarget" class="delete-overlay" @click.self="deleteTarget = null">
        <div class="delete-box">
          <h3>Delete "{{ deleteTarget.title }}"?</h3>
          <p>This cannot be undone.</p>
          <div class="delete-actions">
            <button class="btn-ghost" @click="deleteTarget = null">Cancel</button>
            <button class="btn-danger" @click="doDelete">Delete</button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, nextTick } from 'vue'
import axios from 'axios'
import draggable from 'vuedraggable'
import ProjectForm from '../components/admin/ProjectForm.vue'
import EditIcon from '../components/admin/EditIcon.vue'
import TrashIcon from '../components/admin/TrashIcon.vue'

// The PIN doubles as the ADMIN_TOKEN the backend expects on write requests
// (set via the ADMIN_TOKEN env var in production) -- it's verified against
// the server via /api/admin/ping rather than checked client-side, so the
// gate actually protects the API and not just this screen.
const storedToken = sessionStorage.getItem('admin_token')
if (storedToken) axios.defaults.headers.common['X-Admin-Token'] = storedToken

const authed = ref(!!storedToken)
const pinEntry = ref('')
const pinError = ref(false)
const pinChecking = ref(false)
const pinInput = ref(null)

// if the token becomes invalid (server restarted with a new ADMIN_TOKEN,
// or a stale session), drop back to the PIN gate on the next 401
axios.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401 && authed.value) logout()
    return Promise.reject(err)
  }
)

async function checkPin() {
  pinChecking.value = true
  try {
    await axios.get('/api/admin/ping', { headers: { 'X-Admin-Token': pinEntry.value } })
    axios.defaults.headers.common['X-Admin-Token'] = pinEntry.value
    sessionStorage.setItem('admin_token', pinEntry.value)
    authed.value = true
    pinError.value = false
  } catch {
    pinError.value = true
    pinEntry.value = ''
    nextTick(() => pinInput.value?.focus())
  } finally {
    pinChecking.value = false
  }
}

function logout() {
  sessionStorage.removeItem('admin_token')
  delete axios.defaults.headers.common['X-Admin-Token']
  authed.value = false
}

// Data
const projects = ref([])
const loading = ref(false)
const saving = ref(false)
const formOpen = ref(false)
const editing = ref(null)
const deleteTarget = ref(null)

const stats = computed(() => {
  const cats = { WEB: 0, BIGDATA: 0, AI: 0, DEVOPS: 0 }
  projects.value.forEach(p => { if (cats[p.category] !== undefined) cats[p.category]++ })
  return [
    { label: 'Total', count: projects.value.length },
    { label: 'Web Dev', count: cats.WEB },
    { label: 'Big Data', count: cats.BIGDATA },
    { label: 'AI / ML', count: cats.AI },
    { label: 'DevOps', count: cats.DEVOPS },
  ]
})

async function load() {
  loading.value = true
  const { data } = await axios.get('/api/projects')
  projects.value = data
  loading.value = false
}

onMounted(() => { if (authed.value) load() })
watch(authed, val => { if (val) load() })

function openForm(project) {
  editing.value = project ? { ...project } : null
  formOpen.value = true
}

function closeForm() {
  formOpen.value = false
  editing.value = null
}

function onSaved() {
  closeForm()
  load()
}

function confirmDelete(p) {
  deleteTarget.value = p
}

async function saveOrder() {
  saving.value = true
  const items = projects.value.map((p, i) => ({ id: p.id, order: i + 1 }))
  await axios.put('/api/projects/reorder', items)
  items.forEach(({ id, order }) => {
    const p = projects.value.find(x => x.id === id)
    if (p) p.order = order
  })
  saving.value = false
}

async function doDelete() {
  await axios.delete(`/api/projects/${deleteTarget.value.id}`)
  deleteTarget.value = null
  load()
}
</script>

<style scoped>
/* ── PIN Gate ── */
.pin-gate {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg);
}

.pin-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 56px 48px;
  border: 1px solid var(--border);
  border-radius: 4px;
  width: 360px;
}

.pin-label {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-light);
}

.pin-title {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.03em;
}

.pin-input {
  width: 100%;
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 12px 16px;
  font-size: 20px;
  font-family: var(--font-mono);
  letter-spacing: 0.3em;
  text-align: center;
  background: var(--bg);
  color: var(--ink);
  outline: none;
  transition: border-color 0.2s;
}
.pin-input:focus { border-color: var(--ink); }

.pin-error {
  font-size: 12px;
  color: #c0392b;
}

/* ── Admin layout ── */
.admin-wrap {
  display: flex;
  min-height: 100vh;
  background: #F5F5F5;
}

/* Sidebar */
.admin-sidebar {
  width: 200px;
  flex-shrink: 0;
  background: var(--ink);
  color: var(--bg);
  display: flex;
  flex-direction: column;
  padding: 28px 20px;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
}

.sidebar-logo {
  display: block;
  margin-bottom: 40px;
  transition: opacity 0.2s;
}
.sidebar-logo:hover { opacity: 0.75; }

.sidebar-section {
  font-size: 9px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  opacity: 0.4;
  display: block;
  margin-bottom: 8px;
}

.sidebar-link {
  display: block;
  font-size: 13px;
  color: rgba(250,250,250,0.7);
  padding: 6px 0;
  transition: color 0.2s;
}
.sidebar-link:hover { color: var(--bg); }

.sidebar-logout {
  margin-top: auto;
  background: none;
  border: 1px solid rgba(255,255,255,0.2);
  color: rgba(255,255,255,0.6);
  border-radius: 2px;
  padding: 8px 12px;
  font-size: 12px;
  cursor: pointer;
  font-family: var(--font-sans);
  transition: border-color 0.2s, color 0.2s;
}
.sidebar-logout:hover { border-color: rgba(255,255,255,0.6); color: var(--bg); }

/* Main */
.admin-main {
  flex: 1;
  margin-left: 200px;
  padding: 40px 48px;
}

.admin-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 32px;
}

.admin-label {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-light);
  margin-bottom: 6px;
}

.admin-title {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.03em;
}

/* Stats */
.stats-bar {
  display: flex;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 28px;
}

.stat-item {
  flex: 1;
  background: var(--bg);
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.stat-num {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1;
}

.stat-label {
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-light);
}

/* Table */
.table-wrap {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  overflow: hidden;
}

.project-table {
  width: 100%;
  border-collapse: collapse;
}

.project-table th {
  text-align: left;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-light);
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  background: #F8F8F8;
}

.table-row {
  border-bottom: 1px solid var(--border);
  transition: background 0.15s;
}
.table-row:last-child { border-bottom: none; }
.table-row:hover { background: #F8F8F8; }

.project-table td { padding: 14px 16px; vertical-align: middle; }

.table-loading { text-align: center; color: var(--ink-light); padding: 40px !important; }

.th-handle { width: 36px; }

.cell-drag { width: 36px; padding-left: 12px !important; }

.drag-handle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  color: var(--ink-light);
  cursor: grab;
  border-radius: 2px;
  transition: color 0.15s, background 0.15s;
}
.drag-handle:hover { color: var(--ink); background: #F0F0F0; }
.drag-handle:active { cursor: grabbing; }

.row-ghost { opacity: 0.4; background: #F0F0F0; }

.table-wrap { position: relative; }

.save-toast {
  position: absolute;
  bottom: 12px;
  right: 16px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-light);
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 4px 10px;
}

.project-name { display: block; font-size: 14px; font-weight: 600; }
.project-slug { display: block; font-size: 11px; font-family: var(--font-mono); color: var(--ink-light); margin-top: 2px; }

.category-badge {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 2px;
}
.cat-web    { background: #E8F4FD; color: #1a6fa0; }
.cat-bigdata { background: #EDF7ED; color: #2a7a2a; }
.cat-ai     { background: #F5ECF5; color: #7a2a7a; }
.cat-devops { background: #FEF4E8; color: #a05a1a; }

.cell-year { font-size: 13px; color: var(--ink-mid); }

.mini-tag {
  display: inline-block;
  font-size: 10px;
  font-family: var(--font-mono);
  background: #F0F0F0;
  color: var(--ink-mid);
  padding: 2px 7px;
  border-radius: 2px;
  margin-right: 4px;
}
.mini-more { color: var(--ink-light); }

.cell-actions { display: flex; gap: 8px; }

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: none;
  border: 1px solid var(--border);
  border-radius: 2px;
  cursor: pointer;
  color: var(--ink-mid);
  transition: background 0.15s, border-color 0.15s, color 0.15s;
}
.action-btn:hover { background: var(--ink); border-color: var(--ink); color: var(--bg); }
.action-btn--danger:hover { background: #c0392b; border-color: #c0392b; }

/* Form panel */
.form-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10,10,10,0.45);
  backdrop-filter: blur(4px);
  z-index: 300;
  display: flex;
  justify-content: flex-end;
}

.form-panel {
  width: min(620px, 100vw);
  height: 100%;
  background: var(--bg);
  overflow-y: auto;
  box-shadow: -24px 0 80px rgba(0,0,0,0.12);
}

.panel-enter-active { transition: opacity 0.25s ease, transform 0.3s ease; }
.panel-leave-active { transition: opacity 0.2s ease, transform 0.22s ease; }
.panel-enter-from { opacity: 0; transform: translateX(40px); }
.panel-leave-to   { opacity: 0; transform: translateX(40px); }

/* Delete confirm */
.delete-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10,10,10,0.55);
  backdrop-filter: blur(4px);
  z-index: 400;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete-box {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 40px;
  width: 360px;
  text-align: center;
}

.delete-box h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
.delete-box p  { font-size: 14px; color: var(--ink-mid); margin-bottom: 28px; }

.delete-actions { display: flex; gap: 12px; justify-content: center; }

/* Shared buttons */
.btn-primary {
  background: var(--ink);
  color: var(--bg);
  border: none;
  border-radius: 2px;
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font-sans);
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: opacity 0.2s;
}
.btn-primary:hover { opacity: 0.8; }

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

.btn-danger {
  background: #c0392b;
  color: #fff;
  border: none;
  border-radius: 2px;
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 600;
  font-family: var(--font-sans);
  cursor: pointer;
  transition: opacity 0.2s;
}
.btn-danger:hover { opacity: 0.85; }
</style>
