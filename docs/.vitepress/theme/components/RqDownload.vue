<script setup lang="ts">
// The Download page's release box: RQ MOD's latest release from the catalog (mods.json).
import { VPButton } from 'vitepress/theme'
import { data as catalog } from '../mods.data'
import { date, size } from '../catalog'

const engine = catalog.engine
</script>

<template>
  <section class="rq-release" aria-label="Latest release">
    <div class="rq-release__head">
      <p class="rq-release__name">
        RQ MOD {{ engine.version }}
        <Badge v-if="engine.stage" type="warning" :text="engine.stage" />
      </p>
      <p class="rq-release__date">Released {{ date(engine.published) }}</p>
    </div>
    <div class="rq-release__actions">
      <VPButton tag="a" theme="brand" :href="engine.zip.url" :text="`Download (${size(engine.zip.size)})`" />
      <VPButton tag="a" theme="alt" :href="engine.notes" text="Release notes" />
    </div>
    <p class="rq-release__file">
      <span>{{ engine.zip.name }}</span>
      <span class="rq-release__sha">SHA-256 <code>{{ engine.zip.sha256 }}</code></span>
    </p>
  </section>
</template>
