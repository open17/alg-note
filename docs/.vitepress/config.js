import { defineConfig } from 'vitepress'
import defaultConfig from 'vitepress-theme-open17/config'
import markdownItFootnote from 'markdown-it-footnote'
import { vitepressPythonEditor } from 'vitepress-python-editor/vite-plugin'

import { generateSidebar } from 'vitepress-sidebar';

const vitepressSidebarOptions = [{
  documentRootPath: 'docs',
  scanStartPath: 'template',
  resolvePath: '/template/',
  collapsed: true,
  useTitleFromFileHeading: true,
  useFolderTitleFromIndexFile: true,
  useFolderLinkFromIndexFile: true,
  rootGroupCollapsed: true,
}];

export default defineConfig({
  vite: {
    plugins: [
      vitepressPythonEditor({ assetsDir: 'docs/.vitepress/dist/assets' }),
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
    sidebar: generateSidebar(vitepressSidebarOptions),
    blog: {
      avatar: "https://avatars.githubusercontent.com/u/125687556?v=4",
      ornateStyle: true,
      title: "Alg Note",
      desc: "Life is not about waiting for the storm to pass, but learning to dance in the rain.",
      pageSize: 10,
      tagPageLink:'/page/tags',
      maxTags:5,
      widgets:[
      ]
    },
    footer: {
      message: '网站基于vitepress主题<a href="https://vitepress.open17.vip" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">open17</a>💙',
      copyright: 'Copyright © 2023-present <a href="https://github.com/open17">open17</a>, 全部博客与文档(除特殊声明)均遵循协议<a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0</a>'
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