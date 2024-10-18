/*

改下传函数的时候右边忘记除以2了,debug了3个小时,引以为戒

 */

// #define USE_DEBUG
// USE_DEBUG 模式下的输出
template <typename T>
void debug(const T &t)
{
#ifdef USE_DEBUG
    std::cout << t << "\n\n";
#endif
}
template <typename T, typename... Args>
void debug(const T &t, const Args... args)
{
#ifdef USE_DEBUG
    std::cout << t << ' ';
    debug(args...);
#endif
}

class Solution
{
public:
    static constexpr int N = 1e5 + 5;
    int val[N];
    int node[N << 2], todo[N << 2];

    void _do(int p, int size)
    {
        node[p] = size - node[p];
        todo[p] ^= 1;
    }

    void _down(int p, int l, int r)
    {
        if (l >= r || !todo[p])
            return;
        int size = r - l + 1;
        _do(p * 2, size - size / 2);
        _do(p * 2 + 1, size / 2);
        todo[p] = 0;
    }

    void _up(int p)
    {
        node[p] = node[p * 2] + node[p * 2 + 1];
    }

    void build(int p, int l, int r)
    {
        if (l == r)
        {
            node[p] = val[l];
            return;
        }
        int mid = (l + r) >> 1;
        build(p * 2, l, mid);
        build(p * 2 + 1, mid + 1, r);
        _up(p);
    }

    void update(int p, int l, int r, int L, int R)
    {
        if (L <= l and r <= R)
        {
            _do(p, r - l + 1);
            return;
        }
        int mid = (l + r) >> 1;
        _down(p, l, r);
        if (L == 2 && R == 3)
        {
            debug(4, node[4], 5, node[5]);
        }
        if (mid >= L)
            update(p * 2, l, mid, L, R);
        if (mid < R)
            update(p * 2 + 1, mid + 1, r, L, R);
        _up(p);
    }

    long long query(int p, int l, int r, int L, int R)
    {
        if (L <= l and r <= R)
        {
            return node[p];
        }
        _down(p, l, r);
        long long ans = 0;
        int mid = (l + r) >> 1;
        if (mid >= L)
            ans += query(p * 2, l, mid, L, R);
        if (mid < R)
            ans += query(p * 2 + 1, mid + 1, r, L, R);
        return ans;
    }

    vector<long long> handleQuery(vector<int> &nums1, vector<int> &nums2, vector<vector<int>> &queries)
    {
        int n = nums1.size();
        for (int i = 0; i < n; i++)
        {
            val[i + 1] = nums1[i];
        }
        build(1, 1, n);
        vector<long long> ans;
        long long s = 0;
        for (auto i : nums2)
        {
            s += i;
        }
        for (auto q : queries)
        {
            if (q[0] == 3)
                ans.push_back(s);
            else if (q[0] == 2)
                s += query(1, 1, n, 1, n) * q[1];
            else
            {
                update(1, 1, n, q[1] + 1, q[2] + 1);
                debug("sum", query(1, 1, n, 1, n));
                for (int i = 1; i <= 5; i++)
                {
                    debug(i, "node", node[i], "todo", todo[i]);
                }
            }
        }
        return ans;
    }
};
