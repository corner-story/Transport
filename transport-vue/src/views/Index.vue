<template>
    <div id="page-top">
        
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container">
            <a class="navbar-brand js-scroll-trigger" href="#">{{ name }}</a>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto my-2 my-lg-0">

                <li class="nav-item">
                    <router-link to="/login" class="nav-link js-scroll-trigger">登录</router-link>
                    
                </li>
                <li class="nav-item">
                    <router-link to="/login" class="nav-link js-scroll-trigger">注册</router-link>
                </li>
                </ul>
            </div>
            </div>
        </nav>

        <!-- Masthead -->
        <header class="masthead">
            <div class="container h-100">
            <div class="row h-100 align-items-center justify-content-center text-center">
                <div class="col-lg-10 align-self-end">
                <h1 class="text-uppercase text-white font-weight-bold">{{ name }}: 物流管理平台</h1>
                <hr class="divider my-4">
                </div>
                <div class="col-lg-8 align-self-baseline">
                <p class="text-white-75 font-weight-light mb-5">便利货车司机与发货人, 提供信息交流!</p>
                <a class="btn btn-primary btn-xl js-scroll-trigger" href="#about">加入我们</a>
                </div>
            </div>
            </div>
        </header>

    </div>
</template>

<script>
export default {
    name: "index",
    data: ()=>{
        return {
            name: "物流-EARTH"
        }
    }
}
</script>

<style lang="stylus" scoped>
    @import "../assets/css/creative.min.css";
</style>