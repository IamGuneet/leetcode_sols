class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # def mergeSort(arr,left,right):
        #     if left>=right:
        #         return
        #     if right>left:

        #         mid = left + (right-left)//2
        #         mergeSort(arr,left,mid)
        #         mergeSort(arr,mid+1,right)
        #         join(arr,left,mid,right)
        
        # def join(arr,left,mid,right):
        #     i = left
        #     j = mid+1
        #     tmp =[]
        #     while (i<=mid and j <= right):

        #         if (arr[i][0] < arr[j][0]):
        #             tmp.append(arr[i])
        #             i+=1
        #         else:
        #             tmp.append(arr[j])
        #             j+=1
        #     while i<= mid:
        #         tmp.append(arr[i])
        #         i+=1
        #     while j<= right:
        #         tmp.append(arr[j])
        #         j+=1
        #     arr[left:right+1]=tmp

        # mergeSort(intervals,0,len(intervals)-1)
        # return intervals
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged

        
