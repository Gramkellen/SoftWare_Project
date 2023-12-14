
<template>
    <div>
        <p>玻璃幕墙裂爆裂检测页面</p>
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
import { ref } from 'vue'

const showResult = ref(false); // 决定是否展示结果框

// 确认上传
const confirmUpload = (file) => {
    // 拿到的file是ImgUpload传递过来的用户决定上传的图片
    console.log("parent has recieved params passed by child");
    console.log(file);
    // 接着就是把图片上传到后端
    // 然后在界面上显示信息
    showResult.value = true;

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