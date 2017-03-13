import java.util.*; 

public class RussianEnvelopes
{
	// time complexity: O(n^2)
	public static int maxEnvelopes(int[][] envelopes) {
        	if (envelopes==null || envelopes.length==0 ||
            	    envelopes[0]==null || envelopes[0].length<2)
            		return 0;
        	Arrays.sort(envelopes, new Comparator<int[]>()
        	{
            		public int compare(int[] t1, int[] t2)
            		{
                		if (t1[0]==t2[0])
                    			return t2[1]-t1[1];
                		else
                    			return t1[0]-t2[0];
            		}
        	});
      
        	int[] table=new int[envelopes.length];
        	for (int i=0;i<envelopes.length;++i)
        	{
            		table[i] = 1;
            		for (int j=0;j<i;++j)
            		{
                		if (envelopes[i][0]>envelopes[j][0] && 
                    		envelopes[i][1]>envelopes[j][1] &&
                    		table[j]+1>table[i])
                    			table[i]=table[j]+1;
            		}
        	}
        	int max = 1;
        	for (int i=0;i<table.length;++i)
        	{
            		if (table[i]>max)
                		max=table[i];
        	}
        	return max;
    	}
}
