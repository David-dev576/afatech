<script setup>
import { inject, reactive, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import api from '../../api'
import { normalizeErrors } from './shared'

const router = useRouter()
const me = inject('me')
const refreshMe = inject('refreshMe')

const profile = reactive({ first_name: '', email: '' })
const pwd = reactive({ old_password: '', new_password: '', confirm: '' })
const profileErrors = ref({})
const pwdErrors = ref({})
const message = ref('')
const savingProfile = ref(false)
const savingPwd = ref(false)

watch(me, (v) => {
  profile.first_name = v.first_name || ''
  profile.email = v.email || ''
}, { immediate: true })

async function saveProfile() {
  profileErrors.value = {}
  message.value = ''
  savingProfile.value = true
  try {
    await api.patch('/auth/profile/', {
      first_name: profile.first_name.trim(),
      email: profile.email.trim(),
    })
    await refreshMe()
    message.value = 'Profil mis à jour.'
  } catch (e) {
    profileErrors.value = normalizeErrors(e)
  } finally {
    savingProfile.value = false
  }
}

async function changePassword() {
  pwdErrors.value = {}
  message.value = ''
  const e = {}
  if (!pwd.old_password) e.old_password = 'Saisissez votre mot de passe actuel.'
  if (pwd.new_password.length < 8) e.new_password = 'Au moins 8 caractères.'
  if (pwd.new_password !== pwd.confirm) e.confirm = 'Les mots de passe ne correspondent pas.'
  if (Object.keys(e).length) return (pwdErrors.value = e)

  savingPwd.value = true
  try {
    await api.post('/auth/password/', { old_password: pwd.old_password, new_password: pwd.new_password })
    message.value = 'Mot de passe modifié. Vous allez être déconnecté.'
    setTimeout(() => {
      localStorage.removeItem('afa_token')
      router.push({ name: 'login' })
    }, 2000)
  } catch (err) {
    pwdErrors.value = normalizeErrors(err)
  } finally {
    savingPwd.value = false
  }
}
</script>

<template>
  <div class="grid max-w-5xl gap-6 lg:grid-cols-12">
    <!-- Identité -->
    <form class="bg-white p-6 lg:col-span-7" novalidate @submit.prevent="saveProfile">
      <div class="flex items-center gap-4 border-b border-mist pb-6">
        <span class="flex h-14 w-14 items-center justify-center bg-midnight font-display text-lg font-bold text-white">
          {{ (me.username || 'AD').slice(0, 2).toUpperCase() }}
        </span>
        <div>
          <p class="font-display text-lg font-bold text-midnight">Compte administrateur</p>
          <p class="text-sm text-slate/60">{{ me.username }}</p>
        </div>
      </div>

      <div class="mt-6 grid gap-5 sm:grid-cols-2">
        <label class="block text-sm font-semibold">
          Nom complet
          <input v-model="profile.first_name" class="field mt-2 font-normal" autocomplete="name" />
          <span v-if="profileErrors.first_name" class="mt-1 block font-normal text-red-700">{{ profileErrors.first_name }}</span>
        </label>
        <label class="block text-sm font-semibold">
          Adresse e-mail
          <input v-model="profile.email" type="email" class="field mt-2 font-normal" autocomplete="email" />
          <span v-if="profileErrors.email" class="mt-1 block font-normal text-red-700">{{ profileErrors.email }}</span>
        </label>
      </div>
      <p v-if="profileErrors.form" role="alert" class="mt-4 text-sm text-red-700">{{ profileErrors.form }}</p>

      <div class="mt-6 flex justify-end border-t border-mist pt-5">
        <button class="btn-primary disabled:opacity-60" :disabled="savingProfile">
          {{ savingProfile ? 'Enregistrement…' : 'Enregistrer le profil' }}
        </button>
      </div>
    </form>

    <!-- Sécurité -->
    <form class="bg-white p-6 lg:col-span-5" novalidate @submit.prevent="changePassword">
      <h2 class="font-display text-lg font-bold text-midnight">Sécurité et mot de passe</h2>
      <p class="mt-1 text-sm text-slate/60">Huit caractères minimum. Vous serez déconnecté après le changement.</p>

      <div class="mt-6 space-y-5">
        <label class="block text-sm font-semibold">
          Mot de passe actuel
          <input v-model="pwd.old_password" type="password" class="field mt-2 font-normal" autocomplete="current-password" />
          <span v-if="pwdErrors.old_password" class="mt-1 block font-normal text-red-700">{{ pwdErrors.old_password }}</span>
        </label>
        <label class="block text-sm font-semibold">
          Nouveau mot de passe
          <input v-model="pwd.new_password" type="password" class="field mt-2 font-normal" autocomplete="new-password" />
          <span v-if="pwdErrors.new_password" class="mt-1 block font-normal text-red-700">{{ pwdErrors.new_password }}</span>
        </label>
        <label class="block text-sm font-semibold">
          Confirmer le mot de passe
          <input v-model="pwd.confirm" type="password" class="field mt-2 font-normal" autocomplete="new-password" />
          <span v-if="pwdErrors.confirm" class="mt-1 block font-normal text-red-700">{{ pwdErrors.confirm }}</span>
        </label>
      </div>
      <p v-if="pwdErrors.form" role="alert" class="mt-4 text-sm text-red-700">{{ pwdErrors.form }}</p>

      <div class="mt-6 flex justify-end border-t border-mist pt-5">
        <button class="btn-primary disabled:opacity-60" :disabled="savingPwd">
          {{ savingPwd ? 'Modification…' : 'Modifier le mot de passe' }}
        </button>
      </div>
    </form>

    <p v-if="message" role="status" class="border-l-4 border-royal bg-white p-4 text-sm lg:col-span-12">
      <i class="fa-solid fa-circle-check mr-2 text-royal"></i>{{ message }}
    </p>
  </div>
</template>