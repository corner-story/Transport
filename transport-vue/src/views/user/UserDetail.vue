<template>
    <div v-if="isdriver">
        <DriverComponent v-bind:id="user_id"></DriverComponent> 
    </div>
    <div v-else>
        <ConsignerComponent v-bind:id="user_id"></ConsignerComponent>
    </div>
</template>

<script>

    import ConsignerComponent from "../../components/Consigner"
    import DriverComponent from "../../components/Driver"

    // 所有的用户中心都会跳转到该界面
    // 使用usertype：consigner, driver来区别不同的类型用户, 使用id确定用户
    export default {
        name: "UserDetail",
        components:{
            ConsignerComponent, DriverComponent
        }, 
        computed: {
            isdriver(){
                return this.$route.params.usertype === "driver"
            },
            user_id(){
                return this.$route.query.id
            }
        },
        
    }

</script>