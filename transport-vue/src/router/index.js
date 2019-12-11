import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from "../views/Index.vue"

Vue.use(VueRouter)


const routes = [{
        path: "/",
        name: "index",
        component: Index,
        meta: {
            login_required: false
        }
    },
    {
        path: '/login',
        name: 'login',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import( /* webpackChunkName: "about" */ '../views/Login.vue'),
        meta: {
            login_required: false
        }
    },
    {
        path: '/home',
        name: 'home',
        component: () => import("../views/Home.vue"),
        meta: {
            login_required: true
        }
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

// beforeEach
router.beforeEach(function(to, from, next){
    // 要访问的路由要求登录
    if(to.meta.login_required){
        if(window.$cookies.isKey("islogin")){
            next()
        }else{
            next({
                path: "/login"
            })
        }
    }else{
        next()
    }
})




export default router