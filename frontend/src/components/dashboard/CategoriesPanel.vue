<script setup>
import { computed, inject, onMounted, ref } from 'vue'
import api, { list } from '../../api'
import { normalizeErrors } from './shared'

const refreshStats = inject('refreshStats')

const categories = ref([])
const projects = ref([])
const loading = ref(true)
const newName = ref('')
const editingId = ref(null)
const editName = ref('')
const errors = ref({})

async function load() {
  try {
    const [c, p] = await Promise.all([list('/categories/'), list('/projects/')])
    categories.value = c
    projects.value = p
  } catch {
    errors.value = { form: 'Impossible de charger les catégories.' }
  } finally {
    loading.value = false
  }
}
onMounted(load)

const countFor = (id) => projects.value.filter((p) => p.category === id).length

async function add() {
  errors.value = {}
  const name = newName.value.trim()
  if (!name) return (errors.value = { form: 'Saisissez un nom de catégorie.' })
  try {
    await api.post('/categories/', { name })
    newName.value = ''
    await load()
  } catch (e) {
    errors.value = normalizeErrors(e)
  }
}

function startEdit(c) {
  editingId.value = c.id
  editName.value = c.name
  errors.value = {}
}

async function saveEdit(c) {
  errors.value = {}
  try {
    await api.patch(`/categories/${c.id}/`, { name: editName.value.trim() })
    editingId.value = null
    await load()
  } catch (e) {
    errors.value = normalizeErrors(e)
  }
}

async function remove(c) {
  if (countFor(c.id) > 0) return
  if (!confirm(`Supprimer la catégorie « ${c.name} » ?`)) return
  try {
    await api.delete(`/categories/${c.id}/`)
    await load()
    refreshStats()
  } catch (e) {
    errors.value = normalizeErrors(e)
  }
}
</script>

<template>
  <div class="grid gap-6 xl:grid-cols-12">
    <form class="bg-white p-6 xl:col-span-4" novalidate @submit.prevent="add">
      <h2 class="font-display text-lg font-bold text-midnight">Nouvelle catégorie</h2>
      <p class="mt-1 text-sm text-slate/60">Regroupe les projets du portfolio, par exemple « Systèmes web ».</p>
      <label class="mt-5 block text-sm font-semibold">
        Nom
        <input v-model="newName" class="field mt-2 font-normal" maxlength="80" />
      </label>
      <p v-if="errors.name" class="mt-2 text-sm text-red-700">{{ errors.name }}</p>
      <button class="btn-primary mt-5 w-full justify-center"><i class="fa-solid fa-plus"></i> Ajouter la catégorie</button>
    </form>

    <div class="bg-white xl:col-span-8">
      <p v-if="errors.form" role="alert" class="m-4 border-l-4 border-red-700 bg-red-50 p-3 text-sm text-red-700">{{ errors.form }}</p>
      <div v-if="loading" class="skeleton m-6 h-40"></div>
      <table v-else class="w-full text-left text-sm">
        <thead class="border-b border-mist text-xs uppercase tracking-wide text-slate/60">
          <tr>
            <th class="px-5 py-3 font-semibold">Catégorie</th>
            <th class="font-semibold">Projets</th>
            <th class="pr-5 text-right font-semibold">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-mist">
          <tr v-for="c in categories" :key="c.id">
            <td class="px-5 py-4">
              <input v-if="editingId === c.id" v-model="editName" class="field py-2" maxlength="80" @keyup.enter="saveEdit(c)" />
              <span v-else class="font-semibold text-midnight">{{ c.name }}</span>
            </td>
            <td>{{ countFor(c.id) }}</td>
            <td class="pr-5 text-right">
              <template v-if="editingId === c.id">
                <button class="mr-4 font-semibold text-royal" @click="saveEdit(c)">Enregistrer</button>
                <button class="font-semibold text-slate/60" @click="editingId = null">Annuler</button>
              </template>
              <template v-else>
                <button class="mr-4 font-semibold text-midnight hover:text-royal" @click="startEdit(c)">Renommer</button>
                <button
                  :disabled="countFor(c.id) > 0"
                  :title="countFor(c.id) > 0 ? 'Déplacez d\'abord les projets de cette catégorie' : 'Supprimer'"
                  :class="['font-semibold', countFor(c.id) > 0 ? 'cursor-not-allowed text-mist' : 'text-red-700 hover:underline']"
                  @click="remove(c)"
                >Supprimer</button>
              </template>
            </td>
          </tr>
          <tr v-if="!loading && !categories.length">
            <td colspan="3" class="px-5 py-8 text-center text-slate/60">Aucune catégorie.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>