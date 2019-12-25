<template>
<div style="margin:0px 80px">
    <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="货物名称">
            <el-input v-model="form.good_name"></el-input>
        </el-form-item>
        <el-form-item label="货物类别">
            <select v-model="form.good_type">
                <option disabled value="">请选择</option>
                <option v-for="gt in goodtypes" v-bind:value="gt.id" v-bind:key="gt.id">
                    {{ gt.type_name}}
                </option>
            </select>
        </el-form-item>
        <el-form-item label="运输时间">
            <el-col :span="11">
                <el-input v-model="form.transport_time"></el-input>
            </el-col>
        </el-form-item>
        <el-form-item label="运输起点">
            <el-input v-model="form.transport_origin"></el-input>
        </el-form-item>

        <el-form-item label="运输终点">
            <el-input v-model="form.transport_des"></el-input>
        </el-form-item>

        <el-form-item label="运费">
            <el-input v-model="form.transport_money"></el-input>
        </el-form-item>

        <el-form-item label="备注">
            <el-input type="textarea" v-model="form.backup"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">发布</el-button>
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
                transport_origin: '',
                transport_des: '',
                transport_money: '',
                transport_time: '',
                backup: ''
            },
            goodtypes: []
        }
    },
    methods: {
        onSubmit() {
            let data = this.form;
            this.$axios.post("/sendgood/", data)
            .then((response) => {
                let data = response.data
                if (data.state === "success") {
                    this.$message.success(data.msg)
                }else{
                    this.$message.error(data.msg)
                }

            })
        }
    },
    created: function () {
        // 获取货物种类信息
        this.$axios.get("/goodtypes")
            .then((response) => {
                let data = response.data
                if (data.state === "success") {
                    this.goodtypes = data.data
                    console.log(this.goodtypes)
                }
            })
    }

}
</script>

<style>

</style>
