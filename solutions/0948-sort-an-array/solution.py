class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = nums
        low = 0
        high = len(arr)-1
        def merge_sort(arr,low,high):
            if(low>=high): return
            mid = (low+high)//2
            merge_sort(arr,low,mid)
            merge_sort(arr,mid+1,high)
            merge(arr,low,mid,high)
            
        
        def merge(arr,low,mid,high):
            tmp = []
            left = low
            right = mid+1

            while left <= mid and right <= high:
                if(arr[left] <= arr[right]):
                    tmp.append(arr[left])
                    left+=1
                else:
                    tmp.append(arr[right])
                    right+=1
            
            while left <= mid:
                tmp.append(arr[left])
                left+=1
            
            while right <= high:
                tmp.append(arr[right])
                right+=1

            arr[low:high+1] = tmp
        
        merge_sort(nums,low,high)
        return nums

