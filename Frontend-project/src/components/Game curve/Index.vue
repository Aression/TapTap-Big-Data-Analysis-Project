<template>
    <div>
        <template v-if="!showChart">
            <el-input v-model="search" placeholder="请输入游戏名称" style="width: 300px;margin-right: 10px;margin-top: 30px;">
            </el-input>
            <el-button icon="el-icon-search" circle @click="search_func"></el-button>
            <div style="width: 700px;margin: 0 auto;">
                <el-table :data="tableData" style="width: 100%;cursor: pointer;" @row-click="toChart">
                    <el-table-column prop="name" label="游戏名称" width="250" align="center">
                    </el-table-column>
                    <el-table-column prop="score" label="评分" width="200" align="center">
                    </el-table-column>
                    <el-table-column prop="type" label="游戏类型" width="250" align="center">
                    </el-table-column>
                </el-table>
            </div>
        </template>
        <Chart v-if="showChart" @openChart="openChart" :click_row_name="click_row_name" />
    </div>
</template>

<script>
    import bus from '@/assets/js/bus.js'
    import Chart from './Chart.vue'
    export default {
        components: { Chart },
        data() {
            return {
                search: '',
                showChart: false,
                click_row_name: '',
                // 定义接受数据的变量
                tableData: []
                /*tableData: [
                  { name: '王者荣耀', score: 9.0, type: 'MOBA' },
                  { name: '泰拉瑞亚', score: 9.3, type: '沙盒 像素 开放世界' },
                  { name: '部落与弯刀', score: 8.2, type: '' },
                  { name: '原神', score: 9.6, type: '' },
                  { name: '金铲铲之战', score: 8.5, type: '' },
                  { name: '香肠派对', score: 8.3, type: '' },
                  { name: '...', score: '', type: '' },
                ]*/
            }
        },
        methods: {
            openChart() {
                this.showChart = !this.showChart
            },
            toChart(row) {
                //console.log(row.name)
                this.click_row_name = row.name
                this.openChart()
            },
            search_func() {
                this.getcurveTabs()
                this.search=''
            },
            //try
            async getHotTable() {
                let param = {
                    list_name: '热门榜'
                }
                let res = this.api.getHotTable(param);
                //读取res中的数据
                res.then((result) => {
                    let tableData = result.tableData.map(item => ({
                        //修改接收到的变量名字
                        name: item.game_name, score: item.stat, type: item.category_name
                    }))
                    // 把let定义的tableData赋值给data中定义的 this.tableData
                    this.tableData = tableData
                    // console.log(this.tableData);
                })
                // console.log(res);
            },
            async getcurveTabs() {
                let param = {
                    search_name: this.search
                }
                console.log(this.search);
                let res = this.api.getcurveTabs(param);
                //读取res中的数据
                res.then((result) => {
                    let tableData = result.tableData.map(item => ({
                        //修改接收到的变量名字
                        name: item.game_name, score: item.stat, type: item.category_name
                    }))
                    this.tableData = tableData
                    console.log(this.tableData);
                })
                // console.log(res);
            }
        },
        mounted() {
            if (this.$route.path == '/index/gameCurve') {
                bus.$emit("changeIndex", 2)
            }
            this.getHotTable()
        },
    }
</script>

<style>
</style>