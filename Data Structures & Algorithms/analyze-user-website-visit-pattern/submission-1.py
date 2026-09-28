class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        collection = []
        for i in range(len(username)):
            name = username[i]
            time = timestamp[i]
            site = website[i]
            collection.append((name, site, time))
        collection.sort(key=lambda x: x[2])

        mapping = defaultdict(list)
        for name, site, time in collection:
            mapping[name].append(site)
        counter = defaultdict(int)
        
        for name in mapping:
            l = mapping[name]
            keys = set()
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    for k in range(j+1, len(l)):
                        key = (l[i], l[j], l[k])
                        keys.add(key)
            for key in keys:
                counter[key] += 1
        maxCount = 0
        res = ()
        for key in counter:
            if counter[key] > maxCount or (counter[key] == maxCount and res > key):
                res = key
                maxCount = counter[key]

        return list(res)





        