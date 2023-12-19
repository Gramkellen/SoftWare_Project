<template>
  <el-menu
    :router="true"
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    :popper-offset="16"
  >
    <el-menu-item index="/">Home</el-menu-item>
    <el-menu-item index="/evenness">平整度检测</el-menu-item>
    <el-menu-item index="/crack">幕墙爆裂检测</el-menu-item>
    <div class="flex-grow"></div>
    <el-menu-item @click="backToDashboard">
        返回dashboard
    </el-menu-item>
  </el-menu>
  <router-view />
</template>

<script setup>
import { ElMessage } from 'element-plus';
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter();
const route = useRoute();
const activeIndex = computed(() => {
  return route.path
})

const handleSelect = (key) => {
  router.push(key)
}

// 返回仪表盘；之后可以导航到他们的页面
const backToDashboard = () => {
  ElMessage.warning("您将回到合作系统仪表盘");
}
</script>

<style lang="scss">
.el-menu-demo {
  padding: 30px;

  .el-menu-item {
    font-weight: bold;
    color: #2c3e50;
    border-bottom: none; // 取消底部边框

    &.is-active, &.is-active:hover {
      color: #1d719e;
      border-bottom: none; // 取消底部边框
    }
  }
}

.flex-grow {
  flex-grow: 1;
}
</style>
