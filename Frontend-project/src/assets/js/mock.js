import Mock from 'mockjs'

const url = 'http://localhost:3000'

let dataTab = [
    {
        dataName: '热门榜',
        dataNum: [
            { name: '王者荣耀', number: 30 },
            { name: '泰拉瑞亚', number: 29 },
            { name: '部落与弯刀', number: 28 },
            { name: '原神', number: 27 },
            { name: '金铲铲之战', number: 26 },
            { name: '香肠派对', number: 25 },
        ],
        data: [
            { name: '王者荣耀', score: 9.0, type: 'MOBA' },
            { name: '泰拉瑞亚', score: 9.3, type: '沙盒 像素 开放世界' },
            { name: '部落与弯刀', score: 8.2, type: '' },
            { name: '原神', score: 9.6, type: '' },
            { name: '金铲铲之战', score: 8.5, type: '' },
            { name: '香肠派对', score: 8.3, type: '' },
        ]
    },
    {
        dataName: '预约榜',
        dataNum: [
            { name: '原神', number: 40 },
            { name: '部落与弯刀', number: 39 },
            { name: '王者荣耀', number: 38 },
            { name: '泰拉瑞亚', number: 37 },
            { name: '金铲铲之战', number: 36 },
            { name: '香肠派对', number: 35 },
        ],
        data: [
            { name: '原神', score: 9.6, type: '原神' },
            { name: '部落与弯刀', score: 8.2, type: '部落与弯刀' },
            { name: '王者荣耀', score: 9.0, type: '' },
            { name: '泰拉瑞亚', score: 9.3, type: '' },
            { name: '金铲铲之战', score: 8.5, type: '' },
            { name: '香肠派对', score: 8.3, type: '' },
        ]
    },
    {
        dataName: '热玩榜',
        dataNum: [
            { name: '金铲铲之战', number: 50 },
            { name: '香肠派对', number: 49 },
            { name: '原神', number: 48 },
            { name: '部落与弯刀', number: 47 },
            { name: '王者荣耀', number: 46 },
            { name: '泰拉瑞亚', number: 45 },
        ],
        data: [
            { name: '金铲铲之战', score: 8.5, type: '金铲铲之战' },
            { name: '香肠派对', score: 8.3, type: '香肠派对' },
            { name: '原神', score: 9.6, type: '' },
            { name: '部落与弯刀', score: 8.2, type: '' },
            { name: '王者荣耀', score: 9.0, type: '' },
            { name: '泰拉瑞亚', score: 9.3, type: '' },
        ]
    },
    {
        dataName: '厂商榜',
        dataNum: [
            { name: '王者荣耀', number: 60 },
            { name: '原神', number: 59 },
            { name: '部落与弯刀', number: 58 },
            { name: '金铲铲之战', number: 57 },
            { name: '香肠派对', number: 56 },
            { name: '泰拉瑞亚', number: 55 },
        ],
        data: [
            { name: '王者荣耀', score: 9.0, type: '王者荣耀' },
            { name: '原神', score: 9.6, type: '' },
            { name: '部落与弯刀', score: 8.2, type: '' },
            { name: '金铲铲之战', score: 8.5, type: '金铲铲之战' },
            { name: '香肠派对', score: 8.3, type: '' },
            { name: '泰拉瑞亚', score: 9.3, type: '泰拉瑞亚' },
        ]
    },
]

function getTab(options) {
    const { dataName } = JSON.parse(options.body);
    console.log(dataName);
    let data = dataTab.filters((item) => {
        return item.dataName == dataName
    })
    return {
        code: 200,
        data
    }
}
//获取表格数据
Mock.mock(url + "basicData/getTab", "get", getTab)