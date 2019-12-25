<template>
<div style="margin:0px 40px">
    <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="货物名称">
            <el-input v-model="form.good_name"></el-input>
        </el-form-item>
        <el-form-item label="货物类别">
            <el-select v-model="form.good_type" placeholder="请选择货物类别">
                <el-option label="一" value="蔬菜水果"></el-option>
                <el-option label="二" value="易碎品"></el-option>
                <el-option label="三" value="贵重物品"></el-option>
                <el-option label="四" value="电子设备"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="送达日期">
            <el-col :span="11">
                <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
                <el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="运输起点">
            <el-input v-model="form.transport_origin"></el-input>
        </el-form-item>

        <el-form-item label="运输目的地">
            <el-input v-model="form.transport_des"></el-input>
        </el-form-item>
        <el-form-item label="备注">
            <el-input type="textarea" v-model="form.backup"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</div>
</template>

<script>
export default {
    name: "SendGood",
    data() {
        return {
            form: {
                good_name: '',
                good_type: '',
                date1: '',
                date2: '',
                transport_origin: '',
                transport_des: '',
                backup: ''
            }
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!');
        }
    }

}
</script>

<style>

</style>
