<template>

</template>

<script>
export default {
    name: "home",
    props: {
        source: String,
    },
    data: () => ({
        
    }),

    methods: {
        changeTheme() {
            if (this.$vuetify.theme.dark) {
                this.$vuetify.theme.dark = false
            } else {
                this.$vuetify.theme.dark = true
            }
            alert(this.$vuetify.theme.dark)
        }
    }
}
</script>
