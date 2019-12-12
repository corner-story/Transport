<template>
<v-app>
    <v-content>
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">

                <v-col cols="12" sm="8" md="6">
                    <v-card class="elevation-12">

                        <v-toolbar color="primary" dark flat>

                            <v-toolbar-title>物流-EARTH</v-toolbar-title>

                            <v-spacer />
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field v-model="username" label="昵称" prepend-icon="person" type="text"></v-text-field>
                                <v-text-field v-model="phone" label="手机号码" name="phone" prepend-icon="phone" type="text" />

                                <v-text-field v-model="password" label="密码" name="password" prepend-icon="lock" type="password" />
                                <v-select v-model="role" :items="roles" menu-props="auto"  hide-details prepend-icon="people" single-line></v-select>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer />
                            <v-btn color="primary" v-on:click="register">注册</v-btn>
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
            username: "",
            phone: "",
            password: "",
            role: "我是司机",
            roles: ["我是司机", "我是货主"]
        }
    },
    methods: {
        register: function () {
            let vm = this
            let data = {
                username: this.username,
                phone: this.phone,
                password: this.password,
                role: this.role === "我是司机" ? "1" : "0"
            }
            this.$axios.post("/register", data)
                .then((res) => {
                    let data = res.data
                    if (data.state === "success") {
                        vm.$router.push("/login")
                    } else {
                        alert("注册失败:" + data.msg)
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
