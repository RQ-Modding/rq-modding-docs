<script setup lang="ts">
// The home page's feature list, from the `rqFeatures` frontmatter ({ title, details }[]).
// Light theme: cards with green title bars. Dark theme: the Config screen's 3D tab, a checklist,
// a list and a text panel, where picking a name shows its text. Both are rendered; style.css
// shows the one for the current theme.
import { computed, ref } from 'vue'
import { useData } from 'vitepress'

type Feature = { title: string; details: string }

const { frontmatter } = useData()
const features = computed<Feature[]>(() => frontmatter.value.rqFeatures ?? [])
const picked = ref(0)
const current = computed(() => features.value[picked.value] ?? features.value[0])
</script>

<template>
  <section v-if="features.length" class="rq-features" aria-label="Features">
    <div class="rq-features__inner">
      <div class="rq-cards">
        <article v-for="f in features" :key="f.title" class="rq-card">
          <h2 class="rq-card__title">{{ f.title }}</h2>
          <p class="rq-card__body" v-html="f.details"></p>
        </article>
      </div>

      <div class="rq-cfg">
        <div class="rq-cfg__checks">
          <h2 class="rq-cfg__label">What a mod can do</h2>
          <button
            v-for="(f, i) in features"
            :key="f.title"
            type="button"
            class="rq-cfg__check"
            :aria-pressed="i === picked"
            @click="picked = i"
          >
            <span class="rq-check" aria-hidden="true">
              <svg v-if="i === picked" width="26" height="24" viewBox="0 0 26 24">
                <path d="M3 12 L10 19 L24 3" fill="none" stroke="#7a0f12" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M3 12 L10 19 L24 3" fill="none" stroke="#e0262b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
            </span>
            {{ f.title }}
          </button>
        </div>
        <div class="rq-slate rq-cfg__list">
          <button
            v-for="(f, i) in features"
            :key="f.title"
            type="button"
            class="rq-cfg__item"
            :class="{ 'is-on': i === picked }"
            @click="picked = i"
          >{{ f.title }}</button>
        </div>
        <div class="rq-slate rq-cfg__text" aria-live="polite">
          <p class="rq-cfg__text-title">{{ current?.title }}</p>
          <p class="rq-cfg__text-body" v-html="current?.details"></p>
        </div>
      </div>
    </div>
  </section>
</template>
