import fs from 'fs';
const baselink = "https://alg.open17.vip";

async function isDirectory(folderPath) {
    try {
        const stats = fs.statSync(folderPath);
        return stats.isDirectory();
    } catch (error) {
        console.error('无法获取文件状态信息：', error);
        return false;
    }
}

export async function generateMenu(folderPath) {
    let menu = "";
    const files = await fs.promises.readdir(folderPath);
    for (const f of files) {
        const fullPath = folderPath + '/' + f;
        if (await isDirectory(fullPath)) {
            menu += "\n- " + f.substring(2, f.length) + "\n";
            menu += await generateMenu(fullPath);
        } else {
            if (f.endsWith('.md') && f !== "README.md" && f !== 'index.md') {
                menu += "\n   - " + "[" + f.substring(0, f.length - 3) + "]" + "(" + baselink + '/' + fullPath.substring(0, fullPath.length - 3) + ") \n";
            }
        }
    }
    return menu;
}