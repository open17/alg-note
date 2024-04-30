import { defineConfig } from 'vitepress'
import defaultConfig from 'vitepress-theme-open17/config'
import markdownItFootnote from 'markdown-it-footnote'
import AutoSidebar from 'vite-plugin-vitepress-auto-sidebar';

export default defineConfig({
  vite: {
    plugins: [
      AutoSidebar({
        ignoreList: ['page', 'posts', 'public'],
        titleFromFile: true,
        beforeCreateSideBarItems: (data) => {
          const indexIndex = data.indexOf("index.md");
          if (indexIndex !== -1) {
            const indexValue = data[indexIndex];
            data.splice(indexIndex, 1);
            data.unshift(indexValue);
          }
          return data;
        }
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
      avatar: "https://avatars.githubusercontent.com/u/125687556?v=4",
      ornateStyle: true,
      // bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404020238396.png",
      // bgImgDark: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404061333172.jpeg",
      title: "Alg Note",
      desc: "Life is not about waiting for the storm to pass, but learning to dance in the rain.",
      pageSize: 3,
      tagPageLink:'/page/tags',
       maxTags:5
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
      { text: '首页', link: '/' },
      { text: '模板', link: '/template/0-Intro/' },
      {
        text: "博客",
        items: [
          { text: '主页', link: '/page/blog' },
          { text: '标签', link: '/page/tags' },
          { text: '归档', link: ' /page/archive' },
        ]
      },
      {
        text: "博客主站",
        link: "https://open17.vip"
      },
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/open17/xcpc-note' }
    ]
  }
})