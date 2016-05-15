# -*- coding: utf-8 -*-
import requests
import hashlib
import base64
from flask import Flask, render_template, url_for, redirect, request
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
    song_info = song_info_get(song_id)
    song_name = song_info[0]
    artist = song_info[1]
    pic_url = song_info[2]
    song_url = song_info[3]
    lyrics = requests.get('http://music.163.com/api/song/lyric/?id=%s&lv=-1&csrf_token='%(song_id),headers={"Referer": "http://music.163.com/"}).json()["lrc"]["lyric"].replace(" ","").replace("\n","\\n")
    return render_template("song.html",song_name=song_name,artist=artist,pic_url=pic_url,song_url=song_url,lyrics=lyrics)

@app.route('/playlist/<int:playlist_id>')
def playlist_player(playlist_id):
    playlist_info = playlist_info_get(playlist_id)
    song_names = playlist_info[0]
    artists = playlist_info[1]
    pic_urls = playlist_info[2]
    song_urls = playlist_info[3]
    lens=len(song_names)
    playlist_name = playlist_info[4]
    return render_template("playlist.html",lens=lens,song_names=song_names,artists=artists,pic_urls=pic_urls,song_urls=song_urls,playlist_name=playlist_name)

@app.route('/album/<int:album_id>')
def album_player(album_id):
    album_info = album_info_get(album_id)
    song_names = album_info[0]
    artists = album_info[1]
    pic_urls = album_info[2]
    song_urls = album_info[3]
    lens=len(song_names)
    album_name = album_info[4]
    artist_name = album_info[5]
    return render_template("album.html",lens=lens,song_names=song_names,artists=artists,pic_urls=pic_urls,song_urls=song_urls,album_name=album_name,artist_name=artist_name)

def song_info_get(song_id):
    r = requests.get('http://music.163.com/api/song/detail/?id=%s&ids=[%s]&csrf_token='%(song_id,song_id),headers={"Referer": "http://music.163.com/"}).json()["songs"][0] 
    songNet = 'p'+r["mp3Url"].split('/')[2][1:]
    if 'hMusic' in r and r['hMusic'] != None:
        dfsId = r["hMusic"]["dfsId"]
    else:
        dfsId = r["bMusic"]["dfsId"]
    song_url = make_url(songNet,dfsId)
    song_name = r["name"]
    pic_url = r["album"]["blurPicUrl"]
    artist = r["artists"][0]["name"]
    return [song_name,artist,pic_url,song_url]

def playlist_info_get(playlist_id):
    l = requests.get("http://music.163.com/api/playlist/detail?id=%s&csrf_token=" % playlist_id, headers={"Referer": "http://music.163.com/"}).json()["result"]
    song_names=[]
    artists=[]
    pic_urls=[]
    song_urls=[]
    for r in l["tracks"]:
        songNet = 'p'+r["mp3Url"].split('/')[2][1:]
        if 'hMusic' in r and r['hMusic'] != None:
            dfsId = r["hMusic"]["dfsId"]
        else:
            dfsId = r["bMusic"]["dfsId"]
        song_urls.append(make_url(songNet,dfsId))
        song_names.append(r["name"])
        pic_urls.append(r["album"]["blurPicUrl"])
        artists.append(r["artists"][0]["name"])
    playlist_name = l["name"]
    return [song_names,artists,pic_urls,song_urls,playlist_name]

def album_info_get(album_id):
    l = requests.get("http://music.163.com/api/album/%s?id=%s&csrf_token=" % (album_id, album_id), headers={"Referer": "http://music.163.com/"}).json()["album"]
    song_names=[]
    artists=[]
    pic_urls=[]
    song_urls=[]
    for r in l["songs"]:
        songNet = 'p'+r["mp3Url"].split('/')[2][1:]
        if 'hMusic' in r and r['hMusic'] != None:
            dfsId = r["hMusic"]["dfsId"]
        else:
            dfsId = r["bMusic"]["dfsId"]
        song_urls.append(make_url(songNet,dfsId))
        song_names.append(r["name"])
        pic_urls.append(r["album"]["blurPicUrl"])
        artists.append(r["artists"][0]["name"])
    album_name = l["name"]
    artist_name = l["artist"]["name"]
    return [song_names,artists,pic_urls,song_urls,album_name,artist_name]

@app.errorhandler(404)
def page_not_found(e):
  return redirect("https://yux.io/2016/05/15/163music/#Error")

@app.errorhandler(500)
def internal_server_error(e):
  return redirect("https://yux.io/2016/05/15/163music/#Error")


if __name__ == '__main__':
    app.run()