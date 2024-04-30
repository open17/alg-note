<template>
    <div class="flex flex-col space-y-4 mt-10">
        <div>
            <div class="flex flex-wrap gap-5">
                <div class="text-xl">标签</div>
                <label v-for="tag in tags" :key="tag" class="flex items-center space-x-2">
                    <input type="checkbox" :value="tag" v-model="selectedTags"
                        class="form-checkbox h-5 w-5 text-indigo-600">
                    <span>{{ tag }}</span>
                </label>
            </div>
        </div>
        <div v-if="selectedTags.length > 0">
            <h2 class="font-bold">题目列表</h2>
            <ul class="mt-2">
                <li v-for="problem in filteredProblems" :key="problem.name" class="my-2">
                    <div class="font-semibold my-5 text-2xl">{{ problem.name }}</div>
                    <div @click="changeCode(problem.name)" class=" cursor-pointer mb-5">{{showCode==problem.name?"折叠代码":"展开代码"  }}</div>
                    <div v-show="showCode==problem.name">
                        <div v-html="problem.html" class=" overflow-auto" v-show="!isDark"></div>
                        <div v-html="problem.htmlDark" class=" overflow-auto" v-show="isDark"></div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { codeToHtml } from 'shiki'
import { useData } from 'vitepress';
import { data as problemWithTags } from '../../auto/problemTags.data.js';

const problems = problemWithTags.problems;
const tags = problemWithTags.allTags;

const { isDark } = useData();

const selectedTags = ref([]);

const showCode = ref("");

const changeCode=(v)=>{
    if(v!=showCode.value){
        showCode.value=v;
    }
    else{
        showCode.value="";
    }
}

const filteredProblems = computed(() => {
    if (selectedTags.value.length === 0) {
        return [];
    }
    return problems.filter(problem => selectedTags.value.some(tag => problem.tags.includes(tag)));
});

onMounted(async () => {
    for (const problem of problems) {
        problem.html = await getCodeHtml(problem.code, problem.lang, 'light-plus');
        problem.htmlDark = await getCodeHtml(problem.code, problem.lang, 'tokyo-night');
    }
});

async function getCodeHtml(code, lang, theme) {
    return await codeToHtml(code, { lang: lang, theme: theme });
}
</script>
