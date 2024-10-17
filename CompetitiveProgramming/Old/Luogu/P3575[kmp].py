def KMP_search(s, pattern,prefix=None):
    # 构建前缀表
    if not prefix:
        prefix = get_prefix(pattern)
    i = 0  # 主字符串的位置
    j = 0  # 模式字符串的位置

    while i < len(s):
        if s[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1

        # 如果完全匹配
        if j == len(pattern):
            print(i - j+1)
            j = prefix[j - 1]  # 继续搜索下一个匹配

def get_prefix(pattern):
    prefix = [0] * len(pattern)
    j = 0  # 长度
    i = 1  # 从第二个字符开始

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1

    return prefix

# 测试代码
text = input()
pattern = input()
prefix = get_prefix(pattern)
KMP_search(text, pattern,prefix)

for idx,i in enumerate(prefix):
    end_f=" "
    if idx==len(prefix):
        end_f="\n"
    print(i,end=end_f)
