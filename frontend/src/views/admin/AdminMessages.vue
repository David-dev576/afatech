<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const messages = ref([])
const isLoading = ref(true)
const errorMessage = ref('')

// Récupération des messages depuis Django
const fetchMessages = async () => {
  isLoading.value = true
  errorMessage.value = ''
  
  const token = localStorage.getItem('auth_token')
  
  if (!token) {
    errorMessage.value = "Vous n'êtes pas connecté."
    isLoading.value = false
    return
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/api/contact/', {
      headers: {
        Authorization: `Token ${token}` // <-- Le mot "Token" est important pour DRF
      }
    })
    messages.value = response.data
  } catch (error) {
    console.error(error)
    if (error.response && error.response.status === 401) {
      errorMessage.value = "Votre session a expiré. Veuillez vous reconnecter."
      localStorage.removeItem('auth_token')
    } else {
      errorMessage.value = "Erreur lors du chargement des messages."
    }
  } finally {
    isLoading.value = false
  }
}

// Marquer un message comme lu
const markAsRead = async (id) => {
  const token = localStorage.getItem('auth_token')
  try {
    await axios.patch(`http://127.0.0.1:8000/api/contact/${id}/`, 
      { is_read: true },
      { headers: { Authorization: `Token ${token}` } }
    )
    // Mise à jour locale de l'interface
    const msg = messages.value.find(m => m.id === id)
    if (msg) msg.is_read = true
  } catch (error) {
    console.error("Erreur lors de la mise à jour", error)
  }
}

onMounted(() => {
  fetchMessages()
})
</script>

<template>
  <div class="space-y-6">
    
    <div class="flex justify-between items-center">
      <h1 class="text-2xl font-heading font-bold text-midnight">Messages de contact</h1>
      <button @click="fetchMessages" class="bg-royal text-white px-4 py-2 rounded-sm text-sm font-bold hover:bg-midnight transition flex items-center gap-2">
        <i class="fa-solid fa-rotate-right"></i> Actualiser
      </button>
    </div>

    <!-- Message d'erreur -->
    <div v-if="errorMessage" class="bg-red-50 text-red-600 p-4 rounded-sm border border-red-200">
      {{ errorMessage }}
    </div>

    <div class="bg-white border border-mist/50 rounded-sm shadow-sm overflow-hidden">
      <div v-if="isLoading" class="p-10 text-center text-slate/50">
        <i class="fa-solid fa-circle-notch fa-spin text-2xl mb-2 text-royal"></i>
        <p>Chargement des messages...</p>
      </div>

      <table v-else class="w-full text-left border-collapse">
        <thead>
          <tr class="bg-icy border-b border-mist/50 text-xs font-bold text-slate/60 uppercase tracking-wider">
            <th class="p-4">Expéditeur</th>
            <th class="p-4">Sujet</th>
            <th class="p-4">Date</th>
            <th class="p-4">Statut</th>
            <th class="p-4 text-right">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-mist/50 text-sm">
          <tr v-for="msg in messages" :key="msg.id" class="hover:bg-icy/50 transition-colors">
            <td class="p-4">
              <div class="font-bold text-midnight">{{ msg.name }}</div>
              <div class="text-slate/60 text-xs">{{ msg.email }}</div>
            </td>
            <td class="p-4 font-semibold text-slate">{{ msg.subject }}</td>
            <td class="p-4 text-slate/70">{{ new Date(msg.created_at).toLocaleDateString('fr-FR') }}</td>
            <td class="p-4">
              <span v-if="!msg.is_read" class="inline-flex items-center gap-1 text-[10px] font-bold bg-red-100 text-red-600 px-2 py-1 rounded-sm uppercase">
                Non lu
              </span>
              <span v-else class="inline-flex items-center gap-1 text-[10px] font-bold bg-green-100 text-green-700 px-2 py-1 rounded-sm uppercase">
                Lu
              </span>
            </td>
            <td class="p-4 text-right">
              <button @click="markAsRead(msg.id)" v-if="!msg.is_read" class="text-slate/40 hover:text-royal p-2 transition" title="Marquer comme lu">
                <i class="fa-solid fa-envelope-open"></i>
              </button>
              <button class="text-slate/40 hover:text-red-500 p-2 transition" title="Supprimer">
                <i class="fa-solid fa-trash"></i>
              </button>
            </td>
          </tr>
          <tr v-if="messages.length === 0">
            <td colspan="5" class="p-8 text-center text-slate/50">Aucun message reçu pour le moment.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>