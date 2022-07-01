<template>
    <div>
        <div class="tab">
            <div style="width: 750px;">
                <el-table :data="tableData" style="width: 100%;" height="360">
                    
                    <el-table-column prop="type" :label="nowIndex == 3 ? '游戏厂商/星级' : '游戏类型/星级'" width="140"
                        align="center">
                    </el-table-column>
                    <el-table-column prop="one" label="一星" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="two" label="二星" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="three" label="三星" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="four" label="四星" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="five" label="五星" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="total" label="总数" width="100" align="center">
                    </el-table-column>
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

            for (let index = 0; index < 5; index++) {
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
            // console.log(JSON.parse(s))
            this.tableData = JSON.parse(s)
        },
    },
    mounted() {
        this.changeform()
        // console.log(this.data_GameType)
        //this.changeform_manu()
    }
}
</script>


<style scoped>
.tab {
    width: 100%;
    height: 100%;
    /* margin: 0 auto; */
    margin: 0 auto; text-align: center;
    display: flex;
    justify-content: center;
    align-content: center;
}
</style>