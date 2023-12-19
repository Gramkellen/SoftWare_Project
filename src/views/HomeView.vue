<template>
  <div>
    <div class="header">
      <transition name="el-zoom-in-center">
        <img v-show="show" @load="handleImageLoad" src="@/assets/高楼1.jpg" alt="Your Image" class="header-image" />
      </transition>
      <div class="title-container">
        <p class="title">玻璃幕墙信息系统</p>
      </div>
      <div class="brief-introduction-container">
        <el-tooltip
        class="tooltip"
        effect="dark"
        placement="top"
        >
          <template #content> 上传幕墙图片，<br />获知幕墙表面是否平整 </template>
          <el-button 
          class="next-page-button" 
          @click="toEvennessPage"
          round
          type="primary"
          >
            平整度检测
          </el-button>
        </el-tooltip>

        <el-tooltip
        class="tooltip"
        effect="dark"
        placement="top"
        >
          <template #content> 上传幕墙图片，<br />获知幕墙玻璃表面爆裂信息 </template>
          <el-button 
          class="next-page-button"
          @click="toCrackPage"
          round
          type="primary"
          >
            玻璃爆裂检测
          </el-button>
        </el-tooltip>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const show = ref(false);
const router = useRouter();

const handleImageLoad = () => {
  show.value = true;
};

const toEvennessPage = () => {
  router.push('/evenness');
}

const toCrackPage = () => { 
  router.push('/crack');
}

onMounted(() => {
  setTimeout(() => {
    show.value = true;
  }, 200); // 延时500毫秒触发过渡效果
});
</script>

<style lang="scss" scoped>
.header {
  position: relative;
}

.header-image {
  width: 100%;
  height: auto;
  display: block;
}

.title-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;

  .title {
    font-size: 40px;
    font-weight: bolder;
    color: white; // 设置文字颜色为白色，以适应可能的背景
    letter-spacing: 5px; // 调整这个值以实现你想要的字间距
  }
}

.brief-introduction-container {
  display: flex;
  justify-content: center;
  text-align: center;
  position: absolute;
  top:65%;
  left:41.5%;
}

.next-page-button {
  margin-right: 5%;
}
</style>
