<template>
    <div class="Main">
        <div class="main_text">
            <span style="color: rgb(88, 113, 135);font-weight: bold;font-size: 35px;">TapTap游戏网站大数据分析</span>
            <br>
            <span style="font-size: 20px">为您持续呈现TapTap平台的最新综合数据</span>
        </div>
        <div class="main_img">
            <div class="main_img_box" v-for="(item, index) in mainImgArr" :key="index"
                @click="changeNav(index, item.router)">
                <img :src='item.img' style="width: 100%;height: 100%;">
            </div>
        </div>
    </div>
</template>

<script>
import bus from '../assets/js/bus'
export default {
    data() {
        return {
            mainImgArr: [
                { img: require('../assets/img/Basic data.png'), router: '/index/basicData' },
                { img: require('../assets/img/Game curve.png'), router: '/index/gameCurve' },
                { img: require('../assets/img/Comprehensive analysis of.png'), router: '/index/comprehensiveAnalysis' }
            ]
        }
    },
    methods: {
        changeNav(index, router) {
            this.$router.push(router)
            bus.$emit("changeIndex", index + 1)
        }
    },
    mounted() {
        if (this.$route.path == '/index/main') {
            bus.$emit("changeIndex", 0)
        }
    },
}
</script>

<style scoped>
.Main {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    margin-top: 3%;
}

.main_text {
    width: 100%;
}

.main_img {
    width: 90%;
    height: 250px;
    display: flex;
    margin: 0 auto;
    cursor: pointer;
    margin-top: 30px;
    justify-content: space-evenly;
    align-items: center;
    border-radius: 50px;
    border: 2px solid rgb(129, 129, 129);
}

.main_img .main_img_box {
    width: 21%;
    height: 200px;
    border: 2.5px solid rgb(121, 121, 121);
}

.main_img .main_img_box:hover {
    border: 2.5px solid rgb(65, 143, 215);
}
</style>