class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        string word="";
        string ans="";
        sentence+=" ";
        int next[100005][26][2];
        memset(next,0,sizeof(next));
        int cnt=0;
        for(auto s:dictionary){
            int cur=0;
            for(int i=0;i<s.size();i++){
                int c=s[i]-'a';
                if(!next[cur][c][0])next[cur][c][0]=++cnt;
                if(i==s.size()-1)next[cur][c][1]=1;
                cur=next[cur][c][0];
            }
        }
        for(auto c:sentence){
            if(c!=' '){
                word+=c;
                continue;
            }
            int cur=0;
            string root="";
            int find=0;
            for(auto cc:word){
                if(!next[cur][cc-'a'][0]){
                    break;
                }
                root+=cc;
                if(next[cur][cc-'a'][1]){
                    find=1;
                    break;
                }
                cur=next[cur][cc-'a'][0];
            }
            if(find)ans+=root;
            else ans+=word;
            ans+=" ";
            word="";
        }
        return ans.substr(0,ans.size()-1);
    }

};