## Simple-Single-Factors-Test-of-Stock
Aim to basiclly test some factors of stock in Chinese stock market, whether they could be good indicators to choose stock.


### The factors in the financial statement — Market value
data source:  https://pan.baidu.com/s/12JgeC6wT6Nj6Pgq7Feg25A


Actually, after the statements are announced, we can use the data to divide the stock into 5 groups in the ascending order. Then use diffrent account to purchase them and calculate the earning respectively. (In fact, I consider the suspended stock, but no fee of trading.)

For some factors, we can get them from the financial statements directly. Take the market-value as an example. (We could get the daily market-value, but here we assume we get factor from seasonal statements.)  

Market-value factor test result is shown below. The 0-20 means the stock group with top 20% market-value, and the 80-100 means the smell companies. Obviously, the small company's return is much higher than the big one, just as the Fama three-factor-model shows. Also, after 2016, comparing to small company, the big company starts to have better performance, which is something we need to pay attention to.
![](https://tva1.sinaimg.cn/large/00831rSTgy1gdg0wwhj5kj30n207y3yt.jpg)

ps: In the code, I calculate the daily earning, so it takes a long time to run. Actually, we can just calculate the earning when we shift the position.

------

### The factors need to be design — Price Variance
data source:https://pan.baidu.com/s/1Q5MTeoSodYWjvn5fX_ltGw

As we know, some derivative factors can not be downloaded directly, we need to calculate them by other data. Here, for instance, the variance of price's changes.

We compute the variance of a certain stock monthly (to make it easier to run, we use the hs300 index's component), and then devide them into 5 groups according to the variance.

Change the position monthly. The result is here. The company, whose price varies dramatically, may have a better return in the long run probably. However, the companies with most stable price are not the worst.
![](https://tva1.sinaimg.cn/large/00831rSTgy1gdg0xgrxqpj30n207imxg.jpg)


----
### Some other tests for whole market
#### Financial Leverag
![](https://tva1.sinaimg.cn/large/00831rSTgy1gdg0wk8lmij30n207sdg3.jpg)

#### ROE
![](https://tva1.sinaimg.cn/large/00831rSTgy1gdg0wc40ppj30n207s3yq.jpg)

#### Revenue
Actually, this factor is similar to market-vaule. For the big company usually has more income.
![](https://tva1.sinaimg.cn/large/00831rSTgy1gdg0vp9lsbj30n207q0t2.jpg)

#### Net Profit
![](https://tva1.sinaimg.cn/large/00831rSTgy1gdg0w04bfgj30n207qdg5.jpg)

