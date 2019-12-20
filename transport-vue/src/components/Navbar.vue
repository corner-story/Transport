<template>
<el-menu mode="horizontal" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
    <el-menu-item index="1" style="margin-left:32px;" v-on:click="to_home">金色大厅</el-menu-item>

    <el-menu-item index="4">订单管理</el-menu-item>
    <el-submenu index="5" style="float:right;margin-right:32px;">
        <template slot="title">{{ username }}</template>
        <el-menu-item index="5-1" @click="to_selfcenter">个人中心</el-menu-item>
        <el-menu-item index="5-2">我的消息</el-menu-item>
        <el-menu-item index="5-3" @click="logout">退出</el-menu-item>
    </el-submenu>
</el-menu>
</template>

<script>
export default {
    name: "Navbar",
    computed: {
        username(){
            return this.$cookies.get("username")
        }
    },
    methods: {
        to_home: function() {
            this.$router.push("/home")
        },

        to_about() {

        },
        to_selfcenter() {
            this.$router.push({ name: 'user', params: { usertype: 'self'}, query: {id: '0'}})
        },
        logout() {
            this.$axios.post("/logout/")
                .then((response) =>{
                    // 清除所有cookie
                    this.$cookies.keys().forEach(cookie => this.$cookies.remove(cookie))
                    let data = response.data
                    if(data.state == "success"){
                        this.$message.success(data.msg)
                        // 回到首页
                        window.top.location.href = "/"
                    }

                })
                .catch((error) =>{
                    // 清除所有cookie
                    this.$cookies.keys().forEach(cookie => this.$cookies.remove(cookie))
                    console.log(error)
                    this.$message.error("发生未知错误, 请联系管理员!")
                })
            
        },
    }
}
</script>
