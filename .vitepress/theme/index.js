//.vitepress/theme/index.js
import Theme from 'vitepress-theme-open17'
import Editor from 'vitepress-python-editor'
import "./style.css"

export default {
  extends: Theme,
  enhanceApp({ app }) {
    app.component('Editor', Editor)
  },
}