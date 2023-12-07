import Request from "@/utils/Request.js";  // 在每个 api 文件里都要引入这两个文件
import Message from "@/utils/Message.js"  // 在每个 api 文件里都要引入这两个文件

// 图像上传
export function UploadCsv(FormData) {  // 在 src/views/login/index.vue 里调用，可以去看看是如何调用的
    return Request({  // 发送请求
        method: 'POST',
        headers: {
            'Content-Type': 'application/form-data', // 设置请求头
        },
        url: '/backend/vibration/uploadCsv/',  // 与后端接口对应！！！
        data: FormData, // 使用FormData作为请求体
    }).then(function (response) {  // then 表示成功接收到响应后的操作
        if (response.status === 200) {
            Message.success("文件上传成功");
            
            console.log(response); // 检查返回的数据
            return response;  //  // 正确响应，返回数据
        } else {
            Message.error("文件上传失败");
        }
    }).catch(function (error) {  // catch 表示接收到错误响应后的操作
        console.log(error);
    });
}

// 异常值过滤
export function FilterOutlier(FormData) {  
    return Request({  // 发送请求
        method: 'POST',
        headers: {
            'Content-Type': 'application/form-data', // 设置请求头
        },
        url: '/backend/vibration/filterOutlier/', 
        data: FormData, 
    }).then(function (response) {  
        if (response.status === 200) {
            Message.success("筛选成功！");
            
            console.log(response); 
            return response;  
        } else {
            Message.error("筛选失败！");
        }
    }).catch(function (error) {  // catch 表示接收到错误响应后的操作
        console.log(error);
    });
}

// 条件搜索数据库
export function ConditionSearch(FormData) {  
    return Request({  // 发送请求
        method: 'POST',
        headers: {
            'Content-Type': 'application/form-data', // 设置请求头
        },
        url: '/backend/vibration/conditionSearch/', 
        data: FormData, 
    }).then(function (response) {  
        if (response.status === 200) {
            Message.success("搜索成功！");
            
            console.log(response); 
            return response;  
        } else {
            Message.error("搜索失败！");
        }
    }).catch(function (error) {  // catch 表示接收到错误响应后的操作
        console.log(error);
    });
}


// 发送邮件
export function SendMail(data) {  
    return Request({  // 发送请求
        method: 'POST',
        url: '/backend/vibration/sendMail/', 
        data: data, 
    }).then(function (response) {  
        if (response.status === 200) {
            Message.success("发送邮件成功！");
            
            console.log(response); 
            return response;  
        } else {
            Message.error("发送邮件失败！");
        }
    }).catch(function (error) {  // catch 表示接收到错误响应后的操作
        console.log(error);
    });
}