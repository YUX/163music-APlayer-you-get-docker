# 163music-APlayer-you-get BETA5 init
## Yes! it's Beta5 now!......what's new?
> I just rewrote everything.

- This project now moved to Python-3.5.1. You may pull a docker image from [yuxio/flask-python351](https://hub.docker.com/r/yuxio/flask-python351/) to play with.
- Now the back-end search requests is asynchronous. Thanks to [requests-futures](https://github.com/ross/requests-futures). It's like at least 5 times faster than normal python-requests
- And there is the second version of API for getting music info.
- I tried to use [DPlayer](https://github.com/DIYgod/DPlayer) - a lovely HTML5 danmaku video player🍭, there is a [demo](http://diygod.github.io/DPlayer/demo), but it seems the MV from 163Music has a Referer test or something to block it. It's too bad.⌇●﹏●⌇ It might be fixed by a fake-referer from a JavaScript of Dplayer or I don't know. It's very cool when I tested it locally. I tried to add a proxy from my server back-end, it works but it takes too much bandwidth. DaoCloud would kill me for that.
- The music player is always [APlayer](http://aplayer.js.org/) by [DIYgod](https://www.anotherhome.net/).
- Add Radio.
- All the APIs of 163Music are from [you-get](https://you-get.org/). Use it if you want to download songs of videos.
- Tout est mieux ٩(ˊᗜˋ*)و

### The web interface
[https://music.daoapp.io/](https://music.daoapp.io/)
The front-end is folked from [No JS: Tabs that scale down to menu](http://codepen.io/jakealbaugh/pen/KBsIo) and [Search Box](http://codepen.io/siwicki/pen/FHkwu). I want somebody to teach me how to do those magic sometime

### iframe
Demos:
- [https://music.daoapp.io/iframe?song=287749&qssl=1&qlrc=1&qnarrow=0&max_width=50%&autoplay=1](https://music.daoapp.io/iframe?song=287749&qssl=1&qlrc=1&qnarrow=0&max_width=50%&autoplay=1)
- [https://music.daoapp.io/iframe?song=287749&qnarrow=1&qssl=1](https://music.daoapp.io/iframe?song=287749&qnarrow=1&qssl=1)

URL: http(s)://music.daoapp.io/  Donot use HTTPS if it's not necessary. But if you do, don't forget set qssl to 1.
Method: GET
The arguments are:
- album=album_id
- playlist=playlist_id
- song=song_id
- program=program_id
- radio=radio_id
- mv=mv_id
- qssl=[0|1] (default:0)
- qlrc=[0|1] (default:0)
- qnarrow=[0|1] (default:0)
- max_width=[100%|32rem|400px|something else] (default:100%)
- max_height=[300px|something else] (default:100%)
- autoplay=[0|1] (default:1)
- mode=[random|single|circulation|order] (default:circulation)

You must choose ONE of those six ids. And it means nothing if you choose more than one of them. You may use [The web interface](https://music.daoapp.io/) to find the id or use 163Music.

### API-V2
URL: https://music.daoapp.io/api/v2
Method: POST
The arguments are:
- s=[album_id|playlist_id|song_id|program_id|radio_id|mv_id]
- genre=[album|playlist|song|program|radio|mv]
- qlrc=[0|1] for song only

### Screenshot
![](http://ww1.sinaimg.cn/large/863bb56fgw1f4fwm41wcyj20oh09jglq.jpg)
![](http://ww3.sinaimg.cn/large/863bb56fgw1f4fwnc0pmjj20ig060t90.jpg)
![](http://ww3.sinaimg.cn/large/863bb56fgw1f4fwovrg9sj20m70cdtai.jpg)

## What's new on version beta 4

### Song API Release
- URL: https://music.daoapp.io/api/v1/song
- Méthode: GET
- Paramètre
  - id (song_id)
  - search_type
    - meta (song's infomation)
    - meta_lrc (song's infomation with lyrics)
    - audio **(The audio stream!!!!)**
    - image **(The album cover image stream!!!!)**
  - qssl=[0|1]


  ### Example
  https://music.daoapp.io/api/v1/song?id=27808044&type=meta
```JSON
{"song_url": "http://p2.music.126.net/oiyHl_q-7m4Z0dFqhLmg_Q==/3319425604329008.mp3", "song_name": "丑八怪", "code": 200, "pic_url": "http://p4.music.126.net/i2YqeMpR2DPuj15M-B1skA==/5816416510959096.jpg", "artist": "薛之谦"}
```
https://music.daoapp.io/api/v1/song?id=27808044&type=meta&qssl=1
```JSON
{"song_url": "https://gossl.daoapp.io/p2.music.126.net/oiyHl_q-7m4Z0dFqhLmg_Q==/3319425604329008.mp3", "song_name": "丑八怪", "code": 200, "pic_url": "https://gossl.daoapp.io/p4.music.126.net/i2YqeMpR2DPuj15M-B1skA==/5816416510959096.jpg", "artist": "薛之谦"}
```

https://music.daoapp.io/api/v1/song?id=27808044&type=meta_lrc
```JSON
{"song_url": "http://p2.music.126.net/oiyHl_q-7m4Z0dFqhLmg_Q==/3319425604329008.mp3", "code": 200, "lyrics": "[00:00.00] 作曲 : 李荣浩\\n[00:01.00] 作词 : 甘世佳\\n[00:19.660]如果世界漆黑 其实我很美\\n[00:23.280]在爱情里面进退 最多被消费\\n[00:27.100]无关痛痒的是非\\n[00:29.090]又怎么不对 无所谓\\n[00:35.090]如果像你一样 总有人赞美\\n[00:38.720]围绕着我的卑微 也许能消退\\n[00:42.720]其实我并不在意 有很多机会\\n[00:46.090]像巨人一样的无畏\\n[00:48.910]放纵我心里的鬼\\n[00:50.600]可是我不配\\n[00:53.860]丑八怪 能否别把灯打开\\n[01:01.610]我要的爱 出没在漆黑一片的舞台\\n[01:08.860]丑八怪 在这暧昧的时代\\n[01:16.980]我的存在 像意外\\n[01:23.880]\\n[01:37.190]有人用一滴泪 会红颜祸水\\n[01:40.750]有人丢掉称谓 什么也不会\\n[01:44.690]只要你足够虚伪\\n[01:46.500]就不怕魔鬼 对不对\\n[01:52.450]如果剧本写好 谁比谁高贵\\n[01:56.140]我只能沉默以对 美丽本无罪\\n[02:00.030]当欲望开始贪杯 有更多机会\\n[02:03.470]像尘埃一样的无畏\\n[02:06.290]化成灰谁认得谁管他配不配\\n[02:11.360]丑八怪 能否别把灯打开\\n[02:18.920]我要的爱 出没在漆黑一片的舞台\\n[02:26.230]丑八怪 在这暧昧的时代\\n[02:34.360]我的存在 不意外\\n[03:02.260]丑八怪 其实见多就不怪\\n[03:10.260]放肆去high 用力踩\\n[03:14.450]那不堪一击的洁白\\n[03:17.510]丑八怪 这是我们的时代\\n[03:25.780]我不存在 才意外\\n", "artist": "薛之谦", "song_name": "丑八怪", "pic_url": "http://p4.music.126.net/i2YqeMpR2DPuj15M-B1skA==/5816416510959096.jpg"}
```

2016-5-18 1:24 à Paris

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
