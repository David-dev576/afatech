<script setup>
// Vous pouvez importer vos données dynamiques ici si nécessaire
</script>

<template>
  <div class="font-body text-slate bg-white pt-20">
    
    <!-- ========================================== -->
    <!-- HERO SECTION DE LA PAGE SERVICES -->
    <!-- ========================================== -->
    <section class="border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-12 gap-10 items-end">
        
        <!-- Titre (Gauche) -->
        <div class="lg:col-span-7">
          <p class="inline-flex items-center gap-3 text-xs font-bold text-royal tracking-widest uppercase mb-4">
            <span class="w-8 h-[2px] bg-royal"></span>
            Capabilities & Digital Expertise
          </p>
          <h1 class="text-4xl lg:text-6xl font-heading font-bold leading-[1.1] text-midnight">
            Technology Services<br>Built for African Growth.
          </h1>
        </div>
        
        <!-- Description (Droite) -->
        <div class="lg:col-span-5 lg:pb-2">
          <p class="text-lg text-slate/70 leading-relaxed border-l-2 border-mist pl-6">
            From foundational IT training for young developers to production web platforms, mobile apps, and cloud infrastructure consulting.
          </p>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SERVICE 01 : IT Fundamentals Training -->
    <!-- ========================================== -->
    <section class="border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
        <!-- Image (Gauche) -->
        <div class="order-2 lg:order-1 relative">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=1000" alt="IT Training" class="rounded-sm object-cover h-[400px] w-full shadow-lg" />
        </div>
        
        <!-- Texte (Droite) -->
        <div class="order-1 lg:order-2 space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold text-royal tracking-widest uppercase">
            <i class="fa-solid fa-code"></i> Service 01 // Éducation
          </p>
          <h2 class="text-3xl lg:text-4xl font-heading font-bold text-midnight leading-tight">
            IT Fundamentals Training
          </h2>
          <p class="text-slate/70 leading-relaxed">
            Practical, structured training in programming, covering both web and database technologies, designed to empower Africa's youth with real software engineering skills.
          </p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/formation" class="inline-flex items-center gap-2 bg-royal text-white px-6 py-3 rounded-sm font-semibold hover:bg-midnight transition">
              Learn More <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 border border-mist text-midnight px-6 py-3 rounded-sm font-semibold hover:bg-icy transition">
              Contact Us
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SERVICE 02 : Website Creation (Fond Bleu Nuit) -->
    <!-- ========================================== -->
    <section class="bg-midnight text-white">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
        <!-- Texte (Gauche) -->
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold text-royal tracking-widest uppercase">
            <i class="fa-solid fa-laptop-code"></i> Service 02 // Ingénierie Web
          </p>
          <h2 class="text-3xl lg:text-4xl font-heading font-bold text-white leading-tight">
            Website Creation & Management Systems
          </h2>
          <p class="text-white/70 leading-relaxed">
            Custom corporate websites, administrative dashboards, and content management systems engineered with modern frontend frameworks and secure backend APIs.
          </p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/contact" class="inline-flex items-center gap-2 bg-royal text-white px-6 py-3 rounded-sm font-semibold hover:bg-white hover:text-midnight transition">
              Learn More <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 border border-white/30 text-white px-6 py-3 rounded-sm font-semibold hover:bg-white/10 transition">
              Contact Us
            </router-link>
          </div>
        </div>
        
        <!-- Image (Droite) -->
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=1000" alt="Web Development" class="rounded-sm object-cover h-[400px] w-full shadow-2xl" />
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SERVICE 03 : Mobile Application Development -->
    <!-- ========================================== -->
    <section class="border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
        <!-- Image (Gauche) -->
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=1000" alt="Mobile App Development" class="rounded-sm object-cover h-[400px] w-full shadow-lg" />
        </div>
        
        <!-- Texte (Droite) -->
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold text-royal tracking-widest uppercase">
            <i class="fa-solid fa-mobile-screen-button"></i> Service 03 // Produits Mobiles
          </p>
          <h2 class="text-3xl lg:text-4xl font-heading font-bold text-midnight leading-tight">
            Mobile Application Development
          </h2>
          <p class="text-slate/70 leading-relaxed">
            Intuitive Android and iOS platforms mobile applications designed around user needs, performance, and offline-first capabilities for low-bandwidth environments.
          </p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/contact" class="inline-flex items-center gap-2 bg-royal text-white px-6 py-3 rounded-sm font-semibold hover:bg-midnight transition">
              Learn More <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 border border-mist text-midnight px-6 py-3 rounded-sm font-semibold hover:bg-icy transition">
              Contact Us
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SERVICE 04 : Web Hosting & Consulting -->
    <!-- ========================================== -->
    <section class="border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">
        <!-- Texte (Gauche) -->
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold text-royal tracking-widest uppercase">
            <i class="fa-solid fa-server"></i> Service 04 // Infrastructure & Stratégie
          </p>
          <h2 class="text-3xl lg:text-4xl font-heading font-bold text-midnight leading-tight">
            Web Hosting, IT Consulting & Digital Transformation
          </h2>
          <p class="text-slate/70 leading-relaxed">
            Dependable web hosting environments, technical architecture consulting, and end-to-end digital transformation guidance for businesses and institutions.
          </p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/contact" class="inline-flex items-center gap-2 bg-royal text-white px-6 py-3 rounded-sm font-semibold hover:bg-midnight transition">
              Learn More <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 border border-mist text-midnight px-6 py-3 rounded-sm font-semibold hover:bg-icy transition">
              Contact Us
            </router-link>
          </div>
        </div>
        
        <!-- Image (Droite) -->
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=1000" alt="IT Consulting" class="rounded-sm object-cover h-[400px] w-full shadow-lg" />
        </div>
      </div>
    </section>

  </div>
</template>