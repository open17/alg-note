---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "xcpc note"
  text: "我的算法竞赛练习,笔记与模板"
  tagline: By open17
  actions:
    - theme: brand
      text: 算法模板
      link: /template/IO
    - theme: alt
      text: 算法博客
      link: https://blog.open17.vip/
  image: /logo.png

bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404020238396.png"
bgImgDark: 'https://cdn.jsdelivr.net/gh/open17/Pic/img/202403302340940.png'


features:
  - title: C++
    icon: 
      src:  https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021557151.svg
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
  - title: Python
    icon: 
      src: https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021557744.svg
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
  - title: Go
    icon: 
      src: https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021557367.svg
    details: Lorem ipsum dolor sit amet, consectetur adipiscing elit
    
---

<script setup> 
import {data as posts} from '../node_modules/vitepress-theme-open17/libs/posts.data.js' 
</script>


## 博客的统计

从{{posts[posts.length-1].frontmatter.date.substring(0,10)}}开始,写下了第一篇博客: {{posts[posts.length-1].frontmatter.title}}

到{{posts[0].frontmatter.date.substring(0,10)}},写下了最近一次的博客: {{posts[0].frontmatter.title}}

总计已经写下了篇{{posts.length}}博客,平均下来{{Math.ceil(((Math.abs((new Date(posts[posts.length-1].frontmatter.date)).getTime()-(new Date(posts[0].frontmatter.date)).getTime())+1)/ (1000 * 3600 * 24))/posts.length)}}天写一篇博客

## 算法竞赛到底要用什么语言?

如果你指的是XCPC类比赛的话,我想C++一定是目前最合适的语言

现在一般XCPC类的比赛支持C++,Java,Python三种语言

但目前为止几乎所有国内参赛者都选择使用C++(排除用py水高精度之类的特殊情况)

很多人会说使用C++是因为运行速度快,所以推荐使用C++

但在我看来,严格意义上来说是不准确的

算法竞赛本质上考察的应该是时间复杂度的优劣,而非运行时间的优劣,不然为什么我们不使用Assembly提升速度呢?

但是正如停机问题所揭示的那样,我们很难直接分析一个复杂算法的准确复杂度,所有才使用时间限制来判断一个算法的优劣

从这个角度来说,理应每个语言对应的时限都是特别设置的,但是如你所见这是一个庞大的工作量,需要每道题目每种语言都进行大量的测试

因此遵循算法竞赛历史原因,同样也是因为C++运行速度的优势,一般题目数据只C++的角度出发设计,所有很多时候py和java并没有非常合理的时间复杂度

那为什么这里还有py和go的内容呢?

在我看来,python很适合新手接触了解算法竞赛,它提供更为语义化更适合算法竞赛的一些语言特点,同时较为简洁清晰

go呢? 你可以参考[0x3f](https://github.com/EndlessCheng/codeforces-go)的回答:smile:

## 学习参考

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=EndlessCheng&repo=codeforces-go)](https://github.com/EndlessCheng/codeforces-go)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=OI-wiki&repo=OI-wiki)](https://github.com/OI-wiki/OI-wiki)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=enkerewpo&repo=OI-Public-Library)](https://github.com/enkerewpo/OI-Public-Library)







