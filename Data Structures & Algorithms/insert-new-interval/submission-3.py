import heapq
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

#            (9,12)
#     (8,10)           (4,5)
# (7,11)  (5,10)     (3,12)      (2,23)

        def overlap(inter1,inter2):
            if inter2[0] > inter1[1] or inter2[1] < inter1[0]:
                return False
            else:
                return True
        def merge_interval(inter_old,inter_new):
            return [min(inter_old[0],inter_new[0])  ,  max(inter_old[1],inter_new[1])   ]

        i=0
        new_list=[]
        new_interval_inserted=False
        while i<len(intervals):
            if not new_interval_inserted and ( newInterval[1]<intervals[i][0] ):
                new_list.append(newInterval)
                new_list.extend(intervals[i:])
                new_interval_inserted=True
                break
            if overlap(intervals[i],newInterval) and not new_interval_inserted:
                new_interval_inserted=True
                new_list.append(merge_interval(intervals[i],newInterval))
            elif new_interval_inserted:
                #print(new_list[len(new_list)-1],intervals[i])
                if overlap(new_list[len(new_list)-1],intervals[i]):
                    pre_interval=new_list[len(new_list)-1]
                    new_list.pop()
                    new_list.append(merge_interval(pre_interval,intervals[i]))
                else:
                    new_list.extend(intervals[i:])
                    break
            else:
                new_list.append(intervals[i])
            i+=1
        if not new_interval_inserted:
            new_list.append(newInterval)
        return new_list


        # newInterval[0] > interval[i...][1] 
        # newInterval[1] < interval[j...][0] 
        # intervals[:i] + [ min(newInterval[0],intervals[i-1][0]) , max(newInterval[1],intervals[j-1][1]) ]  +intervals[j:] 







        