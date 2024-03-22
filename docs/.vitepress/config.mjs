import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "xcpc note",
  description: "My xcpc note website",
  themeConfig: {
    logo: '/logo.png',
    search: {
      provider: 'local'
    },
     footer: {
      message: 'Released under the Apache License.',
      copyright: 'Copyright © 2023-present open17'
    },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/open17/' }
    ]
  }
})
