<template>
  <div>
    <div class="Main">
      <div class="main_text">
        <span style="color: rgb(88, 113, 135);font-weight: bold;font-size: 35px;">小组成员</span>
      </div>
    </div>
    <div class="team_img">
      <div>
        <span style="color: rgb(88, 113, 135);font-weight: bold;font-size: 15px">后端小组</span>
      </div>
      <div class="team_img_box" v-for="(item, index) in mainImgArr1" :key="index">
        <img :src='item.img' style="width: 120px;height: 120px;">
        <p>{{item.name}}</p>
      </div>
    </div>
    <div class="team_img">
      <div>
        <span style="color: rgb(88, 113, 135);font-weight: bold;font-size: 15px">前端小组</span>
      </div>
      <div class="team_img_box" v-for="(item, index) in mainImgArr2" :key="index">
        <img :src='item.img' style="width: 120px;height: 120px;">
        <p>{{item.name}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import bus from '@/assets/js/bus';
export default {
  data() {
    return {
      mainImgArr1: [
        {
          img: require('@/assets/img/zxp.jpg'),
          name: "湛宵鹏"
        },
        {
          img: require('@/assets/img/ld.jpg'),
          name: "吕迪"
        },
        {
          img: require('@/assets/img/zxr.jpg'),
          name: "曾萧然"
        }
      ],
      mainImgArr2: [
        {
          img: require('@/assets/img/yrh.jpg'),
          name: "闫若华"
        },
        {
          img: require('@/assets/img/lch.jpg'),
          name: "陆程辉"
        },
        {
          img: require('@/assets/img/hlj.jpg'),
          name: "黄柳金"
        }
      ],
      mainNameArr1: [
        1, 2, 3
      ],
    }
  },
  methods: {

  },
  mounted() {
    if (this.$route.path == '/index/teamMembers') {
      bus.$emit("changeIndex", 4)
    }
  },
}
</script>

<style scoped>
.team_img {
  display: flex;
  margin: 0 auto;
  cursor: pointer;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 30px;
}

.team_img .team_img_box {
  width: 30%;
  height: 30%;
}

.Main {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    margin-top: 1.5%;
}

.main_text {
    width: 100%;
}
</style>