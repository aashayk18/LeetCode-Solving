class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        if (candidates[0] > target) return res; 
        dfs(candidates, target, 0, res, new ArrayList<>());
        return res;
    }

    private void dfs(int[] candidates, int target, int start, List<List<Integer>> res, List<Integer> tracker) 
{
     if (target == 0) res.add(new ArrayList<>(tracker));
     else 
     {
        for (int i = start; i < candidates.length; i++) 
        {
	        if (candidates[i] > target) return;
	        tracker.add(candidates[i]);
            dfs(candidates, target - candidates[i], i, res, tracker);
            tracker.remove(tracker.size() - 1);
	    }
     }
}
}
