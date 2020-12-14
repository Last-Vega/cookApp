import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*'

Vue.config.productionTip = false

Vue.prototype.$api = axios // this.$apiでaxiosを呼び出せるようにする。

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
