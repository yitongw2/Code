
public class ReverseString
{
	public static String reverseString(String str)
	{
		char[] charArr = str.toCharArray();
		int size = str.length();
		for (int i = 0; i < size/2; ++i)
		{
			char tmp = charArr[i];
			charArr[i] = charArr[size-1-i];
			charArr[size-1-i] = tmp;
		}
		return new String(charArr);
	}
} 
