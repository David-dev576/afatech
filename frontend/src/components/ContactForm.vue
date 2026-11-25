<script setup>
import { reactive, ref } from 'vue'
import api from '../api'

const props = defineProps({ defaultSubject: { type: String, default: 'Training' } })

// Valeurs envoyées au serveur : ne pas les traduire
const subjects = [
  { value: 'Formation', label: 'IT Fundamentals Training' },
  { value: 'Site web ou système de gestion', label: 'Website or management system' },
  { value: 'Application mobile', label: 'Mobile application' },
  { value: 'Hébergement et conseil IT', label: 'Web hosting and IT consulting' },
  { value: 'Autre', label: 'Other' },
]

const emptyForm = () => ({
  name: '',
  email: '',
  phone: '',
  subject: props.defaultSubject === 'Training' ? 'Formation' : props.defaultSubject,
  message: '',
})

const form = reactive(emptyForm())
// Champ piège anti-spam : invisible pour les visiteurs, doit rester vide
const trap = reactive({ hp_check: '' })
const consent = ref(false)

const errors = ref({})
const loading = ref(false)
const status = ref('') // '', 'ok', 'error', 'throttled', 'network'

const messages = {
  name: 'Please enter your name.',
  email: 'Please enter a valid email address.',
  subject: 'Please choose a subject.',
  message: 'Your message must contain at least 10 characters.',
  consent: 'Please tick this box to send your message.',
}

function validate() {
  const e = {}
  if (!form.name.trim()) e.name = messages.name
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) e.email = messages.email
  if (!form.subject) e.subject = messages.subject
  if (form.message.trim().length < 10) e.message = messages.message
  if (!consent.value) e.consent = messages.consent
  errors.value = e
  return Object.keys(e).length === 0
}

// Traduit les erreurs renvoyées par Django (qui sont en français)
function translateServerError(msg) {
  const text = String(msg)
  if (/au moins 10/i.test(text)) return messages.message
  if (/valide|valid/i.test(text)) return messages.email
  return 'This field is invalid.'
}

async function submit() {
  status.value = ''
  if (!validate()) {
    status.value = 'error'
    return
  }

  loading.value = true
  try {
    await api.post('/messages/', {
      name: form.name.trim(),
      email: form.email.trim(),
      phone: form.phone.trim(),
      subject: form.subject,
      message: form.message.trim(),
      hp_check: trap.hp_check,
    })
    status.value = 'ok'
    Object.assign(form, emptyForm())
    consent.value = false
    errors.value = {}
  } catch (err) {
    if (!err.response) {
      status.value = 'network'
    } else if (err.response.status === 429) {
      status.value = 'throttled'
    } else if (err.response.status === 400) {
      const data = err.response.data || {}
      errors.value = Object.fromEntries(
        Object.entries(data).map(([field, msgs]) => [field, translateServerError([].concat(msgs)[0])])
      )
      status.value = 'error'
    } else {
      status.value = 'error'
    }
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <form class="relative space-y-6" novalidate @submit.prevent="submit">
    <!-- Honeypot anti-spam: hidden from visitors, must stay empty -->
    <div class="absolute -left-[10000px] top-0 h-0 overflow-hidden" aria-hidden="true">
      <label>
        Do not fill this in
        <input v-model="trap.hp_check" type="text" name="hp_check" tabindex="-1" autocomplete="off" />
      </label>
    </div>

    <!-- Status messages -->
    <div v-if="status === 'ok'" role="status" class="flex items-start gap-3 border border-royal/30 bg-royal/5 p-4 text-sm">
      <i class="fa-solid fa-circle-check mt-0.5 text-royal"></i>
      <span>Your message has been sent. We will reply shortly.</span>
    </div>
    <div v-if="status === 'error'" role="alert" class="flex items-start gap-3 border border-red-700/30 bg-red-50 p-4 text-sm text-red-700">
      <i class="fa-solid fa-triangle-exclamation mt-0.5"></i>
      <span>Your message was not sent. Please check the highlighted fields.</span>
    </div>
    <div v-if="status === 'throttled'" role="alert" class="flex items-start gap-3 border border-red-700/30 bg-red-50 p-4 text-sm text-red-700">
      <i class="fa-solid fa-clock mt-0.5"></i>
      <span>Too many messages sent from this connection. Please try again later.</span>
    </div>
    <div v-if="status === 'network'" role="alert" class="flex items-start gap-3 border border-red-700/30 bg-red-50 p-4 text-sm text-red-700">
      <i class="fa-solid fa-plug-circle-xmark mt-0.5"></i>
      <span>Unable to reach the server. Please check that Django is running (python manage.py runserver).</span>
    </div>

    <div class="grid gap-6 sm:grid-cols-2">
      <label class="block text-sm font-semibold text-midnight">
        Full name *
        <input v-model="form.name" class="field mt-2 font-normal" autocomplete="name" placeholder="First and last name" />
        <span v-if="errors.name" class="mt-1 block text-sm font-normal text-red-700">{{ errors.name }}</span>
      </label>
      <label class="block text-sm font-semibold text-midnight">
        Email address *
        <input v-model="form.email" type="email" class="field mt-2 font-normal" autocomplete="email" placeholder="name@organization.com" />
        <span v-if="errors.email" class="mt-1 block text-sm font-normal text-red-700">{{ errors.email }}</span>
      </label>
    </div>

    <div class="grid gap-6 sm:grid-cols-2">
      <label class="block text-sm font-semibold text-midnight">
        Phone number
        <input v-model="form.phone" type="tel" class="field mt-2 font-normal" autocomplete="tel" placeholder="+257 00 00 00 00" />
      </label>
      <label class="block text-sm font-semibold text-midnight">
        Subject *
        <select v-model="form.subject" class="field mt-2 font-normal">
          <option value="" disabled>Choose a subject</option>
          <option v-for="s in subjects" :key="s.value" :value="s.value">{{ s.label }}</option>
        </select>
        <span v-if="errors.subject" class="mt-1 block text-sm font-normal text-red-700">{{ errors.subject }}</span>
      </label>
    </div>

    <label class="block text-sm font-semibold text-midnight">
      Message *
      <textarea
        v-model="form.message"
        rows="6"
        class="field mt-2 font-normal"
        placeholder="Describe your project, your goals, or your training request…"
      ></textarea>
      <span v-if="errors.message" class="mt-1 block text-sm font-normal text-red-700">{{ errors.message }}</span>
    </label>

    <div class="flex flex-col gap-5 pt-2 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <label class="flex items-center gap-3 text-sm text-slate/80">
          <input v-model="consent" type="checkbox" class="h-4 w-4 accent-royal" />
          We respect your privacy and reply directly.
        </label>
        <span v-if="errors.consent" class="mt-1 block text-sm text-red-700">{{ errors.consent }}</span>
      </div>

      <button
        type="submit"
        class="btn justify-center bg-midnight text-white hover:bg-midnight-700 disabled:opacity-60"
        :disabled="loading"
      >
        <i :class="loading ? 'fa-solid fa-spinner fa-spin' : 'fa-regular fa-paper-plane'"></i>
        {{ loading ? 'Sending…' : 'Send inquiry' }}
      </button>
    </div>
  </form>
</template>