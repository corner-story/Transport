<template>
<el-container>
    <el-header>
        <el-menu mode="horizontal" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
            <el-menu-item index="1" @click="to_home">处理中心</el-menu-item>
            <el-submenu index="2">
                <template slot="title">我的工作台</template>
                <el-menu-item index="2-1">选项1</el-menu-item>
                <el-menu-item index="2-2">选项2</el-menu-item>
                <el-menu-item index="2-3">选项3</el-menu-item>
                <el-submenu index="2-4">
                    <template slot="title">选项4</template>
                    <el-menu-item index="2-4-1">选项1</el-menu-item>
                    <el-menu-item index="2-4-2">选项2</el-menu-item>
                    <el-menu-item index="2-4-3">选项3</el-menu-item>
                </el-submenu>
            </el-submenu>
            <el-menu-item index="3" @click="to_about">消息中心</el-menu-item>
            <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        </el-menu>
    </el-header>

    <el-main>
        <component v-bind:is="currentTab"></component>
    </el-main>

    <el-footer>

    </el-footer>
</el-container>
</template>

<script>
import HelloWorld from '../components/HelloWorld'
import About from '../components/About'

export default {
    name: "home",
    props: {
        source: String,
    },
    data: () => {
        return {
            currentTab: HelloWorld
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

        to_home() {
            this.currentTab = HelloWorld
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
