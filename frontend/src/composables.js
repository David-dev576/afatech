import { onMounted, ref } from 'vue'
import { list } from './api'
export function useList(path, fallback = []) {
  const items = ref([]), loading = ref(true), failed = ref(false)
  onMounted(async () => {
    try { const d = await list(path); items.value = d.length ? d : fallback }
    catch { items.value = fallback; failed.value = !fallback.length }
    finally { loading.value = false }
  })
  return { items, loading, failed }
}
