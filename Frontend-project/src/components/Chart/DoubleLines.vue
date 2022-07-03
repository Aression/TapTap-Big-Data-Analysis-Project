<template>
    <div>
        <div class="chart">
            <div id="doubleLines" style="width: 1100px; height: 450px"></div>
        </div>
    </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
    props: ['doubleline_data'],
    data() {
        return {
            myChart: '',
            date: [],
            data_a: [],
            data_c: []
        }
    },
    methods: {
        toArray() {
            for (let index = 0; index < this.doubleline_data.length; index++) {
                this.date.push(this.doubleline_data[index].date)
                this.data_a.push(this.doubleline_data[index].data_a)
                this.data_c.push(this.doubleline_data[index].data_c)
            }
            // console.log(this.date)
            // console.log(this.data_a)
            // console.log(this.data_c)
        }
    },
    mounted() {
        // this.toArray()
        this.myChart = echarts.init(document.getElementById('doubleLines'));
        this.myChart.setOption({
            tooltip: {
                trigger: 'axis'
            },
            legend: {},
            xAxis: {
                type: 'category',
                data: this.doubleline_data[0].date
            },
            yAxis: {
                type: 'value',
                axisLabel: {
                    formatter: '{value}'
                }
            },
            series: [
                {
                    name: '综合关注度',
                    type: 'line',
                    data: this.doubleline_data[0].data_a
                },
                {
                    name: '叫座率',
                    type: 'line',
                    data: this.doubleline_data[0].data_c
                }
            ]
        })
    },
}
</script>

<style scoped>
.chart {
    width: 100%;
    display: flex;
    justify-content: center;
}
</style>