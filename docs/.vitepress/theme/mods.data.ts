// The mods' catalog (docs/public/mods.json, written by scripts/catalog.py), read at build time so
// the Download and Mods pages are in the built HTML.
import fs from 'node:fs'

export interface CatalogFile {
  name: string
  url: string
  size: number
  sha256: string
}

export interface CatalogMod {
  id: string
  name: string
  author: string
  description: string
  tags: string[]
  save: 'none' | 'stays'
  version: string
  loader: string
  dependencies: string[]
  loadAfter: string[]
  loadBefore: string[]
  conflicts: string[]
  license: string
  repo: string
  tag: string
  published: string
  zip: CatalogFile
}

export interface Catalog {
  format: number
  generated: string
  engine: {
    version: string
    stage: string
    tag: string
    published: string
    notes: string
    zip: CatalogFile
  }
  mods: CatalogMod[]
}

declare const data: Catalog
export { data }

export default {
  watch: ['../../public/mods.json'],
  load(files: string[]): Catalog {
    return JSON.parse(fs.readFileSync(files[0], 'utf8'))
  },
}
