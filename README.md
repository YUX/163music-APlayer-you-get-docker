![](https://github.blog/wp-content/uploads/2020/07/87581945-94a94b80-c68e-11ea-8934-0870b0025e7e.jpg?w=1200)



# 1AYGD

*a [**2020 Arctic Vault program**](https://archiveprogram.github.com) project*



Many thanks for all of your support, this was a sideproject for my noob blog when I was a maths student at UPMC (Sorbonne Université Campus Pierre et Marie Curie),  I cannot even bear to look at it now. If you find it in 3020 at the North Pole, which I hope not, please take the limitations of the times into account. 

July 19, 2020

Yu XIAO

p.s.

This project is no longer maintained.🍺







***

***



## 163music-APlayer-you-get BETA5 init


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
- qssl=[0|1] default:0
- qlrc=[0|1] default:0
- qnarrow=[0|1] default:0
- max_width=[100%|32rem|400px|something else] default:100%
- max_height=[300px|something else] default:100%
- autoplay=[0|1] default:1
- mode=[random|single|circulation|order] default:circulation

You must choose ONE of those six ids. And it means nothing if you choose more than one of them. You may use [The web interface](https://music.daoapp.io/) to find the id or use 163Music.

### API-V2
URL: https://music.daoapp.io/api/v2
Method: POST
The arguments are:
- s=[album_id|playlist_id|song_id|program_id|radio_id|mv_id]
- genre=[album|playlist|song|program|radio|mv]
- qlrc=[0|1] for song only

### Screenshot
![](http://ww3.sinaimg.cn/large/863bb56fgw1f4fwnc0pmjj20ig060t90.jpg)
![](http://ww3.sinaimg.cn/large/863bb56fgw1f4fwovrg9sj20m70cdtai.jpg)