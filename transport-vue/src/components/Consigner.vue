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
        <el-tabs tab-position="right">
            <el-tab-pane label="个人信息">个人信息</el-tab-pane>

            <el-tab-pane label="申请管理">
                <Application v-bind:id="id"></Application>
            </el-tab-pane>

            <el-tab-pane label="货物跟踪">
                <AgreedGood v-bind:id="id"></AgreedGood>
            </el-tab-pane>

            <el-tab-pane label="货主发货">货主发货</el-tab-pane>

            <el-tab-pane label="司机评价">司机评价</el-tab-pane>

            <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
        </el-tabs>
    </div>
    <div style="margin-top:400px;">123</div>
</div>
</template>

<script>

import Application from "./applications/Application"
import AgreedGood from './applications/AgreedGood'


export default {
    name: "Consigner",
    props: ["id"],   //用户id
    components: {
        Application, AgreedGood
    },
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
