---
layout: blog
lastUpdated: false
bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404061333025.webp"
bgImgDark: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404061333172.jpeg"
widgets:
    - name: "题目分析"
      html: '<div class="flex justify-center items-center w-full"><div id="code-chart"></div></div>'
    - name: "题目分析"
      html: '<div class="flex justify-center items-center w-full"><div id="code-date"></div></div>'
---

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

function getVirtualData(year) {
  const date = +echarts.time.parse(year + '-01-01');
  const end = +echarts.time.parse(year + '-02-28');
  const dayTime = 3600 * 24 * 1000;
  const data = [];
  for (let time = date; time <= end; time += dayTime) {
    data.push([
      echarts.time.format(time, '{yyyy}-{MM}-{dd}', false),
      Math.floor(Math.random() * 12)
    ]);
  }
  return data;
}

onMounted(() => {

    let chartDom = document.getElementById('code-chart');
    let myChart = echarts.init(chartDom);
    let option;
    const problemCnt = []

    Object.keys(problems.typeCount).forEach(p => {
        problemCnt.push({ value: problems.typeCount[p], name: p });
    });

    option = {
        tooltip: {
            trigger: 'item'
        },
         series: [
            {
                name: '题数统计',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: false,
                        fontSize: 16,
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

    let dateDom = document.getElementById('code-date');
    let myDate = echarts.init(dateDom);
    let option2;

    const now = new Date();
    const formattedDate = `${now.getFullYear()}-${(now.getMonth() + 1).toString().padStart(2, '0')}`;
    option2 = {
        tooltip: {
            position: 'top',
            formatter: function (p) {
            const format = echarts.time.format(p.data[0], '{yyyy}-{MM}-{dd}', false);
            return format + ': ' + p.data[1]+"题";
            }
        },
        visualMap: {
            show: false,
            min: 0,
            max: 10,
            left: 'center',
            inRange: {
                color: ['#C7DBFF','#5291FF']
            },
        },
        calendar: {
            range: formattedDate,
            orient: 'vertical',
            left: 'center',
            top: 'middle',
            cellSize: [30 ,30],
            monthLabel: {
                show: false
            },
            yearLabel:{
                show:false
            },
            dayLabel:{
                show:false
            }
        },
        series: {
            type: 'heatmap',
            coordinateSystem: 'calendar',
            data: Object.entries(problems["dateCount"])
        }
    };

    option2 && myDate.setOption(option2);

})
</script>

<style>
#code-chart{
width: 20rem;
height: 20rem;
}
@media (min-width: 768px) {
    #code-chart {
        /* width:20rem; */
        height:20rem;
    }
}
#code-date{
width: 100%;
height: 30rem;
}
@media (min-width: 768px) {
    #code-date {
        width:20rem;
        height:20rem;
    }
}
</style>