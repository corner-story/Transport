<template>
<el-container>
        <el-menu mode="horizontal" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
            <el-menu-item index="1" @click="to_home" style="margin-left:32px;">金色大厅</el-menu-item>
            
            <el-menu-item index="4" @click="to_about">订单管理</el-menu-item>
            <el-submenu index="5" style="float:right;margin-right:32px;">
                <template slot="title">{{ username }}</template>
                <el-menu-item index="5-1">个人中心</el-menu-item>
                <el-menu-item index="5-2">我的消息</el-menu-item>
                <el-menu-item index="5-3" @click="logout">退出</el-menu-item>
            </el-submenu>
        </el-menu>
    <el-main>
        <component v-bind:is="currentTab"></component>
    </el-main>

    <el-footer>

    </el-footer>
</el-container>
</template>

<script>
import GoodHall from '../components/GoodHall'
import About from '../components/About'

export default {
    name: "home",
    props: {
        source: String,
    },
    data: () => {
        return {
            currentTab: GoodHall
        }
    },
    computed: {
        username: function(){
            return this.$cookies.get("username")
        }
    },
    methods: {
        changeTheme() {
            if (this.$vuetify.theme.dark) {
                this.$vuetify.theme.dark = false
            } else {
                this.$vuetify.theme.dark = true
            }
            alert(this.$vuetify.theme.dark)
        },
        logout() {
            // 清除所有cookie
            this.$cookies.keys().forEach(cookie => this.$cookies.remove(cookie))
            // 回到首页
            this.$router.push("/")
        },

        to_home() {
            this.currentTab = GoodHall
        },

        to_about(){
            this.currentTab = About
        }
    },

    created: function () {
        this.$message.success("Hello, " + this.$cookies.get("username") + " , 欢迎使用物流-EARTH!")
    }
}
</script>
