import axios from './axios.js'
let url = {
    // 获取榜单
    getHotTable(data) {
        return axios({
            url: "/BasicData/getHotTable?list_name="+data.list_name,
            method: "post",
            data
        })
    },
    // 获取榜单统计图表
    getHotTableChart(data) {
        return axios({
            url: "/BasicData/getHotTableChart?list_name="+data.list_name,
            method: "post",
            data
        })
    },
    // 获取榜单(综合关注度 或者 叫座榜)
    getTabs_ac(data) {
        return axios({
            url: "/Comprehensive/GetTableAC?list_name="+data.list_name,
            method: "post",
            data
        })
    },

     // 游戏类型  评分和下载量
     get_gametype(data) {
        return axios({
            url: "/Comprehensive/GameTypeAnalysis?gametype_list="+data.gametype_list,
            method: "post",
            data
        })
    },

    //厂商评分分析
    get_manu(data) {
        return axios({
            url: "/Comprehensive/ManuScore?manufacturer="+data.manufacturer,
            method: "post",
            data
        })
    },
     //搜索榜单
     getcurveTabs(data) {
        return axios({
            url: "/search-page?search_game-name=" + data.search_name,
            method: "post",
            data
        })
    },
    //曲线数据
    getcurve(data) {
        return axios({
            url: "/data?game_name="+ data.game_name,
            method: "post",
            data
        })
    },
}
export default url