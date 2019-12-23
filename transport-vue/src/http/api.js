import axios from 'axios'

const URL = "http://127.0.0.1:5000/api"

axios.defaults.baseURL = URL; // 配置axios请求的地址
axios.defaults.headers.post['Content-Type'] = 'application/json; charset=utf-8';
axios.defaults.crossDomain = true;
axios.defaults.withCredentials = true; //设置cross跨域 并设置访问权限 允许跨域携带cookie信息


const instance = axios.create();

// Add a request interceptor
instance.interceptors.request.use(function (config) {
    // Do something before request is sent
    
    return config;
}, function (error) {
    // Do something with request error
  
    return Promise.reject(error);
});

// Add a response interceptor
instance.interceptors.response.use(
    response => {
        // console.log("axios response!")
        return response;
    },
    error => {
        // console.log("axios error: " + error.response.status)
        if (error.response) {
            switch (error.response.status) {
                case 403:
                    alert("登录超时, 请重新登录!")
                    // 清除所有cookie
                    window.$cookies.keys().forEach(cookie => window.$cookies.remove(cookie))
                    // 回到首页
                    window.top.location.href = "/login"
                    break;
            }
        }
        return Promise.reject(error) // 返回接口返回的错误信息
    });

export default instance;