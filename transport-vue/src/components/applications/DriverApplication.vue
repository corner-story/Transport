<template>
  <div>
      <el-table :data="applications" style="width:100%;">
        <el-table-column label="货物名称" width="100" prop="good_name">
        </el-table-column>
        <el-table-column label="货主" prop="consigner_name" width="100"></el-table-column>
        <el-table-column label="货主手机" prop="consigner_phone_number" width="120"></el-table-column>

        <el-table-column label="起始地" prop="transport_origin" width="200"></el-table-column>
        <el-table-column label="终点" prop="transport_des"  width="200"></el-table-column>
        <el-table-column label="运费" prop="transport_money" width="100"></el-table-column>

        <el-table-column label="货物状态" prop="good_status"></el-table-column>
        <el-table-column label="申请结果" prop="result"></el-table-column>

        <!-- <el-table-column label="#" width="120">
            <template>
                <el-button size="mini">同意</el-button>
            </template>
        </el-table-column> -->
    </el-table>

  </div>
</template>

<script>
export default {
    name: "DriverApplication",
    data: ()=>{
        return {
            applications: []
        }
    },
    methods: {
        get_tasks() {
            this.$axios.get("/dapps", {
                    params: {
                        app_type: "all"
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