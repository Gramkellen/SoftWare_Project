<!-- 排版页面 -->
<template>
    <!-- 侧边栏区域begin -->
    <div class = "menu">
        <SideBar />
    </div>
    <!-- 侧边栏区域end -->
    <!-- 右侧功能区域begin -->
    <div class = "func-zone">
        <dashboard v-if="choice == 'dashboard'"/>
        <segmentation v-if="choice == 'segmentation'"/>
        <smoothness v-if="choice == 'smoothness'"/>
        <explosion_identify v-if="choice == 'explosion_identify'"/>
        <vibration v-if="choice == 'vibration'"/>
        <vibrationData v-if="choice == 'vibration_data'"/>
        <model v-if="choice == '3Dmodel'"/>
    </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUpdated, computed} from 'vue'
import SideBar from '@/components/SideBar.vue'
import dashboard from '@/views/layout/dashboard/index.vue'
import smoothness from '@/views/layout/smoothness/index.vue'
import segmentation from '@/views/layout/segmentation/index.vue'
import explosion_identify from '@/views/layout/explosion_identify/index.vue'
import vibration from '@/views/layout/vibration/index.vue'
import vibrationData from '@/views/layout//vibration_data/index.vue'
import model from '@/views/layout/3Dmodel/index.vue'
import { useRoute } from 'vue-router'

const route = useRoute();
const choice = ref();//根据路由传值对应功能区的显示内容

// 监听路由变化并执行不同逻辑
onMounted(() => {
  updateLogic();
});
onUpdated(() => {
  updateLogic();
});

// 执行不同逻辑的函数
const updateLogic = () => {
  if (route.params.choice === 'dashboard') {
    choice.value = 'dashboard'
  } else if (route.params.choice === 'segmentation') {
    choice.value = 'segmentation'
  }
  else if (route.params.choice === 'smoothness') {
    choice.value = 'smoothness'
  }
  else if (route.params.choice === 'explosion_identify') {
    choice.value = 'explosion_identify'
  }
  else if (route.params.choice === 'vibration') {
    choice.value = 'vibration'
  }
  else if (route.params.choice === 'vibration_data'){
    choice.value = 'vibration_data'
  }
  else if (route.params.choice === '3Dmodel'){
    choice.value = '3Dmodel'
  }
};
</script>

<style scoped>
.menu{
    position: fixed;
    left:0%;
    top:0%;
    width:15%;
    height:100%;
    background-color: rgb(0, 23, 52);
    color:white;
}
.func-zone{
    position: absolute;
    left:15%;
    top:0%;
    width:85%;
    height:100%;
}
</style>