
<template>
    <div>
        <p class="page-title">玻璃幕墙爆裂检测</p>
        <p class="tips">请您上传一张图片</p>
        <ImgUpload 
        @confirmUpload="confirmUpload"
        @onCancel="onCancel"
        :disabled="uploadCompleted"
        >
        </ImgUpload>  

        <div 
        class="result-list-container"
        v-if="showResult"
        >
        <!-- 第一行展示整体结果 -->
        <br/>
        <el-row>
            <p class="sub-tips-item">幕墙爆裂检测结果:</p>
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
import axios from 'axios'
import { ref } from 'vue'

const uploadCompleted = ref(false);  // 标志变量，控制按钮显示和隐藏

const showResult = ref(false); // 决定是否展示结果框
//onst imgUploadAPI = "http://pjh754.cn:8000/";
//const img_base_url = "http://106.14.240.164:8080/output/"; // 之后进行路径拼接
const results = ref({
    textTip:'',
    imgURL:[]
}); // 最终的结果展示;texTip:string;imgURL:array<string>



const confirmUpload = async (file) => {
    uploadCompleted.value = true;  // 设置为true，禁用按钮
    showResult.value = true;

    const formData = new FormData();
    formData.append('photo', file.fileList[0].raw);

    try {
        const response = await axios.post('http://106.14.240.164:8000/', formData);
        
        if (response.status === 200) {
            // 服务器返回的完整玻璃和破碎玻璃结果字符串
            results.value.textTip = response.data;
        } else {
            console.error('服务器返回状态不是 200');
        }
    } catch (error) {
        console.error('接口调用失败！');
        console.error(error);
    }
};

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