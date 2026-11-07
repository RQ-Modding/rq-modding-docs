<script setup lang="ts">
// Replaces the hero's name/text/tagline block so the name can use RqBrand.
// Text comes from the page's hero frontmatter, as with the default hero.
import { computed } from 'vue'
import { useData } from 'vitepress'
import RqBrand from './RqBrand.vue'

const { frontmatter } = useData()
const hero = computed(() => frontmatter.value.hero ?? {})
</script>

<template>
  <h1 class="heading rq-hero-heading">
    <RqBrand size="hero" />
    <span v-if="hero.text" class="text" v-html="hero.text"></span>
  </h1>
  <p v-if="hero.tagline" class="tagline" v-html="hero.tagline"></p>
</template>
