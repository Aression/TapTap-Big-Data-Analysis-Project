<template>
  <div>
    <!-- <span class="text">综合分析</span> -->
    <div class="nav">
      <ul>
        <li v-for="(item, index) in navArr" :key="index" :class="[nowIndex == index ? 'selected' : '']"
          @click="changeNav(index)">
          {{ item.name }}
        </li>
      </ul>
    </div>
    <DoubleBrokenLine v-if="nowIndex === 0 && doubleline_data.length > 0" :doubleline_data.sync='doubleline_data' />
    <Tab :nowIndex='nowIndex' :data_GameType.sync='data_GameType' v-if="nowIndex !== 0 && data_GameType.length > 0" />

  </div>
</template >
    
<script>
import bus from '@/assets/js/bus';
import DoubleBrokenLine from "../Chart/DoubleLines.vue";
import Tab from './Tab.vue'
export default {
  components: { DoubleBrokenLine, Tab },
  data() {
    return {
      navArr: [
        { name: '叫座榜与综合关注度榜' },
        { name: '游戏类型评分分析' },
        { name: '游戏类型下载量分析' },
        { name: '厂商评分分析' }
      ],
      nowIndex: 0,
      now_name: '叫座榜与综合关注度榜',
      //定义接收数据的变量
      doubleline_data: [],
      data_GameType: [],//游戏类型评分、游戏类型下载量、厂商
      //manu:[]
    }
  },
  methods: {
    //改变index时候，获取一遍榜单
    changeNav(index) {
      this.nowIndex = index
      // console.log(this.nowIndex);
      if (index == 0) {
        this.now_name = '叫座榜与综合关注度榜'
        this.getTabs_ac()
      }
      if (index == 1) {
        this.now_name = '游戏类型评分分析'
        this.get_gametype()
      }
      if (index == 2) {
        this.now_name = '游戏类型下载量分析'
        this.get_gametype()
      }
      if (index == 3) {
        this.now_name = '厂商评分分析'
        this.get_manu()
      }
    },
    //getTabs_ac 获取综合分析的数据
    async getTabs_ac() {
      let param = {
        list_name: this.now_name
      }
      let res = this.api.getTabs_ac(param);

      res.then((result) => {
        let doubleline_data = result.list_info
        this.doubleline_data = doubleline_data
        console.log(this.doubleline_data);
      })
      // console.log(res);
    },


    // 游戏类型  下载量 评分
    async get_gametype() {
      this.data_GameType = []
      let param = {
        gametype_list: this.now_name
      }
      let res = this.api.get_gametype(param);
      if (this.nowIndex == 1) {
        res.then((result) => {
          let data_GameType = result.data_list.map(item => ({
            //修改接收到的变量名字
            type: item.game_typename, list: item.score_list
          }))

          this.data_GameType = data_GameType
          // console.log(this.data_GameType);
        })
      } else if (this.nowIndex == 2) {
        res.then((result) => {
          let data_GameType = result.data_list.map(item => ({
            //修改接收到的变量名字
            type: item.game_typename, list: item.download_list
          }))

          this.data_GameType = data_GameType
          // console.log(this.data_GameType);
        })
      }
    },
    //厂商评分
    async get_manu() {
      this.data_GameType = []
      let param = {
        manufacturer: this.now_name
      }
      let res = this.api.get_manu(param);
      // console.log(res);
      //nowIndex = 3
      res.then((result) => {
        let data_GameType = result.data_list.map(item => ({
          //修改接收到的变量名字
          type: item.manu_name, list: item.manu_score
        }))

        this.data_GameType = data_GameType
        // console.log(this.data_GameType);
      })
    },
  },
  mounted() {
    if (this.$route.path == '/index/comprehensiveAnalysis') {
      bus.$emit("changeIndex", 3)
    }
    this.getTabs_ac()
    // this.get_gametype()
    // this.get_manu()
  },
}
</script>

<style scoped>
/* .text {
  color: rgb(98, 124, 147);
  font-size: 25px;
  position: absolute;
  left: 15%;
  top: 13%;
} */

.nav {
  width: 100%;
  position: relative;
  margin: 0 auto; 
  text-align: center;
  margin-top: auto;
}

ul {
  display: flex;
  margin: 0 auto; text-align: center;
  list-style: none;
}

li {
  margin: 21.7px;
  cursor: pointer;
  margin: 0 auto; text-align: center;
  color: rgb(98, 124, 147);
}

.selected {
  font-weight: bold;
  color: #797979;
}
</style>
