<template>
    <div>
        <div id="bar" style="width: 500px; height: 500px;margin-top: -60px;"></div>
    </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
    data() {
        return {
            myChart: ''
        }
    },
    mounted() {
        this.myChart = echarts.init(document.getElementById('bar'));
        this.myChart.setOption({
            dataset: {
                source: [
                    ['score', 'amount', 'product'],
                    [20, 20, 'Matcha Latte'],
                    [21, 21, 'Milk Tea'],
                    [22, 22, 'Cheese Cocoa'],
                    [23, 23, 'Cheese Brownie'],
                    [24, 24, 'Matcha Cocoa'],
                    [25, 25, 'Tea'],
                    [26, 26, 'Orange Juice'],
                    [27, 27, 'Lemon Juice'],
                    [28, 28, 'Walnut Brownie']
                ]
            },
            grid: { containLabel: true },
            xAxis: { name: 'amount' },
            yAxis: { type: 'category' },
            visualMap: {
                orient: 'horizontal',
                left: 'center',
                min: 10,
                max: 100,
                text: ['High Score', 'Low Score'],
                // Map the score column to color
                dimension: 0,
                inRange: {
                    color: ['#65B581', '#FFCE34', '#FD665F']
                }
            },
            series: [
                {
                    type: 'bar',
                    encode: {
                        // Map the "amount" column to X axis.
                        x: 'amount',
                        // Map the "product" column to Y axis
                        y: 'product'
                    }
                }
            ]
        })
    },
}
</script>

<style>
</style>