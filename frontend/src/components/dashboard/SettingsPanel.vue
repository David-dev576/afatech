<script setup>
import { onMounted, reactive, ref } from 'vue'
import api from '../../api'
import { buildForm, mediaUrl, normalizeErrors } from './shared'

const loading = ref(true)
const saving = ref(false)
const saved = ref(false)
const errors = ref({})
const socials = ref([])
const logoFile = ref(null)
const logoPreview = ref('')

const form = reactive({ name: '', description: '', email: '', phone: '', linkedin: '', github: '' })

async function load() {
  try {
    const { data } = await api.get('/settings/')
    form.name = data.name || ''
    form.description = data.description || ''
    form.email = data.email || ''
    form.phone = data.phone || ''
    socials.value = data.socials || []
    form.linkedin = socials.value.find((s) => s.platform === 'linkedin')?.url || ''
    form.github = socials.value.find((s) => s.platform === 'github')?.url || ''
    logoPreview.value = mediaUrl(data.logo)
  } catch {
    errors.value = { form: 'Impossible de charger les paramètres.' }
  } finally {
    loading.value = false
  }
}
onMounted(load)

function onLogo(e) {
  const f = e.target.files[0]
  if (!f) return
  logoFile.value = f
  logoPreview.value = URL.createObjectURL(f)
}

function validate() {
  const e = {}
  if (!form.name.trim()) e.name = 'Le nom de l\'entreprise est obligatoire.'
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) e.email = 'Entrez une adresse e-mail valide.'
  errors.value = e
  return !Object.keys(e).length
}

async function saveSocial(platform) {
  const url = form[platform].trim()
  const existing = socials.value.find((s) => s.platform === platform)
  if (!url && existing) return api.delete(`/socials/${existing.id}/`)
  if (!url) return
  if (existing) return api.patch(`/socials/${existing.id}/`, { url })
  return api.post('/socials/', { platform, url })
}

async function save() {
  if (!validate()) return
  saving.value = true
  saved.value = false
  errors.value = {}
  try {
    const payload = buildForm(
      { name: form.name.trim(), description: form.description.trim(), email: form.email.trim(), phone: form.phone.trim() },
      'logo',
      logoFile.value
    )
    await api.patch('/settings/', payload)
    await saveSocial('linkedin')
    await saveSocial('github')
    logoFile.value = null
    saved.value = true
    await load()
  } catch (e) {
    errors.value = normalizeErrors(e)
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <div v-if="loading" class="skeleton h-96"></div>

  <form v-else class="max-w-4xl bg-white" novalidate @submit.prevent="save">
    <!-- Logo -->
    <div class="flex flex-wrap items-center justify-between gap-6 border-b border-mist p-6">
      <div class="flex items-center gap-5">
        <div class="flex h-16 w-16 items-center justify-center overflow-hidden bg-midnight">
          <img v-if="logoPreview" :src="logoPreview" alt="Logo de l'entreprise" class="h-full w-full object-contain p-2" />
          <i v-else class="fa-solid fa-microchip text-2xl text-royal"></i>
        </div>
        <div>
          <h2 class="font-display text-lg font-bold text-midnight">Logo de l'entreprise</h2>
          <p class="text-sm text-slate/60">SVG ou PNG haute résolution, affiché dans l'en-tête et le pied de page.</p>
        </div>
      </div>
      <label class="btn-ghost !px-4 !py-2 cursor-pointer text-sm">
        <i class="fa-solid fa-arrow-up-from-bracket"></i> Changer le logo
        <input type="file" accept="image/png,image/jpeg,image/svg+xml,image/webp" class="sr-only" @change="onLogo" />
      </label>
    </div>

    <div class="space-y-6 p-6">
      <p v-if="errors.form" role="alert" class="border-l-4 border-red-700 bg-red-50 p-3 text-sm text-red-700">{{ errors.form }}</p>
      <p v-if="saved" role="status" class="border-l-4 border-royal bg-icy p-3 text-sm">
        <i class="fa-solid fa-circle-check mr-2 text-royal"></i>Paramètres enregistrés.
      </p>

      <div class="grid gap-5 md:grid-cols-2">
        <label class="block text-sm font-semibold">
          Nom de l'entreprise
          <input v-model="form.name" class="field mt-2 font-normal" />
          <span v-if="errors.name" class="mt-1 block font-normal text-red-700">{{ errors.name }}</span>
        </label>
        <label class="block text-sm font-semibold">
          Téléphone
          <input v-model="form.phone" type="tel" class="field mt-2 font-normal" placeholder="+257 00 00 00 00" />
        </label>
      </div>

      <label class="block text-sm font-semibold">
        Mission et description
        <textarea v-model="form.description" rows="4" class="field mt-2 font-normal"></textarea>
      </label>

      <div class="grid gap-5 md:grid-cols-2">
        <label class="block text-sm font-semibold">
          E-mail officiel
          <input v-model="form.email" type="email" class="field mt-2 font-normal" />
          <span v-if="errors.email" class="mt-1 block font-normal text-red-700">{{ errors.email }}</span>
        </label>
        <label class="block text-sm font-semibold">
          LinkedIn
          <input v-model="form.linkedin" type="url" class="field mt-2 font-normal" placeholder="https://linkedin.com/company/…" />
          <span v-if="errors.url" class="mt-1 block font-normal text-red-700">{{ errors.url }}</span>
        </label>
      </div>
      <label class="block text-sm font-semibold md:w-1/2 md:pr-2.5">
        GitHub
        <input v-model="form.github" type="url" class="field mt-2 font-normal" placeholder="https://github.com/…" />
      </label>
    </div>

    <div class="flex justify-end border-t border-mist p-6">
      <button class="btn-primary disabled:opacity-60" :disabled="saving">
        <i :class="saving ? 'fa-solid fa-spinner fa-spin' : 'fa-solid fa-floppy-disk'"></i>
        {{ saving ? 'Enregistrement…' : 'Enregistrer les paramètres' }}
      </button>
    </div>
  </form>
</template>