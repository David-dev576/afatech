const API = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'
export const BACKEND = API.replace(/\/api\/?$/, '')
export const ADMIN_URL = `${BACKEND}/admin/`

export const fmtDate = (d) =>
  d ? new Date(d).toLocaleString('fr-FR', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' }) : '—'

export const mediaUrl = (p) => (!p ? '' : /^https?:/.test(p) ? p : BACKEND + p)

export const slugify = (s) =>
  s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60)

export const msgStatus = {
  new: { label: 'Non lu', cls: 'bg-royal text-white' },
  read: { label: 'Lu', cls: 'bg-icy text-slate ring-1 ring-mist' },
  archived: { label: 'Archivé', cls: 'bg-mist/50 text-slate' },
}

// Construit un FormData si un fichier est présent, sinon renvoie l'objet JSON.
export function buildForm(data, fileField, file) {
  if (!file) return data
  const fd = new FormData()
  Object.entries(data).forEach(([k, v]) => fd.append(k, v === null || v === undefined ? '' : String(v)))
  fd.append(fileField, file)
  return fd
}

// Transforme les erreurs DRF en { champ: message, form: message }.
export function normalizeErrors(e) {
  if (e.response?.status === 429) return { form: 'Trop de tentatives. Réessayez plus tard.' }
  const data = e.response?.data
  if (!data || typeof data !== 'object') return { form: 'Une erreur est survenue. Réessayez.' }
  const out = {}
  for (const [k, v] of Object.entries(data)) {
    const key = k === 'detail' || k === 'non_field_errors' ? 'form' : k
    out[key] = [].concat(v)[0]
  }
  return out
}