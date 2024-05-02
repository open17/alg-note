<template>
    <div class="flex flex-col space-y-4 gap-2 justify-center items-center mb-5">
        <div class="text-3xl w-full text-center font-bold mt-5">题库</div>
        <div class="text-xl text-center">目前累计收入{{ problems.length }}题</div>
        <el-card class="w-full md:w-10/12">
        <el-table ref="tableRef" row-key="date" :data="filterProblems" stripe :border="true" style="width: 100%">
            <el-table-column prop="category" label="类别" sortable width="180" column-key="date" />
            <el-table-column prop="name" label="题号/标题" width="180" sortable />
            <el-table-column prop="tags" label="标签" width="180" align="center">
                <template #default="scope">
                    <el-tag v-if="scope.row.tags.length === 0" type="info" disable-transitions>
                        暂无标签
                    </el-tag>
                    <el-tag v-for="tag in scope.row.tags" disable-transitions class="mr-1 mb-1" :type="getTagType(tag)">
                        {{ tag }}
                    </el-tag>
                </template>
            </el-table-column>
            <el-table-column align="center">
                <template #header>
                     <div class="flex justify-between items-center gap-5">
                        <el-select v-model="selectedTags" filterable placeholder="选择标签" multiple collapse-tags
                            collapse-tags-tooltip class="w-7/12">
                            <el-option v-for="item in allTags" :key="item" :label="item" :value="item" />
                        </el-select>
                        <el-input v-model="search" placeholder="搜索题号/标题" />
                    </div>
                    
                </template>
                <template #default="scope">
                    <el-button size="small" type="success" @click="showCode(scope.row.html)">
                        查看代码
                    </el-button>
                    <el-button size="small" type="info" @click="getLink(scope.row)">
                        题目链接
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        </el-card>
        <el-dialog v-model="dialogVisible" title="代码" width="800">
            <div class="code" v-html="code"></div>
        </el-dialog>
    </div>
</template>

<script setup>
import 'element-plus/theme-chalk/dark/css-vars.css'
import 'element-plus/dist/index.css'
import { ElDialog,ElCard } from 'element-plus'
import { ElTable, ElTableColumn } from 'element-plus'
import { ElButton, ElTag, ElInput, ElSelect, ElOption } from 'element-plus'
import { ElNotification } from 'element-plus'
import { ref, computed, onMounted } from 'vue'
import { codeToHtml } from 'shiki'
import { useData } from 'vitepress';
import { data as problemWithTags } from '../../auto/problemTags.data.js';

const problems = problemWithTags.problems;
const allTags = problemWithTags.allTags;

const { isDark } = useData();
const dialogVisible = ref(false);
const code = ref({});
const showCode = (html) => {
    dialogVisible.value = true;
    code.value = html;
}

const selectedTags = ref([]);

onMounted(async () => {
    for (const problem of problems) {
        problem.html = await getCodeHtml(problem.code, problem.lang);
    }
});

async function getCodeHtml(code, lang) {
    return await codeToHtml(code, { lang: lang, themes: { light: 'github-light', dark: 'github-dark' } });
}


const getLink = (msg) => {
    let link=null;
  if (msg.category==="luogu") {
      link=`https://www.luogu.com.cn/problem/${msg.name}`;
  }
  else if(msg.category==="Codeforces"){
    if ('0'<=msg.name[msg.name.length - 1]<='9'){
      link=`https://codeforces.com/contest/${msg.name.slice(0, -2)}/problem/${msg.name.slice(-2).toUpperCase()}`;
    }
    else{
      link=`https://codeforces.com/contest/${msg.name.slice(0,-1)}/problem/${msg.name.slice(-1).toUpperCase()}`;
    }
  }
  else if(msg.category==="acwing"){
      link=`https://www.acwing.com/problem/search/1/?search_content=${msg.name}`;
  }
  else if(msg.category==="VirtualJudge"){
    link=`https://vjudge.net/problem#OJId=All&probNum=&title=${msg.name}&source=&category=all`;
  }
  else if(msg.category==="LeetCode"){
      link=`https://leetcode.cn/problemset/?search=${msg.name}&page=1`;
  }
  if(link){
    window.open(link);
    return;
  }
  ElNotification({
    title: '题目链接',
    message: `未找到题目${msg.category}/${msg.name}的相关链接`,
    type: 'warning',
  })
}

const search = ref('')
const filterProblems = computed(() =>
    problems.filter(
        (data) =>
            !search.value ||
            data.name.toLowerCase().includes(search.value.toLowerCase())
    ).filter(problem => selectedTags.value.length === 0 || selectedTags.value.some(tag => problem.tags.includes(tag)))
)


const getTagType=(tag)=>{
    const types=['warning','danger','primary','success']
    const index=tag.length%types.length;
    return types[index];
}
</script>


<style>
html.dark .shiki,
html.dark .shiki span {
  color: var(--shiki-dark) !important;
  background-color: var(--shiki-dark-bg) !important;
  font-style: var(--shiki-dark-font-style) !important;
  font-weight: var(--shiki-dark-font-weight) !important;
  text-decoration: var(--shiki-dark-text-decoration) !important;
}
</style>


<style scoped>
.code :deep(pre){
    padding: 10px;
    width: 100%;
    overflow-x: auto;
}
</style>