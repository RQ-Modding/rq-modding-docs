import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import RqBrand from './components/RqBrand.vue'
import RqHeroInfo from './components/RqHeroInfo.vue'
import RqHeroIcon from './components/RqHeroIcon.vue'
import RqFeatures from './components/RqFeatures.vue'
import RqDownload from './components/RqDownload.vue'
import RqMods from './components/RqMods.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'nav-bar-title-after': () => h(RqBrand, { size: 'nav' }),
      'home-hero-info': () => h(RqHeroInfo),
      'home-hero-image': () => h(RqHeroIcon),
      'home-features-before': () => h(RqFeatures),
    }),
  enhanceApp({ app }) {
    // The Download and Mods pages place these in their Markdown.
    app.component('RqDownload', RqDownload)
    app.component('RqMods', RqMods)
  },
} satisfies Theme
