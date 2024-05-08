import fs from 'node:fs';
import path from 'node:path';

export default {
    load() {
        const content = tryReadFile('./problems_statistics.json');
        return JSON.parse(content); // 返回解析后的JSON对象
    }
}

function tryReadFile(filePath) {
    try {
        return fs.readFileSync(filePath, 'utf-8');
    } catch (err) {
        console.error(`Error reading file ${filePath}: ${err}`);
        return null;
    }
}