<script setup>
import ContactForm from '../components/ContactForm.vue'
</script>

<template>
  <section class="bg-icy pb-20 pt-36">
    <div class="mx-auto grid max-w-7xl gap-12 px-5 lg:grid-cols-12">
      
      <!-- Colonne Gauche : Infos -->
      <div class="lg:col-span-5">
        <p class="flex items-center gap-3 text-xs font-bold uppercase tracking-wider text-royal">
          <span class="h-px w-8 bg-royal"></span>Start a conversation
        </p>
        <h1 class="mt-6 text-5xl font-heading font-bold leading-[1.05] text-midnight sm:text-6xl">
          Let's build something meaningful together.
        </h1>
        <p class="mt-6 max-w-md text-lg leading-relaxed text-slate/80">
          Reach out to discuss custom web systems, mobile applications, IT consulting, or enrolling in our IT Fundamentals Training.
        </p>

        <div class="mt-10 space-y-4">
          
          <!-- Email Officiel -->
          <a href="mailto:Afatechsolutions@gmail.com" class="flex items-center gap-5 border border-mist/60 bg-white p-5 rounded-sm transition-colors hover:border-royal group">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center bg-icy text-royal group-hover:bg-royal group-hover:text-white transition-colors">
              <i class="fa-regular fa-envelope"></i>
            </span>
            <span>
              <span class="block text-xs font-bold uppercase tracking-wide text-slate/50">Official email</span>
              <span class="block font-heading font-bold text-midnight">Afatechsolutions@gmail.com</span>
            </span>
          </a>

          <!-- Téléphones -->
          <div class="border border-mist/60 bg-white p-5 rounded-sm">
            <div class="flex items-center gap-5 mb-4">
              <span class="flex h-11 w-11 shrink-0 items-center justify-center bg-icy text-royal">
                <i class="fa-solid fa-phone"></i>
              </span>
              <span class="block text-xs font-bold uppercase tracking-wide text-slate/50">Phone numbers</span>
            </div>
            <div class="space-y-2 pl-16">
              <a href="tel:+25769142998" class="block font-heading font-bold text-midnight hover:text-royal transition">+257 69 14 29 98</a>
              <a href="tel:+243987950424" class="block font-heading font-bold text-midnight hover:text-royal transition">+243 98 79 50 424</a>
              <a href="tel:+25766444255" class="block font-heading font-bold text-midnight hover:text-royal transition">+257 66 44 42 55</a>
              <a href="tel:+25765247128" class="block font-heading font-bold text-midnight hover:text-royal transition">+257 65 24 71 28</a>
            </div>
          </div>

          <!-- Fondation -->
          <div class="flex items-center gap-5 border border-mist/60 bg-white p-5 rounded-sm">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center bg-icy text-royal">
              <i class="fa-regular fa-calendar-check"></i>
            </span>
            <span>
              <span class="block text-xs font-bold uppercase tracking-wide text-slate/50">Company foundation</span>
              <span class="block font-heading font-bold text-midnight">13 November 2025</span>
            </span>
          </div>

        </div>
      </div>

      <!-- Colonne Droite : Formulaire -->
      <div class="bg-white p-8 shadow-sm lg:col-span-6 lg:col-start-7 lg:p-10 rounded-sm border border-mist/50">
        <h2 class="font-heading text-2xl font-bold text-midnight">Send us a message</h2>
        <p class="mt-2 text-sm text-slate/60">Fields marked with an asterisk are required.</p>
        <div class="mt-8">
          <ContactForm />
        </div>
      </div>
      
    </div>
  </section>
</template>