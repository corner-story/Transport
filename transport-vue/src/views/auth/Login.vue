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
                    <el-form-item label="手机号码">
                        <el-input v-model="phone" placehoder="请输入手机号码" prefix-icon="el-icon-mobile-phone"></el-input>
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="password" placehoder="请输入密码" prefix-icon="el-icon-lock" show-password></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="login">登录</el-button>
                        <el-button @click="to_register" icon="el-icon-right">去注册?</el-button>
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
            phone: "",
            password: "",
        }
    },
    methods: {
        login: function () {
            let data = {
                phone: this.phone,
                password: this.password
            }
            this.$axios.post("/login", data)
                .then((res) => {
                    let data = res.data
                    if (data.state === "success") {
                        this.$message({message: data.msg, type: "success"})
                        vm.$router.push("/home")
                    } else {
                        this.$message.error("登录失败, 请检查手机号码和密码是否正确!")
                    }
                    return true
                })
                .catch((error) => {
                    this.$message.error("请求失败, 请检查网络!")
                    console.log(error)
                })
        },
        to_register: function () {
            this.$router.push("/register")
        }
    }
}
</script>
