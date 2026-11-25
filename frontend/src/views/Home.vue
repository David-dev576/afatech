<script setup>
import { t } from '../i18n'

const expertise = ['home.exp1', 'home.exp2', 'home.exp3', 'home.exp4', 'home.exp5', 'home.exp6', 'home.exp7', 'home.exp8']

// Préfixe des clés : home.v1Title / home.v1Text
const values = [
  ['fa-diagram-project', 'home.v1'],
  ['fa-users', 'home.v2'],
  ['fa-shield-halved', 'home.v3'],
  ['fa-earth-africa', 'home.v4'],
]

const phones = [
  { href: 'tel:+25769142998', label: '+257 69 14 29 98' },
  { href: 'tel:+243987950424', label: '+243 98 79 50 424' },
  { href: 'tel:+25766444255', label: '+257 66 44 42 55' },
  { href: 'tel:+25765247128', label: '+257 65 24 71 28' },
]
</script>

<template>
  <div class="font-body text-slate bg-white">

    <!-- HERO -->
    <section
      class="relative bg-cover bg-center bg-no-repeat pb-24 pt-32 lg:pb-32 lg:pt-40"
      style="background-image: url('https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=2000');"
    >
      <div class="absolute inset-0 bg-midnight/85"></div>

      <div class="relative z-10 mx-auto grid max-w-7xl items-center gap-12 px-5 lg:grid-cols-12">
        <!-- Texte -->
        <div class="space-y-6 lg:col-span-7">
          <p class="inline-flex items-center gap-3 text-xs font-bold uppercase tracking-widest text-royal">
            <span class="h-[2px] w-8 bg-royal"></span>
            {{ t('home.eyebrow') }}
          </p>

          <h1 class="font-display text-5xl font-bold leading-[1.05] text-white sm:text-6xl lg:text-7xl">
            <span class="block">{{ t('home.heroLine1') }}</span>
            <span class="block">{{ t('home.heroLine2') }}</span>
            <span class="block">{{ t('home.heroLine3') }}</span>
          </h1>

          <p class="max-w-xl text-lg leading-relaxed text-white/80">{{ t('home.heroText') }}</p>

          <div class="flex flex-wrap gap-4 pt-4">
            <router-link to="/services" class="inline-flex items-center gap-2 rounded-sm bg-royal px-6 py-3 font-semibold text-white transition hover:bg-white hover:text-midnight">
              {{ t('home.ctaPrimary') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
            <router-link to="/a-propos" class="inline-flex items-center gap-2 rounded-sm border border-white/30 px-6 py-3 font-semibold text-white transition hover:bg-white/10">
              {{ t('home.ctaSecondary') }} <i class="fa-solid fa-arrow-right text-sm"></i>
            </router-link>
          </div>

          <!-- Repères -->
          <div class="mt-8 flex flex-wrap gap-8 border-t border-white/20 pt-8">
            <div>
              <span class="mb-1 block text-[10px] font-bold uppercase tracking-wider text-white/50">{{ t('home.founded') }}</span>
              <span class="text-sm font-semibold text-white">{{ t('home.foundedValue') }}</span>
            </div>
            <div>
              <span class="mb-1 block text-[10px] font-bold uppercase tracking-wider text-white/50">{{ t('home.focus') }}</span>
              <span class="text-sm font-semibold text-white">{{ t('home.focusValue') }}</span>
            </div>
            <div>
              <span class="mb-1 block text-[10px] font-bold uppercase tracking-wider text-white/50">{{ t('home.email') }}</span>
              <a href="mailto:Afatechsolutions@gmail.com" class="text-sm font-semibold text-royal transition hover:text-white">Afatechsolutions@gmail.com</a>
            </div>
            <div>
              <span class="mb-1 block text-[10px] font-bold uppercase tracking-wider text-white/50">{{ t('home.phones') }}</span>
              <div class="flex flex-col gap-1 text-sm font-semibold text-white">
                <a v-for="p in phones" :key="p.href" :href="p.href" class="transition hover:text-royal">{{ p.label }}</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Encart code -->
        <div class="hidden lg:col-span-5 lg:block">
          <div class="rounded-sm border border-white/10 bg-midnight/50 p-8 shadow-2xl backdrop-blur-md">
            <div class="mb-6 flex gap-2">
              <span class="h-3 w-3 rounded-full bg-red-500"></span>
              <span class="h-3 w-3 rounded-full bg-yellow-500"></span>
              <span class="h-3 w-3 rounded-full bg-green-500"></span>
            </div>
            <pre class="overflow-x-auto font-mono text-sm leading-relaxed text-white/80"><code><span class="text-royal">const</span> afa = {
  mission: <span class="text-green-400">"{{ t('home.codeMission') }}"</span>,
  continent: <span class="text-green-400">"{{ t('home.codeContinent') }}"</span>,
  stack: [<span class="text-green-400">"Vue"</span>, <span class="text-green-400">"Django"</span>, <span class="text-green-400">"MySQL"</span>],
  ambition: <span class="text-green-400">"{{ t('home.codeAmbition') }}"</span>
};</code></pre>
          </div>
        </div>
      </div>
    </section>

    <!-- INTRODUCTION -->
    <section class="bg-icy py-24">
      <div class="mx-auto grid max-w-7xl items-center gap-12 px-5 lg:grid-cols-12">
        <div class="lg:col-span-5">
          <img
            src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80&w=800"
            :alt="t('home.introImgAlt')"
            class="h-[400px] w-full rounded-sm object-cover shadow-md"
          />
        </div>
        <div class="space-y-6 lg:col-span-7">
          <p class="text-xs font-bold uppercase tracking-widest text-royal">{{ t('home.introLabel') }}</p>
          <h2 class="font-display text-3xl font-bold leading-tight text-midnight sm:text-4xl">{{ t('home.introTitle') }}</h2>
          <p class="text-lg leading-relaxed text-slate/80">{{ t('home.introP1') }}</p>
          <p class="text-lg leading-relaxed text-slate/80">{{ t('home.introP2') }}</p>
          <router-link to="/a-propos" class="inline-flex items-center gap-2 pt-2 font-bold text-royal transition hover:text-midnight">
            {{ t('home.introLink') }} <i class="fa-solid fa-arrow-right text-sm"></i>
          </router-link>
        </div>
      </div>
    </section>

    <!-- SERVICES -->
    <section class="mx-auto max-w-7xl px-5 py-24">
      <div class="mb-12 flex items-end justify-between">
        <div>
          <p class="mb-2 text-xs font-bold uppercase tracking-widest text-royal">{{ t('home.servicesLabel') }}</p>
          <h2 class="font-display text-3xl font-bold text-midnight sm:text-4xl">
            {{ t('home.servicesTitle1') }}<br>{{ t('home.servicesTitle2') }}
          </h2>
        </div>
        <router-link to="/services" class="hidden items-center gap-2 pb-2 text-sm font-bold text-royal hover:text-midnight md:flex">
          {{ t('home.viewAll') }} <i class="fa-solid fa-arrow-right text-xs"></i>
        </router-link>
      </div>

      <div class="grid grid-cols-1 gap-8 md:grid-cols-2">
        <!-- Service 1 -->
        <div class="group flex flex-col overflow-hidden rounded-sm border border-mist/60 bg-white">
          <div class="space-y-4 p-8">
            <i class="fa-solid fa-code text-2xl text-royal"></i>
            <h3 class="font-display text-xl font-bold text-midnight">{{ t('home.s1Title') }}</h3>
            <p class="text-sm leading-relaxed text-slate/70">{{ t('home.s1Text') }}</p>
          </div>
          <div class="mt-auto h-48 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=800" :alt="t('home.s1Title')" class="h-full w-full object-cover transition duration-500 group-hover:scale-105" />
          </div>
          <div class="border-t border-mist/60 bg-white p-4">
            <router-link to="/formation" class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-royal hover:text-midnight">
              {{ t('home.s1Link') }} <i class="fa-solid fa-arrow-right text-xs"></i>
            </router-link>
          </div>
        </div>

        <!-- Service 2 -->
        <div class="group flex flex-col overflow-hidden rounded-sm border border-mist/60 bg-white">
          <div class="space-y-4 p-8">
            <i class="fa-solid fa-laptop-code text-2xl text-royal"></i>
            <h3 class="font-display text-xl font-bold text-midnight">{{ t('home.s2Title') }}</h3>
            <p class="text-sm leading-relaxed text-slate/70">{{ t('home.s2Text') }}</p>
          </div>
          <div class="mt-auto h-64 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&q=80&w=800" :alt="t('home.s2Title')" class="h-full w-full object-cover transition duration-500 group-hover:scale-105" />
          </div>
        </div>

        <!-- Service 3 -->
        <div class="group relative h-[400px] overflow-hidden rounded-sm bg-midnight">
          <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=800" :alt="t('home.s3Title')" class="h-full w-full object-cover opacity-60 transition duration-700 group-hover:scale-105" />
          <div class="absolute inset-0 flex flex-col justify-end bg-gradient-to-t from-midnight/90 via-midnight/40 to-transparent p-8 text-white">
            <i class="fa-solid fa-mobile-screen-button mb-4 text-2xl"></i>
            <h3 class="mb-2 font-display text-2xl font-bold">{{ t('home.s3Title') }}</h3>
            <p class="mb-4 max-w-sm text-sm text-white/80">{{ t('home.s3Text') }}</p>
          </div>
        </div>

        <!-- Service 4 -->
        <div class="group flex flex-col justify-center rounded-sm border border-mist/60 bg-icy p-8">
          <i class="fa-solid fa-server mb-4 text-2xl text-royal"></i>
          <h3 class="mb-3 font-display text-xl font-bold text-midnight">{{ t('home.s4Title') }}</h3>
          <p class="mb-6 text-sm leading-relaxed text-slate/70">{{ t('home.s4Text') }}</p>
          <router-link to="/contact" class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-royal hover:text-midnight">
            {{ t('home.s4Link') }} <i class="fa-solid fa-arrow-right text-xs"></i>
          </router-link>
        </div>
      </div>
    </section>

    <!-- COMPÉTENCES -->
    <section class="mx-auto max-w-7xl border-t border-mist/50 px-5 py-24">
      <p class="mb-2 text-xs font-bold uppercase tracking-widest text-royal">{{ t('home.capLabel') }}</p>
      <h2 class="mb-8 font-display text-3xl font-bold text-midnight sm:text-4xl">{{ t('home.capTitle') }}</h2>
      <p class="font-display text-3xl font-bold leading-snug text-slate/30 sm:text-5xl lg:text-6xl">
        <template v-for="(key, i) in expertise" :key="key">
          <span class="cursor-default transition-colors hover:text-royal">{{ t(key) }}</span><span v-if="i < expertise.length - 1" class="text-midnight">, </span>
        </template>.
      </p>
    </section>

    <!-- POURQUOI NOUS -->
    <section class="bg-icy py-24">
      <div class="mx-auto grid max-w-7xl gap-12 px-5 lg:grid-cols-12">
        <div class="lg:col-span-4">
          <p class="mb-2 text-xs font-bold uppercase tracking-widest text-royal">{{ t('home.whyLabel') }}</p>
          <h2 class="mb-6 font-display text-3xl font-bold leading-tight text-midnight sm:text-4xl">{{ t('home.whyTitle') }}</h2>
          <p class="text-sm leading-relaxed text-slate/70">{{ t('home.whyText') }}</p>
        </div>

        <dl class="grid gap-6 sm:grid-cols-2 lg:col-span-8">
          <div v-for="v in values" :key="v[1]" class="rounded-sm border border-mist/50 bg-white p-6 shadow-sm">
            <dt class="mb-2 flex items-center gap-3 font-display text-lg font-bold text-midnight">
              <i :class="['fa-solid', v[0], 'text-royal']"></i> {{ t(`${v[1]}Title`) }}
            </dt>
            <dd class="text-sm leading-relaxed text-slate/70">{{ t(`${v[1]}Text`) }}</dd>
          </div>
        </dl>
      </div>
    </section>

    <!-- CTA -->
    <section class="mx-auto max-w-7xl px-5 py-16">
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
    </section>

  </div>
</template>