import config from '../docs/.vitepress/config.js'
import fs from 'fs';
const filePath = './README.md';
const preFilePath='./auto/README_pre.md';
const aftFilePath='./auto/README_aft.md';
const menu=config.themeConfig.sidebar['/template/'];
const baselink="https://alg.open17.vip"



let data = fs.readFileSync(preFilePath, 'utf8');
menu.forEach(fa => {
    data+="- "+fa.text+"\n";
    fa.items.forEach(son => {
        data+="    - "+"["+son.text+"]"+"("+baselink+son.link+")\n";
    })
});
data += fs.readFileSync(aftFilePath, 'utf8');

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.error('写入文件时出错：', err);
    return;
  }
  console.log('文件已成功写入！');
});