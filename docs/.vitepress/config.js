import { defineConfig } from 'vitepress'
import defaultConfig from 'vitepress-theme-open17/config'
import markdownItFootnote from 'markdown-it-footnote'
import AutoSidebar from 'vite-plugin-vitepress-auto-sidebar';

export default defineConfig({
  vite: {
    plugins: [
      AutoSidebar({
        ignoreList:['page','posts','public']
      })
    ]
  },
  extends: defaultConfig,
  title: "Alg Note",
  description: "我的算法竞赛练习,笔记,博客与模板",
  markdown: {
    math: true,
    lineNumbers: true,
    config: (md) => {
      md.use(markdownItFootnote)
    }
  },
  head: [['link', { rel: 'icon', href: '/logo.png' }]],
  themeConfig: {
    blog: {
      avatar: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202402050154255.png",
      ornateStyle: true,
      bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404020226261.png",
      bgImgDark: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404061333172.jpeg",
      title: "Alg Note",
      desc: "Life is not about waiting for the storm to pass, but learning to dance in the rain.",
      pageSize: 5
    },
    footer: {
      message: 'All blogs and docs are licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0</a>',
      copyright: 'Copyright © 2023-present <a href="https://github.com/open17">open17</a>'
    },
    editLink: {
      pattern: 'https://github.com/open17/xcpc-note/edit/vitepress/docs/:path',
      text: 'Edit this page on GitHub'
    },
    logo: '/logo.png',
    search: {
      provider: 'local'
    },
    lastUpdated: {
      text: 'Updated at',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'medium'
      }
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Template', link: '/template/Intro/IO.html' },
      {
        text: "Blog",
        items: [
          { text: 'Home', link: '/page/blog' },
          { text: 'Tags', link: '/page/tags' },
          { text: 'Archive', link: ' /page/archive' },
        ]
      },
      {
        text: "博客主站",
        link: "https://open17.vip"
      },
    ],
    // sidebar: {
    //   '/template/': [
    //     {
    //       text: '前言',
    //       items: [
    //         { text: '输入输出', link: '/template/Intro/IO' },
    //         { text: '附录', link: '/template/Intro/append' },
    //       ]
    //     },
    //     {
    //       text: '基础算法',
    //       items: [
    //         { text: '二进制与集合', link: '/template/Alg/binary_set' },
    //         { text: '二分查找', link: '/template/Alg/binary_search' },
    //         { text: '前缀和与差分', link: '/template/Alg/presum' },
    //         { text: '离散化', link: '/template/Alg/discrete' },
    //         { text: '倍增', link: '/template/Alg/binary_lifting' },
    //         { text: ' 双指针', link: '/template/Alg/double_pointer' },
    //       ]
    //     },
    //     {
    //       text: '数据结构',
    //       items: [
    //         { text: '01字典树', link: '/template/DS/01tire' },
    //         { text: '对顶堆', link: '/template/DS/2heap' },
    //         { text: '树状数组', link: '/template/DS/BIT' },
    //         { text: '线段树', link: '/template/DS/segment_tree' },
    //         { text: 'ST表', link: '/template/DS/st' },
    //       ]
    //     },
    //     {
    //       text: '字符串',
    //       items: [
    //         { text: '后缀数组', link: '/template/String/SA' },
    //         { text: '字典树', link: '/template/String/Tire' },
    //         {text:'字符串哈希',link:'/template/String/hash'},
    //       ]
    //     },
    //     {
    //       text: '图论',
    //       items: [
    //         { text: '存图', link: '/template/Graph/save_graph' },
    //         { text: '最短路', link: '/template/Graph/shortest_graph' },
    //         {text:'割点与桥',link:'/template/Graph/cut'},
    //         { text: '拓扑排序', link: '/template/Graph/topo_sort' },
    //         { text: '并查集', link: '/template/Graph/BUF' },
    //       ]
    //     },
    //     // {
    //     //   text: '动态规划',
    //     //   items: [
    //     //     { text: '0.Intro & Logic', link: '/computer-basic/distcrete-structures/' },
    //     //   ]
    //     // },
    //     {
    //       text: '数学',
    //       items: [
    //         { text: '基本数论', link: '/template/Math/math_theory' },
    //       ]
    //     },
    //     {
    //       text: '杂项',
    //       items: [
    //         { text: '说明', link: '/template/Others/' },
    //         { text: '矩阵快速幂', link: '/template/Others/matrix_qpower' },
    //         { text: '快速幂', link: '/template/Others/qpower' },
    //         { text: '语法糖', link: '/template/Others/candy' },
    //         { text: '卡常', link: '/template/Others/Maybe-Faster' },
    //         { text: 'pick定理', link: '/template/Others/pick' },
    //         { text: '数论分块', link: '/template/Others/sqrt-decomposition' },
    //         { text: '非常用平衡树', link: '/template/Others/balance_tree' },

    //       ]
    //     }
    //   ],
    // },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/open17/xcpc-note' }
    ]
  }
})