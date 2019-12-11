import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueCookies from 'vue-cookies'

// 一定要导入下面这两个文件
import "vuetify/dist/vuetify.min.css";
import 'material-design-icons-iconfont/dist/material-design-icons.css';

Vue.config.productionTip = false
Vue.use(VueCookies)

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
