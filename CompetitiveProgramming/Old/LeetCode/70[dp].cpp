class Solution {
public:
    int climbStairs(int n) {
        // f(i)=f(i-1)+f(i-2)
        int f[n+1];
        memset(f,0,sizeof(f));
        f[0]=1;
        for(int i=1;i<=n;i++){
            f[i]=f[i-1];
            if(i-2>=0)f[i]+=f[i-2];
        }
        return f[n];
    }
};