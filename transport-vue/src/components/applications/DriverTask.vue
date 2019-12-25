<template>
<div>
    <el-table :data="applications" style="width:100%;">
        <el-table-column label="货物名称" width="100" prop="good_name">
        </el-table-column>
        <el-table-column label="货主" prop="consigner_name" width="100"></el-table-column>
        <el-table-column label="货主手机" prop="consigner_phone_number" width="120"></el-table-column>

        <el-table-column label="起始地" prop="transport_origin" width="150"></el-table-column>
        <el-table-column label="终点" prop="transport_des"  width="150"></el-table-column>
        <el-table-column label="运费" prop="transport_money" width="120"></el-table-column>

        <el-table-column label="货物状态" prop="good_status"></el-table-column>
        <el-table-column label="申请结果" prop="result"></el-table-column>

        <el-table-column label="#" width="250">
            <template slot-scope="scope">

                <el-button size="mini" v-if="scope.row.next_status === '确定'" disabled>运输完成</el-button>
                <el-button size="mini" v-else type="success" @click="change_status(scope.row.id, scope.row.next_status)">{{ scope.row.next_status }}</el-button>
            </template>
        </el-table-column>
    </el-table>
</div>
</template>

<script>
export default {
    name: "DriverTask",
    data: () => {
        return {
            applications: []
        }
    },
    methods: {
        change_status(id, status){
            // this.$message.success(id + status)
            let data = {
                id: id,
                status: status
            }
            this.$axios.post("/appstatus/", data)
                .then((response) => {
                    let data = response.data
                    if (data.state === "success") {
                        // this.$message.success(data.msg)
                        // this.applications = data.data
                        this.get_tasks()
                    } else {
                        this.$message.error(data.msg)
                    }
                    
                })

        },
        get_tasks() {
            this.$axios.get("/dapps", {
                    params: {
                        app_type: "同意"
                    }
                })
                .then((response) => {
                    let data = response.data
                    if (data.state === "success") {
                        this.$message.success(data.msg)
                        this.applications = data.data
                    } else {
                        this.$message.error(data.msg)
                    }
                })
        }
    },
    created: function () {
        this.get_tasks()

    }
}
</script>

<style>

</style>
