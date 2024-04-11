import fs from 'node:fs'

export default {
    watch: ['../code/**/*.py','../code/**/*.cpp'],
    load(watchedFiles) {
        const whiteList = ['duipai'];
        const m = {}
        watchedFiles.forEach(w => {
            let arr = w.split('/');
            const type = arr[arr.length - 2];
            if (!whiteList.includes(type)) {
                if (m[type] != null) {
                    m[type] += 1;
                } else {
                    m[type] = 1;
                }
            }
        });
        return m;
    }
}