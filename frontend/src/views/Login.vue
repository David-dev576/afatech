<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'

const router = useRouter()
const form = reactive({ username: '', password: '' })
const error = ref('')
const loading = ref(false)

async function login() {
  error.value = ''
  loading.value = true
  try {
    const { data } = await api.post('/auth/login/', {
      username: form.username.trim(),
      password: form.password,
    })
    localStorage.setItem('afa_token', data.token)
    router.push({ name: 'dashboard' })
  } catch (e) {
    if (!e.response) {
      // Pas de réponse : le backend ou le tunnel n'est pas joignable
      error.value = 'Impossible de joindre le serveur. Vérifiez que runserver et cloudflared tournent, et que VITE_API_URL est à jour.'
    } else if (e.response.status === 429) {
      error.value = 'Trop de tentatives. Réessayez plus tard.'
    } else {
      // Le serveur a répondu : le mot de passe ou le nom d'utilisateur est refusé
      error.value = e.response.data?.detail || 'Identifiants invalides.'
    }
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-icy p-5">
    <div class="w-full max-w-md rounded-sm border border-mist/50 bg-white p-10 shadow-sm">
      <div class="text-center">
        <img
          src="/logo.png"
          alt="Logo AFA TECH"
          class="mx-auto h-16 w-16 rounded-full border border-mist/50 bg-white object-cover p-1 shadow-sm"
        />
        <h1 class="mt-5 font-display text-3xl font-bold text-midnight">Espace Administrateur</h1>
        <p class="mt-2 text-slate/70">Connectez-vous pour gérer votre site.</p>
      </div>

      <form class="mt-8 space-y-5" novalidate @submit.prevent="login">
        <label class="block text-xs font-bold uppercase tracking-wide text-slate">
          Nom d'utilisateur
          <input v-model="form.username" class="field mt-2 normal-case" autocomplete="username" required />
        </label>
        <label class="block text-xs font-bold uppercase tracking-wide text-slate">
          Mot de passe
          <input v-model="form.password" type="password" class="field mt-2" autocomplete="current-password" required />
        </label>

        <p v-if="error" role="alert" class="border-l-4 border-red-700 bg-red-50 p-3 text-sm text-red-700">
          <i class="fa-solid fa-triangle-exclamation mr-2"></i>{{ error }}
        </p>

        <button type="submit" class="btn-primary w-full justify-center disabled:opacity-60" :disabled="loading">
          <i :class="loading ? 'fa-solid fa-spinner fa-spin' : 'fa-solid fa-right-to-bracket'"></i>
          {{ loading ? 'Connexion…' : 'Se connecter' }}
        </button>
      </form>

      <div class="mt-8 text-center">
        <router-link to="/" class="text-sm font-semibold text-royal hover:underline">
          <i class="fa-solid fa-arrow-left mr-1"></i>Retour au site public
        </router-link>
      </div>
    </div>
  </div>
</template>