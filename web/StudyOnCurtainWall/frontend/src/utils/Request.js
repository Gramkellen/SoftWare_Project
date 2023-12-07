import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000';
// const baseURL = 'http://124.220.110.93:5045/api'

const Request = axios.create({  // 创建axios实例
    baseURL: baseURL,
    timeout: 50000
})

// interceptors axios的拦截器对象
Request.interceptors.request.use(config => {
    // config 请求的信息
   return config // 将配置完成的config对象返回出去 如果不返回 请求则不会进行
}, err => {
   // 请求发生错误时的处理 抛出错误
  Promise.reject(err)
})

Request.interceptors.response.use(res => {
    // 我们一般在这里处理，请求成功后的错误状态码 例如状态码是500，404，403
    // res 是所有相应的信息
    console.log(res)
   return Promise.resolve(res)
}, err => {
    // 服务器响应发生错误时的处理
    Promise.reject(err)
})

export default Request;