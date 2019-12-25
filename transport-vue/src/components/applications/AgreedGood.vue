<template>
<div>
    <el-table :data="goods" style="width:100%;">
        <el-table-column label="货物名称" width="100" prop="good_name">
        </el-table-column>
        <el-table-column label="承运司机" prop="driver_name" width="80"></el-table-column>
        <el-table-column label="司机手机" prop="driver_phone" width="120"></el-table-column>
        <el-table-column label="发货地" prop="transport_origin"></el-table-column>
		<el-table-column label="终点" prop="transport_des"></el-table-column>
		<el-table-column label="货物状态" prop="good_status" width="120"></el-table-column>
        <el-table-column label="#" width="120">
            <template slot-scope="scope">
                <el-button size="mini" v-if="scope.row.good_status === '运输完成'" type="success">确定收货</el-button>
                <el-button size="mini" v-else disabled>确定收货</el-button>
            </template>
        </el-table-column>
    </el-table>
</div>
</template>

<script>
export default {
    name: "AgreedGood",
    data: () => {
        return {
            goods: []
        }
    },
    methods: {
        get_goods() {
            // 该界面只有已经登陆的发货人才能看见, 所以不用传参数
            this.$axios.get("/goods/agreed")
                .then((response) => {
                    let data = response.data
                    if (data.state === "success") {
                        this.$message.success(data.msg)
                        this.goods = data.data
                    } else {
                        this.$message.error(data.msg)
                    }
                })
        }
    },
    created: function () {
        this.get_goods()
    }
}
</script>

<style>

</style>
