import fs from 'node:fs';
import path from 'node:path';

export default {
    watch: ['../code/**/*.py', '../code/**/*.cpp'],
    load(watchedFiles) {
        const problems = [];
        const allTags = new Set();
        const whiteList = ['duipai','tmp'];
        watchedFiles.forEach(file => {
            const parsedPath = path.parse(file);
            const folderName = path.basename(path.dirname(file));
            const regex = /\[([^\]]*?)\]/g;
            let tags = [];
            const name=parsedPath.name.replace(regex, (match, p1) => {
                tags.push(p1);
                allTags.add(p1);
                return "";
            });
            const content = tryReadFile(file);
            const lang = getLanguageFromExtension(parsedPath.ext);
            if (content&& !whiteList.includes(folderName)) {
                problems.push({ category: folderName,name: name, code: content, tags: tags, lang });
            }
        });

        return { problems: problems, allTags: Array.from(allTags) };
    }
};

function tryReadFile(filePath) {
    try {
        return fs.readFileSync(filePath, 'utf-8');
    } catch (err) {
        console.error(`Error reading file ${filePath}: ${err}`);
        return null;
    }
}

function getLanguageFromExtension(extension) {
    const extensions = { '.cpp': 'cpp', '.py': 'python' };
    return extensions[extension] || 'unknown';
}
