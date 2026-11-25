<script setup>
import { computed, inject, onMounted, reactive, ref } from 'vue'
import api, { list } from '../../api'
import { ADMIN_URL, buildForm, normalizeErrors, slugify } from './shared'

const search = inject('dashSearch')
const refreshStats = inject('refreshStats')

const items = ref([])
const loading = ref(true)
const error = ref('')
const editing = ref(null) // null = fermé, {} = nouveau, objet = modification
const saving = ref(false)
const errors = ref({})
const file = ref(null)
const form = reactive(blank())

function blank() {
  return { title: '', icon: 'fa-solid fa-code', summary: '', description: '', position: 0, is_published: true }
}

async function load() {
  try {
    items.value = await list('/services/')
  } catch {
    error.value = 'Impossible de charger les services.'
  } finally {
    loading.value = false
  }
}
onMounted(load)

const filtered = computed(() => {
  const q = (search.value || '').trim().toLowerCase()
  return q ? items.value.filter((i) => i.title.toLowerCase().includes(q)) : items.value
})

function openNew() {
  editing.value = {}
  Object.assign(form, blank())
  file.value = null
  errors.value = {}
}
function openEdit(s) {
  editing.value = s
  Object.assign(form, {
    title: s.title, icon: s.icon, summary: s.summary, description: s.description,
    position: s.position, is_published: s.is_published,
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
  if (!form.icon.trim()) e.icon = 'Indiquez une classe Font Awesome, par exemple fa-solid fa-code.'
  if (!form.summary.trim()) e.summary = 'Ajoutez un résumé court.'
  if (!form.description.trim()) e.description = 'La description est obligatoire.'
  errors.value = e
  return !Object.keys(e).length
}

async function save() {
  if (!validate()) return
  saving.value = true
  errors.value = {}
  const data = {
    title: form.title.trim(),
    icon: form.icon.trim(),
    summary: form.summary.trim(),
    description: form.description.trim(),
    position: Number(form.position) || 0,
    is_published: form.is_published,
  }
  const isNew = !editing.value.id
  if (isNew) data.slug = `${slugify(data.title)}-${Date.now().toString(36)}`
  try {
    const payload = buildForm(data, 'image', file.value)
    if (isNew) await api.post('/services/', payload)
    else await api.patch(`/services/${editing.value.id}/`, payload)
    close()
    await load()
    refreshStats()
  } catch (e) {
    errors.value = normalizeErrors(e)
  } finally {
    saving.value = false
  }
}

async function togglePublish(s) {
  await api.patch(`/services/${s.id}/`, { is_published: !s.is_published })
  await load()
}

async function remove(s) {
  if (!confirm(`Supprimer le service « ${s.title} » ?`)) return
  await api.delete(`/services/${s.id}/`)
  await load()
  refreshStats()
}
</script>

<template>
  <div class="flex flex-wrap items-center justify-between gap-4">
    <p class="text-sm text-slate/70">{{ items.length }} service(s) enregistré(s)</p>
    <div class="flex gap-3">
      <a :href="ADMIN_URL" target="_blank" rel="noopener" class="btn-ghost !px-4 !py-2 text-sm">Gérer dans l'admin</a>
      <button class="btn-primary" @click="openNew"><i class="fa-solid fa-plus"></i> Ajouter un service</button>
    </div>
  </div>

  <p v-if="error" role="alert" class="mt-4 border-l-4 border-red-700 bg-white p-3 text-red-700">{{ error }}</p>

  <div class="mt-6 overflow-x-auto bg-white">
    <div v-if="loading" class="skeleton m-5 h-40"></div>
    <table v-else class="w-full text-left text-sm">
      <thead class="border-b border-mist text-xs uppercase tracking-wide text-slate/60">
        <tr>
          <th class="px-5 py-3 font-semibold">Service</th>
          <th class="font-semibold">Position</th>
          <th class="font-semibold">Statut</th>
          <th class="pr-5 text-right font-semibold">Actions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-mist">
        <tr v-for="s in filtered" :key="s.id">
          <td class="px-5 py-4">
            <div class="flex items-center gap-4">
              <span class="flex h-10 w-10 shrink-0 items-center justify-center bg-icy text-royal"><i :class="s.icon"></i></span>
              <div>
                <p class="font-semibold text-midnight">{{ s.title }}</p>
                <p class="text-slate/60">{{ s.summary }}</p>
              </div>
            </div>
          </td>
          <td>{{ s.position }}</td>
          <td>
            <button
              :class="['px-2.5 py-1 text-xs font-semibold', s.is_published ? 'bg-emerald-50 text-emerald-700' : 'bg-mist/50 text-slate']"
              @click="togglePublish(s)"
            >{{ s.is_published ? 'Publié' : 'Non publié' }}</button>
          </td>
          <td class="pr-5 text-right">
            <button class="mr-4 font-semibold text-midnight hover:text-royal" @click="openEdit(s)">Modifier</button>
            <button class="font-semibold text-red-700 hover:underline" @click="remove(s)">Supprimer</button>
          </td>
        </tr>
        <tr v-if="!loading && !filtered.length">
          <td colspan="4" class="px-5 py-8 text-center text-slate/60">Aucun service.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Éditeur -->
  <form v-if="editing" class="mt-8 space-y-5 bg-white p-6" novalidate @submit.prevent="save">
    <div class="flex items-center justify-between">
      <h2 class="font-display text-lg font-bold text-midnight">{{ editing.id ? 'Modifier le service' : 'Nouveau service' }}</h2>
      <button type="button" aria-label="Fermer" class="text-slate/60 hover:text-midnight" @click="close"><i class="fa-solid fa-xmark"></i></button>
    </div>

    <p v-if="errors.form" role="alert" class="border-l-4 border-red-700 bg-red-50 p-3 text-sm text-red-700">{{ errors.form }}</p>

    <div class="grid gap-5 md:grid-cols-2">
      <label class="block text-sm font-semibold">
        Titre du service
        <input v-model="form.title" class="field mt-2 font-normal" />
        <span v-if="errors.title" class="mt-1 block text-sm font-normal text-red-700">{{ errors.title }}</span>
      </label>
      <label class="block text-sm font-semibold">
        Icône Font Awesome
        <input v-model="form.icon" class="field mt-2 font-normal" placeholder="fa-solid fa-code" />
        <span v-if="errors.icon" class="mt-1 block text-sm font-normal text-red-700">{{ errors.icon }}</span>
      </label>
    </div>

    <label class="block text-sm font-semibold">
      Résumé (affiché dans les listes)
      <input v-model="form.summary" class="field mt-2 font-normal" maxlength="300" />
      <span v-if="errors.summary" class="mt-1 block text-sm font-normal text-red-700">{{ errors.summary }}</span>
    </label>

    <label class="block text-sm font-semibold">
      Description
      <textarea v-model="form.description" rows="5" class="field mt-2 font-normal"></textarea>
      <span v-if="errors.description" class="mt-1 block text-sm font-normal text-red-700">{{ errors.description }}</span>
    </label>

    <div class="grid gap-5 md:grid-cols-3">
      <label class="block text-sm font-semibold">
        Image de couverture (facultatif)
        <input type="file" accept="image/jpeg,image/png,image/webp" class="field mt-2 py-2 font-normal" @change="onFile" />
        <span v-if="errors.image" class="mt-1 block text-sm font-normal text-red-700">{{ errors.image }}</span>
      </label>
      <label class="block text-sm font-semibold">
        Position
        <input v-model="form.position" type="number" min="0" class="field mt-2 font-normal" />
      </label>
      <label class="block text-sm font-semibold">
        Statut de publication
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
        {{ saving ? 'Enregistrement…' : 'Enregistrer le service' }}
      </button>
    </div>
  </form>
</template>