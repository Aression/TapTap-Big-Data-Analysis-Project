<template>
    <div>
        <el-container>
            <el-header>
                <Header />
            </el-header>
            <el-main>
                <div class="main">
                    <!-- <Main /> -->
                    <router-view></router-view>
                </div>
            </el-main>
            <el-footer>
                © Copyright Mamba. All Rights Reserved
            </el-footer>
        </el-container>
    </div>
</template>

<script>
import Header from "./Header.vue";
import Main from "../components/Main.vue";
export default {
    components: { Header, Main },
    data() {
        return {}
    },
    methods: {},
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
}
</style>

<style scoped>
.main {
    width: 80%;
    height: 100%;
    margin: 0 auto;
    border: 1px solid rgb(98, 124, 147);
}

.el-container {
    height: 100vh;
}

.el-header {
    background-color: white;
    color: #333;
    text-align: center;
    line-height: 60px;
}

.el-footer {
    background-color: rgb(88, 113, 135);
    color: white;
    text-align: center;
    line-height: 60px;
}

.el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    text-align: center;
    line-height: 50px;
}

body>.el-container {
    margin-bottom: 40px;
}
</style>