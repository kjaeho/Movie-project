import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)
    // Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

Vue.use(VueCookies)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')