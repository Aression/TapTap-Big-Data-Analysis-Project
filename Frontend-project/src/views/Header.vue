<template>
    <div>
        <div class="header">
            <div class="header_title">
                Group_name
            </div>
            <div class="header_nav">
                <ul>
                    <li v-for="(item, index) in navArr" :key="index" :class="[nowIndex == index ? 'selected' : '']"
                        @click="changeNav(index, item.router)">
                        {{ item.name }}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import bus from '../assets/js/bus.js'
export default {
    data() {
        return {
            nowIndex: 0,
            navArr: [
                { name: '首页', router: '/index/main' },
                { name: '基础数据', router: '/index/basicData' },
                { name: '游戏曲线', router: '/index/gameCurve' },
                { name: '综合分析', router: '/index/comprehensiveAnalysis' },
                { name: '团队成员', router: '/index/teamMembers' },
            ]
        }
    },
    methods: {
        changeNav(index, router) {
            this.nowIndex = index
            this.$router.push(router)
        }
    },
    mounted() {
        let that = this;
        bus.$on('changeIndex', function (index) {
            that.nowIndex = index
        })
    },
}
</script>

<style scoped>
.header {
    width: 75%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
}

.header .header_title {
    font-size: larger;
    color: rgb(98, 124, 147);
}

ul {
    display: flex;
    list-style: none;
}

li {
    margin: 10px;
    cursor: pointer;
    color: rgb(98, 124, 147);
}

.selected {
    font-weight: bold;
}
</style>