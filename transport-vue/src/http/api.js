import axios from 'axios'

const URL = "http://127.0.0.1:5000/api"

axios.defaults.baseURL = URL; // 配置axios请求的地址
axios.defaults.headers.post['Content-Type'] = 'application/json; charset=utf-8';
axios.defaults.crossDomain = true;
axios.defaults.withCredentials = true; //设置cross跨域 并设置访问权限 允许跨域携带cookie信息

// Add a request interceptor
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
    return config;
}, function (error) {
    // Do something with request error
    return Promise.reject(error);
});

// Add a response interceptor
axios.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        console.log("axios error!")
        if (error.response) {
            switch (error.response.status) {
                case 403:
                    // 返回 401 清除token信息并跳转到登录页面
                    // 清除所有cookie
                    this.$cookies.keys().forEach(cookie => this.$cookies.remove(cookie))
                    // 回到首页
                    window.top.location.href = "/"
                    break;
            }
        }
        return Promise.reject(error.response.data) // 返回接口返回的错误信息
    });

export default axios.create()