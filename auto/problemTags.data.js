import fs from 'node:fs';
import path from 'node:path';

export default {
    watch: ['../code/**/*.py', '../code/**/*.cpp'],
    load(watchedFiles) {
        const problems = [];
        const allTags = new Set();
        allTags.add("全部");
        watchedFiles.forEach(file => {
            const parsedPath = path.parse(file);
            const folderName = path.basename(path.dirname(file));
            const regex = /\[([^\]]*?)\]/g;
            let tags = ["全部"];
            parsedPath.name.replace(regex, (match, p1) => {
                tags.push(p1);
                allTags.add(p1);
            });
            const fileName = `${folderName} ${parsedPath.name}`;
            const content = tryReadFile(file);

            const lang = getLanguageFromExtension(parsedPath.ext);
            if (tags.length > 0 && content) {
                problems.push({ name: fileName, code: content, tags: tags, lang });
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
