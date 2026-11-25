<script setup>
import { useList } from '../composables'
import { mediaUrl } from '../components/dashboard/shared'

const { items, loading } = useList('/projects/')
</script>

<template>
  <section class="bg-icy pb-16 pt-36">
    <div class="mx-auto max-w-7xl px-5">
      <p class="text-sm font-semibold uppercase tracking-wide text-royal">Portfolio</p>
      <h1 class="mt-3 max-w-3xl text-5xl font-bold leading-tight sm:text-6xl">Our projects</h1>
      <p class="mt-6 max-w-2xl text-lg">
        Demonstration projects are clearly labelled as such. Open a project to see its details and source code.
      </p>
    </div>
  </section>

  <section class="mx-auto max-w-7xl px-5 py-16">
    <div v-if="loading" class="grid gap-6 md:grid-cols-2">
      <div v-for="n in 2" :key="n" class="skeleton h-64"></div>
    </div>

    <p v-else-if="!items.length" class="border border-dashed border-mist p-10 text-center">
      No published project yet. Please come back soon.
    </p>

    <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
      <router-link
        v-for="p in items"
        :key="p.id"
        :to="`/projets/${p.id}`"
        class="group block"
      >
        <div class="aspect-[4/3] overflow-hidden bg-midnight">
          <img
            v-if="p.image"
            :src="mediaUrl(p.image)"
            :alt="p.title"
            loading="lazy"
            class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
          />
          <div v-else class="flex h-full items-center justify-center text-mist/40">
            <i class="fa-solid fa-image text-4xl"></i>
          </div>
        </div>
        <p class="mt-3 text-sm font-semibold text-royal">
          {{ p.category_name }}
          <span v-if="p.is_demo" class="ml-2 font-normal text-slate/60">Demonstration</span>
        </p>
        <h2 class="mt-1 font-display text-xl font-bold text-midnight group-hover:text-royal">{{ p.title }}</h2>
        <p class="mt-1 text-slate/80">{{ p.summary }}</p>
      </router-link>
    </div>
  </section>
</template>