<script setup>
import { onMounted, ref } from 'vue'
import api from '../api'
import { t } from '../i18n'

const s = ref({ email: 'afatechsolution@gmail.com', phone: '', socials: [] })

onMounted(async () => {
  try {
    s.value = (await api.get('/settings/')).data
  } catch {
    /* valeurs par défaut conservées */
  }
})

const icon = (p) =>
  ['facebook', 'linkedin', 'instagram', 'x-twitter', 'whatsapp', 'youtube', 'github'].includes(p)
    ? `fa-brands fa-${p}`
    : 'fa-solid fa-link'
</script>

<template>
  <footer class="bg-midnight text-mist">
    <div class="mx-auto grid max-w-7xl gap-10 px-5 py-14 md:grid-cols-[2fr_1fr_1fr_1.5fr]">
      <!-- Colonne 1 : logo et description -->
      <div>
        <router-link to="/" class="flex items-center gap-3">
          <img src="/logo.png" :alt="t('nav.logoAlt')" class="h-10 w-10 rounded-full bg-white object-cover p-0.5 shadow-sm" />
          <span class="font-display text-lg font-bold tracking-wide text-white">AFA TECH SOLUTIONS</span>
        </router-link>

        <p class="mt-4 max-w-sm text-sm leading-relaxed">{{ t('footer.description') }}</p>

        <div class="mt-5 flex gap-4 text-xl">
          <a
            v-for="l in s.socials"
            :key="l.id"
            :href="l.url"
            target="_blank"
            rel="noopener"
            :aria-label="l.platform"
            class="transition-colors hover:text-white"
          >
            <i :class="icon(l.platform)"></i>
          </a>
        </div>
      </div>

      <!-- Colonne 2 : navigation -->
      <nav :aria-label="t('footer.aria')">
        <p class="font-display font-bold text-white">{{ t('footer.navigation') }}</p>
        <ul class="mt-3 space-y-2 text-sm">
          <li><router-link to="/a-propos" class="transition-colors hover:text-white">{{ t('nav.about') }}</router-link></li>
          <li><router-link to="/projets" class="transition-colors hover:text-white">{{ t('nav.projects') }}</router-link></li>
          <li><router-link to="/contact" class="transition-colors hover:text-white">{{ t('nav.contact') }}</router-link></li>
        </ul>
      </nav>

      <!-- Colonne 3 : offres -->
      <nav>
        <p class="font-display font-bold text-white">{{ t('footer.offers') }}</p>
        <ul class="mt-3 space-y-2 text-sm">
          <li><router-link to="/services" class="transition-colors hover:text-white">{{ t('nav.services') }}</router-link></li>
          <li><router-link to="/formation" class="transition-colors hover:text-white">{{ t('nav.training') }}</router-link></li>
        </ul>
      </nav>

      <!-- Colonne 4 : contact -->
      <div>
        <p class="font-display font-bold text-white">{{ t('footer.contact') }}</p>
        <ul class="mt-3 space-y-2 text-sm">
          <li class="flex items-center">
            <i class="fa-regular fa-envelope mr-2 text-royal"></i>
            <a :href="`mailto:${s.email}`" class="transition-colors hover:text-white">{{ s.email }}</a>
          </li>
          <li v-if="s.phone" class="flex items-center">
            <i class="fa-solid fa-phone mr-2 text-royal"></i>
            <span>{{ s.phone }}</span>
          </li>
        </ul>
      </div>
    </div>

    <div class="border-t border-midnight-700 py-5 text-center text-xs">
      <p>© {{ new Date().getFullYear() }} AFA TECH SOLUTIONS. {{ t('footer.rights') }}</p>
    </div>
  </footer>
</template>