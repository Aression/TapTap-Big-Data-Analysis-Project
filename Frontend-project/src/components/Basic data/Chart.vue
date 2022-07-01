<template>
    <div>
        <!-- <span class="chart_text">{{ chartTitle }}</span> -->
        <div class="button">
            <el-button icon="el-icon-close" @click="closeChart" circle></el-button>
        </div>
        <div class="chart">
            <Rose :chartTitle="chartTitle" :chart_data="chart_data"></Rose>
        </div>
    </div>
</template>

<script>
import Rose from "../Chart/Rose.vue";
export default {
    props: ['chartTitle','chart_data'],
    components: { Rose },
    data() {
        return {

        }
    },
    methods: {
        closeChart() {
            this.$emit('openChart', '')
        }
    },
    mounted() {

    }

}
</script>

<style scoped>
.chart_text {
    font-size: 20px;
    color: rgb(98, 124, 147);
}

.button {
    position: absolute;
    top: 12%;
    right: 13%;
}

.chart {
    width: 90%;
    height: 500px;
    margin: 0 auto;
    margin-top: 30px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
}
</style>