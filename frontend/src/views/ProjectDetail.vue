<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import api from '../api'
import { mediaUrl } from '../components/dashboard/shared'
import { t } from '../i18n'

const route = useRoute()
const project = ref(null)
const loading = ref(true)
const notFound = ref(false)

async function load(id) {
  loading.value = true
  notFound.value = false
  project.value = null
  try {
    const { data } = await api.get(`/projects/${id}/`)
    project.value = data
  } catch {
    notFound.value = true
  } finally {
    loading.value = false
  }
}

watch(() => route.params.id, (id) => load(id), { immediate: true })

const technologies = computed(() =>
  (project.value?.technologies || '')
    .split(',')
    .map((x) => x.trim())
    .filter(Boolean)
)

const imageUrl = computed(() => (project.value?.image ? mediaUrl(project.value.image) : ''))
</script>

<template>
  <div v-if="loading" class="mx-auto max-w-7xl space-y-6 px-5 pb-16 pt-36">
    <div class="skeleton h-12 w-2/3"></div>
    <div class="skeleton h-96"></div>
  </div>

  <section v-else-if="notFound" class="mx-auto max-w-3xl px-5 pb-24 pt-44 text-center">
    <p class="font-display text-6xl font-bold text-royal">404</p>
    <h1 class="mt-4 font-display text-3xl font-bold text-midnight">{{ t('detail.notFoundTitle') }}</h1>
    <p class="mt-4 text-lg">{{ t('detail.notFoundText') }}</p>
    <router-link to="/projets" class="btn-primary mt-8">
      <i class="fa-solid fa-arrow-left"></i> {{ t('detail.back') }}
    </router-link>
  </section>

  <article v-else-if="project" class="pb-24">
    <!-- Fil d'Ariane -->
    <nav :aria-label="t('detail.breadcrumb')" class="bg-white px-5 pt-32">
      <ol class="mx-auto flex max-w-7xl items-center gap-2 text-sm text-slate/60">
        <li><router-link to="/" class="hover:text-royal">{{ t('detail.home') }}</router-link></li>
        <li><i class="fa-solid fa-chevron-right text-[10px]"></i></li>
        <li><router-link to="/projets" class="hover:text-royal">{{ t('detail.projects') }}</router-link></li>
        <li><i class="fa-solid fa-chevron-right text-[10px]"></i></li>
        <li class="truncate text-midnight" aria-current="page">{{ project.title }}</li>
      </ol>
    </nav>

    <!-- En-tête -->
    <header class="mx-auto max-w-7xl px-5 pt-8">
      <div class="flex flex-wrap gap-2">
        <span class="border border-mist bg-white px-3 py-1 text-sm font-semibold">{{ project.category_name }}</span>
        <span
          class="border px-3 py-1 text-sm font-semibold"
          :class="project.is_demo ? 'border-mist bg-white' : 'border-midnight bg-midnight text-white'"
        >
          {{ project.is_demo ? t('detail.demo') : t('detail.company') }}
        </span>
      </div>

      <div class="mt-6 flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
        <h1 class="max-w-3xl font-display text-4xl font-bold leading-tight text-midnight sm:text-5xl lg:text-6xl">
          {{ project.title }}
        </h1>
        <router-link to="/contact" class="btn shrink-0 justify-center bg-midnight text-white hover:bg-midnight-700">
          {{ t('detail.request') }} <i class="fa-solid fa-arrow-right"></i>
        </router-link>
      </div>
    </header>

    <!-- Photo -->
    <div class="mx-auto mt-12 max-w-7xl px-5">
      <div class="aspect-[16/9] overflow-hidden bg-midnight">
        <img v-if="imageUrl" :src="imageUrl" :alt="project.title" class="h-full w-full object-cover" />
        <div v-else class="flex h-full flex-col items-center justify-center gap-3 text-mist/50">
          <i class="fa-solid fa-image text-5xl"></i>
          <span class="text-sm">{{ t('detail.noImage') }}</span>
        </div>
      </div>
    </div>

    <!-- Contenu -->
    <div class="mx-auto mt-14 grid max-w-7xl gap-12 px-5 lg:grid-cols-12">
      <div class="lg:col-span-8">
        <h2 class="font-display text-2xl font-bold text-midnight">{{ t('detail.about') }}</h2>
        <p class="mt-2 text-lg leading-relaxed">{{ project.summary }}</p>
        <p v-if="project.description" class="mt-6 whitespace-pre-line leading-relaxed text-slate/90">
          {{ project.description }}
        </p>
      </div>

      <aside class="space-y-6 lg:col-span-4">
        <div class="bg-white p-6">
          <h2 class="font-display text-lg font-bold text-midnight">{{ t('detail.techs') }}</h2>
          <ul v-if="technologies.length" class="mt-4 flex flex-wrap gap-2">
            <li v-for="tech in technologies" :key="tech" class="border border-mist px-3 py-1 text-sm font-semibold">
              {{ tech }}
            </li>
          </ul>
          <p v-else class="mt-4 text-sm text-slate/60">{{ t('detail.techsNone') }}</p>
        </div>

        <div class="bg-white p-6">
          <h2 class="font-display text-lg font-bold text-midnight">{{ t('detail.source') }}</h2>
          <a
            v-if="project.github_url"
            :href="project.github_url"
            target="_blank"
            rel="noopener noreferrer"
            class="btn-primary mt-4 w-full justify-center"
          >
            <i class="fa-brands fa-github"></i> {{ t('detail.github') }}
          </a>
          <p v-else class="mt-4 text-sm text-slate/60">{{ t('detail.noRepo') }}</p>
        </div>

        <p v-if="project.is_demo" class="border-l-4 border-mist bg-white p-5 text-sm leading-relaxed">
          {{ t('detail.demoNote') }}
        </p>
      </aside>
    </div>
  </article>
</template>