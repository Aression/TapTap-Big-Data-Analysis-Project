<template>
    <div>
        <div id="pie" style="width: 600px; height: 500px"></div>
    </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
    props: [],
    data() {
        return {
            myChart: ''
        }
    },
    mounted() {
        this.myChart = echarts.init(document.getElementById('pie'));
        this.myChart.setOption({
            title: {
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            legend: {
                orient: 'vertical',
                left: 'left'
            },
            series: [
                {
                    type: 'pie',
                    radius: '50%',
                    data: [
                        { value: 1048, name: 'Search Engine' },
                        { value: 735, name: 'Direct' },
                        { value: 580, name: 'Email' },
                        { value: 484, name: 'Union Ads' },
                        { value: 300, name: 'Video Ads' }
                    ],
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        })
    },

}
</script>

<style>
</style>