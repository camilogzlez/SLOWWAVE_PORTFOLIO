<template>
  <section id="about" class="about-section">
    <div class="container about-inner">
      <div class="about-label-col">
        <p class="section-label">{{ t('about.label') }}</p>
        <div class="about-line"></div>
      </div>

      <div class="about-content">
        <h2 class="about-title">
          {{ t('about.titleLine1') }}<br />
          <span class="text-outline">{{ t('about.titleLine2') }}</span>
        </h2>
        <p class="about-text">
          {{ t('about.text1Before') }}
          <strong>{{ t('about.text1Web') }}</strong>, <strong>{{ t('about.text1Big') }}</strong> {{ t('about.text1And') }}
          <strong>{{ t('about.text1Ai') }}</strong> {{ t('about.text1After') }}
        </p>
        <p class="about-text">
          {{ t('about.text2') }}
        </p>
        <p class="about-text">
          <strong>{{ t('about.text3') }}</strong>
        </p>

        <div class="about-links">
          <a
            href="https://www.linkedin.com/in/camilogzlez"
            target="_blank"
            rel="noopener"
            class="about-link"
          >
            <svg width="15" height="15" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
              <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
            </svg>
            {{ t('about.professionalExperience') }}
            <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
              <path d="M2 9L9 2M9 2H4M9 2v5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </div>

        <div class="skills-grid">
          <div v-for="skill in skills" :key="skill.labelKey" class="skill-item">
            <span class="skill-label">{{ t(skill.labelKey) }}</span>
            <div class="skill-tags">
              <span v-for="item in skill.items" :key="item" class="stack-tag">{{ item }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

// tech/tool names are proper nouns and stay the same in both locales;
// only the group label is translated (via labelKey)
const skills = [
  { labelKey: 'about.skillsFrontend', items: ['Vue.js', 'JavaScript', 'TypeScript', 'HTML/CSS'] },
  { labelKey: 'about.skillsBackend', items: ['Python', 'FastAPI', 'Node.js', 'Ruby on Rails'] },
  { labelKey: 'about.skillsData', items: ['PySpark', 'TensorFlow', 'spaCy', 'Pandas'] },
  { labelKey: 'about.skillsInfra', items: ['Docker', 'Kubernetes', 'AWS', 'PostgreSQL'] },
]
</script>

<style scoped>
.about-section {
  padding: 100px 0;
  position: relative;
  z-index: 1;
  background: linear-gradient(to right, #F5F5F5 0%, #F5F5F5 48%, transparent 56%);
}

.about-inner {
  display: grid;
  grid-template-columns: 160px 1fr;
  gap: 64px;
}

.section-label {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-light);
  margin-bottom: 16px;
}

.about-line {
  width: 1px;
  height: 48px;
  background: var(--border);
}

.about-title {
  font-size: clamp(32px, 4.5vw, 56px);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.1;
  margin-bottom: 28px;
}

.about-text {
  font-size: 16px;
  line-height: 1.8;
  color: var(--ink-mid);
  margin-bottom: 20px;
  max-width: 560px;
}

.about-text strong { color: var(--ink); font-weight: 600; }

.about-links {
  margin-bottom: 36px;
}

.about-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--ink);
  border: 1px solid var(--border);
  border-radius: 2px;
  padding: 9px 16px;
  transition: background 0.2s, border-color 0.2s, color 0.2s;
}
.about-link:hover {
  background: var(--ink);
  border-color: var(--ink);
  color: var(--bg);
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
  margin-top: 40px;
  padding-top: 32px;
  border-top: 1px solid var(--border);
}

.skill-label {
  display: block;
  font-size: 10px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink-light);
  margin-bottom: 10px;
}

.skill-tags { display: flex; flex-wrap: wrap; gap: 6px; }

.stack-tag {
  font-size: 11px;
  font-family: var(--font-mono);
  background: var(--bg);
  border: 1px solid var(--border);
  padding: 4px 10px;
  border-radius: 2px;
  color: var(--ink-mid);
}

@media (max-width: 768px) {
  .about-inner { grid-template-columns: 1fr; gap: 32px; }
  .skills-grid { grid-template-columns: 1fr; }
}
</style>
