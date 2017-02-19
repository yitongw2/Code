import java.util.Hashtable;

public class Reverse_Vowels_String 
{
    public void setUpTable(Hashtable<Character, Integer> htable, char[] vowels, int size)
    {
        
        for (int i=0;i<size;++i)
        {
            htable.put(vowels[i], 1);
        }
    }
    
    public String reverseVowels(String s) {
    	char[] vowels={'a','e','i','o','u'};
        Hashtable<Character, Integer> htable=new Hashtable<Character, Integer>();
        setUpTable(htable, vowels, 5);
        char[] string=s.toCharArray();
        char temp;
        int i=0;
        int j=s.length()-1;
        while (i<j)
        {
            while (i<j && !htable.containsKey(Character.toLowerCase(string[i])))
            {
                ++i;    
            }
            while (i<j && !htable.containsKey(Character.toLowerCase(string[j])))
            {
                --j;
            }
            temp=string[i];
            string[i]=string[j];
            string[j]=temp;
            ++i;
            --j;
        }
        return new String(string);
    }
}