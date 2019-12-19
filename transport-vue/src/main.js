import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueCookies from 'vue-cookies';
import axios from './http/api';
// 高德地图
import VueAMap from "vue-amap";

import './plugins/element.js'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.prototype.$axios = axios

Vue.config.productionTip = false

Vue.use(VueCookies)
Vue.use(ElementUI)
Vue.use(VueAMap);
VueAMap.initAMapApiLoader({
  key: 'f73154b35c07480e1ce8e137fc916b00',
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor'],
  // 默认高德 sdk 版本为 1.4.4
  v: '1.4.4'
});


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
