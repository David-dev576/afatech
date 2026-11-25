<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const sidebarOpen = ref(false)

const menuItems = [
  { name: 'Overview', icon: 'fa-chart-pie', path: '/admin', exact: true },
  { name: 'Services', icon: 'fa-layer-group', path: '/admin/services' },
  { name: 'Training Programs', icon: 'fa-graduation-cap', path: '/admin/training' },
  { name: 'Projects', icon: 'fa-briefcase', path: '/admin/projects' },
  { name: 'Project Categories', icon: 'fa-tags', path: '/admin/categories' },
  { name: 'Contact Messages', icon: 'fa-comments', path: '/admin/messages', badge: 3 },
  { name: 'Company Settings', icon: 'fa-gear', path: '/admin/settings' },
  { name: 'Profile', icon: 'fa-user', path: '/admin/profile' },
]

const handleLogout = () => {
  localStorage.removeItem('afa_token')
  router.push('/login')
}
</script>

<template>
  <div class="min-h-screen bg-[#F4F7FA] flex font-body text-slate">
    
    <!-- SIDEBAR -->
    <aside 
      :class="[
        'fixed inset-y-0 left-0 z-50 w-[240px] bg-[#0F2942] text-white transition-transform duration-300 transform lg:translate-x-0 lg:static lg:inset-0 flex flex-col',
        sidebarOpen ? 'translate-x-0' : '-translate-x-full'
      ]"
    >
      <!-- Logo -->
      <div class="flex items-center gap-3 h-[70px] px-6 border-b border-white/10 shrink-0">
        <img src="/logo.png" alt="Logo" class="h-8 w-8 rounded-full bg-white p-0.5" />
        <div class="leading-tight">
          <span class="block font-heading font-bold text-sm tracking-wide text-white">AFA TECH</span>
          <span class="block text-[9px] text-white/50 tracking-widest uppercase">Solutions</span>
        </div>
      </div>

      <!-- Menu -->
      <nav class="p-3 space-y-0.5 mt-2 overflow-y-auto flex-1">
        <router-link 
          v-for="item in menuItems" 
          :key="item.path" 
          :to="item.path"
          class="flex items-center justify-between px-3 py-2.5 rounded-sm text-[13px] font-medium text-white/70 hover:bg-white/10 hover:text-white transition-colors"
          active-class="bg-[#2563EB] text-white"
          :exact="item.exact"
        >
          <div class="flex items-center gap-3">
            <i :class="['fa-solid', item.icon, 'w-4 text-center text-xs']"></i>
            {{ item.name }}
          </div>
          <span v-if="item.badge" class="bg-royal text-white text-[10px] font-bold px-1.5 py-0.5 rounded-sm">{{ item.badge }}</span>
        </router-link>
      </nav>

      <!-- Déconnexion -->
      <div class="p-3 border-t border-white/10 shrink-0">
        <button @click="handleLogout" class="flex items-center gap-3 px-3 py-2.5 w-full rounded-sm text-[13px] font-medium text-white/70 hover:bg-white/10 hover:text-white transition-colors">
          <i class="fa-solid fa-arrow-right-from-bracket w-4 text-center text-xs"></i>
          Logout
        </button>
      </div>
    </aside>

    <!-- CONTENU PRINCIPAL -->
    <div class="flex-1 flex flex-col min-w-0 h-screen overflow-hidden">
      
      <!-- TOPBAR -->
      <header class="bg-white border-b border-[#CBD5E1]/50 h-[70px] flex items-center justify-between px-6 shadow-sm z-10 shrink-0">
        <div class="flex items-center gap-2 text-sm font-semibold">
          <span class="text-midnight">Dashboard Overview</span>
          <span class="text-slate/40 font-normal mx-1">›</span> 
          <span class="text-slate/60 font-normal">Sample: Backup Data</span>
        </div>
        
        <div class="flex items-center gap-4">
          <!-- Recherche -->
          <div class="relative hidden md:block">
            <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate/40 text-xs"></i>
            <input type="text" placeholder="Search services, projects..." class="bg-[#F4F7FA] border border-[#CBD5E1]/50 text-xs pl-8 pr-4 py-2 rounded-sm w-64 focus:outline-none focus:border-royal transition" />
          </div>
          
          <!-- Profil -->
          <div class="flex items-center gap-2 cursor-pointer bg-[#F4F7FA] border border-[#CBD5E1]/50 px-2 py-1 rounded-sm">
            <span class="text-xs font-semibold text-midnight">Admin</span>
            <div class="h-6 w-6 rounded-full bg-[#0F2942] flex items-center justify-center text-white text-xs font-bold">
              A
            </div>
          </div>
        </div>
      </header>

      <!-- ROUTER VIEW -->
      <main class="flex-1 overflow-y-auto p-6">
        <router-view></router-view>
      </main>

    </div>
  </div>
</template>