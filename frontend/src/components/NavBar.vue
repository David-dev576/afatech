<script setup>
import { onMounted, onUnmounted, ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const links = [
  { to: '/', label: 'Home' }, 
  { to: '/a-propos', label: 'About' },
  { to: '/services', label: 'Services' }, 
  { to: '/formation', label: 'Formation' },
  { to: '/projets', label: 'Projects' }, 
  { to: '/contact', label: 'Contact' },
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
})

// Bloquer le scroll en arrière-plan quand le menu est ouvert
watch(open, (isOpen) => {
  document.body.style.overflow = isOpen ? 'hidden' : ''
})

// Fermer le menu au changement de page
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
        : 'bg-transparent py-4'
    ]"
  >
    <nav class="mx-auto flex max-w-7xl items-center justify-between px-5" aria-label="Navigation principale">
      
      <!-- Logo (visible seulement quand le menu est fermé) -->
      <router-link 
        to="/" 
        v-show="!open"
        :class="[
          'flex items-center gap-3 font-display text-lg font-bold transition-colors',
          hasWhiteBg ? 'text-midnight' : 'text-white'
        ]"
      >
        <img 
          src="/logo.png" 
          alt="Logo AFA TECH" 
          class="h-10 w-10 object-cover rounded-full bg-white p-0.5 shadow-sm"
        />
        
      </router-link>

      <!-- Menu Desktop -->
      <ul class="hidden items-center gap-8 lg:flex">
        <li v-for="l in links" :key="l.to">
          <router-link 
            :to="l.to" 
            :class="[
              'py-1 text-sm font-semibold transition-colors',
              hasWhiteBg ? 'text-slate hover:text-royal' : 'text-white/80 hover:text-white'
            ]"
            exact-active-class="!text-royal border-b-2 border-royal"
          >
            {{ l.label }}
          </router-link>
        </li>
        <li>
          <router-link 
            to="/contact" 
            :class="[
              'inline-flex items-center gap-2 px-6 py-2.5 rounded-sm font-bold text-sm transition-colors shadow-md',
              hasWhiteBg ? 'bg-royal text-white hover:bg-midnight' : 'bg-white text-midnight hover:bg-icy'
            ]"
          >
            <i class="fa-regular fa-comments"></i> Let's Talk
          </router-link>
        </li>
      </ul>

      <!-- Bouton Menu Mobile (Hamburger) -->
      <button 
        v-show="!open"
        :class="[
          'text-2xl lg:hidden transition-colors p-2',
          hasWhiteBg ? 'text-midnight' : 'text-white'
        ]"
        aria-label="Ouvrir le menu" 
        @click="open = true"
      >
        <i class="fa-solid fa-bars"></i>
      </button>
    </nav>
  </header>

  <!-- MENU MOBILE PLEIN ÉCRAN (OVERLAY) -->
  <transition name="fade">
    <div 
      v-if="open" 
      class="fixed inset-0 z-[100] flex flex-col bg-white/95 backdrop-blur-md lg:hidden"
    >
      <!-- En-tête interne du menu (Logo + Bouton Fermer) -->
      <div class="flex h-20 items-center justify-between px-5 border-b border-mist/30 shrink-0">
        <router-link to="/" class="flex items-center gap-3" @click="open = false">
          <img src="/logo.png" alt="Logo" class="h-10 w-10 rounded-full bg-white p-0.5 shadow-sm" />
          <span class="font-heading font-bold text-midnight text-lg">AFA TECH</span>
        </router-link>
        
        <!-- BOUTON FERMER (X) -->
        <button @click="open = false" class="text-midnight text-3xl p-2 hover:text-royal transition-colors">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Liens de navigation centrés -->
      <nav class="flex-1 flex flex-col items-center justify-center gap-8 px-6">
        <router-link 
          v-for="l in links" 
          :key="l.to"
          :to="l.to" 
          class="text-sm font-bold tracking-[0.2em] uppercase text-slate hover:text-royal transition-colors"
          active-class="text-royal"
        >
          {{ l.label }}
        </router-link>
      </nav>

      <!-- Bouton CTA en bas -->
      <div class="p-6 shrink-0 mb-8">
        <router-link 
          to="/contact" 
          class="w-full flex items-center justify-center gap-2 bg-royal text-white px-6 py-4 rounded-sm font-bold hover:bg-midnight transition shadow-lg"
        >
          <i class="fa-regular fa-comments"></i> Parlons-en
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