import config from '../docs/.vitepress/config.js'
import fs from 'fs';
const filePath = './README.md';
const menu = config.themeConfig.sidebar['/template/'];
const baselink = "https://alg.open17.vip";



let data = '';
// 平衡因子
let p = 1;
fs.readFileSync(filePath, 'utf8').split('\n').forEach(line => {
  if (line.includes('!menu start')) {
    data += line;
    p = 0;
    data+='\n';
    menu.forEach(fa => {
      data += "- " + fa.text + "\n";
      fa.items.forEach(son => {
        data += "    - " + "[" + son.text + "]" + "(" + baselink + son.link + ")\n";
      })
    });
    data+='\n';
  }
  if (line.includes('!menu end')) p = 1;
  if (p===1) data += line+'\n';
})


fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.error('写入文件时出错：', err);
    return;
  }
  console.log('文件已成功写入！');
});