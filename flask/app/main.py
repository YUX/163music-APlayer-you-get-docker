# -*- coding: utf-8 -*-
import requests
import hashlib
import base64
import re
from flask import Flask, render_template, url_for, redirect, request, abort
app = Flask(__name__)
app.debug = False

def netease_hymn():
    return """
    player's Game Over,
    u can abandon.
    u get pissed,
    get pissed,
    Hallelujah my King!
    errr oh! fuck ohhh!!!!
    """

def encrypted_id(dfsId):
    x = [ord(i[0]) for i in netease_hymn().split()]
    y = ''.join([chr(i - 61) if i > 96 else chr(i + 32) for i in x])
    byte1 = bytearray(y, encoding='ascii')
    byte2 = bytearray(str(dfsId), encoding='ascii')
    for i in range(len(byte2)):
        byte2[i] ^= byte1[i % len(byte1)]
    m = hashlib.md5()
    m.update(byte2)
    result = base64.b64encode(m.digest()).decode('ascii')
    result = result.replace('/', '_')
    result = result.replace('+', '-')
    return result

def make_url(songNet, dfsId):
    encId = encrypted_id(dfsId)
    mp3_url = "http://%s/%s/%s.mp3" % (songNet, encId, dfsId)
    return mp3_url

def song_info_get(song_id,qssl,qlrc):
    r = requests.get('http://music.163.com/api/song/detail/?id=%s&ids=[%s]&csrf_token='%(song_id,song_id),headers={"Referer": "http://music.163.com/"}).json()["songs"]
    if r == []:
        code = 404
        return [code]
    elif not r[0]["mp3Url"]:
        code = 403
        return [code]
    else:
        code = 200
        r = r[0]
        songNet = 'p'+r["mp3Url"].split('/')[2][1:]
        if 'hMusic' in r and r['hMusic'] != None:
            dfsId = r["hMusic"]["dfsId"]
        else:
            dfsId = r["bMusic"]["dfsId"]
        song_url = make_url(songNet,dfsId)
        song_name = r["name"]
        pic_url = r["album"]["blurPicUrl"]
        artist = r["artists"][0]["name"]
        if qssl:
            song_url = song_url.replace("http://","https://gossl.daoapp.io/")
            pic_url = pic_url.replace("http://","https://gossl.daoapp.io/")
        else:
            pass
        if qlrc:
            lyrics = requests.get('http://music.163.com/api/song/lyric/?id=%s&lv=-1&csrf_token='%(song_id),headers={"Referer": "http://music.163.com/"}).json()["lrc"]["lyric"].replace("\n","\\n")
        else:
            lyrics = 0
        return [code,song_name,artist,song_url,pic_url,lyrics]

def playlist_info_get(playlist_id,qssl):
    l = requests.get("http://music.163.com/api/playlist/detail?id=%s&csrf_token=" % playlist_id, headers={"Referer": "http://music.163.com/"}).json()
    if l["code"] != 200:
        code = l["code"]
        return [code]
    else:
        l = l["result"]
    codes = []
    playlist_name = l["name"]
    song_names = []
    artists = []
    song_urls = []
    pic_urls = []
    lyricss = []
    for r in l["tracks"]:
        try:
            code = 200
            songNet = 'p'+r["mp3Url"].split('/')[2][1:]
            if 'hMusic' in r and r['hMusic'] != None:
                dfsId = r["hMusic"]["dfsId"]
            else:
                dfsId = r["bMusic"]["dfsId"]
            song_url = make_url(songNet,dfsId)
            song_name = r["name"]
            song_id = r["id"]
            pic_url = r["album"]["blurPicUrl"]
            artist = r["artists"][0]["name"]
            if qssl:
                song_url = song_url.replace("http://","https://gossl.daoapp.io/")
                pic_url = pic_url.replace("http://","https://gossl.daoapp.io/")
            else:
                pass
            song_names.append(song_name)
            artists.append(artist)
            song_urls.append(song_url)
            pic_urls.append(pic_url)
        except:
            pass
    return [code,codes,playlist_name,song_names,artists,song_urls,pic_urls]

def album_info_get(album_id,qssl):
    l = requests.get("http://music.163.com/api/album/%s?id=%s&csrf_token=" % (album_id, album_id), headers={"Referer": "http://music.163.com/"}).json()
    if l["code"] != 200:
        code = l["code"]
        return [code]
    else:
        l = l["album"]
        codes = []
        album_name = l["name"]
        song_names=[]
        artists=[]
        song_urls=[]
        pic_urls=[]
        for r in l["songs"]:
            try:
                code = 200
                songNet = 'p'+r["mp3Url"].split('/')[2][1:]
                if 'hMusic' in r and r['hMusic'] != None:
                    dfsId = r["hMusic"]["dfsId"]
                else:
                    dfsId = r["bMusic"]["dfsId"]
                song_url = make_url(songNet,dfsId)
                song_name = r["name"]
                song_id = r["id"]
                pic_url = r["album"]["blurPicUrl"]
                artist = r["artists"][0]["name"]
                if qssl:
                    song_url = song_url.replace("http://","https://gossl.daoapp.io/")
                    pic_url = pic_url.replace("http://","https://gossl.daoapp.io/")
                else:
                    pass
                song_names.append(song_name)
                artists.append(artist)
                song_urls.append(song_url)
                pic_urls.append(pic_url)
            except:
                pass
        return [code,codes,album_name,song_names,artists,song_urls,pic_urls]

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/s', methods=['GET', 'POST'])
def s():
    if request.method == 'POST':
        s = request.form['s']
        s_type = request.form['type']

        sids = []
        stitles = []
        sstitles = []

        songs_lens = 0
        albums_lens = 0
        playlists_lens = 0

        l = requests.post("http://music.163.com/api/search/get/",{'s':s,'limit':100,'sub':'false','type':s_type,'offset':0}, headers={"Referer": "http://music.163.com/"}).json()["result"]

        if s_type == str(1):
            l = l["songs"]
            for r in l:
                if r["status"]<0:
                    pass
                else:
                    try:
                        sids.append(r["id"])
                        stitles.append(r["name"])
                        sstitles.append(r["album"]["name"]+" - "+r["artists"][0]["name"])
                    except:
                        pass
            songs_lens = len(sids)


        elif s_type == str(10):
            l = l["albums"]
            for r in l:
                if r["status"]<0:
                    pass
                else:
                    try:
                        sids.append(r["id"])
                        stitles.append(r["name"])
                        sstitles.append(r["artists"][0]["name"])
                    except:
                        pass
            albums_lens = len(sids)
        elif s_type == str(100):
            aid = l["artists"][0]["id"]
            l = requests.get("http://music.163.com/api/artist/albums/%s?offset=0&limit=50"%aid, headers={"Referer": "http://music.163.com/"}).json()["hotAlbums"]
            for r in l:
                if r["status"]<0:
                    pass
                else:
                    try:
                        sids.append(r["id"])
                        stitles.append(r["name"])
                        sstitles.append(r["artists"][0]["name"])
                    except:
                        pass
            albums_lens = len(sids)
        else:
            l = l["playlists"]
            for r in l:
                try:
                    sids.append(r["id"])
                    stitles.append(r["name"]+"("+str(r["trackCount"])+")")
                    sstitles.append("by"+r["creator"]["nickname"])
                except:
                    pass
            playlists_lens = len(sids)

        return render_template('s.html',sids=sids,stitles=stitles,sstitles=sstitles,songs_lens=songs_lens,albums_lens=albums_lens,playlists_lens=playlists_lens,s=s)

    if request.method == 'GET':
        return redirect("/")

@app.route('/song/<int:song_id>')
def song_player(song_id):
    song_info = song_info_get(song_id,0,1)
    code = song_info[0]
    if code != 200:
        abort(code)
    else:
        song_name = song_info[1]
        artist = song_info[2]
        song_url = song_info[3]
        pic_url = song_info[4]
        lyrics = song_info[5]
        return render_template("song.html",song_name=song_name,artist=artist,song_url=song_url,pic_url=pic_url,lyrics=lyrics)

@app.route('/iframe/song', methods=['GET'])
def iframe_song_player():
    song_id = request.args.get('id', '')
    qssl = request.args.get('qssl', '')
    max_width = request.args.get('max_width', '')
    qlrc = request.args.get('qlrc', '')
    autoplay = request.args.get('autoplay', '')
    narrow = request.args.get('narrow', '')
    if qssl == 'O' or qssl == '1':
        qssl = int(qssl)
    else:
        qssl = 0
    if qlrc == '0' or qlrc == '1':
        qlrc = int(qlrc)
    else:
        qlrc = 0
    if autoplay == '0' or autoplay == '1':
        autoplay = int(autoplay)
    else:
        autoplay = 0
    if narrow == '0' or narrow == '1':
        narrow = int(narrow)
    else:
        narrow = 0
    song_info = song_info_get(song_id,qssl,qlrc)
    code = song_info[0]
    if code != 200:
        abort(code)
    else:
        song_name = song_info[1]
        artist = song_info[2]
        song_url = song_info[3]
        pic_url = song_info[4]
        lyrics = song_info[5]
        return render_template("iframe_song.html",song_name=song_name,artist=artist,song_url=song_url,pic_url=pic_url,lyrics=lyrics,max_width=max_width,autoplay=autoplay,narrow=narrow)

@app.route('/playlist/<int:playlist_id>')
def playlist_player(playlist_id):
    playlist_info = playlist_info_get(playlist_id,0)
    code = playlist_info[0]
    if code != 200:
        abort(code)
    else:
        codes = playlist_info[1]
        playlist_name = playlist_info[2]
        song_names = playlist_info[3]
        artists = playlist_info[4]
        song_urls = playlist_info[5]
        pic_urls = playlist_info[6]
        lens=len(song_names)
        return render_template("playlist.html",lens=lens,codes=codes,playlist_name=playlist_name,song_names=song_names,artists=artists,song_urls=song_urls,pic_urls=pic_urls)

@app.route('/iframe/playlist', methods=['GET'])
def iframe_playlist_player():
    playlist_id = request.args.get('id', '')
    qssl = request.args.get('qssl', '')
    max_width = request.args.get('max_width', '')
    autoplay = request.args.get('autoplay', '')
    narrow = request.args.get('narrow', '')
    if qssl == 'O' or qssl == '1':
        qssl = int(qssl)
    else:
        qssl = 0
    if autoplay == '0' or autoplay == '1':
        autoplay = int(autoplay)
    else:
        autoplay = 0
    if narrow == '0' or narrow == '1':
        narrow = int(narrow)
    else:
        narrow = 0
    playlist_info = playlist_info_get(playlist_id,qssl)
    code = playlist_info[0]
    if code != 200:
        abort(code)
    else:
        codes = playlist_info[1]
        playlist_name = playlist_info[2]
        song_names = playlist_info[3]
        artists = playlist_info[4]
        song_urls = playlist_info[5]
        pic_urls = playlist_info[6]
        lens=len(song_names)
        return render_template("iframe_playlist.html",lens=lens,codes=codes,playlist_name=playlist_name,song_names=song_names,artists=artists,song_urls=song_urls,pic_urls=pic_urls,max_width=max_width,autoplay=autoplay,narrow=narrow)


@app.route('/album/<int:album_id>')
def album_player(album_id):
    album_info = album_info_get(album_id,0)
    code = album_info[0]
    if code != 200:
        abort(code)
    else:
        codes = album_info[1]
        album_name = album_info[2]
        song_names = album_info[3]
        artists = album_info[4]
        song_urls = album_info[5]
        pic_urls = album_info[6]
        lens=len(song_names)
        return render_template("album.html",lens=lens,codes=codes,album_name=album_name,song_names=song_names,artists=artists,song_urls=song_urls,pic_urls=pic_urls)

@app.route('/iframe/album', methods=['GET'])
def iframe_album_player():
    album_id = request.args.get('id', '')
    qssl = request.args.get('qssl', '')
    max_width = request.args.get('max_width', '')
    autoplay = request.args.get('autoplay', '')
    narrow = request.args.get('narrow', '')
    if qssl == 'O' or qssl == '1':
        qssl = int(qssl)
    else:
        qssl = 0
    if autoplay == '0' or autoplay == '1':
        autoplay = int(autoplay)
    else:
        autoplay = 0
    if narrow == '0' or narrow == '1':
        narrow = int(narrow)
    else:
        narrow = 0
    album_info = album_info_get(album_id,qssl)
    code = album_info[0]
    if code != 200:
        abort(code)
    else:
        codes = album_info[1]
        album_name = album_info[2]
        song_names = album_info[3]
        artists = album_info[4]
        song_urls = album_info[5]
        pic_urls = album_info[6]
        lens=len(song_names)
        return render_template("iframe_album.html",lens=lens,codes=codes,album_name=album_name,song_names=song_names,artists=artists,song_urls=song_urls,pic_urls=pic_urls,max_width=max_width,autoplay=autoplay,narrow=narrow)

if __name__ == '__main__':
    app.run()
