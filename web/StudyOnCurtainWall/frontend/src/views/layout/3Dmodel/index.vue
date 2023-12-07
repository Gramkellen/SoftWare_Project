<template>
  <header>
    <el-menu
    :default-active="selected_item"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect">
      <el-menu-item index="1">地震工程馆</el-menu-item>
      <el-menu-item index="2">图书馆</el-menu-item>
    </el-menu>
  </header>

</template>

<script setup>
import { ref } from 'vue'

const selected_item = ref('1')

const handleSelect = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.el-menu{
  background: linear-gradient(270deg, rgba(172, 176, 255, 0.94) 3.68%, rgba(209, 241, 255, 0.97) 34.53%, rgba(210, 241, 255, 0.97) 34.54%, rgba(251, 254, 255, 0.98) 58.26%, rgba(254, 254, 255, 1.00) 94.07%, #D8E6FF 99.65%, #FEFEFF 99.87%);
  height: 7vh;
}
.router-link-active {
  text-decoration: none;
  color: #409EFF;
}
a{
  text-decoration: none;
  color: black;
}
</style>
