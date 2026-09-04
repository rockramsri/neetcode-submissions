class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result=sorted(zip(position,speed),key=lambda x:x[0])
        position,speed=map(list,zip(*result))
        # print(position,speed)

        hrs=[ (target-position[i])/speed[i] for i in range(0,len(position))]
        #print(hrs)
        current_fleet_count=1
        fleet_arr=[1]
        longest_car_infront=hrs[len(hrs)-1]
        for i in range(len(hrs)-2,-1,-1):
            if hrs[i]<=longest_car_infront:
                fleet_arr.append(current_fleet_count)
            else:
                longest_car_infront=hrs[i]
                current_fleet_count+=1
                fleet_arr.append(current_fleet_count)
        #print(fleet_arr)
        return current_fleet_count
        #[5,2.75hr, 6hrs]

        #[1,1,12,7,3]
        # [3,4.5,10,3hrs]
        # (target-postion[i])/speed =  9/3 = 3hrs it will be one car
        # 6/2 = 3 hrs

        # 10hrs , 4.5hrs , 3hrs , 3hrs
        # for i in range(0,len(position)):
        #     if 
        