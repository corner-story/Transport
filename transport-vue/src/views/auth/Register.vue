<template>
<v-app id="inspire">
    
    <v-content>

        <v-container class="fill-height" fluid>

            <v-row align="center" justify="center">

                <!-- 弹出框 -->
                <template width="400px">
                    <v-card>
                        <v-card-title class="grey darken-2">
                            物流-Earth
                        </v-card-title>
                        <v-container>
                            <v-row class="mx-2">
                                <v-col class="align-center justify-space-between" cols="12">
                                    <v-row align="center" class="mr-0">
                                        <v-avatar size="40px" class="mx-3">
                                            <img src="//ssl.gstatic.com/s2/oz/images/sge/grey_silhouette.png" alt="">
                                        </v-avatar>
                                        <v-text-field placeholder="Name" />
                                    </v-row>
                                </v-col>
                                <v-col cols="6">
                                    <v-text-field prepend-icon="business" placeholder="Company" />
                                </v-col>
                                <v-col cols="6">
                                    <v-text-field placeholder="Job title" />
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field prepend-icon="mail" placeholder="Email" />
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field type="tel" prepend-icon="phone" placeholder="(000) 000 - 0000" />
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field prepend-icon="notes" placeholder="Notes" />
                                </v-col>
                            </v-row>
                        </v-container>
                        <v-card-actions>
                            <v-btn text color="primary">更多</v-btn>
                            <v-spacer />
                            <v-btn text color="primary" v-on:click="cancel">取消</v-btn>
                            <v-btn text v-on:click="register">注册</v-btn>
                        </v-card-actions>
                    </v-card>
                </template>
            </v-row>
        </v-container>
    </v-content>
    
</v-app>
</template>

<script>
export default {
    name: "register",
    methods: {
        register() {
            
            this.$router.push("/login")
        },
        cancel(){
            this.$router.push("/")
        }
    }
}
</script>
