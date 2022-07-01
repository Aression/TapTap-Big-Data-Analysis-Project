<template>
    <div>
        <div style="width: 700px;margin: 0 auto;">
            <el-table :data="tableData" style="width: 100%;" height="400">
                <el-table-column prop="name" label="游戏名称" width="250" align="center">
                </el-table-column>
                <el-table-column prop="score" label="评分" width="200" align="center">
                </el-table-column>
                <el-table-column prop="type" label="游戏类型" width="250" align="center">
                    <template slot="header" slot-scope="scope">
                        游戏类型
                        <i class="el-icon-s-data" @click="toChart"></i>
                    </template>
                </el-table-column>
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