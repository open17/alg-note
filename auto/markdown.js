import fs from 'fs';


import { generateMenu } from './menuGenerator.js';

const writePath = './README.md';
const readPath = './README.md';

(async () => {
  const path = 'docs/template';
  const menu = await generateMenu(path);
  let data = '';
  // 平衡因子
  let p = 1;
  fs.readFileSync(readPath, 'utf8').split('\n').forEach(line => {
    if (line.includes('!menu start')) {
      data += line;
      p = 0;
      data+=menu;
    }
    if (line.includes('!menu end')) p = 1;
    if (p === 1) data += line + '\n';
  })


  fs.writeFile(writePath, data, (err) => {
    if (err) {
      console.error('写入文件时出错：', err);
      return;
    }
    console.log('文件已成功写入！');
  });
})();



