<template>
<div class="amap-page-container" style="margin:0px 60px">
    <div :style="{width:'100%',height:'600px'}">
        <!-- <el-amap-search-box class="search-box" :search-option="searchOption" :on-search-result="onSearchResult"></el-amap-search-box> -->
        <el-amap vid="amap" :center="center" :plugin="plugin">
            <!-- <el-amap-marker v-for="marker in markers" :key="marker" :position="marker"></el-amap-marker> -->
        </el-amap>
    </div>
    <el-card class="box-card" style="margin-top:60px;">
        <div slot="header" class="clearfix">
            <span><strong>货物名称:</strong> {{ good.good_name }}</span>
            <el-button style="float: right; padding: 3px 0" type="text">查看发货地点</el-button>
        </div>

		<ul>
			<li><strong>发货人: </strong>{{ good.consigner }}  {{ good.phone_number}}</li>
			<li><strong>发货地: </strong> {{ good.transport_origin }}</li>
			<li><strong>终点站: </strong> {{ good.transport_des }}</li>
			<li><strong>运费: </strong> {{ good.transport_money }}</li>
			<li><strong>备注: </strong> {{ good.backup }}</li>
		</ul>
    </el-card>
	<div style="margin:100px;">
		<el-divider></el-divider>
	</div>
</div>
</template>

<script>
export default {
    data() {
        const self = this;
        return {
            good: {},
            center: [121.59996, 31.197646],
            loaded: false,
            markers: [
                [121.59996, 31.197646],
                [121.40018, 31.197622],
                [121.69991, 31.207649]
            ],
            plugin: [{
                pName: 'ToolBar',
                events: {
                    init(instance) {
                        console.log(instance);
                    }
                }
            }],
            events: {
                click(e) {

                }
            }
        }
    },
    computed: {

    },
    created: function () {
        let id = this.$route.params.id
        this.$axios.get("/good/", {
                params: {
                    id: id
                }
            })
            .then((response) => {
                let data = response.data
                if (data.state === "success") {
                    this.good = data.data
                }
            })
    },
    methods: {

    }
}
</script>

<style lang="stylus" scoped>
.search-box {
    position: absolute;
    top: 80px;
    right: 80px;
}
</style>
