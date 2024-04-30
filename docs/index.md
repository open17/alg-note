---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "Alg Note"
  text: "我的算法竞赛练习,笔记与模板"
  tagline: By open17
  actions:
    - theme: brand
      text: 查看模板
      link: /template/0-Intro/IO
    - theme: alt
      text: 浏览博客
      link: /page/blog
  image: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202402082225465.png"

# bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404020238396.png"
# bgImgDark: 'https://cdn.jsdelivr.net/gh/open17/Pic/img/202403302340940.png'


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
import DataShow from './components/DataShow.vue'

</script>

<DataShow class="mt-10"/>



