<script setup>
import { ref } from 'vue'

// --- DONNÉES DES MODULES FRONTEND ---
const frontendModules = [
  {
    title: 'HTML',
    icon: 'fa-brands fa-html5',
    description: 'HTML, the standard markup language for documents designed to be displayed in a web browser.',
    points: ['Semantic layout & document structure', 'Forms, accessibility & media integration'],
    badge: 'WEB 1'
  },
  {
    title: 'CSS',
    icon: 'fa-brands fa-css3-alt',
    description: 'CSS, a style sheet language used for describing the presentation of a document written in HTML.',
    points: ['Responsive layouts, Flexbox & Grid', 'Modern UI styling, animations & transitions'],
    badge: 'WEB 1'
  },
  {
    title: 'JavaScript',
    icon: 'fa-brands fa-js',
    description: 'JavaScript is a programming language that enables interactive web pages and dynamic content.',
    points: ['DOM manipulation & event handling', 'Variables, functions & logic structures'],
    badge: 'WEB 1'
  },
  {
    title: 'Vue.js',
    icon: 'fa-brands fa-vuejs',
    description: 'Progressive JavaScript framework for building user interfaces and single-page applications.',
    points: ['Component-based architecture', 'Reactive data binding & Composition API'],
    badge: 'WEB 2'
  },
  {
    title: 'Nuxt.js',
    icon: 'fa-solid fa-layer-group',
    description: 'Intuitive Vue framework for building server-side rendered and static web applications.',
    points: ['SEO-friendly server-side rendering', 'Automatic routing & file-based system'],
    badge: 'WEB 2'
  },
  {
    title: 'Tailwind CSS',
    icon: 'fa-solid fa-wind',
    description: 'Utility-first CSS framework for rapidly building modern, responsive interfaces directly in your markup.',
    points: ['Utility classes & design tokens', 'Custom configuration & dark mode'],
    badge: 'WEB 2'
  }
]

// --- DONNÉES DES MODULES BACKEND ---
const backendModules = [
  {
    title: 'Python',
    icon: 'fa-brands fa-python',
    description: 'Versatile, high-level programming language known for readability and a massive ecosystem.',
    points: ['Scripting & automation', 'Object-oriented programming'],
    badge: 'WEB 2',
    theme: 'dark'
  },
  {
    title: 'Django',
    icon: 'fa-solid fa-cube',
    description: 'High-level Python web framework that encourages rapid development and clean design.',
    points: ['REST API development', 'ORM & database migrations'],
    badge: 'WEB 2',
    theme: 'dark'
  },
  {
    title: 'Java',
    icon: 'fa-brands fa-java',
    description: 'Robust, object-oriented language widely used for enterprise applications and Android.',
    points: ['Object-oriented principles', 'JVM & cross-platform execution'],
    badge: 'WEB 2',
    theme: 'light'
  },
  {
    title: 'Spring Boot',
    icon: 'fa-solid fa-leaf',
    description: 'Java-based framework for building production-grade, stand-alone web applications quickly.',
    points: ['Microservices architecture', 'Dependency injection & REST controllers'],
    badge: 'WEB 2',
    theme: 'light'
  },
  {
    title: 'SQL',
    icon: 'fa-solid fa-database',
    description: 'Standard language for storing, manipulating and retrieving data in relational databases.',
    points: ['Relational database modeling', 'Complex queries (JOIN, GROUP BY, etc.)'],
    badge: 'WEB 2',
    theme: 'light'
  },
  {
    title: 'MongoDB',
    icon: 'fa-solid fa-database',
    description: 'NoSQL document-oriented database designed for scalability and flexibility.',
    points: ['Document-based data storage', 'Aggregation pipelines & indexing'],
    badge: 'WEB 2',
    theme: 'light'
  }
]

const benefits = [
  ['fa-laptop-code', 'Project-Based Practice', 'Apply every concept directly by building real websites and database-backed projects.'],
  ['fa-arrow-trend-up', 'Clear Progression', 'Move step by step from foundational frontend to advanced backend architecture.'],
  ['fa-users', 'Guided Mentorship', 'Learn alongside peers and receive guidance from experienced instructors.'],
  ['fa-briefcase', 'Build Technical Habits', 'Develop clean code organization, debugging discipline, and structured thinking.']
]

// --- FORMULAIRE D'INSCRIPTION ---
const form = ref({
  name: '',
  email: '',
  phone: '',
  cohort: 'Frontend (HTML, CSS, JS, Vue, Nuxt, Tailwind)',
  message: ''
})

const isSubmitting = ref(false)
const submitStatus = ref(null)

const handleSubmit = async () => {
  isSubmitting.value = true
  submitStatus.value = null
  
  try {
    // Remplacer par votre appel API Axios vers Django
    // await axios.post('/api/training/register/', form.value)
    await new Promise(resolve => setTimeout(resolve, 1500)) 
    
    submitStatus.value = 'success'
    form.value = { name: '', email: '', phone: '', cohort: 'Frontend (HTML, CSS, JS, Vue, Nuxt, Tailwind)', message: '' }
  } catch (error) {
    submitStatus.value = 'error'
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <div class="font-body text-slate bg-white pt-20">
    
    <!-- ========================================== -->
    <!-- HERO SECTION -->
    <!-- ========================================== -->
    <section class="border-b border-mist/50 bg-white">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Texte (Gauche) -->
        <div class="lg:col-span-6 space-y-6">
          <p class="inline-flex items-center gap-3 text-xs font-bold text-royal tracking-widest uppercase">
            <span class="w-8 h-[2px] bg-royal"></span>
            IT Training // Career Launch Program
          </p>
          <h1 class="text-4xl lg:text-5xl font-heading font-bold leading-[1.1] text-midnight">
            Practical Foundations for Africa's Next Software Builders.
          </h1>
          <p class="text-lg text-slate/70 leading-relaxed">
            Our IT Fundamentals training program helps young and aspiring developers build real-world skills and gain exposure to the software engineering lifecycle — from frontend interfaces and digital logic to backend architecture and data management.
          </p>
          <div class="flex flex-wrap gap-4 pt-4">
            <a href="#curriculum" class="inline-flex items-center gap-2 bg-midnight text-white px-6 py-3 rounded-sm font-bold hover:bg-royal transition">
              Explore Curriculum <i class="fa-solid fa-arrow-right text-sm"></i>
            </a>
            <a href="#register" class="inline-flex items-center gap-2 border border-mist text-midnight px-6 py-3 rounded-sm font-bold hover:bg-icy transition">
              Inquire About Training
            </a>
          </div>
        </div>

        <!-- Image (Droite) -->
        <div class="lg:col-span-6 relative">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=1000" alt="Students in IT training" class="rounded-sm object-cover h-[400px] w-full shadow-lg" />
          <div class="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur-sm p-3 text-xs font-semibold text-midnight flex justify-between items-center shadow-md">
            <span>Students in practical web lab</span>
            <i class="fa-solid fa-camera text-slate/50"></i>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- CURRICULUM (Modules) -->
    <!-- ========================================== -->
    <section id="curriculum" class="py-16 lg:py-24 bg-white border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5">
        <h2 class="text-3xl font-heading font-bold text-midnight mb-2">Two Progressive Web Engineering Modules.</h2>
        <div class="w-16 h-1 bg-royal mb-12"></div>

        <!-- MODULE FRONTEND -->
        <div class="mb-16">
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-4">
              <span class="bg-royal text-white text-xs font-bold px-3 py-1 rounded-sm uppercase tracking-wider">Frontend</span>
              <h3 class="text-xl font-heading font-bold text-midnight">Structure, Presentation & Interactivity</h3>
            </div>
            <span class="text-xs font-bold text-slate/50 uppercase tracking-widest hidden md:block">Client-Side Foundations</span>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="mod in frontendModules" :key="mod.title" class="border border-mist/60 p-6 rounded-sm bg-white flex flex-col shadow-sm">
              <div class="flex justify-between items-start mb-4">
                <i :class="[mod.icon, 'text-3xl text-royal']"></i>
                <span class="text-[10px] font-bold text-slate/40 uppercase tracking-wider">{{ mod.badge }}</span>
              </div>
              <h4 class="text-lg font-heading font-bold text-midnight mb-2">{{ mod.title }}</h4>
              <p class="text-sm text-slate/70 mb-4 flex-grow">{{ mod.description }}</p>
              <ul class="space-y-2 mt-auto">
                <li v-for="point in mod.points" :key="point" class="text-xs text-slate/80 flex items-start gap-2">
                  <i class="fa-solid fa-check text-royal mt-0.5"></i> {{ point }}
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- MODULE BACKEND -->
        <div>
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-4">
              <span class="bg-midnight text-white text-xs font-bold px-3 py-1 rounded-sm uppercase tracking-wider">Backend</span>
              <h3 class="text-xl font-heading font-bold text-midnight">Backend Logic & Relational Data</h3>
            </div>
            <span class="text-xs font-bold text-slate/50 uppercase tracking-widest hidden md:block">Server-Side & Databases</span>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div 
              v-for="mod in backendModules" 
              :key="mod.title" 
              :class="[
                'border p-6 rounded-sm flex flex-col shadow-sm',
                mod.theme === 'dark' ? 'bg-midnight border-midnight text-white' : 'bg-white border-mist/60 text-slate'
              ]"
            >
              <div class="flex justify-between items-start mb-4">
                <i :class="[mod.icon, 'text-3xl', mod.theme === 'dark' ? 'text-royal' : 'text-royal']"></i>
                <span :class="['text-[10px] font-bold uppercase tracking-wider', mod.theme === 'dark' ? 'text-white/40' : 'text-slate/40']">{{ mod.badge }}</span>
              </div>
              <h4 :class="['text-lg font-heading font-bold mb-2', mod.theme === 'dark' ? 'text-white' : 'text-midnight']">{{ mod.title }}</h4>
              <p :class="['text-sm mb-4 flex-grow', mod.theme === 'dark' ? 'text-white/70' : 'text-slate/70']">{{ mod.description }}</p>
              <ul class="space-y-2 mt-auto">
                <li v-for="point in mod.points" :key="point" :class="['text-xs flex items-start gap-2', mod.theme === 'dark' ? 'text-white/80' : 'text-slate/80']">
                  <i :class="['fa-solid fa-check mt-0.5', mod.theme === 'dark' ? 'text-royal' : 'text-royal']"></i> {{ point }}
                </li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- BÉNÉFICES / MÉTHODE -->
    <!-- ========================================== -->
    <section class="py-16 lg:py-24 bg-icy">
      <div class="mx-auto max-w-7xl px-5 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Image (Gauche) -->
        <div class="lg:col-span-5">
          <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80&w=800" alt="Learning environment" class="rounded-sm object-cover h-[450px] w-full shadow-md" />
        </div>

        <!-- Texte (Droite) -->
        <div class="lg:col-span-7">
          <p class="text-xs font-bold text-royal tracking-widest uppercase mb-2">Learning Methodology</p>
          <h2 class="text-3xl font-heading font-bold text-midnight mb-8">Designed to Turn Curiosity Into Practical Capability.</h2>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
            <div v-for="(benefit, index) in benefits" :key="index" class="bg-white p-5 rounded-sm shadow-sm border border-mist/50">
              <div class="flex items-center gap-3 mb-3">
                <div class="flex h-8 w-8 items-center justify-center rounded-full bg-icy text-royal">
                  <i :class="['fa-solid', benefit[0], 'text-sm']"></i>
                </div>
                <h4 class="font-heading font-bold text-midnight text-sm">{{ benefit[1] }}</h4>
              </div>
              <p class="text-xs text-slate/70 leading-relaxed">{{ benefit[2] }}</p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- FORMULAIRE D'INSCRIPTION -->
    <!-- ========================================== -->
    <section id="register" class="py-16 lg:py-24 bg-white border-t border-mist/50">
      <div class="mx-auto max-w-7xl px-5 grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        
        <!-- Texte (Gauche) -->
        <div class="lg:col-span-5 space-y-6 sticky top-32">
          <p class="text-xs font-bold text-royal tracking-widest uppercase">Enrollment Inquiry</p>
          <h2 class="text-3xl lg:text-4xl font-heading font-bold text-midnight leading-tight">
            Interested in Joining Our Next IT Fundamentals Cohort?
          </h2>
          <p class="text-slate/70 leading-relaxed">
            Send us your details and preferred track (Frontend or Backend). Our team will follow up directly via <a href="mailto:Afatechsolutions@gmail.com" class="text-royal font-semibold hover:underline">Afatechsolutions@gmail.com</a>.
          </p>
        </div>

        <!-- Formulaire (Droite) -->
        <div class="lg:col-span-7">
          <div class="border border-mist/60 bg-white p-8 rounded-sm shadow-sm">
            
            <!-- Messages d'état -->
            <div v-if="submitStatus === 'success'" class="mb-6 p-4 bg-green-50 text-green-700 rounded-sm text-sm flex items-center gap-3">
              <i class="fa-solid fa-circle-check"></i> Votre demande a bien été envoyée.
            </div>
            <div v-if="submitStatus === 'error'" class="mb-6 p-4 bg-red-50 text-red-700 rounded-sm text-sm flex items-center gap-3">
              <i class="fa-solid fa-circle-exclamation"></i> Une erreur est survenue.
            </div>

            <form @submit.prevent="handleSubmit" class="space-y-5">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div>
                  <label class="block text-xs font-bold text-slate mb-2 uppercase tracking-wide">Full Name *</label>
                  <input v-model="form.name" type="text" required placeholder="Your full name" class="w-full border border-mist rounded-sm px-4 py-3 text-sm focus:border-royal focus:ring-1 focus:ring-royal outline-none transition" />
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate mb-2 uppercase tracking-wide">Email Address *</label>
                  <input v-model="form.email" type="email" required placeholder="you@example.com" class="w-full border border-mist rounded-sm px-4 py-3 text-sm focus:border-royal focus:ring-1 focus:ring-royal outline-none transition" />
                </div>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div>
                  <label class="block text-xs font-bold text-slate mb-2 uppercase tracking-wide">Phone Number</label>
                  <input v-model="form.phone" type="tel" placeholder="+257 XX XX XX XX" class="w-full border border-mist rounded-sm px-4 py-3 text-sm focus:border-royal focus:ring-1 focus:ring-royal outline-none transition" />
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate mb-2 uppercase tracking-wide">Desired Track *</label>
                  <select v-model="form.cohort" required class="w-full border border-mist rounded-sm px-4 py-3 text-sm focus:border-royal focus:ring-1 focus:ring-royal outline-none transition bg-white">
                    <option value="Frontend (HTML, CSS, JS, Vue, Nuxt, Tailwind)">Frontend (HTML, CSS, JS, Vue, Nuxt, Tailwind)</option>
                    <option value="Backend (Python, Django, Java, Spring Boot, SQL, MongoDB)">Backend (Python, Django, Java, Spring Boot, SQL, MongoDB)</option>
                    <option value="Full Stack (Frontend + Backend)">Full Stack (Frontend + Backend)</option>
                  </select>
                </div>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate mb-2 uppercase tracking-wide">Learning Goals</label>
                <textarea v-model="form.message" rows="4" placeholder="Tell us about your current background and what you hope to learn..." class="w-full border border-mist rounded-sm px-4 py-3 text-sm focus:border-royal focus:ring-1 focus:ring-royal outline-none transition resize-none"></textarea>
              </div>

              <div class="pt-2">
                <button type="submit" :disabled="isSubmitting" class="w-full md:w-auto inline-flex items-center justify-center gap-2 bg-midnight text-white px-8 py-3 rounded-sm font-bold hover:bg-royal transition disabled:opacity-50 disabled:cursor-not-allowed">
                  <i v-if="isSubmitting" class="fa-solid fa-circle-notch fa-spin"></i>
                  <i v-else class="fa-regular fa-paper-plane"></i>
                  {{ isSubmitting ? 'Sending...' : 'Request Training Info' }}
                </button>
              </div>
            </form>
          </div>
        </div>

      </div>
    </section>

  </div>
</template>