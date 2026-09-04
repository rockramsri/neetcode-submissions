class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlapping(inter_old,inter_new):
            if inter_new[1] < inter_old[0] or inter_new[0] > inter_old[1]:
                return False
            else:
                return True
        def merge_overlap(inter_1,inter_2):
            return [min(inter_1[0],inter_2[0]) , max(inter_1[1],inter_2[1])    ]
        intervals.sort(key=lambda x:x[0])
        # need to hanlde hte empty list
        new_list=[intervals[0]]
        for i in range(1,len(intervals)):
            if is_overlapping(new_list[len(new_list)-1],intervals[i]):
                temp_inter=new_list[len(new_list)-1]
                new_list.pop()
                new_list.append(merge_overlap(temp_inter,intervals[i]))
            else:
                new_list.append(intervals[i])
        #print(new_list)
        return new_list
        