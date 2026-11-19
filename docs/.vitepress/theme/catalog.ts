// Words and numbers the Download and Mods pages share.

export const TAG_NAMES: Record<string, string> = {
  characters: 'Characters',
  skills: 'Skills',
  items: 'Items',
  battle: 'Battle',
  dungeons: 'Dungeons',
  quests: 'Quests',
  shops: 'Shops',
  interface: 'Interface',
  modes: 'Modes and speed',
  saves: 'Saves',
  fixes: 'Fixes',
}

export function size(bytes: number): string {
  if (bytes >= 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
  return `${Math.max(1, Math.round(bytes / 1024))} KB`
}

const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

// "2026-11-18" -> "18 November 2026", the same on the server and in the browser.
export function date(day: string): string {
  const [y, m, d] = day.split('-').map(Number)
  return y && m && d ? `${d} ${MONTHS[m - 1]} ${y}` : day
}
