<script setup>
import { computed, reactive, ref } from 'vue'
import api from '../api'
import { locale, t } from '../i18n'

const lang = computed(() => (locale.value === 'en' ? 'en' : 'fr'))

// Textes des modules : titre, badge et icône sont communs, descriptions et points par langue
const frontendModules = [
  { title: 'HTML', icon: 'fa-brands fa-html5', badge: 'WEB 1', text: {
    fr: { desc: 'HTML, le langage de balisage standard pour les documents affichés dans un navigateur web.', points: ['Structure sémantique et organisation du document', 'Formulaires, accessibilité et intégration de médias'] },
    en: { desc: 'HTML, the standard markup language for documents displayed in a web browser.', points: ['Semantic layout & document structure', 'Forms, accessibility & media integration'] } } },
  { title: 'CSS', icon: 'fa-brands fa-css3-alt', badge: 'WEB 1', text: {
    fr: { desc: "CSS, le langage de feuilles de style qui décrit la présentation d'un document HTML.", points: ['Mises en page responsives, Flexbox et Grid', "Style d'interface moderne, animations et transitions"] },
    en: { desc: 'CSS, a style sheet language used for describing the presentation of an HTML document.', points: ['Responsive layouts, Flexbox & Grid', 'Modern UI styling, animations & transitions'] } } },
  { title: 'JavaScript', icon: 'fa-brands fa-js', badge: 'WEB 1', text: {
    fr: { desc: 'JavaScript, le langage de programmation qui rend les pages web interactives et dynamiques.', points: ['Manipulation du DOM et gestion des événements', 'Variables, fonctions et structures logiques'] },
    en: { desc: 'JavaScript is a programming language that makes web pages interactive and dynamic.', points: ['DOM manipulation & event handling', 'Variables, functions & logic structures'] } } },
  { title: 'Vue.js', icon: 'fa-brands fa-vuejs', badge: 'WEB 2', text: {
    fr: { desc: 'Framework JavaScript progressif pour construire des interfaces et des applications monopage.', points: ['Architecture à base de composants', 'Liaison réactive des données et Composition API'] },
    en: { desc: 'Progressive JavaScript framework for building user interfaces and single-page applications.', points: ['Component-based architecture', 'Reactive data binding & Composition API'] } } },
  { title: 'Nuxt.js', icon: 'fa-solid fa-layer-group', badge: 'WEB 2', text: {
    fr: { desc: 'Framework Vue intuitif pour créer des applications web rendues côté serveur ou statiques.', points: ['Rendu côté serveur favorable au référencement', 'Routage automatique basé sur les fichiers'] },
    en: { desc: 'Intuitive Vue framework for server-side rendered and static web applications.', points: ['SEO-friendly server-side rendering', 'Automatic routing & file-based system'] } } },
  { title: 'Tailwind CSS', icon: 'fa-solid fa-wind', badge: 'WEB 2', text: {
    fr: { desc: 'Framework CSS utilitaire pour créer rapidement des interfaces modernes et responsives directement dans le balisage.', points: ['Classes utilitaires et jetons de design', 'Configuration personnalisée et mode sombre'] },
    en: { desc: 'Utility-first CSS framework for rapidly building modern, responsive interfaces directly in your markup.', points: ['Utility classes & design tokens', 'Custom configuration & dark mode'] } } },
]

const backendModules = [
  { title: 'Python', icon: 'fa-brands fa-python', badge: 'WEB 2', dark: true, text: {
    fr: { desc: 'Langage de programmation polyvalent et de haut niveau, réputé pour sa lisibilité et son vaste écosystème.', points: ['Scripting et automatisation', 'Programmation orientée objet'] },
    en: { desc: 'Versatile, high-level programming language known for readability and a massive ecosystem.', points: ['Scripting & automation', 'Object-oriented programming'] } } },
  { title: 'Django', icon: 'fa-solid fa-cube', badge: 'WEB 2', dark: true, text: {
    fr: { desc: 'Framework web Python de haut niveau qui favorise un développement rapide et une conception propre.', points: ["Développement d'API REST", 'ORM et migrations de base de données'] },
    en: { desc: 'High-level Python web framework that encourages rapid development and clean design.', points: ['REST API development', 'ORM & database migrations'] } } },
  { title: 'Java', icon: 'fa-brands fa-java', badge: 'WEB 2', dark: false, text: {
    fr: { desc: "Langage robuste et orienté objet, très utilisé pour les applications d'entreprise et Android.", points: ['Principes de la programmation orientée objet', 'JVM et exécution multiplateforme'] },
    en: { desc: 'Robust, object-oriented language widely used for enterprise applications and Android.', points: ['Object-oriented principles', 'JVM & cross-platform execution'] } } },
  { title: 'Spring Boot', icon: 'fa-solid fa-leaf', badge: 'WEB 2', dark: false, text: {
    fr: { desc: 'Framework Java pour créer rapidement des applications web autonomes de qualité production.', points: ['Architecture en microservices', 'Injection de dépendances et contrôleurs REST'] },
    en: { desc: 'Java-based framework for building production-grade, stand-alone web applications quickly.', points: ['Microservices architecture', 'Dependency injection & REST controllers'] } } },
  { title: 'SQL', icon: 'fa-solid fa-database', badge: 'WEB 2', dark: false, text: {
    fr: { desc: 'Langage standard pour stocker, manipuler et récupérer des données dans les bases relationnelles.', points: ['Modélisation de bases relationnelles', 'Requêtes complexes (JOIN, GROUP BY, etc.)'] },
    en: { desc: 'Standard language for storing, manipulating and retrieving data in relational databases.', points: ['Relational database modeling', 'Complex queries (JOIN, GROUP BY, etc.)'] } } },
  { title: 'MongoDB', icon: 'fa-solid fa-database', badge: 'WEB 2', dark: false, text: {
    fr: { desc: 'Base de données NoSQL orientée documents, conçue pour la scalabilité et la flexibilité.', points: ['Stockage de données sous forme de documents', "Pipelines d'agrégation et indexation"] },
    en: { desc: 'NoSQL document-oriented database designed for scalability and flexibility.', points: ['Document-based data storage', 'Aggregation pipelines & indexing'] } } },
]

const benefitsData = {
  fr: [
    ['fa-laptop-code', 'Pratique par projets', 'Appliquez chaque notion en construisant des sites web réels et des projets avec base de données.'],
    ['fa-arrow-trend-up', 'Progression claire', "Avancez étape par étape, du frontend fondamental à l'architecture backend avancée."],
    ['fa-users', 'Mentorat guidé', 'Apprenez avec vos pairs et bénéficiez des conseils de formateurs expérimentés.'],
    ['fa-briefcase', 'Bonnes habitudes techniques', 'Développez une organisation de code propre, une discipline de débogage et une pensée structurée.'],
  ],
  en: [
    ['fa-laptop-code', 'Project-Based Practice', 'Apply every concept directly by building real websites and database-backed projects.'],
    ['fa-arrow-trend-up', 'Clear Progression', 'Move step by step from foundational frontend to advanced backend architecture.'],
    ['fa-users', 'Guided Mentorship', 'Learn alongside peers and receive guidance from experienced instructors.'],
    ['fa-briefcase', 'Build Technical Habits', 'Develop clean code organization, debugging discipline, and structured thinking.'],
  ],
}
const benefits = computed(() => benefitsData[lang.value])

const frontend = computed(() => frontendModules.map((m) => ({ ...m, ...m.text[lang.value] })))
const backend = computed(() => backendModules.map((m) => ({ ...m, ...m.text[lang.value] })))

// --- Formulaire d'inscription : envoi réel vers Django ---
const form = reactive({ name: '', email: '', phone: '', track: 'front', goals: '' })
const trap = reactive({ hp_check: '' })
const errors = ref({})
const loading = ref(false)
const status = ref('') // '', 'ok', 'error', 'throttled', 'network'

const trackOptions = computed(() => [
  { value: 'front', label: t('training.trackFront') },
  { value: 'back', label: t('training.trackBack') },
  { value: 'full', label: t('training.trackFull') },
])

function validate() {
  const e = {}
  if (!form.name.trim()) e.name = t('err.name')
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) e.email = t('err.email')
  errors.value = e
  return Object.keys(e).length === 0
}

async function submit() {
  status.value = ''
  if (!validate()) {
    status.value = 'error'
    return
  }
  loading.value = true
  const trackLabel = trackOptions.value.find((o) => o.value === form.track)?.label || ''
  try {
    await api.post('/messages/', {
      name: form.name.trim(),
      email: form.email.trim(),
      phone: form.phone.trim(),
      subject: 'Formation',
      message: `${t('training.fTrack')} ${trackLabel}\n\n${t('training.fGoals')} : ${form.goals.trim() || '-'}`,
      hp_check: trap.hp_check,
    })
    status.value = 'ok'
    Object.assign(form, { name: '', email: '', phone: '', track: 'front', goals: '' })
    errors.value = {}
  } catch (err) {
    if (!err.response) status.value = 'network'
    else if (err.response.status === 429) status.value = 'throttled'
    else status.value = 'error'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="font-body text-slate bg-white pt-20">

    <!-- HERO -->
    <section class="border-b border-mist/50 bg-white">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-16 lg:grid-cols-12 lg:py-24">
        <div class="space-y-6 lg:col-span-6">
          <p class="inline-flex items-center gap-3 text-xs font-bold uppercase tracking-widest text-royal">
            <span class="h-[2px] w-8 bg-royal"></span>{{ t('training.eyebrow') }}
          </p>
          <h1 class="font-display text-4xl font-bold leading-[1.1] text-midnight lg:text-5xl">{{ t('training.title') }}</h1>
          <p class="text-lg leading-relaxed text-slate/70">{{ t('training.lead') }}</p>
          <div class="flex flex-wrap gap-4 pt-4">
            <a href="#curriculum" class="inline-flex items-center gap-2 rounded-sm bg-midnight px-6 py-3 font-bold text-white transition hover:bg-royal">
              {{ t('training.btnCurriculum') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </a>
            <a href="#register" class="inline-flex items-center gap-2 rounded-sm border border-mist px-6 py-3 font-bold text-midnight transition hover:bg-icy">
              {{ t('training.btnInquire') }}
            </a>
          </div>
        </div>

        <div class="relative lg:col-span-6">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=1000" :alt="t('training.imgAlt')" class="h-[400px] w-full rounded-sm object-cover shadow-lg" />
          <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between bg-white/90 p-3 text-xs font-semibold text-midnight shadow-md backdrop-blur-sm">
            <span>{{ t('training.imgCaption') }}</span>
            <i class="fa-solid fa-camera text-slate/50"></i>
          </div>
        </div>
      </div>
    </section>

    <!-- CURSUS -->
    <section id="curriculum" class="border-b border-mist/50 bg-white py-16 lg:py-24">
      <div class="mx-auto max-w-7xl px-5">
        <h2 class="mb-2 font-display text-3xl font-bold text-midnight">{{ t('training.currTitle') }}</h2>
        <div class="mb-12 h-1 w-16 bg-royal"></div>

        <!-- Frontend -->
        <div class="mb-16">
          <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center gap-4">
              <span class="rounded-sm bg-royal px-3 py-1 text-xs font-bold uppercase tracking-wider text-white">{{ t('training.frontTag') }}</span>
              <h3 class="font-display text-xl font-bold text-midnight">{{ t('training.frontTitle') }}</h3>
            </div>
            <span class="hidden text-xs font-bold uppercase tracking-widest text-slate/50 md:block">{{ t('training.frontSub') }}</span>
          </div>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            <div v-for="mod in frontend" :key="mod.title" class="flex flex-col rounded-sm border border-mist/60 bg-white p-6 shadow-sm">
              <div class="mb-4 flex items-start justify-between">
                <i :class="[mod.icon, 'text-3xl text-royal']"></i>
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate/40">{{ mod.badge }}</span>
              </div>
              <h4 class="mb-2 font-display text-lg font-bold text-midnight">{{ mod.title }}</h4>
              <p class="mb-4 flex-grow text-sm text-slate/70">{{ mod.desc }}</p>
              <ul class="mt-auto space-y-2">
                <li v-for="point in mod.points" :key="point" class="flex items-start gap-2 text-xs text-slate/80">
                  <i class="fa-solid fa-check mt-0.5 text-royal"></i> {{ point }}
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Backend -->
        <div>
          <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center gap-4">
              <span class="rounded-sm bg-midnight px-3 py-1 text-xs font-bold uppercase tracking-wider text-white">{{ t('training.backTag') }}</span>
              <h3 class="font-display text-xl font-bold text-midnight">{{ t('training.backTitle') }}</h3>
            </div>
            <span class="hidden text-xs font-bold uppercase tracking-widest text-slate/50 md:block">{{ t('training.backSub') }}</span>
          </div>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            <div
              v-for="mod in backend"
              :key="mod.title"
              :class="['flex flex-col rounded-sm border p-6 shadow-sm', mod.dark ? 'border-midnight bg-midnight text-white' : 'border-mist/60 bg-white text-slate']"
            >
              <div class="mb-4 flex items-start justify-between">
                <i :class="[mod.icon, 'text-3xl text-royal']"></i>
                <span :class="['text-[10px] font-bold uppercase tracking-wider', mod.dark ? 'text-white/40' : 'text-slate/40']">{{ mod.badge }}</span>
              </div>
              <h4 :class="['mb-2 font-display text-lg font-bold', mod.dark ? 'text-white' : 'text-midnight']">{{ mod.title }}</h4>
              <p :class="['mb-4 flex-grow text-sm', mod.dark ? 'text-white/70' : 'text-slate/70']">{{ mod.desc }}</p>
              <ul class="mt-auto space-y-2">
                <li v-for="point in mod.points" :key="point" :class="['flex items-start gap-2 text-xs', mod.dark ? 'text-white/80' : 'text-slate/80']">
                  <i class="fa-solid fa-check mt-0.5 text-royal"></i> {{ point }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- MÉTHODE -->
    <section class="bg-icy py-16 lg:py-24">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 lg:grid-cols-12">
        <div class="lg:col-span-5">
          <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80&w=800" :alt="t('training.imgAlt')" class="h-[450px] w-full rounded-sm object-cover shadow-md" />
        </div>
        <div class="lg:col-span-7">
          <p class="mb-2 text-xs font-bold uppercase tracking-widest text-royal">{{ t('training.benLabel') }}</p>
          <h2 class="mb-8 font-display text-3xl font-bold text-midnight">{{ t('training.benTitle') }}</h2>
          <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
            <div v-for="(b, i) in benefits" :key="i" class="rounded-sm border border-mist/50 bg-white p-5 shadow-sm">
              <div class="mb-3 flex items-center gap-3">
                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-icy text-royal">
                  <i :class="['fa-solid', b[0], 'text-sm']"></i>
                </div>
                <h4 class="font-display text-sm font-bold text-midnight">{{ b[1] }}</h4>
              </div>
              <p class="text-xs leading-relaxed text-slate/70">{{ b[2] }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- INSCRIPTION -->
    <section id="register" class="border-t border-mist/50 bg-white py-16 lg:py-24">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-start gap-12 px-5 lg:grid-cols-12">
        <div class="sticky top-32 space-y-6 lg:col-span-5">
          <p class="text-xs font-bold uppercase tracking-widest text-royal">{{ t('training.regLabel') }}</p>
          <h2 class="font-display text-3xl font-bold leading-tight text-midnight lg:text-4xl">{{ t('training.regTitle') }}</h2>
          <p class="leading-relaxed text-slate/70">
            {{ t('training.regText') }}
            <a href="mailto:Afatechsolutions@gmail.com" class="font-semibold text-royal hover:underline">Afatechsolutions@gmail.com</a>.
          </p>
        </div>

        <div class="lg:col-span-7">
          <form class="relative space-y-5 rounded-sm border border-mist/60 bg-white p-8 shadow-sm" novalidate @submit.prevent="submit">
            <!-- Champ piège anti-spam -->
            <div class="absolute -left-[10000px] top-0 h-0 overflow-hidden" aria-hidden="true">
              <label>
                {{ t('contact.honeypot') }}
                <input v-model="trap.hp_check" type="text" name="hp_check" tabindex="-1" autocomplete="off" />
              </label>
            </div>

            <div v-if="status === 'ok'" role="status" class="flex items-center gap-3 rounded-sm bg-royal/5 p-4 text-sm text-midnight">
              <i class="fa-solid fa-circle-check text-royal"></i> {{ t('training.fOk') }}
            </div>
            <div v-if="status === 'error'" role="alert" class="flex items-center gap-3 rounded-sm bg-red-50 p-4 text-sm text-red-700">
              <i class="fa-solid fa-circle-exclamation"></i> {{ t('training.fErr') }}
            </div>
            <div v-if="status === 'throttled'" role="alert" class="flex items-center gap-3 rounded-sm bg-red-50 p-4 text-sm text-red-700">
              <i class="fa-solid fa-clock"></i> {{ t('contact.throttled') }}
            </div>
            <div v-if="status === 'network'" role="alert" class="flex items-center gap-3 rounded-sm bg-red-50 p-4 text-sm text-red-700">
              <i class="fa-solid fa-plug-circle-xmark"></i> {{ t('contact.network') }}
            </div>

            <div class="grid grid-cols-1 gap-5 md:grid-cols-2">
              <div>
                <label class="mb-2 block text-xs font-bold uppercase tracking-wide text-slate">{{ t('training.fName') }}</label>
                <input v-model="form.name" type="text" :placeholder="t('training.fNamePh')" class="w-full rounded-sm border border-mist px-4 py-3 text-sm outline-none transition focus:border-royal focus:ring-1 focus:ring-royal" />
                <p v-if="errors.name" class="mt-1 text-sm text-red-700">{{ errors.name }}</p>
              </div>
              <div>
                <label class="mb-2 block text-xs font-bold uppercase tracking-wide text-slate">{{ t('training.fEmail') }}</label>
                <input v-model="form.email" type="email" :placeholder="t('training.fEmailPh')" class="w-full rounded-sm border border-mist px-4 py-3 text-sm outline-none transition focus:border-royal focus:ring-1 focus:ring-royal" />
                <p v-if="errors.email" class="mt-1 text-sm text-red-700">{{ errors.email }}</p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-5 md:grid-cols-2">
              <div>
                <label class="mb-2 block text-xs font-bold uppercase tracking-wide text-slate">{{ t('training.fPhone') }}</label>
                <input v-model="form.phone" type="tel" placeholder="+257 00 00 00 00" class="w-full rounded-sm border border-mist px-4 py-3 text-sm outline-none transition focus:border-royal focus:ring-1 focus:ring-royal" />
              </div>
              <div>
                <label class="mb-2 block text-xs font-bold uppercase tracking-wide text-slate">{{ t('training.fTrack') }}</label>
                <select v-model="form.track" class="w-full rounded-sm border border-mist bg-white px-4 py-3 text-sm outline-none transition focus:border-royal focus:ring-1 focus:ring-royal">
                  <option v-for="o in trackOptions" :key="o.value" :value="o.value">{{ o.label }}</option>
                </select>
              </div>
            </div>

            <div>
              <label class="mb-2 block text-xs font-bold uppercase tracking-wide text-slate">{{ t('training.fGoals') }}</label>
              <textarea v-model="form.goals" rows="4" :placeholder="t('training.fGoalsPh')" class="w-full resize-none rounded-sm border border-mist px-4 py-3 text-sm outline-none transition focus:border-royal focus:ring-1 focus:ring-royal"></textarea>
            </div>

            <div class="pt-2">
              <button type="submit" :disabled="loading" class="inline-flex w-full items-center justify-center gap-2 rounded-sm bg-midnight px-8 py-3 font-bold text-white transition hover:bg-royal disabled:cursor-not-allowed disabled:opacity-50 md:w-auto">
                <i :class="loading ? 'fa-solid fa-circle-notch fa-spin' : 'fa-regular fa-paper-plane'"></i>
                {{ loading ? t('training.fSending') : t('training.fSubmit') }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>
</template>