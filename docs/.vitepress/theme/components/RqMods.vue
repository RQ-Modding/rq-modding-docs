<script setup lang="ts">
// The Mods page's list: one card per mod of the catalog (mods.json), with a search, a tag filter
// and a sort. Every card is in the built HTML; the filters only hide cards.
import { computed, ref } from 'vue'
import { data as catalog, type CatalogMod } from '../mods.data'
import { TAG_NAMES, date, size } from '../catalog'

const mods = catalog.mods
const query = ref('')
const tag = ref('')
const sort = ref<'name' | 'newest'>('name')

const tags = computed(() =>
  Object.keys(TAG_NAMES)
    .map((t) => ({ id: t, name: TAG_NAMES[t], count: mods.filter((m) => m.tags.includes(t)).length }))
    .filter((t) => t.count > 0),
)

function matches(m: CatalogMod): boolean {
  if (tag.value && !m.tags.includes(tag.value)) return false
  const q = query.value.trim().toLowerCase()
  if (!q) return true
  const text = [m.name, m.id, m.description, m.author, ...m.tags.map((t) => TAG_NAMES[t] ?? t)].join(' ').toLowerCase()
  return q.split(/\s+/).every((word) => text.includes(word))
}

const shown = computed(() => {
  const list = mods.filter(matches)
  if (sort.value === 'newest')
    return list.sort((a, b) => b.published.localeCompare(a.published) || a.name.localeCompare(b.name))
  return list.sort((a, b) => a.name.localeCompare(b.name))
})

const nameOf = (id: string) => mods.find((m) => m.id === id)?.name ?? id
const readme = (m: CatalogMod) => `${m.repo}/blob/${m.tag}/README.md`
const notes = (m: CatalogMod) => `${m.repo}/releases/tag/${m.tag}`
</script>

<template>
  <section class="rq-mods" aria-label="Mods">
    <div class="rq-mods__bar">
      <label class="rq-mods__search">
        <span class="visually-hidden">Search the mods</span>
        <input v-model="query" type="search" placeholder="Search: a name, a character, a word" />
      </label>
      <label class="rq-mods__sort">
        Sort
        <select v-model="sort">
          <option value="name">By name</option>
          <option value="newest">Newest first</option>
        </select>
      </label>
    </div>

    <div class="rq-mods__tags" role="group" aria-label="Show only">
      <button type="button" class="rq-tag" :aria-pressed="tag === ''" @click="tag = ''">
        All <span class="rq-tag__count">{{ mods.length }}</span>
      </button>
      <button
        v-for="t in tags"
        :key="t.id"
        type="button"
        class="rq-tag"
        :aria-pressed="tag === t.id"
        @click="tag = tag === t.id ? '' : t.id"
      >
        {{ t.name }} <span class="rq-tag__count">{{ t.count }}</span>
      </button>
    </div>

    <p class="rq-mods__count" aria-live="polite">
      <template v-if="shown.length === mods.length">{{ mods.length }} mods</template>
      <template v-else>{{ shown.length }} of {{ mods.length }} mods</template>
    </p>

    <div class="rq-mods__grid">
      <article v-for="m in shown" :id="m.id" :key="m.id" class="rq-mod">
        <header class="rq-mod__title">
          <h3 class="rq-mod__name">{{ m.name }}</h3>
          <span class="rq-mod__version">{{ m.version }}</span>
        </header>
        <div class="rq-mod__body">
          <p class="rq-mod__desc">{{ m.description }}</p>
          <p class="rq-mod__tags">
            <button v-for="t in m.tags" :key="t" type="button" class="rq-chip" @click="tag = t">
              {{ TAG_NAMES[t] ?? t }}
            </button>
          </p>
          <dl class="rq-mod__facts">
            <div>
              <dt>Needs</dt>
              <dd>RQ MOD {{ m.loader }} or newer</dd>
            </div>
            <div v-if="m.dependencies.length">
              <dt>With</dt>
              <dd>
                <template v-for="(d, i) in m.dependencies" :key="d">
                  <a :href="`#${d}`">{{ nameOf(d) }}</a><template v-if="i < m.dependencies.length - 1">, </template>
                </template>
                (install it too)
              </dd>
            </div>
            <div v-if="m.conflicts.length">
              <dt>Not with</dt>
              <dd>{{ m.conflicts.map(nameOf).join(', ') }}</dd>
            </div>
            <div>
              <dt>Save</dt>
              <dd v-if="m.save === 'none'">Safe to remove: your save does not need it.</dd>
              <dd v-else>
                Leaves things in your save. Read its
                <a :href="`${readme(m)}#saves`">Saves</a> part before you remove it.
              </dd>
            </div>
            <div>
              <dt>By</dt>
              <dd>{{ m.author }} · {{ m.license }} · {{ date(m.published) }}</dd>
            </div>
          </dl>
          <p class="rq-mod__actions">
            <a class="rq-btn rq-btn--brand" :href="m.zip.url">Download <span class="rq-btn__size">{{ size(m.zip.size) }}</span></a>
            <a class="rq-btn" :href="readme(m)">Read me</a>
            <a class="rq-btn" :href="notes(m)" title="The release's notes on GitHub">Changes</a>
          </p>
        </div>
      </article>
    </div>

    <p v-if="!shown.length" class="rq-mods__none">
      No mod matches.
      <button type="button" class="rq-chip" @click="query = ''; tag = ''">Show all</button>
    </p>
  </section>
</template>
