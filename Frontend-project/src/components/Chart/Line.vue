<template>
  <div>
    <div class="chart">
      <div class="chart_box">
        <div id="score" style="width: 700px; height: 200px"></div>
      </div>
      <div class="chart_box">
        <div id="price" style="width: 700px; height: 200px"></div>
      </div>
      <div class="chart_box">
        <div id="emojibar" style="width: 700px; height: 200px"></div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  props: ['Line', 'com_emoji'],
  data() {
    return {
      scoreChart: '',
      priceChart: '',
      emojiChart: ''
    }
  },
  methods: {
    //处理多个图形的自适应
    getEchartObj(){
        let arr = ['scoreChart','priceChart','emojiChart']
        arr.map(v => {
        let  _ref=this.$refs[v];//遍历生成的折线图的Dom
        let myEchars = _ref?echarts.getInstanceByDom(_ref):undefined;
        if(myEchars!== undefined){
          myEchars.resize();
        }
      })
    }
  },
  mounted() {
    // console.log(this.Line)
    this.scoreChart = echarts.init(document.getElementById('score'));
    this.priceChart = echarts.init(document.getElementById('price'));
    this.emojiChart = echarts.init(document.getElementById('emojibar'));
    window.addEventListener("resize", () => {
        this.getEchartObj();
    });
    this.scoreChart.setOption({
      title: {
        text: '评分变化',
        textStyle: {
          fontSize: 15,
          top: 'center',
          fontWeight: 'normal',
        },
      },
      tooltip: {
        trigger: 'axis'
      },
      xAxis: {
        type: 'category',
        data: this.Line[0].data1,
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: '评分变化',
          data: this.Line[0].data2,
          type: 'line'
        }
      ]
    })
    this.priceChart.setOption({
      title: {
        text: '价格变化',
        textStyle: {
          fontSize: 15,
          top: 'center',
          fontWeight: 'normal',
        },
      },
      tooltip: {
        trigger: 'axis'
      },
      xAxis: {
        type: 'category',
        data: this.Line[0].data1,
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: '价格变化',
          data: this.Line[0].data3,
          type: 'line'
        }
      ]
    })
    this.emojiChart.setOption({
      title: {
        text: '评论情感分布',
        textStyle: {
          fontSize: 15,
          top: 'center',
          fontWeight: 'normal',
        },
      },
      tooltip: {
        trigger: 'axis'
      },
      xAxis: {
        type: 'value'
      },
      yAxis: {
        type: 'category',
        data: ['积极', '消极']
      },
      series: [
        {
          name: '评论数量',
          data: this.com_emoji,
          type: 'bar'
        }
      ]
    })
    
  },
}


</script>

<style scoped>
.chart {
  width: 100%;
  height: 450px;
  /* margin-top: 10px; */
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
}

.chart .chart_box {
  width: 70%;
  height: 150px;
  border: 1px solid rgb(79,79,79);
  margin-top: 10px;
}
</style>