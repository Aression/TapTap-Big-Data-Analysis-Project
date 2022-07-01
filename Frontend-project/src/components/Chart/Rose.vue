<template>
    <div>
        <div id="rose" style="width: 700px; height: 550px;"></div>
    </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
    props: ['chartTitle', 'chart_data'],
    data() {
        return {
            myChart: ''
        }
    },
    mounted() {
        this.myChart = echarts.init(document.getElementById('rose'));
        this.myChart.setOption({
            title: {
                text: this.chartTitle,
                textStyle: {
                    fontSize: 15,
                    top: 'center',
                    fontWeight: 'normal',
                },
            },
            legend: {
                top: "bottom"
            },
            textStyle: {
                fontSize: 12
            },
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b} : {c} ({d}%)'
            },
            series: [
                {
                    name: this.chartTitle,
                    type: 'pie',
                    radius: [40, 200],
                    center: ['50%', '50%'],
                    roseType: 'area',
                    itemStyle: {
                        borderRadius: 5
                    },
                    data: this.chart_data
                }
            ]
        })
    },
}
</script>

<style>
</style>