<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
  >
    <el-menu-item index="/">Home</el-menu-item>
    <el-menu-item index="/evenness">平整度检测</el-menu-item>
    <el-menu-item index="/crack">幕墙爆裂检测</el-menu-item>
  </el-menu>
  <router-view />
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeIndex = ref(router.currentRoute.value.path)

const handleSelect = (key) => {
  console.log(key)
  router.push(key)
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
</style>
