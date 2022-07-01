import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "./http/axios.js";
import api from "./http/api.js";
import './plugins/element.js'

Vue.config.productionTip = false

Vue.prototype.axios = axios
Vue.prototype.api = api

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
