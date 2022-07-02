import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import Main from '../components/Main.vue'
import BasicData from '../components/Basic data/Index.vue'
import GameCurve from '../components/Game curve/Index.vue'
import ComprehensiveAnalysis from '../components/Comprehensive analysis/Index.vue'
import TeamMembers from '../components/Team members/Index.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/index/main'
  },
  {
    path: '/index',
    component: Index,
    children: [
      {
        path: 'main', // 首页
        component: Main,
      },
      {
        path: 'basicData', // 基础数据
        component: BasicData,
      },
      {
        path: 'gameCurve', // 游戏曲线
        component: GameCurve,
      },
      {
        path: 'comprehensiveAnalysis', // 综合分析
        component: ComprehensiveAnalysis,
      },
      {
        path: 'teamMembers', // 团队成员
        component: TeamMembers,
      },
    ]
  },
]

const router = new VueRouter({
  mode:'hash',
  base:process.env.BASE_URL,
  routes
})

export default router
