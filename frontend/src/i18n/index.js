import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import fr from './locales/fr.json'

export const SUPPORTED_LOCALES = ['en', 'fr']
export const DEFAULT_LOCALE = 'en'
const STORAGE_KEY = 'slowwave-locale'

export function detectLocale() {
  const stored = localStorage.getItem(STORAGE_KEY)
  if (stored && SUPPORTED_LOCALES.includes(stored)) return stored

  const browser = (navigator.language || '').slice(0, 2)
  if (SUPPORTED_LOCALES.includes(browser)) return browser

  return DEFAULT_LOCALE
}

export function persistLocale(locale) {
  if (SUPPORTED_LOCALES.includes(locale)) localStorage.setItem(STORAGE_KEY, locale)
}

export const i18n = createI18n({
  legacy: false,
  locale: DEFAULT_LOCALE,
  fallbackLocale: DEFAULT_LOCALE,
  messages: { en, fr },
})
