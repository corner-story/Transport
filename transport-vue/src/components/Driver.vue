<template>
	<div>Driver! {{ id }}</div>
</template>

<script>
export default {
	name: "Driver",
	data: ()=>{
		return {
			driver: {}
		}
	},
	props: ["id"]
}
</script>

<style>

</style>