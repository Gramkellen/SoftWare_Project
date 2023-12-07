<template>
    <div>这是振动数据风震图页面</div>
    <el-button @click="GoToDash">进入仪表盘</el-button>

    <div>
        <h2>1.请上传振动数据文件（csv）</h2>
        <input type="file" ref="fileInput"  accept=".csv" @change="handleFileInputChange" />
        <button @click="uploadFile" :disabled="!selectedFile">上传文件</button>
    </div>

    <h2 v-if="showNormal" style="margin:30px">2.风震图显示</h2>
    <div id="main" style="width: 100%;height:500px;"></div>

    <h2 v-if="showNormal" style="margin:30px">3.请选择异常阈值</h2>
    <div v-if="showNormal" class="slider-block" style="width: 400px;">
        <el-slider v-model="range" range step="0.1" :min="-5" :max="5"  range-start-label range-end-label/>
        <div>异常值上下限：【{{ range[0] }}，{{ range[1] }}】</div>
        <div style="margin:20px">
            <el-button @click="filterOutlier">确认筛选</el-button>
        </div>
    </div>

    <h2 v-if="showAbnormal" style="margin:30px">4.异常值筛选结果</h2>
    <div v-if="showAbnormal">
        <el-button type="danger" style="margin-bottom: 20px" @click="dialogVisible = true">发送报告</el-button>
        <el-dialog
            v-model="dialogVisible"
            title="提示"
            width="30%"
            :before-close="handleClose"
        >
            <span>发送报告到邮箱1156504938@qq.com？</span>
            <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="sendMail">
                    确定
                </el-button>
            </span>
            </template>
        </el-dialog>
    </div>
    <div id="abnormal" style="width: 100%;height:500px;"></div>
</template>

<script setup>
    import router from "@/router/index.js"
    import { UploadCsv, FilterOutlier, SendMail } from '@/api/vibration.js'
    import { ref, reactive } from 'vue'
    import * as echarts from 'echarts';
    import { ElMessage } from "element-plus";

    var chartData = ref();
    const dialogVisible = ref(false);
    let abnormalData;

    const range = ref([-0.5, 0.5])

    const selectedFile = ref(null); //已选文件
    const file_url = ref('');//文件url

    const showNormal = ref(false);//显示平滑后的风震图
    const showAbnormal = ref(false); //显示异常风震图


    // 跳转到仪表盘
    const GoToDash = () => {
        //跳转仪表盘页面
        router.push({ 
            name: 'layout', 
            params:{ 
                choice:'dashboard' 
            } 
        })
    }


    // 选择文件
    const handleFileInputChange = (event) => {
        const file = event.target.files[0];
        selectedFile.value = file;
        console.log(selectedFile.value);
    };

    // 上传文件
    const uploadFile = () => {
        if (selectedFile.value) {
            let formData = new FormData();
            formData.append('csv', selectedFile.value);

            UploadCsv(formData)
                .then(function (result) {
                    chartData.value = result.data;
                    file_url.value = result.data.csv_url;

                    // 绘制echarts折线图
                    var myChart = echarts.init(document.getElementById('main'));
                    let option;
                    let yData=chartData.value.yData;
                    let series = [];
                    for (let name in yData) {
                    series.push({
                        name: name,
                        type: 'line',
                        data: yData[name],
                        smooth: false,
                    })
                    }
                    option = {
                        title: {
                            text: '振动数据风震图'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            data: ['x', 'y', 'z']
                        },
                        grid: {
                            left: '3%',
                            right: '4%',
                            bottom: '3%',
                            containLabel: true
                        },
                        xAxis: {
                            type: 'category',
                            boundaryGap: false,
                            data: []
                        },
                        yAxis: {
                            type: 'value'
                        },
                        series: series
                    };
                    myChart.setOption(option);

                    showNormal.value = true;
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
        else{
            ElMessage.error('请选择csv文件')
        }
    }


    // 异常值筛选
    const filterOutlier = () => {
        // 向后端发送请求
        let formData = new FormData();
        formData.append('min',range.value[0])
        formData.append('max',range.value[1])
        formData.append('csv_url',file_url.value)
        console.log(file_url.value)

        FilterOutlier(formData)
        .then(function(result){

            // 绘制echarts折线图
            var myChart = echarts.init(document.getElementById('abnormal'));
            let option;
            abnormalData = result.data.yData;
            let series = [];
            for (let name in abnormalData) {
                series.push({
                    name: name,
                    type: 'line',
                    data: abnormalData[name],
                    smooth: false,
                    markLine: {
                                data: [
                                    { type: 'none', name: 'Max', yAxis: range.value[1] },
                                    { type: 'none', name: 'Min', yAxis: range.value[0] }
                                ],
                                itemStyle: {
                                    normal: {
                                        lineStyle: {
                                            color: '#ff0000',
                                        }
                                    }
                                },
                                label: {
                                    position: 'end',
                                    formatter: function (params) {
                                        if (params.name === 'Max') {
                                            return '异常上限{{range.value[1]}}';
                                        } else if (params.name === 'Min') {
                                            return '异常下限{{range.value[0]}}';
                                        }
                                    },
                                    color: '#ff0000'
                                }
                            }
                })
            }



            option = {
                title: {
                    text: '异常值风震图'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['x', 'y', 'z']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: []
                },
                yAxis: {
                    type: 'value',
                    min: Math.min(range.value[0], Math.min(...abnormalData['x']), Math.min(...abnormalData['y']), Math.min(...abnormalData['z']),),
                    max: Math.max(range.value[1], Math.max(...abnormalData['x']), Math.max(...abnormalData['y']),Math.max(...abnormalData['z'])),
                },
                series: series
            };
            myChart.setOption(option);

            showAbnormal.value = true;
        })
        .catch(function (error) {
            console.log(error);
        });
    }


    //发送邮件
    const sendMail = () =>{
        dialogVisible.value = false;

        SendMail({
            address: '1156504938@qq.com',
            data: abnormalData,
            max: range.value[1],
            min: range.value[0],
            device: 'Device320EA412',
        })
        .then(function(result){
            console.log(result);
        })
        .catch(function (error) {
            console.log(error);
        })
    }
    

</script>

<style>

    .upload-container{
        margin:30px;
    }

    .slider-block{
        margin: auto;

    }

</style>