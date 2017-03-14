import java.util.*;

public class LongestIncreasingSubsequence
{
	// time : O(nlogn)
	public static int lengthOfLISBST(int[] nums)
	{
		// table used to keep track of the increasing subsequence itself
		int[] table = new int[nums.length];
		// keep track of the length of longest subsequence 
		int len = 0;
		for (int x: nums)
		{
			// binary search in table[0:len] for x.
			// bst returns the index of element if found; 
			// otherwise, returns -insert_point-1 (insert_point	
			// is where the x should be inserted in table).
			int i = Arrays.binarySearch(table, 0, len, x);
			// if i<0 --> not found
			if (i < 0)
				// recover insert_point for i
				i = -(i+1);
			// set the ith cell in table to be x
			table[i] = x;
			// insert_point i reaches len --> the length of longest
			// sequence increases
			if (i == len)
				++len;
		}
		return len;	
	}
	

	// time : O(n^2)
	public static int lengthOfLIS(int[] nums)
	{
		if (nums == null || nums.length == 0)
			return 0;
		int[] table = new int[nums.length];
		for (int i = 0;i < nums.length;++i)
		{
			table[i] = 1;
			for (int j = 0;j < i;++j)
			{
				if (nums[i] > nums[j] && table[j]+1 > table[i])
					table[i] = table[j]+1;
			}
		}
		int max = 1;
		for (int x: table)
		{
			if (x > max)
				max = x;
		}
		return max;
	}
}

