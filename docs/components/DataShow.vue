<script setup>
import { data as posts } from '../../node_modules/vitepress-theme-open17/libs/posts.data.js'
import { data as problems } from '../../auto/problems.data.js'
import * as echarts from 'echarts';
import { onMounted } from 'vue';
import { useData } from "vitepress";
const { theme } = useData()
const blogConfig = theme.value.blog;

const props = defineProps({
  hideAvatar:Boolean
})

onMounted(() => {

    let chartDom = document.getElementById('code-chart');
    let myChart = echarts.init(chartDom);
    let option;
    const problemCnt = []

    Object.keys(problems).forEach(p => {
        problemCnt.push({ value: problems[p], name: p });
    });

    option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center',
            textStyle: {
                backgroundColor: "rgba(255, 255, 255, 1)",
                borderWidth: 0,
                borderRadius: [4, 4, 4, 4],
                padding: 4
            }
        }, series: [
            {
                name: '题数统计',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                padAngle: 5,
                itemStyle: {
                    borderRadius: 10,
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: 20,
                    }
                },
                labelLine: {
                    show: false,
                },
                data: problemCnt,
            }
        ]
    };

    option && myChart.setOption(option);

})

let s = 0;

Object.keys(problems).forEach(p => {
    s += problems[p];
});

const data = [
    {
        value: posts.length + " 篇",
        name: '博客数量',
    }, {
        value: Math.ceil(((Math.abs((new
            Date(posts[posts.length - 1].frontmatter.date)).getTime() - (new Date()).getTime()) + 1) / (1000 * 3600
                *
                24)) / posts.length) + " 天/篇",
        name: '平均更新 ',
    }, {
        name: "解题数量",
        value: s + " 题"
    }
]

</script>

<template>
    <div class=" flex justify-center items-center gap-5 flex-wrap md:flex-row flex-col">
        <div
            v-if="!hideAvatar"
            class="flex justify-center flex-col gap-5 items-center bg-white dark:bg-gray-700 rounded-2xl shadow-md p-5 md:w-[32rem] md:h-[32rem] w-full overflow-y-auto overflow-hidden">
            <img :src="blogConfig.avatar" v-if="blogConfig.avatar" alt="avatar"
                class=" object-cover object-center w-[10rem] rounded-3xl" />
            <div class="text-3xl font-bold mt-5">{{ blogConfig.title }}</div>
            <div class="text-center">{{ blogConfig.desc }}</div>
            <div class="flex justify-center flex-row gap-2 " v-for="d in data">
                <div class="text-center font-bold">
                    {{ d.name }}
                </div>
                <div class="text-center font-semibold">
                    {{ d.value }}
                </div>
            </div>
        </div>
        <div class="flex justify-center items-center bg-white dark:bg-gray-700 rounded-2xl shadow-md p-5 ">
            <div id="code-chart" style=""></div>
        </div>
    </div>

</template>

<style>
#code-chart{
width: 80vw;
height: 30rem;

}
@media (min-width: 768px) {
    #code-chart {
        width:30rem;height:30rem
    }
}
</style>