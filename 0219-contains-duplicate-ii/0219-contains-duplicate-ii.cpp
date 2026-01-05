class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
      int n = nums.size();
  
    // Traverse for every element
    for (int i = 0; i < n; i++) {
      
        // Traverse next k elements 
        for (int c = 1; c <= k && (i + c) < n; c++) {
            int j = i + c;
          
            // If we find one more occurrence 
            // within k
            if (nums[i] == nums[j])
              return true;
        }
    }
    return false;  
    }
};