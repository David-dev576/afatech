<script setup>
import { computed, inject, onMounted, reactive, ref } from 'vue'
import api, { list } from '../../api'
import { ADMIN_URL, buildForm, mediaUrl, normalizeErrors, slugify } from './shared'

const search = inject('dashSearch')
const refreshStats = inject('refreshStats')

const items = ref([])
const categories = ref([])
const loading = ref(true)
const error = ref('')
const catFilter = ref('')
const editing = ref(null)
const saving = ref(false)
const errors = ref({})
const file = ref(null)
const form = reactive(blank())

// Accepte github.com (dépôts) et github.io (GitHub Pages)
const GITHUB_URL = /^https?:\/\/([\w-]+\.)*(github\.com|github\.io)(\/.*)?$/i

function blank() {
  return {
    title: '', category: '', summary: '', description: '', technologies: '',
    github_url: '', is_demo: true, is_published: false,
  }
}

async function load() {
  try {
    const [p, c] = await Promise.all([list('/projects/'), list('/categories/')])
    items.value = p
    categories.value = c
  } catch {
    error.value = 'Impossible de charger les projets.'
  } finally {
    loading.value = false
  }
}
onMounted(load)

const filtered = computed(() => {
  const q = (search.value || '').trim().toLowerCase()
  return items.value.filter((p) =>
    (!catFilter.value || p.category === Number(catFilter.value)) &&
    (!q || `${p.title} ${p.summary}`.toLowerCase().includes(q))
  )
})

const techList = (t) => (t || '').split(',').map((x) => x.trim()).filter(Boolean)

function openNew() {
  editing.value = {}
  Object.assign(form, blank())
  file.value = null
  errors.value = {}
}
function openEdit(p) {
  editing.value = p
  Object.assign(form, {
    title: p.title,
    category: p.category,
    summary: p.summary,
    description: p.description,
    technologies: p.technologies,
    github_url: p.github_url || '',
    is_demo: p.is_demo,
    is_published: p.is_published,
  })
  file.value = null
  errors.value = {}
}
function close() {
  editing.value = null
}
function onFile(e) {
  file.value = e.target.files[0] || null
}

function validate() {
  const e = {}
  if (!form.title.trim()) e.title = 'Le titre est obligatoire.'
  if (!form.category) e.category = 'Choisissez une catégorie.'
  if (!form.summary.trim()) e.summary = 'Ajoutez un résumé court.'
  const gh = form.github_url.trim()
  if (gh && !GITHUB_URL.test(gh)) {
    e.github_url = 'Le lien doit être une adresse GitHub (github.com ou github.io).'
  }
  errors.value = e
  return !Object.keys(e).length
}

async function save() {
  if (!validate()) return
  saving.value = true
  errors.value = {}
  const data = {
    title: form.title.trim(),
    category: form.category,
    summary: form.summary.trim(),
    description: form.description.trim(),
    technologies: form.technologies.trim(),
    github_url: form.github_url.trim(),
    is_demo: form.is_demo,
    is_published: form.is_published,
  }
  const isNew = !editing.value.id
  if (isNew) data.slug = `${slugify(data.title)}-${Date.now().toString(36)}`
  try {
    const payload = buildForm(data, 'image', file.value)
    if (isNew) await api.post('/projects/', payload)
    else await api.patch(`/projects/${editing.value.id}/`, payload)
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
  await api.patch(`/projects/${p.id}/`, { is_published: !p.is_published })
  await load()
  refreshStats()
}

async function remove(p) {
  if (!confirm(`Supprimer le projet « ${p.title} » ?`)) return
  await api.delete(`/projects/${p.id}/`)
  await load()
  refreshStats()
}
</script>

<template>
  <div class="flex flex-wrap items-center justify-between gap-4 bg-white p-4">
    <div class="flex flex-wrap items-center gap-3">
      <select v-model="catFilter" aria-label="Filtrer par catégorie" class="field w-auto py-2 text-sm">
        <option value="">Toutes les catégories</option>
        <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.name }}</option>
      </select>
      <span class="text-sm text-slate/60">{{ filtered.length }} projet(s)</span>
    </div>
    <div class="flex gap-3">
      <a :href="ADMIN_URL" target="_blank" rel="noopener" class="btn-ghost !px-4 !py-2 text-sm">Gérer dans l'admin</a>
      <button class="btn-primary" @click="openNew"><i class="fa-solid fa-plus"></i> Ajouter un projet</button>
    </div>
  </div>

  <p v-if="error" role="alert" class="mt-4 border-l-4 border-red-700 bg-white p-3 text-red-700">{{ error }}</p>
  <div v-if="loading" class="skeleton mt-6 h-64"></div>

  <div class="mt-6 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    <article v-for="p in filtered" :key="p.id" class="flex flex-col bg-white">
      <div class="relative aspect-[16/10] bg-midnight">
        <img v-if="p.image" :src="mediaUrl(p.image)" :alt="p.title" class="h-full w-full object-cover" />
        <div v-else class="flex h-full items-center justify-center text-mist/40"><i class="fa-solid fa-image text-4xl"></i></div>
        <span class="absolute left-3 top-3 bg-midnight px-2 py-1 text-[11px] font-semibold text-white">
          {{ p.is_demo ? 'Démonstration' : 'Initiative' }}
        </span>
      </div>
      <div class="flex flex-1 flex-col p-5">
        <div class="flex items-center justify-between gap-3">
          <p class="text-xs font-semibold text-royal">{{ p.category_name }}</p>
          <button
            :class="['px-2 py-0.5 text-xs font-semibold', p.is_published ? 'bg-emerald-50 text-emerald-700' : 'bg-mist/50 text-slate']"
            @click="togglePublish(p)"
          >{{ p.is_published ? 'Publié' : 'Brouillon' }}</button>
        </div>
        <h2 class="mt-2 font-display text-lg font-bold text-midnight">{{ p.title }}</h2>
        <p class="mt-1 line-clamp-2 text-sm text-slate/70">{{ p.summary }}</p>
        <p v-if="techList(p.technologies).length" class="mt-3 text-xs text-royal">{{ techList(p.technologies).join(' · ') }}</p>
        <p v-if="p.github_url" class="mt-2 truncate text-xs text-slate/60">
          <i class="fa-brands fa-github mr-1"></i>{{ p.github_url }}
        </p>
        <div class="mt-auto flex justify-between gap-4 border-t border-mist pt-4 text-sm font-semibold">
          <button class="text-midnight hover:text-royal" @click="openEdit(p)">Modifier</button>
          <button class="text-red-700 hover:underline" @click="remove(p)">Supprimer</button>
        </div>
      </div>
    </article>
    <p v-if="!loading && !filtered.length" class="bg-white p-8 text-center text-slate/60 md:col-span-2 xl:col-span-3">
      Aucun projet ne correspond.
    </p>
  </div>

  <form v-if="editing" class="mt-8 space-y-5 bg-white p-6" novalidate @submit.prevent="save">
    <div class="flex items-center justify-between">
      <h2 class="font-display text-lg font-bold text-midnight">{{ editing.id ? 'Modifier le projet' : 'Nouveau projet' }}</h2>
      <button type="button" aria-label="Fermer" class="text-slate/60 hover:text-midnight" @click="close"><i class="fa-solid fa-xmark"></i></button>
    </div>

    <p v-if="errors.form" role="alert" class="border-l-4 border-red-700 bg-red-50 p-3 text-sm text-red-700">{{ errors.form }}</p>

    <div class="grid gap-5 md:grid-cols-2">
      <label class="block text-sm font-semibold">
        Titre
        <input v-model="form.title" class="field mt-2 font-normal" />
        <span v-if="errors.title" class="mt-1 block text-sm font-normal text-red-700">{{ errors.title }}</span>
      </label>
      <label class="block text-sm font-semibold">
        Catégorie
        <select v-model="form.category" class="field mt-2 font-normal">
          <option value="" disabled>Choisir…</option>
          <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.name }}</option>
        </select>
        <span v-if="errors.category" class="mt-1 block text-sm font-normal text-red-700">{{ errors.category }}</span>
      </label>
    </div>

    <label class="block text-sm font-semibold">
      Résumé
      <input v-model="form.summary" class="field mt-2 font-normal" maxlength="300" />
      <span v-if="errors.summary" class="mt-1 block text-sm font-normal text-red-700">{{ errors.summary }}</span>
    </label>

    <label class="block text-sm font-semibold">
      Description détaillée
      <textarea v-model="form.description" rows="5" class="field mt-2 font-normal"></textarea>
    </label>

    <div class="grid gap-5 md:grid-cols-2">
      <label class="block text-sm font-semibold">
        Technologies utilisées (séparées par des virgules)
        <input v-model="form.technologies" class="field mt-2 font-normal" placeholder="Vue 3, Django, MySQL" />
      </label>
      <label class="block text-sm font-semibold">
        Lien GitHub (facultatif)
        <input v-model="form.github_url" type="url" class="field mt-2 font-normal" placeholder="https://github.com/votre-compte/projet" />
        <span v-if="errors.github_url" class="mt-1 block text-sm font-normal text-red-700">{{ errors.github_url }}</span>
      </label>
    </div>

    <div class="grid gap-5 md:grid-cols-3">
      <label class="block text-sm font-semibold">
        Photo du projet (facultatif)
        <input type="file" accept="image/jpeg,image/png,image/webp" class="field mt-2 py-2 font-normal" @change="onFile" />
        <span class="mt-1 block text-xs font-normal text-slate/60">JPG, PNG ou WebP, 3 Mo maximum.</span>
      </label>
      <label class="block text-sm font-semibold">
        Type
        <select v-model="form.is_demo" class="field mt-2 font-normal">
          <option :value="true">Démonstration</option>
          <option :value="false">Initiative de l'entreprise</option>
        </select>
      </label>
      <label class="block text-sm font-semibold">
        Publication
        <select v-model="form.is_published" class="field mt-2 font-normal">
          <option :value="true">Publié</option>
          <option :value="false">Brouillon</option>
        </select>
      </label>
    </div>
    <p class="text-sm text-slate/60">Un projet de démonstration n'est jamais présenté comme livré à un client.</p>

    <div class="flex justify-end gap-3 border-t border-mist pt-5">
      <button type="button" class="btn-ghost" @click="close">Annuler</button>
      <button class="btn-primary disabled:opacity-60" :disabled="saving">
        <i :class="saving ? 'fa-solid fa-spinner fa-spin' : 'fa-solid fa-floppy-disk'"></i>
        {{ saving ? 'Enregistrement…' : 'Enregistrer le projet' }}
      </button>
    </div>
  </form>
</template>