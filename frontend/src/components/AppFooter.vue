<template>
  <footer id="contact" class="site-footer">
    <div class="container footer-inner">
      <div class="footer-top">
        <div class="footer-left">
          <p class="footer-label">{{ t('footer.getInTouch') }}</p>
          <a href="mailto:camilogzlez@gmail.com" class="footer-email">
            camilogzlez@gmail.com
          </a>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copy">{{ t('footer.copy', { year }) }}</p>
        <div class="footer-links">
          <a href="https://github.com/camilogzlez" target="_blank" rel="noopener" class="footer-link">
            GitHub
          </a>
          <a href="https://linkedin.com/in/camilogzlez" target="_blank" rel="noopener" class="footer-link">
            LinkedIn
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const year = new Date().getFullYear()
</script>

<style scoped>
.site-footer {
  border-top: 1px solid var(--border);
  padding: 56px 0 64px;
  margin-top: 120px;
  position: relative;
  z-index: 1;
  background: linear-gradient(to right, var(--bg) 0%, var(--bg) 48%, transparent 56%);
}

.footer-inner {
  display: flex;
  flex-direction: column;
  gap: 48px;
}

.footer-top { display: flex; align-items: flex-start; }

.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}

.footer-label {
  font-size: 10px;
  letter-spacing: 0.12em;
  color: var(--ink-light);
  margin-bottom: 6px;
  text-transform: uppercase;
}

.footer-email {
  font-size: 18px;
  font-weight: 500;
  border-bottom: 1px solid var(--ink);
  padding-bottom: 2px;
  transition: opacity 0.2s;
}
.footer-email:hover { opacity: 0.6; }

.footer-links {
  display: flex;
  gap: 24px;
}

.footer-link {
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--ink-mid);
  border-bottom: 1px solid transparent;
  transition: color 0.2s, border-color 0.2s;
}
.footer-link:hover { color: var(--ink); border-bottom-color: var(--ink); }

.footer-copy {
  font-size: 12px;
  color: var(--ink-light);
}
</style>
