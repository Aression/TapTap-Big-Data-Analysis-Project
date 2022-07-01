<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {

    }
  },
  methods: {},
}
</script>

<style>
.el-tabs__item {
  font-size: 18px !important;
  color: rgb(121, 121, 121) !important;
}

.el-tabs__nav-scroll {
  width: 29.8% !important;
  margin: 0 auto !important;
}

/* 切换活动项的文字样式 */
.el-tabs__item.is-active {
  font-size: 20px !important;
  font-weight: bold;
}

/* 切换活动项的长条样式 */
.el-tabs__active-bar {
  background-color: rgb(121, 121, 121) !important;
}

/* 导航条下方边框阴影*/
.el-tabs__nav-wrap {
  box-shadow: 0px 2px 10px 0px rgba(0, 0, 0, 0.15);
}
</style>
