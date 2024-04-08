---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "xcpc note"
  text: "我的算法竞赛练习,笔记与模板"
  tagline: By open17
  actions:
    - theme: brand
      text: 查看模板
      link: /template/Others/IO
    - theme: alt
      text: 浏览博客
      link: /page/blog
  image: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202402082225465.png"

bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404020238396.png"
bgImgDark: 'https://cdn.jsdelivr.net/gh/open17/Pic/img/202403302340940.png'


features:
  - title: C++
    icon: 
      src:  https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021557151.svg
    details: "C++ 是一种高级语言，它是由 Bjarne Stroustrup 于 1979 年在贝尔实验室开始设计开发的。C++ 进一步扩充和完善了 C 语言，是一种面向对象的程序设计语言"
  - title: Python
    icon: 
      src: https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021557744.svg
    details: "Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。Python 由 Guido van Rossum 于 1989 年底发明，第一个公开发行版发行于 1991 年。"
  - title: Go
    icon: 
      src: https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021557367.svg
    details: "Go 是一个开源的编程语言，它能让构造简单、可靠且高效的软件变得容易。Go是从2007年末由Robert Griesemer, Rob Pike, Ken Thompson主持开发，并最终于2009年11月开源。"
    
---

<script setup> 
import {data as posts} from '../node_modules/vitepress-theme-open17/libs/posts.data.js' 

import { VPTeamMembers } from 'vitepress/theme'

const webSvg=`<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 16.875h3.375m0 0h3.375m-3.375 0V13.5m0 3.375v3.375M6 10.5h2.25a2.25 2.25 0 0 0 2.25-2.25V6a2.25 2.25 0 0 0-2.25-2.25H6A2.25 2.25 0 0 0 3.75 6v2.25A2.25 2.25 0 0 0 6 10.5Zm0 9.75h2.25A2.25 2.25 0 0 0 10.5 18v-2.25a2.25 2.25 0 0 0-2.25-2.25H6a2.25 2.25 0 0 0-2.25 2.25V18A2.25 2.25 0 0 0 6 20.25Zm9.75-9.75H18a2.25 2.25 0 0 0 2.25-2.25V6A2.25 2.25 0 0 0 18 3.75h-2.25A2.25 2.25 0 0 0 13.5 6v2.25a2.25 2.25 0 0 0 2.25 2.25Z" />
</svg>
`;

const contributers = [
  {
    avatar: 'https://camo.githubusercontent.com/a39422b1f8c7b28c67af50d4216b618b220946624ce7558461b2396ced787fa5/68747470733a2f2f7777772e6f70656e31372e7669702f6c6f676f2e706e67',
    name: 'open17',
    title: 'the builder of this repositories',
    links: [
      { icon: 'github', link: 'https://github.com/open17/' },
      {icon:{svg: webSvg},link: 'https://open17.vip'}
    ]
  },
]
</script>


:::details 博客的统计

从{{posts[posts.length-1].frontmatter.date.substring(0,10)}}开始, 写下了第一篇博客: {{posts[posts.length-1].frontmatter.title}}; 到{{posts[0].frontmatter.date.substring(0,10)}}, 写下了最近一次的博客: {{posts[0].frontmatter.title}}

总计已经写下了{{posts.length}}篇博客, 平均每{{Math.ceil(((Math.abs((new Date(posts[posts.length-1].frontmatter.date)).getTime()-(new Date(posts[0].frontmatter.date)).getTime())+1)/ (1000 * 3600 * 24))/posts.length)}}天完成一篇博客

:::

:::details 博客的贡献者

<VPTeamMembers size="medium" :members="contributers" />

:::




