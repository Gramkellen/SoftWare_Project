<script>
import Unity from "vue-unity-webgl";

  export default {
    name: 'UnityModel',
    methods:{
      sendOrders(order){
        //this.$refs.unityIframe.contentWindow.sendOrders(order);
      },
      draw_des(des){        
        this.$refs.unityIframe.contentWindow.draw_des(des);
      },
      hide_des(des){
        this.$refs.unityIframe.contentWindow.hide_des(des);
      },
      specialize_des(des){
        this.$refs.unityIframe.contentWindow.specialize_des(des);
      },
      changeUse(type, state){
        if(type === 'key'){
          //alert('键盘' + state);
          this.$refs.unityIframe.contentWindow.useKeyboard(state);
        }
        else if(type === 'mouse'){
          //alert('鼠标' + state);
          this.$refs.unityIframe.contentWindow.useMouse(state);
        }
      },
      changeMode(value) {
        this.$refs.unityIframe.contentWindow.changeMode(value);
      },
      reset() {
        this.$refs.unityIframe.contentWindow.reset();
      },
      setRotating(type){
        //alert('旋转' + type);
        this.$refs.unityIframe.contentWindow.setRotating(type);
      },
      setSize(type){
        //alert('调整' + type);
        this.$refs.unityIframe.contentWindow.setSize(type);
      },
      setQuick(type){
        //alert(type);
        this.$refs.unityIframe.contentWindow.setQuick(type);
      },
      isMeasuring(state){
        this.$refs.unityIframe.contentWindow.isMeasuring(state);
        //alert(state);
      },
    },
  }
</script>

<template>
    <div>
      <iframe id="unity-iframe" 
        ref="unityIframe"
        src="/unityModel/index.html" 
        width="1000" 
        height="660">
      </iframe>
    </div>
</template>
  
<style scoped>
  div {
    width: 1000px;
    height: 700px;
  }
</style>