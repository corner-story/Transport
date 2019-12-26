<template>
<div>
    <el-table :data="applications" style="width:100%;">
        <el-table-column label="货物名称" width="250" prop="good_name">
        </el-table-column>
        <el-table-column label="申请人" prop="driver_name" width="250"></el-table-column>
        <el-table-column label="申请人手机" prop="driver_phone" width="250"></el-table-column>
        <el-table-column label="申请时间" prop="timestamp" width="250"></el-table-column>
        <el-table-column label="#" width="250">
            <template slot-scope="scope">
                <el-button size="mini" @click="isagree(scope.row.id, '同意')">同意</el-button>
                <el-button size="mini" type="danger" @click="isagree(scope.row.id, '拒绝')">拒绝</el-button>
            </template>
        </el-table-column>
    </el-table>
</div>
</template>

<script>
// 父组件下传用户id, 根据用户id找到所有申请记录
export default {
    name: "Application",
    data: () => {
        return {
            applications: []
        }
    },
    // props: ["id"],   //用户id
    methods: {
        isagree(id, state) {
            this.$message.info(id + " " + state)
            let data = {
                id: id,
                state: state
            }
            this.$axios.post("/isagree/", data)
                .then((response) => {
                    let data = response.data
                    if (data.state === "success") {
						this.$message.success(data.msg)
						this.get_applications()
                    }else{
						this.$message.error(data.msg)
					}
                })
        },
        get_applications() {
            this.$axios.get("/applications")
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
		this.get_applications()
    }
}
</script>

<style>

</style>
