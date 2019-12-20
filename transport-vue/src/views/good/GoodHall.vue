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
            <div>
                <el-row>
                    <el-col :span="1"><strong>城市:</strong></el-col>
                    <el-col v-for="city in citys.display" :key="city.name" :span="1"><el-link @click="search_info(city.name.substr(0,2))"> {{ city.name.substr(0,2) }}</el-link></el-col>
                    <el-col :span="6"><el-button size="mini" style="float:right;">所有地区</el-button></el-col>
                </el-row>
                <el-row>
                    <el-col :span="1"><strong>类型:</strong></el-col>
                    <el-col v-for="goodtype in goodtypes" :key="goodtype" :span="1"><el-link @click="search_info(goodtype)"> {{ goodtype }}</el-link></el-col>
                </el-row>
            </div>
        </el-card>

        <el-divider></el-divider>
        <el-table :data="goods" style="width:100%;">
            <el-table-column label="发货人" width="120">
                <template slot-scope="scope">
                    <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                    <el-link :underline="false" @click="to_usercenter(scope.row.consigner_id)">{{ scope.row.username }}</el-link>
                </template>
            </el-table-column>
            <el-table-column label="货物" prop="good_name" width="80"></el-table-column>
            <el-table-column label="发货地" prop="transport_origin"></el-table-column>
            <el-table-column label="终点" prop="transport_des"></el-table-column>
            <el-table-column label="#" width="120">
                <template slot-scope="scope">
                    <el-button style="margin-left: 10px" type="info" size="mini" @click="good_details(scope.row.id)" plain>货物详情</el-button>
                </template>
            </el-table-column>
        </el-table>

        
    </div>
</div>
</template>

<script>
export default {
    name: "GoodHall",
    data: () => {
        return {
            search: "",
            goods: [],
            loading: false,
            citys: {
                display: [],
                all: []
            },
            goodtypes: ["水果", "玻璃", "金属", "其他"]      
        }
    },
    created: function () {
        // 获取货物信息
        this.$axios.get("/goods/", {
                params: {
                    page: 1,
                    limit: 8
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
            

        // 获取城市信息
        this.$axios.get("https://unpkg.com/province-city-china@4.0.3/dist/province.json", {withCredentials: false})
            .then((response) =>{
                let data = response.data
                // console.log(data)
                let length = data.length
                this.citys.display = data.slice(0, length/2)
                this.citys.all = data
            })
    },
    methods: {
        good_details(id) {
            // this.$message.info("货物ID: " + id)
            this.$router.push({ name: 'good', params: { id: id }})
        },
        search_info(city){
            this.$message.info("搜索城市: " + city)
        },
        to_usercenter(id){
            // 转到consigner的个人界面
            if(id !== null){
                // this.$message.info("consigner id: " + id)
                this.$router.push({ name: 'user', params: { usertype: 'consigner'}, query: {id: id}})
            }
        }
    }

}
</script>

<style>

</style>
