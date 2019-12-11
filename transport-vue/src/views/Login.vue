<template>
<div>
    <h1 v-on:click="login">点我登录</h1>
</div>
</template>

<script>

export default {
	name: "login",
	methods: {
		login(){
			window.$cookies.set("islogin", "true")
			alert("登录成功!")
		}
	}
}
</script>
