class Solution {
public:
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        int src = 0;
        vector<vector<pair<int, int>>> graph(n);
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }
        const int inf = 0x3f3f3f;
        vector<int> dist(n, inf);
        dist[src] = 0;
        vector<int> visited(n, 0);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        heap.push({0, src});
        while (!heap.empty()) {
            auto [d, u] = heap.top();
            heap.pop();
            if (visited[u] || d >= disappear[u]) {
                continue;
            }
            visited[u] = 1;
            for (const auto& [v, w] : graph[u]) {
                dist[v] = min(dist[v], dist[u] + w);
                if (dist[v] >= disappear[v]) {
                    dist[v] = inf;
                }
                heap.push({dist[v], v});
            }
        }
        vector<int> result;
        for (int i : dist) {
            result.push_back(i != inf ? i : -1);
        }
        return result;
    }
};