import java.util.List;

class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        // Initialize min and max with the first array's values
        int minValue = arrays.get(0).get(0);
        int maxValue = arrays.get(0).get(arrays.get(0).size() - 1);
        
        // Initialize maxDistance to store the result
        int maxDistance = 0;

        // Iterate through all arrays starting from the second array
        for (int i = 1; i < arrays.size(); i++) {
            List<Integer> currentArray = arrays.get(i);
            int currentMin = currentArray.get(0);
            int currentMax = currentArray.get(currentArray.size() - 1);

            // Calculate the maximum distance using the global min and max
            maxDistance = Math.max(maxDistance, Math.abs(currentMax - minValue));
            maxDistance = Math.max(maxDistance, Math.abs(maxValue - currentMin));

            // Update the global min and max
            minValue = Math.min(minValue, currentMin);
            maxValue = Math.max(maxValue, currentMax);
        }

        return maxDistance;
    }
}

