import { defineConfig } from 'vitepress'
import defaultConfig from 'vitepress-theme-open17/config'
import markdownItFootnote from 'markdown-it-footnote'
import { vitepressPythonEditor } from 'vitepress-python-editor/vite-plugin'

import { generateSidebar } from 'vitepress-sidebar';

const vitepressSidebarOptions = [{
  // documentRootPath: '/',
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
      vitepressPythonEditor({ assetsDir: './vitepress/dist/assets' }),
    ]
  },
  extends: defaultConfig,
  title: "Alg Note",
  description: "xcpc练习,笔记与模板",
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
    siteTitle: false,
    logo: '/logo.png',
    blog: {
      ornateStyle: true,
    },
    nav: [
      { text: '首页', link: '/' },
      { text: '模板', link: '/template/0-Intro/' },
      { text: '题库', link: 'website/page/problems' },

      {
        text: "更多",
        items: [
          { text: '在线运行', link: 'website/page/playground' },
          {
            text: "算法博客",
            link: "https://open17.vip"
          },
          {
            text: "Clist统计",
            link: "https://clist.by/coder/"
          }
        ]
      },

    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/open17/xcpc-note' }
    ],
    footer: {
      message: '网站基于vitepress主题<a href="https://vitepress.open17.vip" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">open17</a>💙',
      copyright: 'Copyright © 2023-present <a href="https://github.com/open17">open17</a>, 全部博客与文档(除特殊声明)均遵循协议<a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0</a>'
    },
    editLink: {
      pattern: 'https://github.com/open17/xcpc-note/edit/vitepress/:path',
      text: 'Edit this page on GitHub'
    },
    search: {
      provider: 'local'
    },
    lastUpdated: {
      text: 'Updated at',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'medium'
      }
    }
  }
})