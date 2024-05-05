class Trie {
int next[50005][26][2],cnt;
public:
    Trie() {
        memset(next, 0, sizeof(next));
        cnt=0;
    }
    
    void insert(string word) {
        int n=word.size();
        int cur=0;
        for(int i=0;i<n;i++){
            int c=word[i]-'a';
            if(!next[cur][c][0])next[cur][c][0]=++cnt;
            if(i==n-1)next[cur][c][1]=1;
            cur=next[cur][c][0];
        }
    }
    
    bool search(string word) {
        int n=word.size();
        int cur=0;
        for(int i=0;i<n;i++){
            int c=word[i]-'a';
            if(!next[cur][c][0])return false;
            if(i==n-1)return next[cur][c][1]==1;
            cur=next[cur][c][0];
        }
        return false;
    }
    
    bool startsWith(string prefix) {
        int n=prefix.size();
        int cur=0;
        for(int i=0;i<n;i++){
            int c=prefix[i]-'a';
            if(!next[cur][c][0])return false;
            cur=next[cur][c][0];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */