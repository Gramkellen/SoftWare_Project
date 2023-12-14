<template>
  <div>
    <div class="header">
      <transition name="el-zoom-in-center">
        <img v-show="show" @load="handleImageLoad" src="@/assets/高楼1.jpg" alt="Your Image" class="header-image" />
      </transition>
      <div class="title-container">
        <p class="title">玻璃幕墙信息系统</p>
      </div>
    </div>
    <div class="brief-introduction-container">
      <p class="brief-introduction">
        您可以选择最上方的“平整度检测”或“玻璃玻璃幕墙爆裂检测” <br/> 并上传相应的图片，以获得您想了解的信息
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const show = ref(false);

const handleImageLoad = () => {
  show.value = true;
};

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
}
</style>
