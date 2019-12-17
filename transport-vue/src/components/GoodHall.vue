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
                <span>卡片名称</span>
                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
        </el-card>
		
		<div v-for="good in goods" :key="good.id">
			<br>
			<el-card class="box-card" shadow="hover">
				货物记录
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
			goods: [{id:"1"}, {id:"2"}]
        }
	},

}
</script>

<style>

</style>
