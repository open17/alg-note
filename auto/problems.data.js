import fs from 'node:fs';
import path from 'node:path';

export default {
    watch: ['../code/**/*.py', '../code/**/*.cpp'],
    load(watchedFiles) {
        const whiteList = ['duipai'];
        const typeCount = {}; // 存储按类型统计的结果
        const dateCount = {}; // 存储按日期统计的结果

        watchedFiles.forEach(filePath => {
            const stats = fs.statSync(filePath); // 获取文件状态信息
            const birthDate = stats.birthtime.toISOString().split('T')[0]; // 获取创建日期并格式化为 YYYY-MM-DD
            const type = path.basename(path.dirname(filePath)); // 获取文件所在的文件夹名称作为类型

            if (!whiteList.includes(type)) {
                // 更新类型统计
                if (!typeCount[type]) {
                    typeCount[type] = 0; // 如果该类型尚未初始化，则初始化
                }
                typeCount[type] += 1; // 对该类型的文件数量进行累加

                // 更新日期统计
                if (!dateCount[birthDate]) {
                    dateCount[birthDate] = 0; // 如果该日期尚未初始化，则初始化
                }
                dateCount[birthDate] += 1; // 对该日期的文件数量进行累加
            }
        });

        return { typeCount, dateCount }; // 返回按类型和日期分开的统计结果
    }
}
