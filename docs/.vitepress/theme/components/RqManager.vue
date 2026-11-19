<script setup lang="ts">
// The Download page's RQ Manager box, from the catalog's manager entry (mods.json). Nothing at all
// while the catalog has none (before RQ Manager's first release).
import { VPButton } from 'vitepress/theme'
import { data as catalog } from '../mods.data'
import { date, size } from '../catalog'

const manager = catalog.manager
</script>

<template>
  <template v-if="manager">
    <p>
      The easy way: <strong>RQ Manager</strong> installs RQ MOD and the mods you pick, keeps them up to
      date, turns mods off and on, and puts the last version back. Unzip it anywhere (the game folder
      is a good place) and start <code>rq-manager.exe</code>.
    </p>
    <section class="rq-release" aria-label="RQ Manager's latest release">
      <div class="rq-release__head">
        <p class="rq-release__name">RQ Manager {{ manager.version }}</p>
        <p class="rq-release__date">Released {{ date(manager.published) }}</p>
      </div>
      <div class="rq-release__actions">
        <VPButton tag="a" theme="brand" :href="manager.zip.url" :text="`Download (${size(manager.zip.size)})`" />
        <VPButton tag="a" theme="alt" href="/guide/manager" text="How it works" />
        <VPButton tag="a" theme="alt" :href="manager.notes" text="Release notes" />
      </div>
      <p class="rq-release__file">
        <span>{{ manager.zip.name }}</span>
        <span class="rq-release__sha">SHA-256 <code>{{ manager.zip.sha256 }}</code></span>
      </p>
    </section>
    <p>Or by hand: RQ MOD's own zip, which you extract into the game folder yourself.</p>
  </template>
</template>
