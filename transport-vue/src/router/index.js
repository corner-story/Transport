import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/auth/Index.vue'
import GoodDetail from "../views/good/GoodDetail.vue"

Vue.use(VueRouter)

const routes = [{
		path: '/',
		name: 'index',
		component: Index,
		meta: {
			login_required: false
		}
	},
	{
		path: '/login',
		name: 'login',
		component: () => import( /* webpackChunkName: "about" */ '../views/auth/Login.vue'),
		meta: {
			login_required: false
		}
	},
	{
		path: '/register',
		name: 'register',
		component: () => import( /* webpackChunkName: "about" */ '../views/auth/Register.vue'),
		meta: {
			login_required: false
		}
	},
	{
		path: "/home",
		name: "home",
		component: () => import("../views/Home.vue"),	
	},
	{
		path: "/good/:id",
		name: "good",
		component: GoodDetail
	}

]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

router.beforeEach((to, from, next) => {
	// 查看是否有login_required这个属性
	if ("login_required" in to.meta) {
		if(window.$cookies.isKey("islogin")){
			next({path: "/home"})
		}else{
			next()
		}
	} else {
		// 查看用户是否登录(根据cookie)
		if (window.$cookies.isKey("islogin")) {
			console.log({cookies: window.$cookies})
			next()
		} else {
			next({
				path: "/login"
			})
		}
	}
})




export default router