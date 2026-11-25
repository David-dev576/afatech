<script setup>
import { onMounted, ref } from 'vue'
import api from '../api'

const s = ref({ email: 'afatechsolution@gmail.com', phone: '', socials: [] })

onMounted(async () => { 
  try { 
    s.value = (await api.get('/settings/')).data 
  } catch {} 
})

const icon = (p) => (['facebook','linkedin','instagram','x-twitter','whatsapp','youtube','github'].includes(p) ? `fa-brands fa-${p}` : 'fa-solid fa-link')
</script>

<template>
  <footer class="bg-midnight text-mist">
    <div class="mx-auto grid max-w-7xl gap-10 px-5 py-14 md:grid-cols-[2fr_1fr_1fr_1.5fr]">
      
      <!-- Colonne 1 : Logo et description -->
      <div>
        <router-link to="/" class="flex items-center gap-3">
          <!-- VOTRE LOGO ICI -->
          <img 
            src="/logo.png" 
            alt="Logo AFA TECH" 
            class="h-10 w-10 object-cover rounded-full bg-white p-0.5 shadow-sm"
          />
          <span class="font-heading font-bold text-white text-lg tracking-wide">AFA TECH SOLUTIONS</span>
        </router-link>
        
        <p class="mt-4 max-w-sm text-sm leading-relaxed">Formation, développement web et mobile, hébergement et conseil pour la transformation digitale de l'Afrique.</p>
        
        <div class="mt-5 flex gap-4 text-xl">
          <a v-for="l in s.socials" :key="l.id" :href="l.url" target="_blank" rel="noopener" :aria-label="l.platform" class="hover:text-white transition-colors">
            <i :class="icon(l.platform)"></i>
          </a>
        </div>
      </div>

      <!-- Colonne 2 : Navigation -->
      <nav aria-label="Pied de page">
        <p class="font-heading font-bold text-white">Navigation</p>
        <ul class="mt-3 space-y-2 text-sm">
          <li><router-link to="/a-propos" class="hover:text-white transition-colors">À propos</router-link></li>
          <li><router-link to="/projets" class="hover:text-white transition-colors">Projets</router-link></li>
          <li><router-link to="/contact" class="hover:text-white transition-colors">Contact</router-link></li>
        </ul>
      </nav>

      <!-- Colonne 3 : Offres -->
      <nav>
        <p class="font-heading font-bold text-white">Offres</p>
        <ul class="mt-3 space-y-2 text-sm">
          <li><router-link to="/services" class="hover:text-white transition-colors">Services</router-link></li>
          <li><router-link to="/formation" class="hover:text-white transition-colors">Formation</router-link></li>
        </ul>
      </nav>

      <!-- Colonne 4 : Contact -->
      <div>
        <p class="font-heading font-bold text-white">Contact</p>
        <ul class="mt-3 space-y-2 text-sm">
          <li class="flex items-center">
            <i class="fa-regular fa-envelope mr-2 text-royal"></i>
            <a :href="`mailto:${s.email}`" class="hover:text-white transition-colors">{{ s.email }}</a>
          </li>
          <li v-if="s.phone" class="flex items-center">
            <i class="fa-solid fa-phone mr-2 text-royal"></i>
            <span>{{ s.phone }}</span>
          </li>
        </ul>
      </div>

    </div>

    <!-- Copyright -->
    <div class="border-t border-midnight-700 py-5 text-center text-xs">
      <p>© {{ new Date().getFullYear() }} AFA TECH SOLUTIONS. Tous droits réservés.</p>
    </div>
  </footer>
</template>