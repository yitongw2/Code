import java.util.*;

public class Solutions
{
	public static void main(String [ ] args)
	{
      		System.out.println("Hello World");

      		// reverse vowels in a string
      		String s = Reverse_Vowels_String.reverseVowels("hello");
      		System.out.println("hello => "+s);
      		
      		// fizz buzz problem
      		List<String> l = FizzBuzz.fizzBuzz(15);
      		for (int i=0;i<l.size();++i)
      		{
      			System.out.println(l.get(i));
      		}

      		// reverse string
		System.out.println(s+"==>"+ReverseString.reverseString(s));
	}
}
