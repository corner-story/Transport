<template>

        <div>个人中心 {{ user_info }}</div>
        
</template>
    
<script>

    export default {
        name: "UserDetail",
        computed: {
            user_info(){
                return this.$route.params.usertype + this.$route.query.id
            }
        }
    }

</script>