title: 豌豆荚二面
Date: 2014-3-28 20:17
Tags: 面试
md_linebreaks:two

豌豆荚的二面来的挺快，形式与一面一样。但可惜这次难度就大了点，不像一面那么随意了。

上来还是一样谈项目，这次这个面试官没有对某个特定的项目感兴趣，几乎是让我把所有的项目都谈了，包括在实验室做的事。最后他可能
对遗传算法有过研究，看到我的QRobot项目，就跟我讨论了一下实现过程，期间遇到的问题等等。这里得出一个经验，写简历介绍项目时适
当的加上该项目使用的核心技术等东西，说不定就戳中了面试官的兴趣点，这点正好又是你擅长的，那么很可能会跟面试官有个很愉快的交流。

本次面试失败在第二环节，现场写代码上。第一道题是要求从一个长串中查找字串，不管顺序，也不管中间是否有其他字符。因为很久没写
过C++代码了，更是一年多没看过动规，上来这个算法题，一看，很快就写出了递归式。因此后面的想法就不可遏制的往递归上想去了。

实际上这次有两道题，我开始想第一道题时，面试官提示我先做会做的。看了看第二道题，要求计算圆周率pi值。这个简单，虽然忘了级数
展开公式，但好歹蒙特卡罗法是记得很轻的。上手用了10分钟写了个蒙特卡罗计算pi的算法：

```c
double compute_pi()
{
    int MAX = 2000000;
    double RAND_MAX_DOUBLE=10000.0;
    int RAND_MAX=10000;
    int count = 0;
    srand(time(NULL));
    for(int i=0;i<MAX;i++)
    {
        int x = rand()%RAND_MAX/RAND_MAX_DOUBLE;
        int y = rand()%RAND_MAX/RAND_MAX_DOUBLE;
        int dis = sqrt(x*x+y*x);
        if(dis>=1)
        {
            count++;
        }
    }

    return 4.0*count/MAX;
}
```

接着开始考虑第二道题，这个就陷入了递归的陷阱里去不能自拔，化了10分钟考虑，差不多都12点了，想了想不好意思再考虑，就先把
自己考虑的递归式写上去了。递归式的思路没错，但最终证明是我问题复杂化了。一开始想写动规程序的，发现比我预想的复杂的多，只
好退而求其次，写个递归程序算了。花了20分钟写出了递归函数。实际上并不完整，还有两种情况没考虑，写到这里才觉得不对劲，怎么
居然有6种情况要考虑，这还是递归的。。。但实际已经12点半了，也不好再写了，匆匆交了。。。

下午跟贞子交流了一下，才知道那个题是leetcode的原题，叫min-window。不用递归是能解得。查了一下，果然。。。递归是走了弯路了。
顿时感觉渺茫，估计是跪了。下午4点左右，突然那面试官给发了条短信，说我理解错了题意，考虑复杂了。让我再重写一下。。。这还是
第一次遇到这种情况，就按刚看的线性算法，自己实现了一个版本，交了上去，不知道后果如何。下面是代码：

```c

//给出一个字符串str，假设是（ABC）；给出一个文档Doc（DEACFBAEEE……）；写在文档Doc中找出包含str所有字符的最短片段（不要求顺序）。上面这种情况的最短片段就是（ACFB）。
#include <iostream>
#include <string.h>
using namespace std;

void find_interval(char* doc,char* str,int* left,int* right)
{
    const int SIGMA=256;
    const int MAXINTERVAL=65535;
    int m=strlen(str);
    int n=strlen(doc);
    bool mark[SIGMA];                 //标记str中的字符
    bool mark_tmp[SIGMA];        //辅助标记哪些字str符已经进入了子序列
    int sigma_count[SIGMA];            //辅助数据结构，记录一个子序列中str字符可以删除的次数
    memset(mark,0,sizeof(bool)*SIGMA);
    memset(mark_tmp,0,sizeof(bool)*SIGMA);
    memset(sigma_count,0,sizeof(int)*SIGMA);
    int short_interval=MAXINTERVAL;

    for(int i=0;i<m;i++)
    {
        mark[str[i]]=true;
        mark_tmp[str[i]]=true;
    }

    int count=0;
    for(int begin=0,end=0;end<n;end++)
    {
        sigma_count[doc[end]]++;
        if(mark_tmp[doc[end]])
        {
            mark_tmp[doc[end]]=false;
            count++;
        }
        if(count==m)
        {
            while(1)
            {
                if(!mark[doc[begin]])                //非str字符，可以删除
                {
                    begin++;
                    continue;
                }
                if(sigma_count[doc[begin]]==1)                //str字符，在子序列中只剩下一次，不能再删除，已经达到一个最小的覆盖str的子序列
                {
                    break;
                }
                else
                {
                    sigma_count[doc[begin]]--;        //str字符，但子序列中出现了多次，可以删除
                    begin++;
                }
            }
            if((end-begin)<short_interval)            //更新记录
            {
                (*left)=begin;
                (*right)=end;
                short_interval=end-begin;
            }
            mark_tmp[doc[begin]]=true;
            sigma_count[doc[begin]]=0;                //删除一个覆盖str的最小子序列的最左边的字符
            count--;
            begin++;
        }
    }
}

int main()
{
    char str[]="ABC";
    char doc[]="DEACFBAEEE";
    int right=0,left=0;
    find_interval(doc,str,&left,&right);
    cout<<left<<" "<<right<<endl;
    return 0;
}

```

这次的教训主要是陷入了思维陷阱，写出的代码也是错的。后面面试中应当注意思维方式，不要钻牛角尖。紧张的问题有很好的改善。
