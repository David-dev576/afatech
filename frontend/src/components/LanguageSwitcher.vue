<script setup>
import { locale, setLocale } from '../i18n'

const langs = [
  { code: 'fr', label: 'FR' },
  { code: 'en', label: 'EN' },
]
</script>

<template>
  <div class="inline-flex border border-mist text-xs font-bold" role="group" aria-label="Langue / Language">
    <button
      v-for="l in langs"
      :key="l.code"
      type="button"
      :aria-pressed="locale === l.code"
      :class="[
        'px-3 py-1.5 transition-colors',
        locale === l.code ? 'bg-midnight text-white' : 'bg-white text-slate hover:bg-icy',
      ]"
      @click="setLocale(l.code)"
    >
      {{ l.label }}
    </button>
  </div>
</template>