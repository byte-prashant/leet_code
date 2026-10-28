class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> ans = new ArrayList<>();

        for (int pos =0;pos<nums.length-2;pos++){

            if((pos>0) && (nums[pos] == nums[pos-1])){
                continue;
            }

            int target =  nums[pos];


            int left = pos+1;
            int right = nums.length -1;


            while(left<right){

                int total = nums[left]+nums[right]+ target;
                if (total<0){

                    left++;

                }else if (total>0){

                    right--;
                
                }else{
                    
                    ans.add(Arrays.asList(nums[left],nums[right],target));
                    left++;
                    right--;

                    while (left < right && nums[left]==nums[left-1]){

                        left++;
                    }

                    while (left < right && nums[right]==nums[right+1]){

                        right--;
                    }

                }


            }


        }
        return ans;
    }
}