import java.util.*;

// Leetcode 412
public class FizzBuzz
{
	public static List<String> fizzBuzz(int n)
	{
		// List is an abstract type implemented with ArrayList
		List<String> result=new ArrayList<String>();
		// Without using %
		for (int i=1, fizz=1, buzz=1;i<=n;++i)
		{
			// fizz is used to count the multiple of 3
			// buzz is used to count the multiple of 5
			if (fizz==3 && buzz==5)
			{
				result.add("FizzBuzz");
				fizz=0;
				buzz=0;
			}
			else if (fizz==3)
			{
				result.add("Fizz");
				fizz=0;
			}
			else if (buzz==5)
			{
				result.add("Buzz");
				buzz=0;
			}
			else
			{
				result.add(String.valueOf(i));
			}
			++fizz;
			++buzz;
		}
		return result;
	}
}