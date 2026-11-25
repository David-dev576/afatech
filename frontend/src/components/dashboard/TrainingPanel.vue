<script setup>
import { computed, inject, onMounted, reactive, ref } from 'vue'
import api, { list } from '../../api'
import { ADMIN_URL, normalizeErrors } from './shared'

const search = inject('dashSearch')
const refreshStats = inject('refreshStats')

const items = ref([])
const loading = ref(true)
const error = ref('')
const editing = ref(null)
const saving = ref(false)
const errors = ref({})
const form = reactive(blank())

function blank() {
  return { track: '', title: '', description: '', technologies: '', status: 'available', position: 0, is_published: true }
}

async function load() {
  try {
    items.value = await list('/training/')
  } catch {
    error.value = 'Impossible de charger les formations.'
  } finally {
    loading.value = false
  }
}
onMounted(load)

const filtered = computed(() => {
  const q = (search.value || '').trim().toLowerCase()
  return q ? items.value.filter((i) => `${i.title} ${i.track}`.toLowerCase().includes(q)) : items.value
})

const techList = (t) => t.split(',').map((x) => x.trim()).filter(Boolean)

function openNew() {
  editing.value = {}
  Object.assign(form, blank())
  errors.value = {}
}
function openEdit(p) {
  editing.value = p
  Object.assign(form, {
    track: p.track, title: p.title, description: p.description, technologies: p.technologies,
    status: p.status, position: p.position, is_published: p.is_published,
  })
  errors.value = {}
}
function close() {
  editing.value = null
}

function validate() {
  const e = {}
  if (!form.track.trim()) e.track = 'Indiquez le parcours, par exemple WEB 1.'
  if (!form.title.trim()) e.title = 'Le titre est obligatoire.'
  if (!form.description.trim()) e.description = 'La description est obligatoire.'
  if (!form.technologies.trim()) e.technologies = 'Listez au moins une technologie.'
  errors.value = e
  return !Object.keys(e).length
}

async function save() {
  if (!validate()) return
  saving.value = true
  errors.value = {}
  const data = {
    track: form.track.trim(),
    title: form.title.trim(),
    description: form.description.trim(),
    technologies: form.technologies.trim(),
    status: form.status,
    position: Number(form.position) || 0,
    is_published: form.is_published,
  }
  try {
    if (editing.value.id) await api.patch(`/training/${editing.value.id}/`, data)
    else await api.post('/training/', data)
    close()
    await load()
    refreshStats()
  } catch (e) {
    errors.value = normalizeErrors(e)
  } finally {
    saving.value = false
  }
}

async function togglePublish(p) {
  await api.patch(`/training/${p.id}/`, { is_published: !p.is_published })
  await load()
}

async function remove(p) {
  if (!confirm(`Supprimer la formation « ${p.title} » ?`)) return
  await api.delete(`/training/${p.id}/`)
  await load()
  refreshStats()
}
</script>

<template>
  <div class="flex flex-wrap items-center justify-between gap-4">
    <p class="text-sm text-slate/70">{{ items.length }} programme(s)</p>
    <div class="flex gap-3">
      <a :href="ADMIN_URL" target="_blank" rel="noopener" class="btn-ghost !px-4 !py-2 text-sm">Gérer dans l'admin</a>
      <button class="btn-primary" @click="openNew"><i class="fa-solid fa-plus"></i> Ajouter un programme</button>
    </div>
  </div>

  <p v-if="error" role="alert" class="mt-4 border-l-4 border-red-700 bg-white p-3 text-red-700">{{ error }}</p>
  <div v-if="loading" class="skeleton mt-6 h-48"></div>

  <div class="mt-6 grid gap-6 md:grid-cols-2">
    <article v-for="p in filtered" :key="p.id" class="flex flex-col bg-white p-6">
      <div class="flex items-start justify-between gap-4">
        <p class="font-display text-xs font-bold uppercase tracking-wider text-royal">{{ p.track }}</p>
        <button
          :class="['px-2.5 py-1 text-xs font-semibold', p.is_published ? 'bg-emerald-50 text-emerald-700' : 'bg-mist/50 text-slate']"
          @click="togglePublish(p)"
        >{{ p.is_published ? 'Publié' : 'Non publié' }}</button>
      </div>
      <h2 class="mt-3 font-display text-xl font-bold text-midnight">{{ p.title }}</h2>
      <p class="mt-2 text-sm leading-relaxed text-slate/80">{{ p.description }}</p>

      <ul class="mt-4 flex flex-wrap gap-2">
        <li v-for="t in techList(p.technologies)" :key="t" class="border border-mist px-2.5 py-1 text-xs font-semibold">{{ t }}</li>
      </ul>

      <div class="mt-auto flex items-center justify-between border-t border-mist pt-4 text-sm">
        <span class="text-slate/60">{{ p.status === 'available' ? 'Disponible' : 'Prévu' }}</span>
        <div class="flex gap-4 font-semibold">
          <button class="text-midnight hover:text-royal" @click="openEdit(p)">Modifier</button>
          <button class="text-red-700 hover:underline" @click="remove(p)">Supprimer</button>
        </div>
      </div>
    </article>
    <p v-if="!loading && !filtered.length" class="bg-white p-8 text-center text-slate/60 md:col-span-2">Aucun programme.</p>
  </div>

  <form v-if="editing" class="mt-8 space-y-5 bg-white p-6" novalidate @submit.prevent="save">
    <div class="flex items-center justify-between">
      <h2 class="font-display text-lg font-bold text-midnight">{{ editing.id ? 'Modifier le programme' : 'Nouveau programme' }}</h2>
      <button type="button" aria-label="Fermer" class="text-slate/60 hover:text-midnight" @click="close"><i class="fa-solid fa-xmark"></i></button>
    </div>

    <p v-if="errors.form" role="alert" class="border-l-4 border-red-700 bg-red-50 p-3 text-sm text-red-700">{{ errors.form }}</p>

    <div class="grid gap-5 md:grid-cols-3">
      <label class="block text-sm font-semibold">
        Parcours
        <input v-model="form.track" class="field mt-2 font-normal" placeholder="WEB 1" />
        <span v-if="errors.track" class="mt-1 block text-sm font-normal text-red-700">{{ errors.track }}</span>
      </label>
      <label class="block text-sm font-semibold md:col-span-2">
        Titre
        <input v-model="form.title" class="field mt-2 font-normal" />
        <span v-if="errors.title" class="mt-1 block text-sm font-normal text-red-700">{{ errors.title }}</span>
      </label>
    </div>

    <label class="block text-sm font-semibold">
      Description
      <textarea v-model="form.description" rows="4" class="field mt-2 font-normal"></textarea>
      <span v-if="errors.description" class="mt-1 block text-sm font-normal text-red-700">{{ errors.description }}</span>
    </label>

    <label class="block text-sm font-semibold">
      Technologies (séparées par des virgules)
      <input v-model="form.technologies" class="field mt-2 font-normal" placeholder="HTML: structurer les pages, CSS: styliser" />
      <span class="mt-1 block text-xs font-normal text-slate/60">Format : Technologie: description. Chaque élément est séparé par une virgule.</span>
      <span v-if="errors.technologies" class="mt-1 block text-sm font-normal text-red-700">{{ errors.technologies }}</span>
    </label>

    <div class="grid gap-5 md:grid-cols-3">
      <label class="block text-sm font-semibold">
        Disponibilité
        <select v-model="form.status" class="field mt-2 font-normal">
          <option value="available">Disponible</option>
          <option value="planned">Prévu</option>
        </select>
      </label>
      <label class="block text-sm font-semibold">
        Position
        <input v-model="form.position" type="number" min="0" class="field mt-2 font-normal" />
      </label>
      <label class="block text-sm font-semibold">
        Publication
        <select v-model="form.is_published" class="field mt-2 font-normal">
          <option :value="true">Publié</option>
          <option :value="false">Non publié</option>
        </select>
      </label>
    </div>

    <div class="flex justify-end gap-3 border-t border-mist pt-5">
      <button type="button" class="btn-ghost" @click="close">Annuler</button>
      <button class="btn-primary disabled:opacity-60" :disabled="saving">
        <i :class="saving ? 'fa-solid fa-spinner fa-spin' : 'fa-solid fa-floppy-disk'"></i>
        {{ saving ? 'Enregistrement…' : 'Enregistrer le programme' }}
      </button>
    </div>
  </form>
</template>