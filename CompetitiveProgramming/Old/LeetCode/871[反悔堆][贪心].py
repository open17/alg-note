class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        h=[]
        cnt=lst=0
        stations.append([target,0])
        stations.sort()
        for pos,f in stations:
            startFuel-=pos-lst
            lst=pos
            while startFuel<0 and len(h)>0:
                startFuel-=heappop(h)
                cnt+=1
            if startFuel<0:
                return -1
            if pos==target:
                break
            heappush(h,-f)
        return cnt