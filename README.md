## Simple-Single-Factors-Test-of-Stock
Aim to basiclly test some factors of stock in Chinese stock market, whether they could be good indicators to choose stock.


### The factors in the financial statement — Market value
data source:  https://pan.baidu.com/s/12JgeC6wT6Nj6Pgq7Feg25A

Actually, after the statements are announced, we can use the data to divide the stock into 5 groups in the ascending order. Then use diffrent account to purchase them and calculate the earning respectively. (In fact, I consider the suspended stock, but no fee of trading.)

For some factors, we can get them from the financial statements directly. Take the market-value as an example. (We could get the daily market-value, but here we assume we get factor from seasonal statements.)  

Market-value factor test result is shown below. The 0-20 means the stock group with top 20% market-value, and the 80-100 means the smell companies. Obviously, the small company's return is much higher than the big one, just as the Fama three-factor-model shows. Also, after 2016, comparing to small company, the big company starts to have better performance, which is something we need to pay attention to.
![](https://ws3.sinaimg.cn/large/006tNc79gy1ftld75nbm0j311e0cqgmb.jpg)

ps: In the code, I calculate the daily earning, so it takes a long time to run. Actually, we can just calculate the earning when we shift the position.

------

### The factors need to be design — Price Variance
data source:https://pan.baidu.com/s/1Q5MTeoSodYWjvn5fX_ltGw

As we know, some derivative factors can not be downloaded directly, we need to calculate them by other data. Here, for instance, the variance of price's changes.

We compute the variance of a certain stock monthly (to make it easier to run, we use the hs300 index's component), and then devide them into 5 groups according to the variance.

Change the position monthly. The result is here. The company, whose price varies dramatically, may have a better return in the long run probably. However, the companies with most stable price are not the worst.
![](https://ws3.sinaimg.cn/large/006tNc79gy1ftmd7xio38j31140csq3h.jpg)


----
### Some other tests for whole market
#### Financial Leverag
![](https://ws2.sinaimg.cn/large/006tNc79gy1ftmde4aa7uj310y0demxs.jpg)

#### ROE
![](https://ws4.sinaimg.cn/large/006tNc79gy1ftmdf1n9v6j310y0cswf0.jpg)

#### Revenue
Actually, this factor is similar to market-vaule. For the big company usually has more income.
![](https://ws2.sinaimg.cn/large/006tNc79gy1ftmdgid159j31160d2t9g.jpg)

#### Net Profit
![](https://ws1.sinaimg.cn/large/006tNc79gy1ftmdfqv0pfj310k0cq74z.jpg)

