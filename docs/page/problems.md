---
# layout: page
---

# 题库

题库共收录{{s}}题

:::details 题目来源组成
<DataShow :hideAvatar="true"/>
:::

<script setup>
import { data as problems } from '../../auto/problems.data.js'
import DataShow from '../components/DataShow.vue'
import ProblemPage from '../components/ProblemPage.vue'
let s = 0;
Object.keys(problems).forEach(p => {
    s += problems[p];
});
</script>

<ProblemPage/>