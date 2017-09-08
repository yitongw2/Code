#include <iostream>
#include <string>

using namespace std;

// compute failure table
void computeLookUpTable(string word, int* f)
{
    int n = word.size();
    f[0] = 0;
    for (int i = 1; i < n; ++i)
    {
        int t = f[i-1];
        while (t>0 && word.at(i)!=word.at(t))
            t = f[t-1];
        if (word.at(i) == word.at(t))
            ++t;
        f[i] = t;
    }
}

int kmp(string word, string text)
{
    int tn = text.size();
    int wn = word.size();
    int f [wn];    
    computeLookUpTable(word, f);

    int i = 0, j = 0;
    while (i < tn && j < wn)
    {
        if (text.at(i) == word.at(j))
        {
            ++i;
            ++j;
        }
        else
        {
            if (j == 0)
                ++i;
            else
                j = f[j-1];
        }   
    }

    if (j == wn)
        return i-j;
    return -1;   
}

int main(int argc, char *argv[])
{
    string text = "Around the time presidential candidate Donald Trump was touting his real estate dealings at a Republican primary debate, a proposal was in the works to build a Trump Tower in Russia that would have given his company a $4 million upfront fee, no upfront costs, a percentage of the sales, and control over marketing and design. And that's not all: the deal included the opportunity to name the hotel spa after his daughter Ivanka.";
    string word (argv[1]);
    int i = kmp(word, text);
    cout << text << endl;
    cout << i << endl;
    cout << (i>0?text.substr(i, word.size()):"N/A") << endl;
    return 0;
}
