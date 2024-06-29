#include<bits/stdc++.h>
using namespace std;
int trie[250005][4],maxnode=0,n,size[250005],mbl,ans;
int p;
char mb[1005],x[1005];
bool b[250005][4],ended[2500005];
void insert(char s[]){
	int now=0,len=strlen(s);
	for(int i=0;i<len;i++){
		if(s[i]=='A')p=0;
		if(s[i]=='C')p=1;
		if(s[i]=='T')p=2;
		if(s[i]=='G')p=3;
	    size[now]++;
		if(!trie[now][p])trie[now][p]=++maxnode;
		now=trie[now][p];
	}
	size[now]++;
	ended[now]=1;
	return;
}
void dfs(int ws,int now){
	if(!size[now])return;
	if(ws==mbl){
		ans+=ended[now];
		size[now]-=ended[now];
		ended[now]=0;
		return;
	}
	if(mb[ws]=='?'){
		for(int i=0;i<4;i++){
		    int son=trie[now][i];
			if(son)dfs(ws+1,son);
		}
	}
	else if(mb[ws]=='*'){
		dfs(ws+1,now);
		for(int i=0;i<4;i++)if(trie[now][i]){
			dfs(ws+1,trie[now][i]);
			dfs(ws,trie[now][i]);
		}
	}
	else {
		if(mb[ws]=='A')p=0;
		if(mb[ws]=='C')p=1;
		if(mb[ws]=='T')p=2;
		if(mb[ws]=='G')p=3;
		if(trie[now][p])dfs(ws+1,trie[now][p]);
	}
	size[now]=0;
	for(int i=0;i<4;i++)if(trie[now][i])size[now]+=size[trie[now][i]];
}
int main(){
	scanf("%s%d",mb,&n);
	mbl=strlen(mb);
	for(int i=1;i<=n;i++){
		scanf("%s",x);
		insert(x);
	}
	dfs(0,0);
	cout<<n-ans;
	return 0;
} 