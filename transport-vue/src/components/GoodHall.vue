<template>
<div style="margin:100px">
    <div style="margin:100px;">
        <el-row type="flex" justify="center">
            <el-col :span="18">
                <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="search"></el-input>
            </el-col>
        </el-row>
    </div>

    <div style="margin:20px">
        <el-card class="box-card" shadow="always">
                <span>货物搜索</span>
                <el-button style="float: right; padding: 3px 0" type="text">搜索</el-button>
        </el-card>
		
		<div v-for="good in goods" :key="good.id">
			<br>
			<el-card class="box-card" shadow="hover">
				<span>{{ good.good_name }}</span> &nbsp;
				<span>{{ good.good_type }}</span> &nbsp;
				<span>{{ good.transport_origin }}</span>--> &nbsp;
				<span>{{ good.transport_des }}</span> &nbsp;
				<span>{{ good.good_status }}</span> &nbsp;
			</el-card>
		</div>
    </div>
</div>
</template>

<script>
export default {
    name: "GoodHall",
    data: () => {
        return {
			search: "",
			goods: []
        }
	},
	created: function(){
		this.$axios.get("/good")
			.then((response)=>{
				let res = response.data
				console.log(res.data)
				if(res.state === "success"){
					this.$message.success(res.msg)
					this.goods = res.data
				}
			})
			.catch((error)=>{
				console.log(error)
			})
	}

}
</script>

<style>

</style>
