import fs from 'node:fs/promises';  // 使用 fs 的 promises API
import path from 'node:path';
import { exec } from 'node:child_process';
import util from 'node:util';

const execAsync = util.promisify(exec);  // 将 exec 转换为返回 promise 的函数

export default {
    watch: ['../code/**/*.py', '../code/**/*.cpp'],
    async load(watchedFiles) {
        const whiteList = ['duipai'];
        const typeCount = {};  // 存储按类型统计的结果
        const dateCount = {};  // 存储按日期统计的结果

        await Promise.all(watchedFiles.map(async (filePath) => {
            let birthDate;
            try {
                // 异步执行 Git 命令获取文件的首次提交日期
                const { stdout } = await execAsync(`git log --reverse --format="%ai" -- "${filePath}" | head -1`);
                birthDate = new Date(stdout.trim()).toISOString().split('T')[0];
            } catch (error) {
                // 如果 Git 命令失败，异步获取本地文件系统的创建日期
                const stats = await fs.stat(filePath);
                birthDate = stats.birthtime.toISOString().split('T')[0];
            }

            const type = path.basename(path.dirname(filePath));  // 获取文件所在的文件夹名称作为类型

            if (!whiteList.includes(type)) {
                // 更新类型统计
                if (!typeCount[type]) {
                    typeCount[type] = 0;  // 如果该类型尚未初始化，则初始化
                }
                typeCount[type] += 1;  // 对该类型的文件数量进行累加

                // 更新日期统计
                if (!dateCount[birthDate]) {
                    dateCount[birthDate] = 0;  // 如果该日期尚未初始化，则初始化
                }
                dateCount[birthDate] += 1;  // 对该日期的文件数量进行累加
            }
        }));

        return { typeCount, dateCount };  // 返回按类型和日期分开的统计结果
    }
}
