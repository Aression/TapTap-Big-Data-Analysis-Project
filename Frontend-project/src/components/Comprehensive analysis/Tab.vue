<template>
    <div>
        <div class="tab">
            <div style="width: 1000px; margin: auto; ">
                <el-table :data="tableData" style="width: 100%;" height="600">
                    <template v-if="nowIndex === 3">
                        <el-table-column prop="type" :label="nowIndex == 3 ? '游戏厂商/星级' : '游戏类型/星级'" width="150"
                            align="center">
                        </el-table-column>
                        <el-table-column prop="one" label="一星" width="141" align="center">
                        </el-table-column>
                        <el-table-column prop="two" label="二星" width="141" align="center">
                        </el-table-column>
                        <el-table-column prop="three" label="三星" width="141" align="center">
                        </el-table-column>
                        <el-table-column prop="four" label="四星" width="141" align="center">
                        </el-table-column>
                        <el-table-column prop="five" label="五星" width="141" align="center">
                        </el-table-column>
                        <el-table-column prop="total" label="总星数" width="141" align="center">
                        </el-table-column>
                    </template>
                    <template v-if="nowIndex == 2">
                        <el-table-column prop="type" label="游戏类型" width="500" align="center">
                        </el-table-column>
                        <el-table-column prop="list" label="总下载量" width="500" align="center">
                        </el-table-column>
                    </template>
                    <template v-if="nowIndex == 1">
                        <el-table-column prop="type" label="游戏类型" width="500" align="center">
                        </el-table-column>
                        <el-table-column prop="list" label="评论总数" width="500" align="center">
                        </el-table-column>
                    </template>

                    <!-- <el-table-column v-for="{ type, one, two, three, four, five, total } in tableData" :key="type"
                        :one="one" :two="two" :three="three" :four="four" :five="five" :total="total">
                    </el-table-column> -->
                </el-table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['nowIndex', 'data_GameType'],
    data() {
        return {
            tableData: []
        }
    },
    methods: {
        changeform() {
            var s = '['
            var index1 = 0

            for (let index = 0; index < this.data_GameType.length; index++) {
                s += '{'
                s += '"type":"'
                s += this.data_GameType[index].type + '",';
                index1 = 0
                s += '"one":"'
                s += this.data_GameType[index].list[index1++] + '",';
                s += '"two":"'
                s += this.data_GameType[index].list[index1++] + '",';
                s += '"three":"'
                s += this.data_GameType[index].list[index1++] + '",';
                s += '"four":"'
                s += this.data_GameType[index].list[index1++] + '",';
                s += '"five":"'
                s += this.data_GameType[index].list[index1++] + '",';
                s += '"total":"'
                s += this.data_GameType[index].list[index1++] + '"';
                s += '},'
            }
            s += '{'
            s += '"type":"'
            s += this.data_GameType[this.data_GameType.length - 1].type + '",';
            index1 = 0
            s += '"one":"'
            s += this.data_GameType[this.data_GameType.length - 1].list[index1++] + '",';
            s += '"two":"'
            s += this.data_GameType[this.data_GameType.length - 1].list[index1++] + '",';
            s += '"three":"'
            s += this.data_GameType[this.data_GameType.length - 1].list[index1++] + '",';
            s += '"four":"'
            s += this.data_GameType[this.data_GameType.length - 1].list[index1++] + '",';
            s += '"five":"'
            s += this.data_GameType[this.data_GameType.length - 1].list[index1++] + '",';
            s += '"total":"'
            s += this.data_GameType[this.data_GameType.length - 1].list[index1++] + '"';
            s += '}'
            s += ']'
            console.log(JSON.parse(s))
            this.tableData = JSON.parse(s)
        },
    },
    mounted() {
        if (this.nowIndex == 3) {
            this.changeform()
        }
        else {
            this.tableData = this.data_GameType
        }
        console.log( this.tableData )
        //this.changeform_manu()
    }
}
</script>


<style scoped>
.tab {
    width: 100%;
    height: 100%;
    /* margin: 0 auto; */
    margin: 0 auto;
    text-align: center;
    display: flex;
    justify-content: center;
    align-content: center;
}
</style>