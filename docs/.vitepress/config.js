import { defineConfig } from 'vitepress'
import defaultConfig from 'vitepress-theme-open17/config'
import markdownItFootnote from 'markdown-it-footnote'
import AutoSidebar from 'vite-plugin-vitepress-auto-sidebar';
import { vitepressPythonEditor } from 'vitepress-python-editor/vite-plugin'

export default defineConfig({
  vite: {
    plugins: [
      vitepressPythonEditor({ assetsDir: 'docs/.vitepress/dist/assets' }),
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
      title: "Alg Note",
      desc: "Life is not about waiting for the storm to pass, but learning to dance in the rain.",
      pageSize: 10,
      tagPageLink:'/page/tags',
      maxTags:5,
      widgets:[
        {
          name:"题目分析", // 自定义链接名称
          link:'/page/problems',  //可以为空,非空会显示对应的链接
          html: `<div class="flex justify-center items-center">
            <div id="code-chart"></div>
        </div>`, //内容html,支持tailwindcss
        },
        {
          name:"做题日历`", // 自定义链接名称
          html:`<div class="flex justify-center items-center">
            <div id="code-date"></div>
        </div>`, //内容html,支持tailwindcss
        },
      ]
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
      { text: '题库', link: '/page/problems' },
      { text: '练习场', link: '/page/playground' },
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