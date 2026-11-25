<script setup>
defineProps({
  items: { type: Array, required: true },
  active: { type: String, required: true },
  collapsed: { type: Boolean, default: false },
  badge: { type: Number, default: 0 },
})
defineEmits(['select', 'toggle', 'logout'])

const siteUrl = window.location.origin + '/'
</script>

<template>
  <aside :class="['sticky top-0 flex h-screen shrink-0 flex-col bg-midnight text-white transition-all duration-300', collapsed ? 'w-20' : 'w-60']">
    <div class="flex h-20 items-center justify-between border-b border-midnight-700 px-4">
      <div class="flex items-center gap-3">
        
        <!-- REMPLACEMENT DU LOGO ICI -->
        <img 
          src="/logo.png" 
          alt="Logo AFA TECH" 
          class="h-9 w-9 shrink-0 rounded-full bg-white object-cover p-0.5 shadow-sm"
        />
        
        <div v-if="!collapsed" class="leading-tight">
          <p class="font-display text-sm font-bold">AFA TECH</p>
          <p class="text-[11px] tracking-wide text-mist/70">ADMIN CMS</p>
        </div>
      </div>
      <button
        :aria-label="collapsed ? 'Agrandir le menu' : 'Réduire le menu'"
        class="text-mist hover:text-white"
        :class="collapsed ? 'hidden' : ''"
        @click="$emit('toggle')"
      >
        <i class="fa-solid fa-angles-left"></i>
      </button>
    </div>

    <nav class="flex-1 space-y-1 p-3" aria-label="Administration">
      <button
        v-for="item in items"
        :key="item.key"
        :aria-current="active === item.key ? 'page' : undefined"
        :title="collapsed ? item.label : undefined"
        :class="[
          'flex w-full items-center gap-3 px-3 py-2.5 text-left text-sm font-semibold transition-colors',
          active === item.key ? 'bg-royal text-white' : 'text-mist hover:bg-midnight-700 hover:text-white',
        ]"
        @click="$emit('select', item.key)"
      >
        <i :class="['fa-solid w-4 text-center', item.icon]"></i>
        <span v-if="!collapsed" class="flex-1">{{ item.label }}</span>
        <span
          v-if="item.key === 'messages' && badge > 0 && !collapsed"
          class="bg-white px-2 py-0.5 text-xs font-bold text-royal"
        >{{ badge }}</span>
      </button>
    </nav>

    <div class="space-y-1 border-t border-midnight-700 p-3">
      <a
        :href="siteUrl"
        target="_blank"
        rel="noopener"
        :title="collapsed ? 'Voir le site' : undefined"
        class="flex w-full items-center gap-3 px-3 py-2.5 text-sm font-semibold text-mist hover:bg-midnight-700 hover:text-white"
      >
        <i class="fa-solid fa-arrow-up-right-from-square w-4 text-center"></i>
        <span v-if="!collapsed">Voir le site</span>
      </a>
      <button
        class="flex w-full items-center gap-3 px-3 py-2.5 text-sm font-semibold text-mist hover:bg-midnight-700 hover:text-white"
        @click="$emit('logout')"
      >
        <i class="fa-solid fa-right-from-bracket w-4 text-center"></i>
        <span v-if="!collapsed">Se déconnecter</span>
      </button>
    </div>
  </aside>
</template>