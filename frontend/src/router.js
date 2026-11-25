import { createRouter, createWebHistory } from 'vue-router'

const titles = {
  home: 'AFA TECH SOLUTIONS — Construire l\'avenir numérique de l\'Afrique',
  about: 'À propos — AFA TECH SOLUTIONS',
  services: 'Services — AFA TECH SOLUTIONS',
  training: 'Formation — AFA TECH SOLUTIONS',
  projects: 'Projets — AFA TECH SOLUTIONS',
  project: 'Projet — AFA TECH SOLUTIONS',
  contact: 'Contact — AFA TECH SOLUTIONS',
  login: 'Connexion — Administration',
  dashboard: 'Tableau de bord — Administration',
}

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ top: 0 }),
  routes: [
    { path: '/', name: 'home', component: () => import('./views/Home.vue') },
    { path: '/a-propos', name: 'about', component: () => import('./views/About.vue') },
    { path: '/services', name: 'services', component: () => import('./views/Services.vue') },
    { path: '/formation', name: 'training', component: () => import('./views/Training.vue') },
    { path: '/projets', name: 'projects', component: () => import('./views/Projects.vue') },
    { path: '/projets/:id', name: 'project', component: () => import('./views/ProjectDetail.vue') },
    { path: '/contact', name: 'contact', component: () => import('./views/Contact.vue') },

    // Connexion : accessible via /admin/login et via /login (raccourci)
    { path: '/login', redirect: { name: 'login' } },
    { path: '/admin/login', name: 'login', component: () => import('./views/Login.vue'), meta: { bare: true } },

    { path: '/admin', name: 'dashboard', component: () => import('./views/Dashboard.vue'), meta: { bare: true, auth: true } },
    { path: '/:pathMatch(.*)*', redirect: '/' },
  ],
})

router.beforeEach((to) => {
  if (to.meta.auth && !localStorage.getItem('afa_token')) return { name: 'login' }
})
router.afterEach((to) => { document.title = titles[to.name] || titles.home })

export default router