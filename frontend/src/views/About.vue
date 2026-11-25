<script setup>
import { t } from '../i18n'

const values = ['about.val1', 'about.val2', 'about.val3', 'about.val4']
const valueIcons = ['fa-lightbulb', 'fa-microchip', 'fa-people-group', 'fa-graduation-cap']
const objectives = ['about.obj1', 'about.obj2', 'about.obj3']
const objectiveIcons = ['fa-book-open', 'fa-laptop-code', 'fa-arrow-trend-up']
</script>

<template>
  <div class="font-body text-slate bg-white pt-20">

    <!-- HERO -->
    <section class="border-b border-mist/50">
      <div class="mx-auto max-w-7xl px-5 py-16 lg:py-24">
        <div class="mb-12 grid grid-cols-1 items-end gap-8 lg:grid-cols-12">
          <div class="lg:col-span-8">
            <p class="mb-4 inline-flex items-center gap-3 text-xs font-bold uppercase tracking-widest text-royal">
              <span class="h-[2px] w-8 bg-royal"></span>{{ t('about.eyebrow') }}
            </p>
            <h1 class="font-display text-4xl font-bold leading-[1.1] text-midnight lg:text-6xl">
              {{ t('about.title1') }}<br>{{ t('about.title2') }}
            </h1>
          </div>
          <div class="lg:col-span-4 lg:pb-2">
            <p class="border-l-2 border-mist pl-6 text-sm leading-relaxed text-slate/70 lg:text-base">{{ t('about.lead') }}</p>
          </div>
        </div>

        <div class="relative h-[300px] w-full overflow-hidden rounded-sm shadow-lg lg:h-[500px]">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=2000" :alt="t('about.imgAlt')" class="h-full w-full object-cover" />
          <div class="absolute bottom-0 left-0 right-0 flex flex-col items-start justify-between gap-4 bg-gradient-to-t from-black/80 to-transparent p-6 text-white md:flex-row md:items-end">
            <p class="max-w-xs text-sm font-semibold">{{ t('about.imgCaption') }}</p>
            <p class="text-xs text-white/70">{{ t('about.imgNote') }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- HISTOIRE -->
    <section class="border-b border-mist/50 bg-white py-20 lg:py-24">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-12 px-5 lg:grid-cols-12">
        <div class="space-y-6 lg:col-span-5">
          <p class="text-xs font-bold uppercase tracking-widest text-royal">{{ t('about.histLabel') }}</p>
          <h2 class="font-display text-3xl font-bold leading-tight text-midnight lg:text-4xl">{{ t('about.histTitle') }}</h2>
          <div class="max-w-sm rounded-sm border border-mist/60 bg-white p-6 shadow-sm">
            <p class="mb-1 text-xs font-bold uppercase tracking-wider text-slate/50">{{ t('about.foundedOn') }}</p>
            <p class="text-lg font-bold text-midnight">{{ t('about.foundedValue') }}</p>
          </div>
        </div>

        <div class="space-y-6 leading-relaxed text-slate/80 lg:col-span-7">
          <p>{{ t('about.histP1') }}</p>
          <p>{{ t('about.histP2') }}</p>
          <div class="grid grid-cols-1 gap-6 pt-4 md:grid-cols-2">
            <div class="flex items-start gap-4">
              <i class="fa-solid fa-compass-drafting mt-1 text-xl text-royal"></i>
              <div>
                <h4 class="mb-1 font-display font-bold text-midnight">{{ t('about.card1Title') }}</h4>
                <p class="text-sm">{{ t('about.card1Text') }}</p>
              </div>
            </div>
            <div class="flex items-start gap-4">
              <i class="fa-solid fa-earth-africa mt-1 text-xl text-royal"></i>
              <div>
                <h4 class="mb-1 font-display font-bold text-midnight">{{ t('about.card2Title') }}</h4>
                <p class="text-sm">{{ t('about.card2Text') }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- MISSION ET VISION -->
    <section class="border-b border-mist/50 bg-icy py-20 lg:py-24">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-5 lg:grid-cols-2 lg:gap-12">
        <div class="flex flex-col rounded-sm border border-mist/50 bg-white p-8 shadow-sm lg:p-12">
          <div class="mb-8 flex items-center justify-between">
            <p class="text-xs font-bold uppercase tracking-widest text-slate/50">{{ t('about.missionLabel') }}</p>
            <div class="flex h-10 w-10 items-center justify-center rounded-sm bg-icy text-royal">
              <i class="fa-solid fa-bullseye"></i>
            </div>
          </div>
          <h3 class="mb-4 font-display text-2xl font-bold leading-tight text-midnight lg:text-3xl">{{ t('about.missionTitle') }}</h3>
          <p class="mt-auto leading-relaxed text-slate/70">{{ t('about.missionText') }}</p>
        </div>

        <div class="relative flex flex-col overflow-hidden rounded-sm bg-midnight p-8 shadow-xl lg:p-12">
          <div class="absolute right-0 top-0 h-48 w-48 -translate-y-1/2 translate-x-1/3 rounded-full bg-royal/20 blur-3xl"></div>
          <div class="relative z-10 mb-8 flex items-center justify-between">
            <p class="text-xs font-bold uppercase tracking-widest text-white/50">{{ t('about.visionLabel') }}</p>
            <div class="flex h-10 w-10 items-center justify-center rounded-sm bg-white/10 text-white">
              <i class="fa-solid fa-eye"></i>
            </div>
          </div>
          <h3 class="relative z-10 mb-4 font-display text-2xl font-bold leading-tight text-white lg:text-3xl">{{ t('about.visionTitle') }}</h3>
          <p class="relative z-10 mt-auto leading-relaxed text-white/70">{{ t('about.visionText') }}</p>
        </div>
      </div>
    </section>

    <!-- OBJECTIFS ET VALEURS -->
    <section class="border-b border-mist/50 bg-white py-20 lg:py-24">
      <div class="mx-auto grid max-w-7xl grid-cols-1 gap-12 px-5 lg:grid-cols-12 lg:gap-20">
        <div class="space-y-8 lg:col-span-5">
          <div>
            <p class="mb-2 text-xs font-bold uppercase tracking-widest text-slate/50">{{ t('about.objLabel') }}</p>
            <h2 class="font-display text-2xl font-bold text-midnight">{{ t('about.objTitle') }}</h2>
          </div>
          <ul class="space-y-6">
            <li v-for="(o, i) in objectives" :key="o" class="flex gap-4">
              <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-sm bg-icy text-royal">
                <i :class="['fa-solid', objectiveIcons[i]]"></i>
              </div>
              <div>
                <h4 class="mb-1 font-display font-bold text-midnight">{{ t(`${o}Title`) }}</h4>
                <p class="text-sm leading-relaxed text-slate/70">{{ t(`${o}Text`) }}</p>
              </div>
            </li>
          </ul>
        </div>

        <div class="rounded-sm border border-mist/50 bg-icy p-8 lg:col-span-7 lg:p-10">
          <p class="mb-2 text-xs font-bold uppercase tracking-widest text-slate/50">{{ t('about.valLabel') }}</p>
          <h2 class="mb-8 font-display text-2xl font-bold text-midnight">{{ t('about.valTitle') }}</h2>
          <div class="grid grid-cols-1 gap-x-8 gap-y-10 sm:grid-cols-2">
            <div v-for="(v, i) in values" :key="v">
              <div class="mb-2 flex items-center gap-3">
                <i :class="['fa-solid', valueIcons[i], 'text-royal']"></i>
                <h4 class="font-display font-bold text-midnight">{{ t(`${v}Title`) }}</h4>
              </div>
              <p class="text-sm leading-relaxed text-slate/70">{{ t(`${v}Text`) }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ENGAGEMENT ET CTA -->
    <section class="bg-icy py-20 lg:py-24">
      <div class="mx-auto max-w-7xl px-5">
        <div class="mb-20 grid grid-cols-1 items-center gap-12 lg:grid-cols-2">
          <div class="space-y-6">
            <p class="text-xs font-bold uppercase tracking-widest text-royal">{{ t('about.contLabel') }}</p>
            <h2 class="font-display text-3xl font-bold leading-tight text-midnight lg:text-4xl">
              {{ t('about.contTitle1') }}<br>{{ t('about.contTitle2') }}
            </h2>
            <p class="leading-relaxed text-slate/70">{{ t('about.contText') }}</p>
            <router-link to="/formation" class="inline-flex items-center gap-2 pt-2 font-bold text-royal transition hover:text-midnight">
              {{ t('about.contLink') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
          </div>
          <div class="relative h-[300px] overflow-hidden rounded-sm shadow-lg lg:h-[400px]">
            <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80&w=1000" :alt="t('about.contImgAlt')" class="h-full w-full object-cover" />
          </div>
        </div>

        <div class="relative flex flex-col items-center justify-between gap-8 overflow-hidden rounded-sm bg-midnight p-10 md:flex-row lg:p-16">
          <div class="absolute right-0 top-0 h-64 w-64 -translate-y-1/2 translate-x-1/3 rounded-full bg-royal/20 blur-3xl"></div>
          <div class="relative z-10 max-w-2xl">
            <p class="mb-3 text-xs font-bold uppercase tracking-widest text-white/50">{{ t('common.partner') }}</p>
            <h2 class="font-display text-3xl font-bold leading-tight text-white sm:text-4xl">{{ t('common.ctaTitle') }}</h2>
          </div>
          <router-link to="/contact" class="relative z-10 flex items-center gap-2 whitespace-nowrap rounded-sm bg-royal px-8 py-4 font-bold text-white transition hover:bg-white hover:text-midnight">
            {{ t('common.ctaButton') }} <i class="fa-solid fa-arrow-right text-sm"></i>
          </router-link>
        </div>
      </div>
    </section>

  </div>
</template>