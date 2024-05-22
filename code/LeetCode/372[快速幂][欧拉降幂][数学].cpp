constexpr int Phi(int n) noexcept
{
    int result = n;
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            while (n % i == 0)
            {
                n /= i;
            }
            result -= result / i;
        }
    }
    if (n > 1)
    {
        result -= result / n;
    }
    return result;
}

class Solution
{
public:
    static constexpr int MOD = 1337;
    static constexpr int PHI_M = Phi(MOD);
    int superPow(int a, vector<int> &b)
    {
        int bm = 0;
        for (int i =0; i < b.size() ; i++)
        {
            bm = ((bm * 10)% PHI_M + b[i]% PHI_M) % PHI_M;
        }
        if (gcd(a, MOD) != 1)
            bm += PHI_M;
        cout<<bm<<endl;
        return qpow(a, bm, MOD);
    }
    int qpow(int a, int b, int p)
    {
        int ans = 1;
        while (b)
        {
            if (b & 1)
                ans = ((ans%p) *(a%p)) % p;
            a = ((a%p) * (a%p)) % p;
            b >>= 1;
        }
        return ans;
    }
};