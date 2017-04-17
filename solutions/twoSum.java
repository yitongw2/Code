import java.util.Hashtable;

public class twoSum
{	
	public static Hashtable<Integer, Integer> buildHashtable(int[] nums)
	{
		Hashtable<Integer, Integer> dict=new Hashtable<Integer, Integer>();
		for (int i=0;i<nums.length;++i)
		{
			dict.put(nums[i], i);
		}
   		return dict;
	}
  
 	 public static int[] twoSum(int[] nums)
       	 {
    		int result=new int[2];
    		Hashtable<Integer, Integer> dict=buildHashtable(nums);
    		for (int i=0;i<nums.length;++i)
    		{
      			if (dict.containsKey(target-nums[i]) && (temp=dict.get(target-nums[i]))!=i)
      			{
        			result[0]=i;
        			result[1]=temp;
        			return result;
      			}
    		}
    		return result;
	 }
}
