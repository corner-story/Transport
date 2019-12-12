<template>
<v-app>
    <v-content>

        <v-container class="fill-height" fluid>

            <v-row align="center" justify="center">
                <v-col cols="12" sm="8" md="4">
                    <v-card class="elevation-12">
                        <v-toolbar color="primary" dark flat>
                            <v-toolbar-title>物流-EARTH</v-toolbar-title>
                            <v-spacer />
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field v-model="phone" label="请输入手机号码" name="phone" prepend-icon="phone" type="text" />

                                <v-text-field v-model="password" label="请输入密码" name="password" prepend-icon="lock" type="password" />
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn color="primary" v-on:click="login">登录</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
</v-app>
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
            let vm = this
            let data = {
                phone: this.phone,
                password: this.password
            }
            this.$axios.post("/login", data)
                .then((res) => {
                    let data = res.data
                    if (data.state === "success") {
                        vm.$router.push("/home")
                    } else {
                        alert("登录失败, 请检查手机号码和密码是否正确!")
                    }
                    return true
                })
                .catch((error) => {
                    alert("请求失败, 请检查网络!")
                    console.log(error)
                })
        }
    }
}
</script>
