<template>
  <div>
    <el-tabs v-if="!showChart" v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="热门榜" name="热门榜">
        <Hot @openChart="openChart" :chartTitle="chartTitle" :tableData="tableData" />
      </el-tab-pane>
      <el-tab-pane label="预约榜" name="预约榜">
        <Hot @openChart="openChart" :chartTitle="chartTitle" :tableData="tableData" />
      </el-tab-pane>
      <el-tab-pane label="热玩榜" name="热玩榜">
        <Hot @openChart="openChart" :chartTitle="chartTitle" :tableData="tableData" />
      </el-tab-pane>
      <el-tab-pane label="厂商榜" name="厂商榜">
        <Hot @openChart="openChart" :chartTitle="chartTitle" :tableData="tableData" />
        <!-- 把tableData传到HOT文件中 :tableData="tableData" -->
      </el-tab-pane>
    </el-tabs>
    <Chart v-if="showChart" @openChart="openChart" :chartTitle="chartTitle" :chart_data='chart_data' />
  </div>
</template>

<script>
import bus from '@/assets/js/bus';
import Chart from './Chart.vue'
import Hot from './Hot.vue'
export default {
  components: { Hot, Chart },
  data() {
    return {
      activeName: '热门榜',
      chartTitle: '热门榜',
      showChart: false,
      // 定义接受数据的变量
      tableData: [],
      chart_data: []
    }
  },
  methods: {
    handleClick(tab) {
      // console.log(tab._props.name);
      this.activeName = tab._props.name
      this.chartTitle = tab._props.name
      this.getHotTable()
      this.getHotTableChart()
    },
    openChart(val) {
      this.showChart = !this.showChart
      // this.chartTitle = val
    },
    async getHotTable() {
      let param = {
        list_name: this.activeName
      }
      let res = this.api.getHotTable(param);
      //读取res中的数据
      // console.log(res)
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
    async getHotTableChart() {
      let param = {
        list_name: this.chartTitle
      }
      let res = this.api.getHotTableChart(param);
      //读取res中的数据
      res.then((result) => {
        let chart_data = result.chart_data.map(item => ({
          name: item.category_name, value: item.amount
        }))
        this.chart_data = chart_data
        // console.log(this.chart_data);
      })
    }
  },
  mounted() {
    if (this.$route.path == '/index/basicData') {
      bus.$emit("changeIndex", 1)
    }
    this.getHotTable()
    this.getHotTableChart()
  },
}
</script>

<style scoped>
.tabs {
  width: 100%;
  height: 200px;
  border: 1px solid red;
}
</style>