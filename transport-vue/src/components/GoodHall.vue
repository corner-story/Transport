<template>
<div style="margin:100px;">
    <div style="margin:100px;">
        <el-row type="flex" justify="center">
            <el-col :span="18">
                <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="search"></el-input>
            </el-col>
        </el-row>
    </div>

    <div style="margin:20px;">
        <el-card class="box-card" shadow="always">
            <span>货物搜索</span>
            <el-button style="float: right; padding: 3px 0" type="text">搜索</el-button>
        </el-card>

        <div v-for="good in goods" :key="good.id">
            <br>
            <el-card class="box-card" shadow="always">
                <el-row tyle="flex" justify="start">
                    <el-col :span="1">
                        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                    </el-col>
                    <el-col :span="2">
                        <span>{{ good.username }}</span>
                    </el-col>
                    <el-col :span="12">
                        <span>{{ good.transport_origin }}</span>-->
                        <span>{{ good.transport_des }}</span>
                    </el-col>
					<el-col :span="7">
                        <el-btn style="float: right" v-on:click="knowmore(good.id)">了解更多 {{ good.id }}</el-btn>
					</el-col>
                </el-row>

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
    created: function () {
        this.$axios.get("/goods", {
                params: {
                    page: 1,
                    limit: 6
                }
            })
            .then((response) => {
                let res = response.data
                console.log(res.data)
                if (res.state === "success") {
                    this.$message.success(res.msg)
                    this.goods = res.data
                }
            })
            .catch((error) => {
                console.log(error)
            })
    },
    methods: {
        knowmore(id){
            this.$message.info("货物ID: " + id)
        }
    }

}
</script>

<style>

</style>
