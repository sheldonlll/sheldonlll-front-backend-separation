import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './assets/global.css'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from 'axios'
import VueTyperPlugin from 'vue-typer'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

Vue.config.productionTip = false
Vue.use(VueTyperPlugin)
Vue.use(mavonEditor)
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
axios.interceptors.request.use(config => {
  config.headers.Authorization = 'Bearer '+window.localStorage.getItem('access')
  return config
})
Vue.prototype.$http = axios
Vue.filter('dateFormat', function(originVal) {
  const dt = new Date(originVal)
  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0')
  const d = (dt.getDate() + '').padStart(2, '0')
  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')
  return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
})
Vue.filter('cutwords', function(originVal) {
	if (!originVal) return ''
	if (originVal.length > 50) {
		return originVal.slice(0,50) + '...'
	}
	return originVal
	}
)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
