import axios from 'axios'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api' })

api.interceptors.request.use((cfg) => {
  const token = localStorage.getItem('afa_token')
  if (token) cfg.headers.Authorization = `Token ${token}`
  return cfg
})
api.interceptors.response.use(
  (r) => r,
  (e) => {
    if (e.response?.status === 401 && location.pathname.startsWith('/admin')) {
      localStorage.removeItem('afa_token')
      location.href = '/admin/login'
    }
    return Promise.reject(e)
  }
)

export const list = (path) => api.get(path).then((r) => r.data.results ?? r.data)
export default api
