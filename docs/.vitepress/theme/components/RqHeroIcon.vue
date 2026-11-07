<script setup lang="ts">
// The hero icon in a frame: a green bevel in the light theme, a slate panel in the dark one.
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'

const { frontmatter } = useData()
const image = computed(() => frontmatter.value.hero?.image ?? { src: '/rq-mod.png', alt: '' })
</script>

<template>
  <div class="rq-hero-icon">
    <img :src="withBase(image.src)" :alt="image.alt" width="48" height="48" />
  </div>
</template>
