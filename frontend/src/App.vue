<script setup>
import { useRoute } from 'vue-router'
import NavBar from './components/NavBar.vue'
import SiteFooter from './components/SiteFooter.vue'
const route = useRoute()
</script>

<template>
  <NavBar v-if="!route.meta.bare" />
  <main>
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in"><component :is="Component" /></transition>
    </router-view>
  </main>
  <SiteFooter v-if="!route.meta.bare" />
</template>
