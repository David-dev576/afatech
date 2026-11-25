<script setup>
import ContactForm from '../components/ContactForm.vue'
import { t } from '../i18n'

const phones = [
  { href: 'tel:+25769142998', label: '+257 69 14 29 98' },
  { href: 'tel:+243987950424', label: '+243 98 79 50 424' },
  { href: 'tel:+25766444255', label: '+257 66 44 42 55' },
  { href: 'tel:+25765247128', label: '+257 65 24 71 28' },
]
</script>

<template>
  <section class="bg-icy pb-20 pt-36">
    <div class="mx-auto grid max-w-7xl gap-12 px-5 lg:grid-cols-12">
      <!-- Colonne gauche : coordonnées -->
      <div class="lg:col-span-5">
        <p class="flex items-center gap-3 text-xs font-bold uppercase tracking-wider text-royal">
          <span class="h-px w-8 bg-royal"></span>{{ t('contact.eyebrow') }}
        </p>
        <h1 class="mt-6 font-display text-5xl font-bold leading-[1.05] text-midnight sm:text-6xl">
          {{ t('contact.title') }}
        </h1>
        <p class="mt-6 max-w-md text-lg leading-relaxed text-slate/80">{{ t('contact.intro') }}</p>

        <div class="mt-10 space-y-4">
          <!-- E-mail -->
          <a
            href="mailto:Afatechsolutions@gmail.com"
            class="group flex items-center gap-5 rounded-sm border border-mist/60 bg-white p-5 transition-colors hover:border-royal"
          >
            <span class="flex h-11 w-11 shrink-0 items-center justify-center bg-icy text-royal transition-colors group-hover:bg-royal group-hover:text-white">
              <i class="fa-regular fa-envelope"></i>
            </span>
            <span>
              <span class="block text-xs font-bold uppercase tracking-wide text-slate/50">{{ t('contact.emailLabel') }}</span>
              <span class="block font-display font-bold text-midnight">Afatechsolutions@gmail.com</span>
            </span>
          </a>

          <!-- Téléphones -->
          <div class="rounded-sm border border-mist/60 bg-white p-5">
            <div class="mb-4 flex items-center gap-5">
              <span class="flex h-11 w-11 shrink-0 items-center justify-center bg-icy text-royal">
                <i class="fa-solid fa-phone"></i>
              </span>
              <span class="block text-xs font-bold uppercase tracking-wide text-slate/50">{{ t('contact.phonesLabel') }}</span>
            </div>
            <div class="space-y-2 pl-16">
              <a
                v-for="p in phones"
                :key="p.href"
                :href="p.href"
                class="block font-display font-bold text-midnight transition hover:text-royal"
              >
                {{ p.label }}
              </a>
            </div>
          </div>

          <!-- Fondation -->
          <div class="flex items-center gap-5 rounded-sm border border-mist/60 bg-white p-5">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center bg-icy text-royal">
              <i class="fa-regular fa-calendar-check"></i>
            </span>
            <span>
              <span class="block text-xs font-bold uppercase tracking-wide text-slate/50">{{ t('contact.foundationLabel') }}</span>
              <span class="block font-display font-bold text-midnight">{{ t('contact.foundationValue') }}</span>
            </span>
          </div>
        </div>
      </div>

      <!-- Colonne droite : formulaire -->
      <div class="rounded-sm border border-mist/50 bg-white p-8 shadow-sm lg:col-span-6 lg:col-start-7 lg:p-10">
        <h2 class="font-display text-2xl font-bold text-midnight">{{ t('contact.formTitle') }}</h2>
        <p class="mt-2 text-sm text-slate/60">{{ t('contact.formNote') }}</p>
        <div class="mt-8">
          <ContactForm />
        </div>
      </div>
    </div>
  </section>
</template>