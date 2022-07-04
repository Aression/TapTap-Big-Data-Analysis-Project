import axios from 'axios'
let axios_new=axios.create({
    //baseURL:提供公共的地址,以后发请求的url之前会自动添加该地址
    // baseURL:"http://localhost:3000",
    baseURL:"http://39.108.88.241:8003",
    //设置超时(毫秒)，如果服务器超过设置的时间没有响应数据则直接报错
    timeout:3000
});
//拦截响应
axios_new.interceptors.response.use(res=>{
    console.log(res);
    //必须有return，才能够放行数据
    return res.data;
},err=>{
    return err
})

//暴露
export default axios_new