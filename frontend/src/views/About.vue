<script setup>
// Les données statiques pour les valeurs et objectifs
const strategicObjectives = [
  ['fa-book-open', 'Accessible Digital Education', 'Promoting technological literacy, coding skills, and digital empowerment.'],
  ['fa-laptop-code', 'Modern Software Delivery', 'Building practical, maintainable web and mobile applications tailored to real needs.'],
  ['fa-arrow-trend-up', 'Guided Digital Transformation', 'Supporting organizations in adopting digital tools effectively.']
]

const coreValues = [
  ['fa-lightbulb', 'Integrity', 'Transparent communication, honesty, and responsible delivery.'],
  ['fa-microchip', 'Technical Rigor', 'Clean, maintainable code, modern standards, and sustainable architecture.'],
  ['fa-people-group', 'Community Impact', 'Work that creates lasting value within African communities.'],
  ['fa-graduation-cap', 'Continuous Learning', 'An engineering culture that stays current and shares knowledge.']
]
</script>

<template>
  <div class="font-body text-slate bg-white pt-20">
    
    <!-- ========================================== -->
    <!-- HERO SECTION -->
    <!-- ========================================== -->
    <section class="border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24">
        <!-- En-tête texte -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-end mb-12">
          <div class="lg:col-span-8">
            <p class="inline-flex items-center gap-3 text-xs font-bold text-royal tracking-widest uppercase mb-4">
              <span class="w-8 h-[2px] bg-royal"></span>
              About AFA TECH SOLUTIONS
            </p>
            <h1 class="text-4xl lg:text-6xl font-heading font-bold leading-[1.1] text-midnight">
              Purpose-Driven Technology<br>for Africa's Next Chapter.
            </h1>
          </div>
          <div class="lg:col-span-4 lg:pb-2">
            <p class="text-slate/70 leading-relaxed border-l-2 border-mist pl-6 text-sm lg:text-base">
              Established on 13 November 2025 to bridge digital education, software engineering, and community impact across the continent.
            </p>
          </div>
        </div>

        <!-- Grande Image -->
        <div class="relative w-full h-[300px] lg:h-[500px] rounded-sm overflow-hidden shadow-lg">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=2000" alt="African Tech Team collaborating" class="w-full h-full object-cover" />
          <!-- Légende en bas de l'image -->
          <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/80 to-transparent p-6 flex flex-col md:flex-row justify-between items-start md:items-end text-white gap-4">
            <p class="text-sm font-semibold max-w-xs">Fostering collaboration, skills, and African tech excellence.</p>
            <p class="text-xs text-white/70">Image for illustrative purposes only. Actual team photos coming soon.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- COMPANY HISTORY -->
    <!-- ========================================== -->
    <section class="bg-white py-20 lg:py-24 border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 grid grid-cols-1 lg:grid-cols-12 gap-12">
        
        <!-- Titre (Gauche) -->
        <div class="lg:col-span-5 space-y-6">
          <p class="text-xs font-bold text-royal tracking-widest uppercase">Company History</p>
          <h2 class="text-3xl lg:text-4xl font-heading font-bold leading-tight text-midnight">
            Born From a Conviction in Youth & Technology.
          </h2>
          <div class="border border-mist/60 p-6 rounded-sm bg-white shadow-sm max-w-sm">
            <p class="text-xs font-bold text-slate/50 uppercase tracking-wider mb-1">Founded on</p>
            <p class="text-midnight text-lg font-bold">13 November 2025</p>
          </div>
        </div>

        <!-- Texte (Droite) -->
        <div class="lg:col-span-7 space-y-6 text-slate/80 leading-relaxed">
          <p>
            AFA TECH SOLUTIONS was founded on 13 November 2025 with a clear mission: to move African communities from passive technology adoption to active creation, ownership, and technical leadership.
          </p>
          <p>
            Recognizing that digital transformation requires more than just tools, we built AFA TECH as a multi-disciplinary hub dedicated to delivering education, web, mobile, and consulting services. We strive to provide young people with the tools they need to build software.
          </p>
          
          <!-- 2 mini-cards sous le texte -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
            <div class="flex gap-4 items-start">
              <i class="fa-solid fa-compass-drafting text-royal text-xl mt-1"></i>
              <div>
                <h4 class="font-heading font-bold text-midnight mb-1">Engineering Practice</h4>
                <p class="text-sm">Focused on building durable, scalable applications and managed hosting.</p>
              </div>
            </div>
            <div class="flex gap-4 items-start">
              <i class="fa-solid fa-earth-africa text-royal text-xl mt-1"></i>
              <div>
                <h4 class="font-heading font-bold text-midnight mb-1">Educational Commitment</h4>
                <p class="text-sm">Empowering through structured IT training: HTML, CSS, JavaScript, PHP, and SQL.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- MISSION & VISION (Blocs Asymétriques) -->
    <!-- ========================================== -->
    <section class="bg-icy py-20 lg:py-24 border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
        
        <!-- Mission (Blanc) -->
        <div class="bg-white p-8 lg:p-12 rounded-sm shadow-sm border border-mist/50 flex flex-col">
          <div class="flex items-center justify-between mb-8">
            <p class="text-xs font-bold text-slate/50 tracking-widest uppercase">Our Mission</p>
            <div class="w-10 h-10 bg-icy rounded-sm flex items-center justify-center text-royal">
              <i class="fa-solid fa-bullseye"></i>
            </div>
          </div>
          <h3 class="text-2xl lg:text-3xl font-heading font-bold text-midnight leading-tight mb-4">
            Empowering Youth & Communities Through Digital Education.
          </h3>
          <p class="text-slate/70 leading-relaxed mt-auto">
            AFA TECH SOLUTIONS was established to encourage African youth to participate in technological development, promote digital education, and help African communities benefit from the opportunities offered by modern technology.
          </p>
        </div>

        <!-- Vision (Bleu Nuit) -->
        <div class="bg-midnight p-8 lg:p-12 rounded-sm shadow-xl relative overflow-hidden flex flex-col">
          <!-- Halo décoratif -->
          <div class="absolute top-0 right-0 w-48 h-48 bg-royal/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
          
          <div class="relative z-10 flex items-center justify-between mb-8">
            <p class="text-xs font-bold text-white/50 tracking-widest uppercase">Our Vision</p>
            <div class="w-10 h-10 bg-white/10 rounded-sm flex items-center justify-center text-white">
              <i class="fa-solid fa-eye"></i>
            </div>
          </div>
          <h3 class="relative z-10 text-2xl lg:text-3xl font-heading font-bold text-white leading-tight mb-4">
            Contributing to Africa's Digital Transformation.
          </h3>
          <p class="relative z-10 text-white/70 leading-relaxed mt-auto">
            To contribute to Africa's technological advancement and participate directly in the continent's digital transformation by building dependable software and cultivating the next generation of engineers.
          </p>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- OBJECTIFS & VALEURS -->
    <!-- ========================================== -->
    <section class="bg-white py-20 lg:py-24 border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20">
        
        <!-- Objectifs (Gauche - 5 cols) -->
        <div class="lg:col-span-5 space-y-8">
          <div>
            <p class="text-xs font-bold text-slate/50 tracking-widest uppercase mb-2">Strategic Objectives</p>
            <h2 class="text-2xl font-heading font-bold text-midnight">What We Work Toward Every Day</h2>
          </div>
          
          <ul class="space-y-6">
            <li v-for="(obj, index) in strategicObjectives" :key="index" class="flex gap-4">
              <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-sm bg-icy text-royal">
                <i :class="['fa-solid', obj[0]]"></i>
              </div>
              <div>
                <h4 class="font-heading font-bold text-midnight mb-1">{{ obj[1] }}</h4>
                <p class="text-sm text-slate/70 leading-relaxed">{{ obj[2] }}</p>
              </div>
            </li>
          </ul>
        </div>

        <!-- Valeurs (Droite - 7 cols) -->
        <div class="lg:col-span-7 bg-icy p-8 lg:p-10 rounded-sm border border-mist/50">
          <p class="text-xs font-bold text-slate/50 tracking-widest uppercase mb-2">Core Values</p>
          <h2 class="text-2xl font-heading font-bold text-midnight mb-8">Principles Behind Our Craft</h2>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-10">
            <div v-for="(val, index) in coreValues" :key="index">
              <div class="flex items-center gap-3 mb-2">
                <i :class="['fa-solid', val[0], 'text-royal']"></i>
                <h4 class="font-heading font-bold text-midnight">{{ val[1] }}</h4>
              </div>
              <p class="text-sm text-slate/70 leading-relaxed">{{ val[2] }}</p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- INVESTISSEMENT / CTA FINAL -->
    <!-- ========================================== -->
    <section class="bg-icy py-20 lg:py-24">
      <div class="mx-auto max-w-7xl px-5">
        
        <!-- Section Image & Texte -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-20">
          <div class="space-y-6">
            <p class="text-xs font-bold text-royal tracking-widest uppercase">Continental Commitment</p>
            <h2 class="text-3xl lg:text-4xl font-heading font-bold leading-tight text-midnight">
              Investing in Africa's<br>Digital Self-Reliance.
            </h2>
            <p class="text-slate/70 leading-relaxed">
              Africa's digital future will be shaped by engineers, educators, and entrepreneurs who understand local contexts firsthand. Through practical training and reliable software systems, AFA TECH SOLUTIONS is committed to making modern technology accessible and sustainable.
            </p>
            <router-link to="/formation" class="inline-flex items-center gap-2 text-royal font-bold hover:text-midnight transition pt-2">
              Explore Our Training Curriculum <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
          </div>
          <div class="relative h-[300px] lg:h-[400px] rounded-sm overflow-hidden shadow-lg">
            <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80&w=1000" alt="Collaboration" class="w-full h-full object-cover" />
          </div>
        </div>

        <!-- Bloc CTA Bleu Nuit -->
        <div class="bg-midnight rounded-sm p-10 lg:p-16 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
          <!-- Halo -->
          <div class="absolute top-0 right-0 w-64 h-64 bg-royal/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
          
          <div class="relative z-10 max-w-2xl">
            <p class="text-xs font-bold text-white/50 tracking-widest uppercase mb-3">Partner With Us</p>
            <h2 class="text-3xl font-heading font-bold text-white sm:text-4xl leading-tight">
              Your Digital Ambition Deserves the Right Technology Partner.
            </h2>
          </div>
          
          <router-link to="/contact" class="relative z-10 bg-royal text-white px-8 py-4 rounded-sm font-bold hover:bg-white hover:text-midnight transition whitespace-nowrap flex items-center gap-2">
            Start a Conversation <i class="fa-solid fa-arrow-right text-sm"></i>
          </router-link>
        </div>

      </div>
    </section>

  </div>
</template>