<script setup>
import { onMounted, onUnmounted, ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { t } from '../i18n'
import LanguageSwitcher from './LanguageSwitcher.vue'

const route = useRoute()

const links = [
  { to: '/', key: 'nav.home' },
  { to: '/a-propos', key: 'nav.about' },
  { to: '/services', key: 'nav.services' },
  { to: '/formation', key: 'nav.training' },
  { to: '/projets', key: 'nav.projects' },
  { to: '/contact', key: 'nav.contact' },
]

const open = ref(false)
const scrolled = ref(false)

const onScroll = () => {
  scrolled.value = window.scrollY > 24
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  document.body.style.overflow = ''
})

// Bloque le défilement de la page quand le menu mobile est ouvert
watch(open, (isOpen) => {
  document.body.style.overflow = isOpen ? 'hidden' : ''
})

// Ferme le menu au changement de page
watch(() => route.path, () => {
  open.value = false
})

const isHome = computed(() => route.path === '/')
const hasWhiteBg = computed(() => scrolled.value || !isHome.value)
</script>

<template>
  <header
    :class="[
      'fixed inset-x-0 top-0 z-40 transition-all duration-300',
      hasWhiteBg && !open
        ? 'bg-white/95 backdrop-blur-md border-b border-mist py-2 shadow-sm'
        : 'bg-transparent py-4',
    ]"
  >
    <nav class="mx-auto flex max-w-7xl items-center justify-between px-5" :aria-label="t('nav.aria')">
      <!-- Logo (visible seulement quand le menu mobile est fermé) -->
      <router-link
        to="/"
        v-show="!open"
        :class="[
          'flex items-center gap-3 font-display text-lg font-bold transition-colors',
          hasWhiteBg ? 'text-midnight' : 'text-white',
        ]"
      >
        <img src="/logo.png" :alt="t('nav.logoAlt')" class="h-10 w-10 rounded-full bg-white object-cover p-0.5 shadow-sm" />
      </router-link>

      <!-- Menu bureau -->
      <ul class="hidden items-center gap-8 lg:flex">
        <li v-for="l in links" :key="l.to">
          <router-link
            :to="l.to"
            :class="[
              'py-1 text-sm font-semibold transition-colors',
              hasWhiteBg ? 'text-slate hover:text-royal' : 'text-white/80 hover:text-white',
            ]"
            exact-active-class="!text-royal border-b-2 border-royal"
          >
            {{ t(l.key) }}
          </router-link>
        </li>
        <li><LanguageSwitcher /></li>
        <li>
          <router-link
            to="/contact"
            :class="[
              'inline-flex items-center gap-2 px-6 py-2.5 rounded-sm font-bold text-sm transition-colors shadow-md',
              hasWhiteBg ? 'bg-royal text-white hover:bg-midnight' : 'bg-white text-midnight hover:bg-icy',
            ]"
          >
            <i class="fa-regular fa-comments"></i> {{ t('nav.cta') }}
          </router-link>
        </li>
      </ul>

      <!-- Sélecteur de langue et bouton hamburger (mobile) -->
      <div v-show="!open" class="flex items-center gap-2 lg:hidden">
        <LanguageSwitcher />
        <button
          :class="['p-2 text-2xl transition-colors', hasWhiteBg ? 'text-midnight' : 'text-white']"
          :aria-label="t('nav.menuOpen')"
          @click="open = true"
        >
          <i class="fa-solid fa-bars"></i>
        </button>
      </div>
    </nav>
  </header>

  <!-- Menu mobile plein écran -->
  <transition name="fade">
    <div v-if="open" class="fixed inset-0 z-[100] flex flex-col bg-white/95 backdrop-blur-md lg:hidden">
      <div class="flex h-20 shrink-0 items-center justify-between border-b border-mist/30 px-5">
        <router-link to="/" class="flex items-center gap-3" @click="open = false">
          <img src="/logo.png" :alt="t('nav.logoAlt')" class="h-10 w-10 rounded-full bg-white object-cover p-0.5 shadow-sm" />
          <span class="font-display text-lg font-bold text-midnight">AFA TECH</span>
        </router-link>

        <div class="flex items-center gap-2">
          <LanguageSwitcher />
          <button
            class="p-2 text-3xl text-midnight transition-colors hover:text-royal"
            :aria-label="t('nav.menuClose')"
            @click="open = false"
          >
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>
      </div>

      <nav class="flex flex-1 flex-col items-center justify-center gap-8 px-6">
        <router-link
          v-for="l in links"
          :key="l.to"
          :to="l.to"
          class="text-sm font-bold uppercase tracking-[0.2em] text-slate transition-colors hover:text-royal"
          active-class="text-royal"
        >
          {{ t(l.key) }}
        </router-link>
      </nav>

      <div class="mb-8 shrink-0 p-6">
        <router-link
          to="/contact"
          class="flex w-full items-center justify-center gap-2 rounded-sm bg-royal px-6 py-4 font-bold text-white shadow-lg transition hover:bg-midnight"
        >
          <i class="fa-regular fa-comments"></i> {{ t('nav.cta') }}
        </router-link>
      </div>
    </div>
  </transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>