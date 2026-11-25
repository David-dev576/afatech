<script setup>
import { computed, inject, onMounted, ref } from 'vue'
import api, { list } from '../../api'
import { fmtDate, msgStatus } from './shared'
import MessagesStats from './MessagesStats.vue'

const goTo = inject('goTo')
const stats = ref({})
const messages = ref([])
const projects = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const [s, m, p] = await Promise.all([api.get('/stats/'), list('/messages/'), list('/projects/')])
    stats.value = s.data
    messages.value = m
    projects.value = p
  } catch {
    error.value = 'Impossible de charger le tableau de bord. Vérifiez que le serveur Django tourne.'
  } finally {
    loading.value = false
  }
})

const cards = computed(() => [
  { label: 'Services', value: stats.value.services ?? 0, icon: 'fa-layer-group', to: 'services' },
  { label: 'Formations', value: stats.value.trainings ?? 0, icon: 'fa-graduation-cap', to: 'training' },
  { label: 'Projets publiés', value: stats.value.projects_published ?? 0, icon: 'fa-diagram-project', to: 'projects' },
  { label: 'Messages non lus', value: stats.value.messages_new ?? 0, icon: 'fa-envelope', to: 'messages' },
])

// Messages reçus par mois, sur les six derniers mois
const monthly = computed(() => {
  const now = new Date()
  const buckets = []
  for (let i = 5; i >= 0; i--) {
    const d = new Date(now.getFullYear(), now.getMonth() - i, 1)
    buckets.push({ key: `${d.getFullYear()}-${d.getMonth()}`, label: d.toLocaleDateString('fr-FR', { month: 'short' }), count: 0 })
  }
  messages.value.forEach((m) => {
    const d = new Date(m.created_at)
    const b = buckets.find((x) => x.key === `${d.getFullYear()}-${d.getMonth()}`)
    if (b) b.count++
  })
  const max = Math.max(1, ...buckets.map((b) => b.count))
  return buckets.map((b) => ({ ...b, px: b.count ? Math.max(14, Math.round((b.count / max) * 180)) : 4 }))
})
const monthlyTotal = computed(() => monthly.value.reduce((s, b) => s + b.count, 0))

const recent = computed(() => messages.value.slice(0, 5))

const activity = computed(() => {
  const items = [
    ...messages.value.map((m) => ({ key: `m${m.id}`, icon: 'fa-envelope', date: m.created_at, text: `Message de ${m.name} : ${m.subject}` })),
    ...projects.value.map((p) => ({ key: `p${p.id}`, icon: 'fa-diagram-project', date: p.updated_at, text: `Projet « ${p.title} » ${p.is_published ? 'publié' : 'enregistré'}` })),
  ]
  return items.sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 6)
})
</script>

<template>
  <p v-if="error" role="alert" class="mb-6 border-l-4 border-red-700 bg-white p-4 text-red-700">{{ error }}</p>

  <div v-if="loading" class="grid gap-6">
    <div class="skeleton h-28"></div>
    <div class="skeleton h-80"></div>
  </div>

  <div v-else class="space-y-6">
    <!-- Indicateurs -->
    <div class="grid gap-px bg-mist md:grid-cols-2 xl:grid-cols-4">
      <button
        v-for="c in cards"
        :key="c.label"
        class="group flex items-center justify-between bg-white p-6 text-left transition-colors hover:bg-icy"
        @click="goTo(c.to)"
      >
        <div>
          <p class="text-sm text-slate/60">{{ c.label }}</p>
          <p class="mt-1 font-display text-3xl font-bold text-midnight">{{ c.value }}</p>
        </div>
        <span class="flex h-10 w-10 items-center justify-center bg-icy text-royal group-hover:bg-royal group-hover:text-white">
          <i :class="['fa-solid', c.icon]"></i>
        </span>
      </button>
    </div>

    <div class="grid gap-6 xl:grid-cols-3">
      <!-- Graphique -->
      <div class="bg-white p-6 xl:col-span-2">
        <div class="flex items-start justify-between gap-4">
          <div>
            <h2 class="font-display text-lg font-bold text-midnight">Demandes de contact</h2>
            <p class="text-sm text-slate/60">Messages reçus sur les six derniers mois</p>
          </div>
          <p class="text-sm font-semibold text-royal">{{ monthlyTotal }} au total</p>
        </div>
        <div class="mt-8 flex h-60 items-end gap-4 border-b border-mist">
          <div v-for="b in monthly" :key="b.key" class="flex flex-1 flex-col items-center justify-end gap-2">
            <span class="text-xs font-semibold text-slate/70">{{ b.count }}</span>
            <div :class="['w-full transition-all duration-500', b.count ? 'bg-royal' : 'bg-mist']" :style="{ height: b.px + 'px' }"></div>
            <span class="pb-2 text-xs capitalize text-slate/60">{{ b.label }}</span>
          </div>
        </div>
      </div>

      <!-- Actions rapides -->
      <div class="bg-white p-6">
        <h2 class="font-display text-lg font-bold text-midnight">Actions rapides</h2>
        <p class="text-sm text-slate/60">Accès direct aux sections à traiter</p>
        <div class="mt-5 grid gap-3">
          <button class="btn-primary justify-start" @click="goTo('services')"><i class="fa-solid fa-plus w-4"></i> Ajouter un service</button>
          <button class="btn-ghost justify-start" @click="goTo('projects')"><i class="fa-solid fa-diagram-project w-4"></i> Nouveau projet</button>
          <button class="btn-ghost justify-start" @click="goTo('messages')"><i class="fa-solid fa-inbox w-4"></i> Lire les messages</button>
          <button class="btn-ghost justify-start" @click="goTo('settings')"><i class="fa-solid fa-sliders w-4"></i> Modifier le site</button>
        </div>
      </div>
    </div>

    <!-- Statistiques des messages (sujets et statuts) -->
    <MessagesStats />

    <div class="grid gap-6 xl:grid-cols-3">
      <!-- Messages récents -->
      <div class="bg-white p-6 xl:col-span-2">
        <div class="flex items-center justify-between">
          <h2 class="font-display text-lg font-bold text-midnight">Messages récents</h2>
          <button class="text-sm font-semibold text-royal hover:underline" @click="goTo('messages')">Voir tout</button>
        </div>
        <div class="mt-4 overflow-x-auto">
          <table class="w-full text-left text-sm">
            <thead class="border-b border-mist text-slate/60">
              <tr>
                <th class="py-3 font-semibold">Expéditeur</th>
                <th class="font-semibold">Sujet</th>
                <th class="font-semibold">Statut</th>
                <th class="font-semibold">Date</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-mist">
              <tr v-for="m in recent" :key="m.id">
                <td class="py-3 font-semibold text-midnight">{{ m.name }}</td>
                <td class="pr-4">{{ m.subject }}</td>
                <td><span :class="['px-2 py-1 text-xs font-semibold', msgStatus[m.status].cls]">{{ msgStatus[m.status].label }}</span></td>
                <td class="whitespace-nowrap text-slate/70">{{ fmtDate(m.created_at) }}</td>
              </tr>
              <tr v-if="!recent.length">
                <td colspan="4" class="py-8 text-center text-slate/60">Aucun message reçu pour le moment.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Activité -->
      <div class="bg-white p-6">
        <h2 class="font-display text-lg font-bold text-midnight">Activité récente</h2>
        <ul class="mt-5 space-y-5">
          <li v-for="a in activity" :key="a.key" class="flex gap-3">
            <span class="flex h-8 w-8 shrink-0 items-center justify-center bg-icy text-royal">
              <i :class="['fa-solid text-sm', a.icon]"></i>
            </span>
            <div class="min-w-0">
              <p class="text-sm">{{ a.text }}</p>
              <p class="text-xs text-slate/60">{{ fmtDate(a.date) }}</p>
            </div>
          </li>
          <li v-if="!activity.length" class="text-sm text-slate/60">Aucune activité enregistrée.</li>
        </ul>
      </div>
    </div>
  </div>
</template>