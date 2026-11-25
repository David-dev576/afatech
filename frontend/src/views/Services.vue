<script setup>
import { t } from '../i18n'
</script>

<template>
  <div class="font-body text-slate bg-white pt-20">

    <!-- HERO -->
    <section class="border-b border-mist/50">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-end gap-10 px-5 py-16 lg:grid-cols-12 lg:py-24">
        <div class="lg:col-span-7">
          <p class="mb-4 inline-flex items-center gap-3 text-xs font-bold uppercase tracking-widest text-royal">
            <span class="h-[2px] w-8 bg-royal"></span>{{ t('services.eyebrow') }}
          </p>
          <h1 class="font-display text-4xl font-bold leading-[1.1] text-midnight lg:text-6xl">
            {{ t('services.title1') }}<br>{{ t('services.title2') }}
          </h1>
        </div>
        <div class="lg:col-span-5 lg:pb-2">
          <p class="border-l-2 border-mist pl-6 text-lg leading-relaxed text-slate/70">{{ t('services.lead') }}</p>
        </div>
      </div>
    </section>

    <!-- SERVICE 01 -->
    <section class="border-b border-mist/50">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-16 lg:grid-cols-2 lg:gap-20 lg:py-24">
        <div class="relative order-2 lg:order-1">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=1000" :alt="t('services.s1Alt')" class="h-[400px] w-full rounded-sm object-cover shadow-lg" />
        </div>
        <div class="order-1 space-y-6 lg:order-2">
          <p class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-royal">
            <i class="fa-solid fa-code"></i> {{ t('services.s1Tag') }}
          </p>
          <h2 class="font-display text-3xl font-bold leading-tight text-midnight lg:text-4xl">{{ t('services.s1Title') }}</h2>
          <p class="leading-relaxed text-slate/70">{{ t('services.s1Text') }}</p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/formation" class="inline-flex items-center gap-2 rounded-sm bg-royal px-6 py-3 font-semibold text-white transition hover:bg-midnight">
              {{ t('common.learnMore') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm border border-mist px-6 py-3 font-semibold text-midnight transition hover:bg-icy">
              {{ t('common.contactUs') }}
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- SERVICE 02 -->
    <section class="bg-midnight text-white">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-16 lg:grid-cols-2 lg:gap-20 lg:py-24">
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-royal">
            <i class="fa-solid fa-laptop-code"></i> {{ t('services.s2Tag') }}
          </p>
          <h2 class="font-display text-3xl font-bold leading-tight text-white lg:text-4xl">{{ t('services.s2Title') }}</h2>
          <p class="leading-relaxed text-white/70">{{ t('services.s2Text') }}</p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm bg-royal px-6 py-3 font-semibold text-white transition hover:bg-white hover:text-midnight">
              {{ t('common.learnMore') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm border border-white/30 px-6 py-3 font-semibold text-white transition hover:bg-white/10">
              {{ t('common.contactUs') }}
            </router-link>
          </div>
        </div>
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=1000" :alt="t('services.s2Alt')" class="h-[400px] w-full rounded-sm object-cover shadow-2xl" />
        </div>
      </div>
    </section>

    <!-- SERVICE 03 -->
    <section class="border-b border-mist/50">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-16 lg:grid-cols-2 lg:gap-20 lg:py-24">
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=1000" :alt="t('services.s3Alt')" class="h-[400px] w-full rounded-sm object-cover shadow-lg" />
        </div>
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-royal">
            <i class="fa-solid fa-mobile-screen-button"></i> {{ t('services.s3Tag') }}
          </p>
          <h2 class="font-display text-3xl font-bold leading-tight text-midnight lg:text-4xl">{{ t('services.s3Title') }}</h2>
          <p class="leading-relaxed text-slate/70">{{ t('services.s3Text') }}</p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm bg-royal px-6 py-3 font-semibold text-white transition hover:bg-midnight">
              {{ t('common.learnMore') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm border border-mist px-6 py-3 font-semibold text-midnight transition hover:bg-icy">
              {{ t('common.contactUs') }}
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- SERVICE 04 -->
    <section class="border-b border-mist/50">
      <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-16 lg:grid-cols-2 lg:gap-20 lg:py-24">
        <div class="space-y-6">
          <p class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-royal">
            <i class="fa-solid fa-server"></i> {{ t('services.s4Tag') }}
          </p>
          <h2 class="font-display text-3xl font-bold leading-tight text-midnight lg:text-4xl">{{ t('services.s4Title') }}</h2>
          <p class="leading-relaxed text-slate/70">{{ t('services.s4Text') }}</p>
          <div class="flex flex-wrap gap-3 pt-4">
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm bg-royal px-6 py-3 font-semibold text-white transition hover:bg-midnight">
              {{ t('common.learnMore') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/contact" class="inline-flex items-center gap-2 rounded-sm border border-mist px-6 py-3 font-semibold text-midnight transition hover:bg-icy">
              {{ t('common.contactUs') }}
            </router-link>
          </div>
        </div>
        <div class="relative">
          <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=1000" :alt="t('services.s4Alt')" class="h-[400px] w-full rounded-sm object-cover shadow-lg" />
        </div>
      </div>
    </section>

  </div>
</template>