<script setup>
import { computed, inject, onMounted, onUnmounted, ref, watch } from 'vue'
import api, { list } from '../../api'
import { fmtDate, msgStatus } from './shared'

const search = inject('dashSearch')
const refreshStats = inject('refreshStats')

const messages = ref([])
const loading = ref(true)
const refreshing = ref(false)
const error = ref('')
const filter = ref('all')
const selectedId = ref(null)
const busy = ref(false)
const lastUpdate = ref(null)

let timer = null
const REFRESH_MS = 15000

async function load(silent = false) {
  if (!silent) refreshing.value = true
  try {
    messages.value = await list('/messages/')
    error.value = ''
    lastUpdate.value = new Date()
    refreshStats()
  } catch {
    error.value = 'Impossible de charger les messages. Vérifiez que le serveur Django tourne.'
  } finally {
    loading.value = false
    refreshing.value = false
  }
}

onMounted(() => {
  load()
  timer = setInterval(() => load(true), REFRESH_MS)
})
onUnmounted(() => clearInterval(timer))

const counts = computed(() => ({
  all: messages.value.length,
  new: messages.value.filter((m) => m.status === 'new').length,
  read: messages.value.filter((m) => m.status === 'read').length,
  archived: messages.value.filter((m) => m.status === 'archived').length,
}))

const visible = computed(() => {
  const q = (search.value || '').trim().toLowerCase()
  return messages.value
    .filter((m) => filter.value === 'all' || m.status === filter.value)
    .filter((m) => !q || `${m.name} ${m.subject} ${m.email}`.toLowerCase().includes(q))
})

const selected = computed(() => messages.value.find((m) => m.id === selectedId.value) || null)

// Sélectionne le premier message visible si la sélection n'est plus dans la liste.
// Cette sélection ne modifie jamais le statut : seul un clic le fait.
watch(visible, (rows) => {
  if (!rows.some((m) => m.id === selectedId.value)) selectedId.value = rows[0]?.id ?? null
})

// Clic sur un message : l'ouvre, et le marque comme lu s'il était non lu
async function openMessage(m) {
  selectedId.value = m.id
  if (m.status === 'new') {
    try {
      await api.patch(`/messages/${m.id}/`, { status: 'read' })
      m.status = 'read'
      refreshStats()
    } catch {
      /* non bloquant : le statut sera relu au prochain rafraîchissement */
    }
  }
}

async function setStatus(status) {
  if (!selected.value) return
  busy.value = true
  try {
    await api.patch(`/messages/${selected.value.id}/`, { status })
    await load(true)
  } finally {
    busy.value = false
  }
}

async function removeSelected() {
  if (!selected.value || !confirm('Supprimer définitivement ce message ?')) return
  busy.value = true
  try {
    await api.delete(`/messages/${selected.value.id}/`)
    selectedId.value = null
    await load(true)
  } finally {
    busy.value = false
  }
}

const replyLink = computed(() =>
  selected.value
    ? `mailto:${selected.value.email}?subject=${encodeURIComponent('Re: ' + selected.value.subject)}`
    : '#'
)

const filters = [
  { key: 'all', label: 'Tous' },
  { key: 'new', label: 'Non lus' },
  { key: 'read', label: 'Lus' },
  { key: 'archived', label: 'Archivés' },
]
</script>

<template>
  <div class="mb-4 flex flex-wrap items-center justify-between gap-3">
    <p class="text-xs text-slate/60">
      Mise à jour automatique toutes les 15 secondes
      <span v-if="lastUpdate"> · dernière mise à jour à {{ lastUpdate.toLocaleTimeString('fr-FR') }}</span>
    </p>
    <button class="btn-ghost !px-4 !py-2 text-sm" :disabled="refreshing" @click="load()">
      <i :class="refreshing ? 'fa-solid fa-spinner fa-spin' : 'fa-solid fa-rotate'"></i> Actualiser
    </button>
  </div>

  <p v-if="error" role="alert" class="mb-6 border-l-4 border-red-700 bg-white p-4 text-red-700">{{ error }}</p>

  <div v-if="loading" class="skeleton h-96"></div>

  <div v-else class="grid gap-6 xl:grid-cols-12">
    <!-- Liste -->
    <div class="bg-white xl:col-span-4">
      <div class="flex flex-wrap gap-2 border-b border-mist p-4">
        <button
          v-for="f in filters"
          :key="f.key"
          :class="[
            'px-3 py-1.5 text-xs font-semibold transition-colors',
            filter === f.key ? 'bg-midnight text-white' : 'bg-icy text-slate hover:bg-mist/60',
          ]"
          @click="filter = f.key"
        >
          {{ f.label }} ({{ counts[f.key] ?? 0 }})
        </button>
      </div>

      <ul class="max-h-[70vh] divide-y divide-mist overflow-y-auto">
        <li v-for="m in visible" :key="m.id">
          <button
            :class="['relative w-full p-4 text-left transition-colors', selectedId === m.id ? 'bg-icy' : 'hover:bg-icy/60']"
            @click="openMessage(m)"
          >
            <span v-if="selectedId === m.id" class="absolute inset-y-0 left-0 w-1 bg-royal"></span>
            <div class="flex items-start justify-between gap-3">
              <p class="flex items-center gap-2 font-semibold text-midnight">
                <span v-if="m.status === 'new'" class="h-2 w-2 bg-royal"></span>
                {{ m.name }}
              </p>
              <span class="shrink-0 text-xs text-slate/60">{{ fmtDate(m.created_at) }}</span>
            </div>
            <p class="mt-1 text-sm font-semibold text-slate">{{ m.subject }}</p>
            <p class="mt-1 truncate text-xs text-slate/60">{{ m.email }} · {{ m.message }}</p>
          </button>
        </li>
        <li v-if="!visible.length" class="p-8 text-center text-sm text-slate/60">
          Aucun message dans cette vue. Vérifiez le filtre sélectionné.
        </li>
      </ul>
    </div>

    <!-- Détail -->
    <div class="bg-white p-6 xl:col-span-8">
      <div v-if="!selected" class="flex min-h-[320px] flex-col items-center justify-center text-center text-slate/60">
        <i class="fa-regular fa-envelope-open mb-3 text-4xl text-mist"></i>
        <p>Sélectionnez un message pour le lire.</p>
      </div>

      <template v-else>
        <div class="flex flex-wrap items-start justify-between gap-4 border-b border-mist pb-5">
          <div>
            <span :class="['px-2 py-1 text-xs font-semibold', msgStatus[selected.status].cls]">{{ msgStatus[selected.status].label }}</span>
            <h2 class="mt-3 font-display text-2xl font-bold text-midnight">{{ selected.subject }}</h2>
            <p class="mt-1 text-sm text-slate/60">Reçu le {{ fmtDate(selected.created_at) }}</p>
          </div>
          <div class="flex flex-wrap gap-3 text-sm font-semibold">
            <button
              v-if="selected.status === 'read'"
              :disabled="busy"
              class="btn-ghost !px-4 !py-2"
              @click="setStatus('new')"
            ><i class="fa-regular fa-envelope mr-1"></i> Marquer non lu</button>
            <button
              v-if="selected.status !== 'archived'"
              :disabled="busy"
              class="btn-ghost !px-4 !py-2"
              @click="setStatus('archived')"
            ><i class="fa-solid fa-box-archive"></i> Archiver</button>
            <button
              v-else
              :disabled="busy"
              class="btn-ghost !px-4 !py-2"
              @click="setStatus('read')"
            ><i class="fa-solid fa-rotate-left"></i> Désarchiver</button>
            <button :disabled="busy" class="btn-ghost !border-red-700 !px-4 !py-2 !text-red-700 hover:!bg-red-700" @click="removeSelected">
              <i class="fa-regular fa-trash-can"></i> Supprimer
            </button>
          </div>
        </div>

        <dl class="mt-5 grid gap-5 bg-icy p-5 sm:grid-cols-3">
          <div>
            <dt class="text-xs font-bold uppercase tracking-wide text-slate/60">Expéditeur</dt>
            <dd class="mt-1 font-semibold text-midnight">{{ selected.name }}</dd>
          </div>
          <div class="min-w-0">
            <dt class="text-xs font-bold uppercase tracking-wide text-slate/60">E-mail</dt>
            <dd class="mt-1 truncate"><a :href="`mailto:${selected.email}`" class="text-royal hover:underline">{{ selected.email }}</a></dd>
          </div>
          <div>
            <dt class="text-xs font-bold uppercase tracking-wide text-slate/60">Téléphone</dt>
            <dd class="mt-1">{{ selected.phone || '—' }}</dd>
          </div>
        </dl>

        <p class="mt-6 min-h-[200px] whitespace-pre-line leading-relaxed">{{ selected.message }}</p>

        <div class="mt-8 border-t border-mist pt-5">
          <a :href="replyLink" class="btn-primary"><i class="fa-solid fa-reply"></i> Répondre par e-mail</a>
        </div>
      </template>
    </div>
  </div>
</template>