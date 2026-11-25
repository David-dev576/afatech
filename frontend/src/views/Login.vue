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
    error.value = e.response?.status === 429
      ? 'Trop de tentatives. Réessayez plus tard.'
      : e.response?.data?.detail || 'Identifiants invalides.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-icy p-5">
    <div class="w-full max-w-md bg-white p-10 shadow-sm rounded-sm">
      <div class="text-center">
        
        <!-- REMPLACEMENT DU LOGO ICI -->
        <img 
          src="/logo.png" 
          alt="Logo AFA TECH" 
          class="h-16 w-16 mx-auto object-cover rounded-full bg-white p-1 shadow-sm border border-mist/50"
        />
        
        <h1 class="mt-5 text-3xl font-heading font-bold text-midnight">Espace Administrateur</h1>
        <p class="mt-2 text-slate/70 font-body">Connectez-vous pour gérer votre site.</p>
      </div>

      <form class="mt-8 space-y-5" @submit.prevent="login">
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

        <button type="submit" class="btn-primary w-full justify-center" :disabled="loading">
          <i :class="loading ? 'fa-solid fa-spinner fa-spin' : 'fa-solid fa-right-to-bracket'"></i>
          {{ loading ? 'Connexion…' : 'Se connecter' }}
        </button>
      </form>

      <div class="mt-8 text-center">
        <router-link to="/" class="font-semibold text-royal hover:underline text-sm">
          <i class="fa-solid fa-arrow-left mr-1"></i>Retour au site public
        </router-link>
      </div>
    </div>
  </div>
</template>