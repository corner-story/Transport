<template>
<div style="margin-top:128px;">
    <el-row type="flex" justify="center">
        <el-col :span="12">
            <el-card class="box-card" shadow="always">
                <div slot="header" class="clearfix">
                    <span>物流-EARTH</span>
                    <el-button style="float: right; padding: 3px 0" type="text">点击我了解更多</el-button>
                </div>
                <el-form ref="form" label-width="80px">
                    <el-form-item label="你的名字">
                        <el-input v-model="username" placehoder="请输入你的昵称" prefix-icon="el-icon-user"></el-input>
                    </el-form-item>
                    <el-form-item label="手机号码">
                        <el-input v-model="phone" placehoder="请输入手机号码" prefix-icon="el-icon-mobile-phone"></el-input>
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="password" placehoder="请输入密码" prefix-icon="el-icon-lock" show-password></el-input>
                    </el-form-item>
                    <el-form-item label="身份">
                        <el-radio v-model="role" label="1">我是司机</el-radio>
                        <el-radio v-model="role" label="0">我是货主</el-radio>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="register">注册</el-button>
                        <el-button @click="to_login" icon="el-icon-right" style="float:right">去登录?</el-button>
                    </el-form-item>
                </el-form>
            </el-card>

        </el-col>
    </el-row>
</div>
</template>

<script>
export default {
    name: "login",
    data: () => {
        return {
            username: "",
            phone: "",
            password: "",
            role: "1",
        }
    },
    methods: {
        register: function () {
            let data = {
                username: this.username,
                phone: this.phone,
                password: this.password,
                role: this.role
            }
            this.$axios.post("/register", data)
                .then((res) => {
                    let data = res.data
                    if (data.state === "success") {
                        this.$message({message: data.msg, type: "success"})
                        this.to_login()
                    } else {
                        this.$message("注册失败:" + data.msg)
                    }
                    return true
                })
                .catch((error) => {
                    this.$message.error("请求失败, 请检查网络!")
                    console.log(error)
                })
        },

        to_login: function () {
            this.$router.push("/login")
        }
    }
}
</script>
