import { createRouter, createWebHistory } from 'vue-router'

const titles = {
  home: 'AFA TECH SOLUTIONS — Construire l\'avenir numérique de l\'Afrique',
  about: 'À propos — AFA TECH SOLUTIONS',
  services: 'Services — AFA TECH SOLUTIONS',
  training: 'Formation — AFA TECH SOLUTIONS',
  projects: 'Projets — AFA TECH SOLUTIONS',
  contact: 'Contact — AFA TECH SOLUTIONS',
  login: 'Connexion — Administration',
  dashboard: 'Tableau de bord — Administration',
}

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ top: 0 }),
  routes: [
    // Pages publiques
    { path: '/', name: 'home', component: () => import('../views/Home.vue') }, // Attention: HomeView.vue ou Home.vue
    { path: '/a-propos', name: 'about', component: () => import('../views/About.vue') },
    { path: '/services', name: 'services', component: () => import('../views/Services.vue') },
    { path: '/formation', name: 'training', component: () => import('../views/Training.vue') },
    { path: '/projets', name: 'projects', component: () => import('../views/Projects.vue') },
    { path: '/contact', name: 'contact', component: () => import('../views/Contact.vue') },
    
    // --- LA CORRECTION EST ICI ---
    // On change '/admin/login' en '/login' pour que votre URL fonctionne
    { path: '/login', name: 'login', component: () => import('../views/Login.vue'), meta: { bare: true } },
    
    // Le Dashboard
    { path: '/admin', name: 'dashboard', component: () => import('../views/Dashboard.vue'), meta: { bare: true, auth: true } },
    
    // Redirection si l'URL n'existe pas
    { path: '/:pathMatch(.*)*', redirect: '/' },
  ],
})

router.beforeEach((to) => {
  if (to.meta.auth && !localStorage.getItem('afa_token')) return { name: 'login' }
})

router.afterEach((to) => { document.title = titles[to.name] || titles.home })

export default router