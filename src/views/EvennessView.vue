<template>
    <div>
        <p class="page-title">玻璃幕墙平整度检测</p>
        <p class="tips">请您上传一张图片</p>
        <ImgUpload 
        @confirmUpload="confirmUpload"
        @onCancel="onCancel"
        >
        </ImgUpload>

        <div 
        class="result-list-container"
        v-if="showResult"
        >
        <!-- 第一行展示整体结果 -->
        <br/>
        <el-row>
            <p class="sub-tips-item">检测结果:&nbsp;</p>
            <p style="display: inline-block;">{{ results.textTip }}</p>
        </el-row>
        <el-divider  class="divider"/>
        <!-- 第二行展示图片 -->
        <el-row>
            <div class="result-img-container">
                <div class="result-img-wrapper"
                v-for="(img,index) in results.imgURL"
                :key="index"
                >
                    <p class="res-type">{{ img.type }}</p>
                    <img :src="img.url" class="res-img">
                </div>
            </div>
        </el-row>
        </div>
    </div>
</template>

<script setup>
import ImgUpload  from '@/components/ImgUpload.vue'
// import axios from 'axios'
import { ref } from 'vue'

const showResult = ref(false); // 决定是否展示结果框
// const imgUploadAPI = "http://pjh754.cn:8000/";
// const img_base_url = "http://106.14.240.164:8080/output/"; // 之后进行路径拼接
const results = ref({
    textTip:'',
    imgURL:[]
}); // 最终的结果展示;texTip:string;imgURL:array<string>


// 确认上传
// const confirmUpload = async (file) => {
//     // 拿到的file是ImgUpload传递过来的用户决定上传的图片
//     console.log("parent has recieved params passed by child");
//     // 接着就是把图片上传到后端
//     // 然后在界面上显示信息
//     const formData = new FormData();
//     formData.append('photo', file.fileList[0].raw);

//     showResult.value = true;
//     try {
//         const res = await axios.post(imgUploadAPI,formData);
//         // res.data中包含了结果字符串和检测图片
//         results.value.textTip = res.status;
//         results.value.imgURL.push({
//             type:'original',
//             url:img_base_url + res.data.original,
//         })
//         results.value.imgURL.push({
//             type:'overlay',
//             url:img_base_url + res.data.overlay,
//         })
//         results.value.imgURL.push({
//             type:'marked',
//             url:img_base_url + res.data.marked,
//         })
//         console.log(results.value);
//     } catch(e) {
//         console.log("接口调用失败！");
//         console.log(e);
//     }

// }

const confirmUpload = () => {
    showResult.value = true;
    results.value.textTip = "只是测试布局";
    results.value.imgURL.push({
        type:'original',
        url:require("@/assets/高楼1.jpg")
    })
    results.value.imgURL.push({
        type:'overlay',
        url:require("@/assets/高楼1.jpg")
    })
    results.value.imgURL.push({
        type:'marked',
        url:require("@/assets/高楼1.jpg")
    })
}
// 更换了想要检测的图片
const onCancel = () => {
    console.log("you have cancel the upload");
    showResult.value = false; // 将刚才拿到的结果清空
    results.value = {
        textTip:'',
        imgURL:[]
    }
}

</script>

<style lang="scss" scoped>
.tips {
    display: flex;
    text-align: center;
    justify-content: center;
}

.divider {
    margin:9px;
}
// 展示结果的盒子
.result-list-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width: 90%;
    margin: 0 auto; /* 居中对齐并给予边距 */
}

.result-img-container {
    display: flex;
    justify-content: space-between; /* 等间距排列 */
    align-items: center;
    padding: 10px; /* 边距 */
    box-sizing: border-box; /* 防止内边距影响宽度 */
}

.result-img-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1; /* 分配相同空间;这个flex应该是对应父元素的flex布局 */
    margin: 0 5px; /* 子元素间距 */
}

.res-img {
    width: 100%; /* 图片填满容器 */
    height: auto; /* 保持图片比例 */
}

.sub-tips-item {
    font-weight: bolder;
    display: inline-block;
}

.page-title {
    font-size: 24px; /* 设置标题字体大小 */
    font-weight: bold; /* 设置标题粗细 */
    text-align: center; /* 居中对齐 */
    margin-bottom: 20px; /* 下方间距 */
}
</style>