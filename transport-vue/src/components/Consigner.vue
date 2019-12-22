<template>
<div style="margin:20px 100px">
    <div>
        <el-card>
            <div style="display: inline-block;margin-top:15px;">
                <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
            </div>

            <div style="display: inline-block; margin: 15px;">
                <div><strong>货主名称: </strong>{{ consigner.username }}</div>
                <div><strong>手机号: </strong>{{ consigner.phone_number }}</div>
                <div><strong>邮箱: </strong>{{ consigner.email }}</div>
                <div><strong>常供货物: </strong>{{ consigner.general_good }}</div>
                <div><strong>常发地址: </strong>{{ consigner.address }}</div>
                <div>
                    <strong>信用: </strong>
                    <el-rate style="display: inline-block;" v-model="value" disabled show-score text-color="#ff9900" score-template="{value}">
                    </el-rate>
                </div>
            </div>
        </el-card>
    </div>
    <div style="margin:60px;"></div>
    <div>
        <el-tabs tab-position="right" style="height: 200px;">
            <el-tab-pane label="用户管理">用户管理</el-tab-pane>
            <el-tab-pane label="配置管理">配置管理</el-tab-pane>
            <el-tab-pane label="角色管理">角色管理</el-tab-pane>
            <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
        </el-tabs>
    </div>
</div>
</template>

<script>
export default {
    name: "Consigner",
    props: ["id"],
    data: () => {
        return {
            value: 3,
            consigner: {}
        }
    },
    created: function () {
        this.$axios.get("/consigner", {
                params: {
                    id: this.id
                }
            })
            .then((response) => {
                let data = response.data
                if (data.state === "success") {
                    this.consigner = data.data
                    this.$message.success(data.msg)
                } else {
                    this.$message.error(data.msg)
                }
            })
    }

}
</script>
