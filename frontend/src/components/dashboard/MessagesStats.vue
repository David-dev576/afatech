<script setup>
import { computed, onMounted, ref } from 'vue'
import { list } from '../../api'

const messages = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    messages.value = await list('/messages/')
  } finally {
    loading.value = false
  }
})

const total = computed(() => messages.value.length)

// Répartition par sujet, du plus fréquent au moins fréquent
const bySubject = computed(() => {
  const map = {}
  messages.value.forEach((m) => {
    map[m.subject] = (map[m.subject] || 0) + 1
  })
  const rows = Object.entries(map)
    .map(([label, count]) => ({ label, count }))
    .sort((a, b) => b.count - a.count)
  const max = Math.max(1, ...rows.map((r) => r.count))
  return rows.map((r) => ({ ...r, pct: Math.round((r.count / max) * 100) }))
})

// Répartition par statut, pour la barre empilée
const statuses = [
  { key: 'new', label: 'Non lus', bar: 'bg-royal', dot: 'bg-royal' },
  { key: 'read', label: 'Lus', bar: 'bg-midnight', dot: 'bg-midnight' },
  { key: 'archived', label: 'Archivés', bar: 'bg-mist', dot: 'bg-mist' },
]

const byStatus = computed(() =>
  statuses.map((s) => {
    const count = messages.value.filter((m) => m.status === s.key).length
    return { ...s, count, pct: total.value ? Math.round((count / total.value) * 100) : 0 }
  })
)
</script>

<template>
  <div class="grid gap-6 xl:grid-cols-3">
    <!-- Sujets -->
    <div class="bg-white p-6 xl:col-span-2">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h2 class="font-display text-lg font-bold text-midnight">Sujets demandés</h2>
          <p class="text-sm text-slate/60">Répartition des messages par sujet</p>
        </div>
        <p class="text-sm font-semibold text-royal">{{ total }} au total</p>
      </div>

      <div v-if="loading" class="skeleton mt-6 h-40"></div>
      <p v-else-if="!bySubject.length" class="mt-6 text-sm text-slate/60">Aucun message pour le moment.</p>

      <ul v-else class="mt-6 space-y-4">
        <li v-for="row in bySubject" :key="row.label">
          <div class="mb-1.5 flex justify-between text-sm">
            <span class="font-semibold text-midnight">{{ row.label }}</span>
            <span class="text-slate/70">{{ row.count }}</span>
          </div>
          <div class="h-3 w-full bg-icy">
            <div class="h-3 bg-royal transition-all duration-500" :style="{ width: row.pct + '%' }"></div>
          </div>
        </li>
      </ul>
    </div>

    <!-- Statuts -->
    <div class="bg-white p-6">
      <h2 class="font-display text-lg font-bold text-midnight">État des messages</h2>
      <p class="text-sm text-slate/60">Suivi du traitement</p>

      <div class="mt-6 flex h-4 w-full overflow-hidden bg-icy">
        <div
          v-for="s in byStatus"
          :key="s.key"
          :class="['h-4 transition-all duration-500', s.bar]"
          :style="{ width: s.pct + '%' }"
        ></div>
      </div>

      <ul class="mt-6 divide-y divide-mist">
        <li v-for="s in byStatus" :key="s.key" class="flex items-center justify-between py-3">
          <span class="flex items-center gap-3 text-sm font-semibold">
            <span :class="['h-3 w-3', s.dot]"></span>{{ s.label }}
          </span>
          <span class="font-display text-xl font-bold text-midnight">{{ s.count }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>