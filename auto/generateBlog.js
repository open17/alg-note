import fs from 'fs';
import readline from 'readline';


const currentDate = new Date();
const year = String(currentDate.getFullYear());
const month = String(currentDate.getMonth() + 1).padStart(2, '0');
const day = String(currentDate.getDate()).padStart(2, '0');
const formattedDate = `${year}-${month}-${day}`;
const targetFolder = './docs/posts/';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question) {
    return new Promise((resolve) => {
        rl.question(question, resolve);
    });
}

(async () => {
    const title = await ask('博客标题：');
    console.log(`${title}`);

    const fileName = await ask('博客文件名：');
    console.log(`${fileName}`);
    const blogTemplate = `---
title: ${title}
date: ${formattedDate}
tags:
    - 标签
---
    
    `;
    fs.writeFile(targetFolder + formattedDate + '-' + fileName + '.md', blogTemplate, (err) => {
        if (err) {
            console.error('写入文件时出错：', err);
            return;
        }
        console.log('博客创建成功');
    });
    rl.close();
})();

