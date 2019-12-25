<template>
<div style="margin:20px 100px">
    <div>
        <el-card>
            <div style="display: inline-block;margin-top:15px;">
                <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
            </div>

            <div style="display: inline-block; margin: 15px;">
                <div><strong>司机名称: </strong>{{ driver.username }}</div>
                <div><strong>手机号: </strong>{{ driver.phone_number }}</div>
                <div><strong>邮箱: </strong>{{ driver.email }}</div>
                <div><strong>汽车类型: </strong>{{ driver.car_type }}</div>
                <div><strong>车牌号码: </strong>{{ driver.car_number }}</div>
				<div><strong>备注: </strong>{{ driver.buckup }}</div>
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

            <el-tab-pane label="接单记录">接单记录</el-tab-pane>

            <el-tab-pane label="司机评价">司机评价</el-tab-pane>
        </el-tabs>
    </div>
    <div style="margin-top:400px;">123</div>
</div>
</template>

<script>
export default {
    name: "Driver",
    data: () => {
        return {
			value: 4,
            driver: {}
        }
    },
	props: ["id"],
	created: function () {
        this.$axios.get("/driver", {
                params: {
                    id: this.id
                }
            })
            .then((response) => {
                let data = response.data
                if (data.state === "success") {
                    this.driver = data.data
                    this.$message.success(data.msg)
                } else {
                    this.$message.error(data.msg)
                }
            })
    }
}
</script>

<style>

</style>
