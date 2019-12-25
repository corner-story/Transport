<template>
<div style="margin:80px;">
    <div v-if="isdriver">
        <el-tabs tab-position="left">

            <el-tab-pane label="我的任务">
                <DriverTask></DriverTask>  
            </el-tab-pane>

            <el-tab-pane label="申请记录">
                <DriverApplication></DriverApplication>
            </el-tab-pane>
        </el-tabs>
    </div>
    <div v-else>
        <el-tabs tab-position="left">

            <el-tab-pane label="货主发货">
                <SendGood></SendGood>
            </el-tab-pane>

            <el-tab-pane label="申请管理">
                <Application></Application>
            </el-tab-pane>

            <el-tab-pane label="货物跟踪">
                <AgreedGood></AgreedGood>
            </el-tab-pane>

        </el-tabs>
    </div>

</div>
</template>

<script>
import Application from "../../components/applications/Application"
import AgreedGood from '../../components/applications/AgreedGood'
import DriverTask from '../../components/applications/DriverTask'
import DriverApplication from '../../components/applications/DriverApplication'
import SendGood from '../../components/SendGood'

export default {
    name: "OrderDetail",
    components: {
        Application,
        AgreedGood,
        DriverTask,
        DriverApplication,
        SendGood
    },
    computed: {
        isdriver() {
            return this.$cookies.get("role") === "driver"
        },
    }
}
</script>

<style>

</style>
