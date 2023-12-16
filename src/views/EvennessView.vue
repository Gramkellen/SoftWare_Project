<template>
    <div>
        <p>这里是玻璃幕墙平整度检测页面</p>
        <!-- 尝试图片上传组件 -->
        <ImgUpload 
        @confirmUpload="confirmUpload"
        @onCancel="onCancel"
        class="img-uploader"
        >
        </ImgUpload>

        <div class="result-list-container"
        v-if="showResult">
            <p>这里将展示后端返回的结果</p>
        </div>
    </div>
</template>

<script setup>
import ImgUpload  from '@/components/ImgUpload.vue'
import axios from 'axios'
import { ref } from 'vue'

const showResult = ref(false); // 决定是否展示结果框
const imgUploadAPI = "http://pjh754.cn:8000/";

// 确认上传
const confirmUpload = async (file) => {
    // 拿到的file是ImgUpload传递过来的用户决定上传的图片
    console.log("parent has recieved params passed by child");
    // 接着就是把图片上传到后端
    // 然后在界面上显示信息
    const formData = new FormData();
    formData.append('photo', file.fileList[0].raw);

    showResult.value = true;
    try {
        const res = await axios.post(imgUploadAPI,formData);
        console.log(res);
    } catch(e) {
        console.log("接口调用失败！");
        console.log(e);
    }

}

// 更换了想要检测的图片
const onCancel = () => {
    console.log("you have cancel the upload");
    showResult.value = false; // 将刚才拿到的结果清空
}

</script>

<style lang="scss" scoped>
.result-list-container {
    width:70%;
    height:70%;
    border:black 1em;
}
</style>