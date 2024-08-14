# :bookmark_tabs:Alg Note
这里是 $\mathcal{\pmb{Open17}}$ 的个人算法竞赛笔记与模板仓库

> 本仓库基于[vitepress-theme-open17](https://vitepress.open17.vip/)模板

## 🏷️ 仓库介绍

这是一个 monorepo 仓库，由一下几个部分组成:
- [code](https://github.com/open17/alg-note/tree/vitepress/code)：平时的练习代码
- [template](https://github.com/open17/alg-note/tree/vitepress/template): 算法模板文档
- [auto](https://github.com/open17/alg-note/tree/vitepress/auto): 一些自动化,包括自动化目录更新,CF打卡仓库自动推送等
- 其他,vitepress站点配置与页面

## 在线查看

- [首页](https://alg.open17.vip/)
- [算法模板](https://alg.open17.vip/template/0-Intro/IO.html)
- [题库](https://alg.open17.vip/page/problems.html)

## 常用指令


### vitepress命令

```shell
yarn dev
yarn build 
```

### 处理临时比赛代码

```shell
yarn move # 处理临时比赛代码
```

### 合并模板准备打印

```shell
python auto/print_pdf.py
```



## 贡献

如果您发现/遇到任何问题或有改进建议，欢迎来提issue或pr

非常感谢您的贡献和星标（⭐）！

## 本地运行/浏览

```shell
git clone https://github.com/open17/alg-note.git
cd alg-note
yarn
yarn dev
```

## 💝 鸣谢

- vitepress
- vitepress-theme-open17
- echart
- tailwindcss  
- element-plus
- shiki
- vitepress-python-editor







































