import { defineConfig, type DefaultTheme } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const here = path.dirname(fileURLToPath(import.meta.url))
const docs = path.resolve(here, '..')
const engine: { version: string; commit: string } = JSON.parse(
  fs.readFileSync(path.join(here, 'engine.json'), 'utf8'),
)

const ORG = 'https://github.com/RQ-Modding'
const DISCORD = 'https://discord.gg/maCKqfTGne'
const COMMUNITY = 'https://discord.gg/RANCE'
const MORU_X = 'https://x.com/Moru_zerinho6'

// Headings get the anchor GitHub gives them ("rq.shop.stock" -> "rqshopstock"), so the generated
// pages link the same way on GitHub and on the site.
function githubSlug(s: string): string {
  return s
    .trim()
    .toLowerCase()
    .replace(/<[^>]*>/g, '')
    .replace(/[^\p{L}\p{N}\s_-]/gu, '')
    .replace(/\s/g, '-')
}

// One sidebar entry per generated page, read from the folder so new namespaces show up by themselves.
function pages(dir: string, prefix: string): DefaultTheme.SidebarItem[] {
  return fs
    .readdirSync(path.join(docs, dir))
    .filter((f) => f.endsWith('.md'))
    .map((f) => f.slice(0, -3))
    .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    .map((name) => ({ text: name, link: `${prefix}/${name}` }))
}

const guide: DefaultTheme.SidebarItem[] = [
  {
    text: 'Players',
    items: [
      { text: 'Download', link: '/download' },
      { text: 'Mods', link: '/mods' },
      { text: 'Install', link: '/guide/install' },
    ],
  },
  {
    text: 'Making mods',
    items: [
      { text: 'Your first mod', link: '/guide/first-mod' },
      { text: 'mod.json', link: '/guide/manifest' },
      { text: 'What a mod can reach', link: '/guide/sandbox' },
      { text: 'Numbers and ids', link: '/guide/ids' },
      { text: "Looking through the game's files", link: '/guide/file-browser' },
      { text: 'Gold, encounters and levels', link: '/guide/game-state' },
      { text: 'Monsters and enemy groups', link: '/guide/monsters' },
      { text: 'Data that follows the save', link: '/guide/save-data' },
      { text: "The game's own code", link: '/guide/game-code' },
      { text: 'Pictures', link: '/guide/pictures' },
      { text: 'Replacing music', link: '/guide/music' },
      { text: 'Battle states', link: '/guide/states' },
      { text: 'Combat rules', link: '/guide/combat' },
      { text: 'Quests and maps', link: '/guide/quests-maps' },
      { text: 'Quests of your own', link: '/guide/new-quests' },
      { text: "Buttons in the game's menus", link: '/guide/game-menus' },
      { text: 'Editor setup', link: '/guide/editor-setup' },
      { text: 'Logs and debugging', link: '/guide/debugging' },
      { text: 'Sharing a mod', link: '/guide/publishing' },
    ],
  },
]

const reference: DefaultTheme.SidebarItem[] = [
  { text: 'Overview', link: '/reference/' },
  { text: 'Namespaces', collapsed: false, items: pages('reference/api', '/reference/api') },
  { text: 'Types', collapsed: true, items: pages('reference/types', '/reference/types') },
]

const data: DefaultTheme.SidebarItem[] = [
  {
    text: 'Game data',
    items: [
      { text: 'Overview', link: '/data/' },
      { text: 'Characters', link: '/data/characters' },
      { text: 'Character types', link: '/data/chara-types' },
      { text: 'Classes', link: '/data/classes' },
      { text: 'Elements', link: '/data/elements' },
      { text: 'Items', link: '/data/items' },
      { text: 'Item kinds', link: '/data/item-kinds' },
      { text: 'Map kinds', link: '/data/map-kinds' },
      { text: 'Monsters', link: '/data/monsters' },
      { text: 'Music', link: '/data/music' },
      { text: 'Party states', link: '/data/party-states' },
      { text: 'Quests', link: '/data/quests' },
      { text: 'Races', link: '/data/races' },
      { text: 'Skills', link: '/data/skills' },
      { text: 'Skill targets', link: '/data/targets' },
      { text: 'States', link: '/data/states' },
    ],
  },
]

export default defineConfig({
  title: 'RQ MOD',
  description: 'Lua mods for Rance Quest Magnum: guides and the rq.* API reference.',
  lang: 'en-US',
  // GitHub Pages serves a project site under /<repo>/; the deploy workflow sets DOCS_BASE.
  base: process.env.DOCS_BASE || '/',
  cleanUrls: true,
  lastUpdated: false,
  // Dark (the game's Config screen) is the default; light is the parchment theme.
  appearance: 'dark',
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: `${process.env.DOCS_BASE || '/'}rq-mod.png` }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    [
      'link',
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Alegreya+SC:wght@700;800&family=Alegreya:wght@700&family=M+PLUS+1p:wght@500;700;800&display=swap',
      },
    ],
  ],
  markdown: {
    anchor: { slugify: githubSlug },
    lineNumbers: false,
  },
  themeConfig: {
    logo: '/rq-mod.png',
    // The theme draws the title itself (RqBrand), styled per theme.
    siteTitle: false,
    nav: [
      { text: 'Download', link: '/download' },
      { text: 'Mods', link: '/mods' },
      { text: 'Guide', link: '/guide/first-mod', activeMatch: '/guide/' },
      { text: 'API reference', link: '/reference/', activeMatch: '/reference/' },
      { text: 'Game data', link: '/data/', activeMatch: '/data/' },
      { text: 'Changelog', link: '/changelog' },
      { text: 'Roadmap', link: '/roadmap' },
      { text: `Loader ${engine.version}`, link: '/changelog' },
    ],
    sidebar: {
      '/guide/': guide,
      '/reference/': reference,
      '/data/': data,
    },
    outline: { level: [2, 3], label: 'On this page' },
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'discord', link: DISCORD, ariaLabel: 'RQ MOD on Discord' },
      { icon: 'x', link: MORU_X, ariaLabel: 'Moru on X' },
      { icon: 'github', link: ORG, ariaLabel: 'RQ Modding on GitHub' },
    ],
    editLink: {
      // The reference and the changelog come from the engine; send their edits there.
      // This function runs in the browser, so it cannot use the constants above.
      pattern: ({ filePath }) => {
        if (filePath.startsWith('reference/'))
          return 'https://github.com/RQ-Modding/RQ-Mod/edit/main/dist/lua/rq.lua'
        if (filePath.startsWith('data/'))
          return 'https://github.com/RQ-Modding/RQ-Mod/tree/main/data/ids'
        if (filePath === 'changelog.md')
          return 'https://github.com/RQ-Modding/RQ-Mod/edit/main/CHANGELOG.md'
        return 'https://github.com/RQ-Modding/rq-modding-docs/edit/main/docs/' + filePath
      },
      text: 'Edit this page on GitHub',
    },
    footer: {
      message: `RQ MOD is a public beta. API reference generated from RQ MOD ${engine.version}${engine.commit ? ` (${engine.commit})` : ''}. RQ MOD is built on xsystem4.<br>Community: <a href="${DISCORD}">RQ MOD on Discord</a> · <a href="${COMMUNITY}">Rance &amp; Alicesoft Western Community</a> · <a href="${MORU_X}">Moru on X</a>`,
      copyright: 'Docs text under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>. Code examples are public domain (<a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a>).',
    },
  },
})
