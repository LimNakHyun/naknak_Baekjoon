import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int N = nums.length;	//폰캣몬의 마리수
        HashSet<Integer> se = new HashSet<>();	//폰캣몬의 종류
        
        for (int i = 0; i < N; i++) {
            se.add(nums[i]);
        }
        
        if (se.size() < N/2) return se.size();
        else return N/2;
    }
}