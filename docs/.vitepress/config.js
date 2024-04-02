import { defineConfig } from 'vitepress'
import defaultConfig from 'vitepress-theme-open17/config'
import markdownItFootnote from 'markdown-it-footnote'

export default defineConfig({
  extends: defaultConfig,
  title: "Open17's Blog",
  description: "My VitePress Blog Site",
  markdown: {
    math: true,
    config: (md) => {
      md.use(markdownItFootnote)
    }
  },
  head: [['link', { rel: 'icon', href: '/logo.png' }]],
  themeConfig: {
    blog: {
      homeImgDark: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404021405381.jpg",
      bgImg: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202404020226261.png",
      ornateStyle: true,
      bgImgDark: "https://cdn.jsdelivr.net/gh/open17/Pic/img/202403011548000.png"
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
      {
        text: "Blog",
        items: [
          { text: 'Home', link: '/page/blog' },
          { text: 'Tags', link: '/page/tags' },
          { text: 'Archive', link: ' /page/archive' },
        ]
      },
      {
        text: "open17",
        link: "https://open17.vip"
      },
    ],
    sidebar: {
      '/template/': [
        {
          text: '算法模板',
          items: [
            { text: '0.Intro & Logic', link: '/computer-basic/distcrete-structures/' },
            { text: '1.SFSS', link: '/computer-basic/distcrete-structures/SFSS' },
            { text: '2.Counting', link: '/computer-basic/distcrete-structures/Counting' },
            { text: '3.Relations', link: '/computer-basic/distcrete-structures/Relations' },
            { text: '4.Graph', link: '/computer-basic/distcrete-structures/Graph' },
            { text: '5.Tree', link: '/computer-basic/distcrete-structures/Tree' }
          ]
        }
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/open17/xcpc-note' }
    ]
  }
})