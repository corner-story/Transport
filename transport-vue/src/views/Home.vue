<template>

    <GoodHall></GoodHall>

</template>

<script>

import GoodHall from './good/GoodHall'

export default {
    name: "home",
    data: () => {
        return {
            currentTab: GoodHall
        }
    },
    components: {
        GoodHall
    },

    created: function () {
        this.$message.success("Hello, " + this.$cookies.get("username") + " , 欢迎使用物流-EARTH!")
    }
}
</script>
