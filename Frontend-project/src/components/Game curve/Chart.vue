<template>
    <div>
        <div class="button">
            <el-button @click="closeChart">返回</el-button>
        </div>
        <BrokenLine v-if="Line.length > 0" :Line.sync="Line"  :com_emoji="com_emoji" />
    </div>
</template>

<script>
import BrokenLine from "../Chart/Line.vue";
export default {
        props: ['click_row_name'],
    components: { BrokenLine },
    data() {
        return {
            Line: [],
            com_emoji:[]
        }
    },
    methods: {
        closeChart() {
            this.$emit('openChart')
        },
        async getcurve() {
            let param = {
            list_name: this.click_row_name
        }
                    console.log(this.click_row_name)
        let res = this.api.getcurve(param);
        //读取res中的数据
                res.then((result) => {
                    let Line = result.Line.map(item => ({
                        //修改接收到的变量名字
                        data1: item.date, data2: item.scoredata, data3: item.pricedata
                    }))
                    // 把let定义的tableData赋值给data中定义的 this.tableData
                    this.Line = Line
                    console.log(this.Line);

                    // let com_emoji = result.com_emoji.map(item => ({
                        //修改接收到的变量名
                    // }))
                    // 把let定义的tableData赋值给data中定义的 this.tableData
                    this.com_emoji = result.com_emoji
                    console.log(this.com_emoji);
                })
        //console.log(res);
        }
    },
    mounted() {
        this.getcurve();
    }
}
</script>

<style scoped>
.button {
    position: absolute;
    top: 12%;
    left: 13%;
}
</style>