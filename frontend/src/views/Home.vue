<script setup>
import { expertise, defaultServices } from '../content'
import { useList } from '../composables'

const { items: services } = useList('/services/', defaultServices)

const values = [
  ['fa-diagram-project', 'Structured Engineering', 'Clean, maintainable web and mobile systems built on modern standards.'],
  ['fa-users', 'Youth Empowerment', 'Promoting youth involvement in shaping the tech landscape of tomorrow.'],
  ['fa-shield-halved', 'Reliable Infrastructure', 'Managed hosting and IT consulting tailored to operational continuity.'],
  ['fa-earth-africa', 'Continental Vision', 'Steady contribution to Africa\'s long-term technological advancement.'],
]
</script>

<template>
  <div class="font-body text-slate bg-white">
    
    <!-- HERO SECTION -->
    <section 
      class="relative pt-32 lg:pt-40 pb-24 lg:pb-32 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=2000');"
    >
      <div class="absolute inset-0 bg-midnight/85"></div>

      <div class="relative z-10 mx-auto grid max-w-7xl gap-12 px-5 lg:grid-cols-12 items-center">
        
        <!-- Texte (Gauche) -->
        <div class="lg:col-span-7 space-y-6">
          <p class="inline-flex items-center gap-3 text-xs font-bold text-royal tracking-widest uppercase">
            <span class="w-8 h-[2px] bg-royal"></span>
            African Technology & Digital Education
          </p>
          
          <h1 class="text-5xl font-heading font-bold leading-[1.05] text-white sm:text-6xl lg:text-7xl">
            Building Africa's<br>Digital Future<br>Through Technology.
          </h1>
          
          <p class="max-w-xl text-lg leading-relaxed text-white/80">
            We empower businesses, entrepreneurs, and the next generation of African innovators through technology, software engineering, digital education, and intelligent digital solutions.
          </p>
          
          <div class="flex flex-wrap gap-4 pt-4">
            <router-link to="/services" class="inline-flex items-center gap-2 bg-royal text-white px-6 py-3 rounded-sm font-semibold hover:bg-white hover:text-midnight transition">
              Explore Our Solutions <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/about" class="inline-flex items-center gap-2 border border-white/30 text-white px-6 py-3 rounded-sm font-semibold hover:bg-white/10 transition">
              Discover AFA TECH <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
          </div>

          <!-- Stats sous le hero -->
          <div class="flex flex-wrap gap-8 pt-8 border-t border-white/20 mt-8">
            <div>
              <span class="block text-white/50 uppercase text-[10px] font-bold tracking-wider mb-1">Founded</span>
              <span class="text-white text-sm font-semibold">13 Nov 2025</span>
            </div>
            <div>
              <span class="block text-white/50 uppercase text-[10px] font-bold tracking-wider mb-1">Focus</span>
              <span class="text-white text-sm font-semibold">4 Core Disciplines</span>
            </div>
            <div>
              <span class="block text-white/50 uppercase text-[10px] font-bold tracking-wider mb-1">Email</span>
              <a href="mailto:Afatechsolutions@gmail.com" class="text-royal text-sm font-semibold hover:text-white transition">Afatechsolutions@gmail.com</a>
            </div>
            <div>
              <span class="block text-white/50 uppercase text-[10px] font-bold tracking-wider mb-1">Phones</span>
              <div class="text-white text-sm font-semibold flex flex-col gap-1">
                <a href="tel:+25769142998" class="hover:text-royal transition">+257 69 14 29 98</a>
                <a href="tel:+243987950424" class="hover:text-royal transition">+243 98 79 50 424</a>
                <a href="tel:+25766444255" class="hover:text-royal transition">+257 66 44 42 55</a>
                <a href="tel:+25765247128" class="hover:text-royal transition">+257 65 24 71 28</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Encart tech (Droite) -->
        <div class="lg:col-span-5 hidden lg:block">
          <div class="bg-midnight/50 backdrop-blur-md border border-white/10 p-8 rounded-sm shadow-2xl">
            <div class="flex gap-2 mb-6">
              <span class="h-3 w-3 rounded-full bg-red-500"></span>
              <span class="h-3 w-3 rounded-full bg-yellow-500"></span>
              <span class="h-3 w-3 rounded-full bg-green-500"></span>
            </div>
            <pre class="text-sm font-mono text-white/80 leading-relaxed overflow-x-auto"><code><span class="text-royal">const</span> afa = {
  mission: <span class="text-green-400">"former, bâtir, connecter"</span>,
  continent: <span class="text-green-400">"Afrique"</span>,
  stack: [<span class="text-green-400">"Vue"</span>, <span class="text-green-400">"Django"</span>, <span class="text-green-400">"MySQL"</span>],
  ambition: <span class="text-green-400">"Transformation Digitale"</span>
};</code></pre>
          </div>
        </div>

      </div>
    </section>

    <!-- INTRODUCTION SECTION -->
    <section class="bg-icy py-24">
      <div class="mx-auto grid max-w-7xl gap-12 px-5 lg:grid-cols-12 items-center">
        <div class="lg:col-span-5">
          <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80&w=800" alt="Team collaboration" class="rounded-sm object-cover h-[400px] w-full shadow-md" />
        </div>
        <div class="lg:col-span-7 space-y-6">
          <p class="text-xs font-bold text-royal tracking-widest uppercase">ABOUT AFA TECH</p>
          <h2 class="text-3xl font-heading font-bold leading-tight text-midnight sm:text-4xl">
            Grounded in African Innovation, Built for Lasting Technological Impact.
          </h2>
          <p class="text-lg leading-relaxed text-slate/80">
            Founded on 13 November 2025, AFA TECH SOLUTIONS was established to encourage African youth to actively participate in technological development, promote digital education, and help African communities benefit from the opportunities offered by modern technology.
          </p>
          <p class="text-lg leading-relaxed text-slate/80">
            Our vision is to contribute to Africa's technological advancement and digital evolution through accessible, professional, and practical IT training.
          </p>
          <router-link to="/about" class="inline-flex items-center gap-2 text-royal font-bold hover:text-midnight transition pt-2">
            Read Our Full Story <i class="fa-solid fa-arrow-right text-sm"></i>
          </router-link>
        </div>
      </div>
    </section>

    <!-- SERVICES SECTION -->
    <section class="py-24 max-w-7xl mx-auto px-5">
      <div class="flex justify-between items-end mb-12">
        <div>
          <p class="text-xs font-bold text-royal tracking-widest uppercase mb-2">OUR SERVICES</p>
          <h2 class="text-3xl font-heading font-bold text-midnight sm:text-4xl">
            Four Specialized Disciplines<br>Driving Digital Readiness.
          </h2>
        </div>
        <router-link to="/services" class="hidden md:flex text-sm font-bold text-royal hover:text-midnight items-center gap-2 pb-2">
          View All Services <i class="fa-solid fa-arrow-right text-xs"></i>
        </router-link>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Service 1 -->
        <div class="border border-mist/60 rounded-sm overflow-hidden flex flex-col group bg-white">
          <div class="p-8 space-y-4">
            <i class="fa-solid fa-code text-2xl text-royal"></i>
            <h3 class="text-xl font-heading font-bold text-midnight">IT Fundamentals Training</h3>
            <p class="text-slate/70 text-sm leading-relaxed">Structured education in foundational web technologies, from HTML to SQL, designed to empower Africa's youth for real software engineering work.</p>
          </div>
          <div class="mt-auto h-48 overflow-hidden">
             <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=800" alt="Training" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
          </div>
          <div class="p-4 border-t border-mist/60 bg-white">
             <router-link to="/training" class="text-xs font-bold text-royal uppercase tracking-wider hover:text-midnight flex items-center gap-2">Explore Curriculum <i class="fa-solid fa-arrow-right text-xs"></i></router-link>
          </div>
        </div>

        <!-- Service 2 -->
        <div class="border border-mist/60 rounded-sm overflow-hidden flex flex-col group bg-white">
          <div class="p-8 space-y-4">
            <i class="fa-solid fa-laptop-code text-2xl text-royal"></i>
            <h3 class="text-xl font-heading font-bold text-midnight">Website Creation & Management Systems</h3>
            <p class="text-slate/70 text-sm leading-relaxed">Custom corporate websites, operational portals, and content management systems designed to scale your digital architecture and maximize operational efficiency.</p>
          </div>
          <div class="mt-auto h-64 overflow-hidden">
             <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=800" alt="Web Dev" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
          </div>
        </div>

        <!-- Service 3 -->
        <div class="relative rounded-sm overflow-hidden h-[400px] group bg-midnight">
          <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=800" alt="Mobile Dev" class="w-full h-full object-cover opacity-60 group-hover:scale-105 transition duration-700" />
          <div class="absolute inset-0 bg-gradient-to-t from-midnight/90 via-midnight/40 to-transparent flex flex-col justify-end p-8 text-white">
            <i class="fa-solid fa-mobile-screen-button text-2xl mb-4"></i>
            <h3 class="text-2xl font-heading font-bold mb-2">Mobile Application Development</h3>
            <p class="text-sm text-white/80 max-w-sm mb-4">We build native and cross-platform mobile applications for seamless user experiences on Android and iOS.</p>
          </div>
        </div>

        <!-- Service 4 -->
        <div class="border border-mist/60 rounded-sm p-8 flex flex-col justify-center bg-icy group">
          <i class="fa-solid fa-server text-2xl text-royal mb-4"></i>
          <h3 class="text-xl font-heading font-bold text-midnight mb-3">Web Hosting, IT Consulting & Digital Transformation</h3>
          <p class="text-slate/70 text-sm leading-relaxed mb-6">Strategic hosting, technical advisory, and digital transformation consulting for growing organizations.</p>
          <router-link to="/contact" class="text-xs font-bold text-royal uppercase tracking-wider hover:text-midnight flex items-center gap-2">Request Consulting <i class="fa-solid fa-arrow-right text-xs"></i></router-link>
        </div>
      </div>
    </section>

    <!-- EXPERTISE SECTION -->
    <section class="mx-auto max-w-7xl px-5 py-24 border-t border-mist/50">
      <p class="text-xs font-bold text-royal tracking-widest uppercase mb-2">DIGITAL EXPERTISE</p>
      <h2 class="text-3xl font-heading font-bold text-midnight sm:text-4xl mb-8">Our Capabilities</h2>
      
      <p class="font-heading text-3xl font-bold leading-snug text-slate/30 sm:text-5xl lg:text-6xl">
        <template v-for="(e, i) in expertise" :key="e">
          <span class="transition-colors hover:text-royal cursor-default">{{ e }}</span>
          <span v-if="i < expertise.length - 1" class="text-midnight">, </span>
        </template>.
      </p>
    </section>

    <!-- WHY US SECTION -->
    <section class="bg-icy py-24">
      <div class="mx-auto grid max-w-7xl gap-12 px-5 lg:grid-cols-12">
        <div class="lg:col-span-4">
          <p class="text-xs font-bold text-royal tracking-widest uppercase mb-2">WHY AFA TECH SOLUTIONS</p>
          <h2 class="text-3xl font-heading font-bold text-midnight sm:text-4xl leading-tight mb-6">
            Practical Engineering Paired With Local Digital Empowerment.
          </h2>
          <p class="text-slate/70 leading-relaxed text-sm">
            Every engagement combines technical rigor with a clear commitment to building sustainable digital capability across African communities.
          </p>
        </div>
        
        <dl class="grid gap-6 sm:grid-cols-2 lg:col-span-8">
          <div v-for="v in values" :key="v[1]" class="bg-white border border-mist/50 p-6 rounded-sm shadow-sm">
            <dt class="flex items-center gap-3 font-heading font-bold text-midnight text-lg mb-2">
              <i :class="['fa-solid', v[0], 'text-royal']"></i> {{ v[1] }}
            </dt>
            <dd class="text-sm text-slate/70 leading-relaxed">{{ v[2] }}</dd>
          </div>
        </dl>
      </div>
    </section>

    <!-- CTA SECTION -->
    <section class="max-w-7xl mx-auto px-5 py-16">
      <div class="bg-midnight rounded-sm p-10 lg:p-16 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-royal/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
        
        <div class="relative z-10 max-w-2xl">
          <p class="text-xs font-bold text-white/50 tracking-widest uppercase mb-3">PARTNER WITH US</p>
          <h2 class="text-3xl font-heading font-bold text-white sm:text-4xl leading-tight">
            Your Digital Ambition Deserves the Right Technology Partner.
          </h2>
        </div>
        
        <router-link to="/contact" class="relative z-10 bg-royal text-white px-8 py-4 rounded-sm font-bold hover:bg-white hover:text-midnight transition whitespace-nowrap flex items-center gap-2">
          Start a Conversation <i class="fa-solid fa-arrow-right text-sm"></i>
        </router-link>
      </div>
    </section>

  </div>
</template>