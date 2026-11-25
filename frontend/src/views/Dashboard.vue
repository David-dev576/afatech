<script setup>
import { computed, onMounted, provide, ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'
import DashSidebar from '../components/dashboard/DashSidebar.vue'
import OverviewPanel from '../components/dashboard/OverviewPanel.vue'
import MessagesPanel from '../components/dashboard/MessagesPanel.vue'
import ServicesPanel from '../components/dashboard/ServicesPanel.vue'
import TrainingPanel from '../components/dashboard/TrainingPanel.vue'
import ProjectsPanel from '../components/dashboard/ProjectsPanel.vue'
import CategoriesPanel from '../components/dashboard/CategoriesPanel.vue'
import SettingsPanel from '../components/dashboard/SettingsPanel.vue'
import ProfilePanel from '../components/dashboard/ProfilePanel.vue'

const router = useRouter()

const sections = [
  { key: 'overview', label: 'Aperçu', icon: 'fa-chart-line', title: 'Aperçu', component: OverviewPanel },
  { key: 'services', label: 'Services', icon: 'fa-layer-group', title: 'Services', component: ServicesPanel },
  { key: 'training', label: 'Formations', icon: 'fa-graduation-cap', title: 'Formations', component: TrainingPanel },
  { key: 'projects', label: 'Projets', icon: 'fa-diagram-project', title: 'Projets', component: ProjectsPanel },
  { key: 'categories', label: 'Catégories', icon: 'fa-tags', title: 'Catégories de projets', component: CategoriesPanel },
  { key: 'messages', label: 'Messages', icon: 'fa-envelope', title: 'Messages de contact', component: MessagesPanel },
  { key: 'settings', label: 'Paramètres', icon: 'fa-sliders', title: 'Paramètres du site', component: SettingsPanel },
  { key: 'profile', label: 'Profil', icon: 'fa-user', title: 'Profil administrateur', component: ProfilePanel },
]
const sidebarItems = sections.map(({ key, label, icon }) => ({ key, label, icon }))

const tab = ref('overview')
const collapsed = ref(false)
const search = ref('')
const stats = ref({ messages_new: 0 })
const me = ref({})

const current = computed(() => sections.find((s) => s.key === tab.value))
const initials = computed(() => (me.value.username || 'AD').slice(0, 2).toUpperCase())

function goTo(key) {
  tab.value = key
  search.value = ''
}
async function refreshStats() {
  try { stats.value = (await api.get('/stats/')).data } catch { /* badge non critique */ }
}
async function refreshMe() {
  try { me.value = (await api.get('/auth/me/')).data } catch { /* géré par le panneau */ }
}
async function logout() {
  try { await api.post('/auth/logout/') } catch { /* jeton déjà invalide */ }
  localStorage.removeItem('afa_token')
  router.push({ name: 'login' })
}

provide('dashSearch', search)
provide('refreshStats', refreshStats)
provide('refreshMe', refreshMe)
provide('goTo', goTo)
provide('me', me)

onMounted(() => {
  refreshStats()
  refreshMe()
})
</script>

<template>
  <div class="flex min-h-screen bg-icy text-slate">
    <DashSidebar
      :items="sidebarItems"
      :active="tab"
      :collapsed="collapsed"
      :badge="stats.messages_new || 0"
      @select="goTo"
      @toggle="collapsed = !collapsed"
      @logout="logout"
    />

    <div class="min-w-0 flex-1">
      <header class="sticky top-0 z-10 flex h-16 items-center justify-between gap-4 border-b border-mist bg-white px-6">
        <h1 class="font-display text-lg font-bold text-midnight">{{ current.title }}</h1>
        <div class="flex items-center gap-4">
          <div class="relative hidden md:block">
            <i class="fa-solid fa-magnifying-glass pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-sm text-slate/50"></i>
            <input v-model="search" type="search" placeholder="Rechercher…" aria-label="Rechercher" class="field w-64 py-2 pl-9 text-sm" />
          </div>
          <div class="flex items-center gap-2 text-sm font-semibold">
            <span class="flex h-8 w-8 items-center justify-center bg-midnight text-xs font-bold text-white">{{ initials }}</span>
            <span class="hidden sm:inline">{{ me.username || 'Admin' }}</span>
          </div>
        </div>
      </header>

      <main class="p-6 lg:p-8">
        <component :is="current.component" :key="tab" />
      </main>
    </div>
  </div>
</template>