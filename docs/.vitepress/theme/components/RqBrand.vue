<script setup lang="ts">
// "RQ MOD" in the icon's brush lettering: a white outline layer under a brick-to-black gradient.
// The nav uses size "nav"; the dark theme shows plain text there (see style.css).
defineProps<{ size?: 'hero' | 'nav' }>()
</script>

<template>
  <span class="rq-brand" :class="size === 'nav' ? 'rq-brand--nav' : 'rq-brand--hero'">
    <span class="rq-brand__back" aria-hidden="true">RQ MOD</span>
    <span class="rq-brand__front">RQ MOD</span>
  </span>
</template>
