class Solution {
public:
    int countTexts(string pressedKeys) {
        // 2 types
        int n=pressedKeys.size();
        int dp1[n+1],dp2[n+1];
        dp1[0]=1;
        dp2[0]=1;
        int MOD=1e9+7;
        for(int i=1;i<=n;i++){
            dp1[i]=dp1[i-1];
            dp2[i]=dp2[i-1];
            if(i>=2){
                dp1[i]=(dp1[i]+dp1[i-2])%MOD;
                dp2[i]=(dp2[i]+dp2[i-2])%MOD;
            }
            if(i>=3){
                dp1[i]=(dp1[i]+dp1[i-3])%MOD;
                dp2[i]=(dp2[i]+dp2[i-3])%MOD;
            }
            if(i>=4)dp2[i]=(dp2[i]+dp2[i-4])%MOD;
        }
        int lst=pressedKeys[0]-'0',len=0;
        long long ans=1;
        pressedKeys+='0';
        for(auto c:pressedKeys){
            int cc=c-'0';
            if(lst==cc){
                len++;
                continue;
            }
            if(lst!=7&&lst!=9)ans*=dp1[len];
            else ans*=dp2[len];
            ans%=MOD;
            len=1;
            lst=cc;
        }
        return ans;
    }
};