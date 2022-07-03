<template>
    <div>
        <div style="width: 1000px;margin: 0 auto;">
            <el-table :data="tableData" style="width: 100%;" height="400">
                <template v-if="chartTitle !== '厂商榜'">
                    <el-table-column key="1" prop="name" label="游戏名称" width="250" align="center">
                    </el-table-column>
                    <el-table-column  key="2" prop="score" label="评分" width="200" align="center">
                    </el-table-column>
                    <el-table-column  key="3" prop="type" label="游戏类型" width="250" align="center">
                        <template slot="header" slot-scope="scope">
                            游戏类型
                            <i class="el-icon-s-data" @click="toChart"></i>
                        </template>
                    </el-table-column>
                </template>

                <template v-if="chartTitle == '厂商榜'">
                    <el-table-column key="1" prop="name" label="厂商名称" width="350" align="center">
                    </el-table-column>
                    <el-table-column key="2" prop="score" label="总下载量" width="350" align="center">
                        <template slot="header" slot-scope="scope">
                            总下载量
                            <i class="el-icon-s-data" @click="toChart"></i>
                        </template>
                    </el-table-column>
                </template>
            </el-table>
        </div>
    </div>
</template>

<script>
import Vue from "vue";
export default {
    //接受参数-tableData
    props: ['chartTitle', 'tableData'],
    data() {
        return {
            chart_data: []
        }
    },
    methods: {
        toChart() {
            this.$emit('openChart', '')
        }
    },
    mounted() {
    }
}
</script>

<style scoped>
</style>