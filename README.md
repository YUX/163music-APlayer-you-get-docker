# 163music-APlayer-you-get

## What's new on version beta 3
### iframe 食用方法
## 单曲播放 https://music.daoapp.io/iframe/song

### 参数：
- id ，顾名思义就是 163 歌曲 ID ，必填
- qssl ，是否使用 HTTPS 协议，非必填，使用为 1 ，不用为 0 ，不填也是 0
- max_width ，非必填，最大宽度，可填写例如 123px, 40%, 32rem 等。不填为 100%
- qlrc ， 1 显示歌词， 0 不显示歌词，非必填，默认不显示
- autoplay ， 1 自动播放， 0 不自动播放 ，默认不自动播放
- narrow ，是否为窄模式(仅显示封面）， 1 显示窄模式， 0 不是窄模式，默认 0

### example :
https://music.daoapp.io/iframe/song?id=27808044&qssl=1&qlrc=1&narrow=0
## 歌单播放 https://music.daoapp.io/iframe/playlist

### 参数：
- id ，顾名思义就是 163 歌单 ID ，必填
- qssl ，是否使用 HTTPS 协议，非必填，使用为 1 ，不用为 0 ，不填也是 0
- max_width ，非必填，最大宽度，可填写例如 123px, 40%, 32rem 等。不填为 100%
- autoplay ， 1 自动播放， 0 不自动播放 ，默认不自动播放

### example :
https://music.daoapp.io/iframe/playlist?id=37288058&qssl=1&autoplay=1&max_width=500px&narrow=0

## 专辑播放 https://music.daoapp.io/iframe/album
### 参数：
- id ，顾名思义就是 163 专辑 ID ，必填
- qssl ，是否使用 HTTPS 协议，非必填，使用为 1 ，不用为 0 ，不填也是 0
- max_width ，非必填，最大宽度，可填写例如 123px, 40%, 32rem 等。不填为 100%
- autoplay ， 1 自动播放， 0 不自动播放 ，默认不自动播放

### example :
https://music.daoapp.io/iframe/album?id=16953&qssl=1&autoplay=1&max_width=500px&narrow=0

## Screenshot
![]( http://ww1.sinaimg.cn/large/863bb56fgw1f3yr5kq63ej207x07i74n.jpg)

## Live demo
[https://yux.io/]( https://yux.io/)


方便大家把音乐放到自己的网页上 SSL 模式求不要滥用带宽有限
其他更新
- 修正了外文歌词没有空格的 bug
- 在搜索结果里剔除了无法播放的歌曲


项目GitHub地址[https://github.com/YUX-IO/163music-APlayer-you-get-docker]( https://github.com/YUX-IO/163music-APlayer-you-get-docker) 求个Star+Fork，有Dockerfile方便部署在自己的主机上
如果部署在自己主机请一并将SSL代理一并部署，Github[https://github.com/YUX-IO/gossl]( https://github.com/YUX-IO/gossl)

播放器是 DIYgod 的 [Aplayer]( http://aplayer.js.org/)

****

## What's new on version beta 2
- 重构代码结构，以便下一版重新打包API
- ~~自动识别HTTPS|HTTP 协议~~  （╯‵□′）╯︵┴─┴ 然而并没有
- 自带HTTPS代理(Beta)
- 修正了外文歌词没有空格的bug
- 在搜索结果里剔除了无法播放的歌曲
- 限定了只在单独歌曲播放时才显示歌词

Todo list:
- 重新整合163musicAPI
- 优化iframe框架
- 有可能开发移动客户端
- 锻炼身体

【2016-5-17 2:38 à Paris】
****
## version beta 1, init

首先这个网页版163音乐播放器是基于无数别人的劳动果实而实现的：
- [APlayer](http://aplayer.js.org/) by [DIYgod](https://www.anotherhome.net/) 这是此网页播放器的作者
- [you-get](https://you-get.org/) by [Mort Yao](https://www.soimort.org/) 分析了此项目的关于获取163音频链接的部分
- [NeteaseCloudMusic](https://github.com/yanunon/NeteaseCloudMusic/wiki/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90API%E5%88%86%E6%9E%90) by [Yang Junyong](http://blog.yanunon.com/) 参考了这篇关于163音乐API分析
- [DailyUI #022 - Search](http://codepen.io/supah/pen/XdKMJK) by [supah](http://www.supah.it/) 照搬了这个搜索UI
- [Monocle List](http://codepen.io/hakimel/pen/zdKGE) by [Hakim](http://hakim.se/) 照搬了这个搜索结果UI
- [tiangolo/uwsgi-nginx:latest](https://github.com/tiangolo/uwsgi-nginx-docker) by [tiangolo](http://artificialintelligence.ninja/) 此Docker基于此
- [DaoCloud](http://www.daocloud.io/) 托管了此网站
- [flask](http://flask.pocoo.org/), [requests](http://docs.python-requests.org/en/master/), [docker](https://www.docker.com/), [python](https://www.python.org/)
- [163music](http://music.163.com/)，以及各位音乐创作者
- [v2ex](https://v2ex.com)

# Demo
[http://music.daoapp.io/](http://music.daoapp.io/)

# Screenshot
![](https://ws4.sinaimg.cn/large/863bb56fgw1f3w7nsvwy3j20qc09kq30.jpg)
![](https://ws2.sinaimg.cn/large/863bb56fgw1f3w7ozgpduj20yc0e9dgq.jpg)
![](https://ws2.sinaimg.cn/large/863bb56fgw1f3w7blk4tqj20wl0dz0tx.jpg)
![](https://ws1.sinaimg.cn/large/863bb56fgw1f3w7mu1l7cj20jn055aae.jpg)

****
这么一看，其实我也并没有做什么，我也造不出这么棒的轮子，好在这个网页还能用，也希望各位不要滥用此站点，对于技术上探讨我非常欢迎，此项目的仓库地址在此：[https://github.com/YUX-IO/163music-APlayer-you-get-docker](https://github.com/YUX-IO/163music-APlayer-you-get-docker)。这是一个Dockerfile，方便各位在自己的主机上自行部署，代码逻辑部分在此：[https://github.com/YUX-IO/163music-APlayer-you-get-docker/tree/master/flask/app](https://github.com/YUX-IO/163music-APlayer-you-get-docker/tree/master/flask/app)，这是一个由flask驱动的网站。欢迎各位Star并Fork此项目并自行部署。还有很多未完成的部分，心理比较急所以现在能用就放出来了，会持续更新。
如果希望下载更多歌曲或视频，请参考[you-get](https://you-get.org/) ，给大神跪了￣﹃￣
![YUX-IO/163music-APlayer-you-get-docker](https://ws3.sinaimg.cn/large/863bb56fgw1f3w5ajmyaij205z03b3yh.jpg)
