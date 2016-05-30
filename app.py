# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, abort, redirect, Response, url_for
import netease
import json
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/s",methods=['GET', 'POST'])
def s():
	if request.method == "POST":
		s = request.form["s"]
		s_info = cache.get(s)
		if s_info is None:
			search_info = netease.netease_search(s)
			songs_info = search_info[0]
			albums_info = search_info[1]
			playlists_info = search_info[2]
			mvs_info = search_info[3]
			radios_info = search_info[4]
			s_info = [songs_info,albums_info,playlists_info,mvs_info,radios_info]
			cache.set(s, s_info, timeout=720000)
		songs_info = s_info[0]
		albums_info = s_info[1]
		playlists_info = s_info[2]
		mvs_info = s_info[3]
		radios_info = s_info[4]
		return render_template("s.html",s=s,songs_info=songs_info,albums_info=albums_info,playlists_info=playlists_info,mvs_info=mvs_info,radios_info=radios_info)
	else:
		return redirect("/")

@app.route("/api/v2",methods=['GET','POST'])
def api_v2():
	if request.method == "POST":
		try:
			s = request.form["s"]
			if s is None:
				api_info = {"code":400, "info":"s is required, may be a name or id"}
				return Response(json.dumps(api_info, ensure_ascii=False),mimetype="application/json")
			else:
				pass
		except:
			api_info = {"code":400, "info":"s is required, may be a name or id"}
			return Response(json.dumps(api_info, ensure_ascii=False),mimetype="application/json")
		try:
			genre = request.form["genre"]
			if genre is None:
				api_info = {"code":400, "info":"genre is required, may be song, album, playlist, program, radio or mv"}
				return Response(json.dumps(api_info, ensure_ascii=False),mimetype="application/json")
			else:
				pass
		except:
			api_info = {"code":400, "info":"genre is required, may be song, album, playlist, program, radio or mv"}
			return Response(json.dumps(api_info, ensure_ascii=False),mimetype="application/json")
		try:
			qlrc = int(request.form["qlrc"])
		except:
			qlrc = 0
		api_info = cache.get((genre,s,qlrc))
		if api_info is None:
			api_info = netease.api_v2(genre, s, qlrc)
			cache.set((genre, s, qlrc), api_info, timeout=720000)
		else:
			pass
		return Response(json.dumps(api_info, ensure_ascii=False),mimetype="application/json")
	else:
		return "WRONG"

@app.route("/player",methods=['GET'])
def player():
	album_id = request.args.get("album")
	playlist_id = request.args.get("playlist")
	song_id = request.args.get("song")
	program_id = request.args.get("program")
	radio_id = request.args.get("radio")
	mv_id = request.args.get("mv")

	if album_id is not None:
		album_info = netease.netease_cloud_music("album",album_id,0)
		songs_info = album_info["songs_info"]
		title = "%s - %s" %(album_info["album"],album_info["artist"])
		showlrc = "0"
	elif playlist_id is not None:
		playlist_info = netease.netease_cloud_music("playlist",playlist_id,0)
		songs_info = playlist_info["songs_info"]
		title = playlist_info["playlist"]
		showlrc = "0"
	elif song_id is not None:
		song_info = netease.netease_cloud_music("song",song_id,1)
		title = "%s - %s" %(song_info["title"],song_info["artist"])
		songs_info = [song_info]
		showlrc = "1"
	elif program_id is not None:
		song_info = netease.netease_cloud_music("program",program_id,0)
		title = song_info["album"]
		songs_info = [song_info]
		showlrc = "0"
	elif radio_id is not None:
		songs_info = netease.netease_cloud_music("radio",radio_id,0)
		title = songs_info[0]["artist"]
		showlrc = "0"
	elif mv_id is not None:
		mv_info = netease.netease_cloud_music("mv",mv_id,0)
		mv_url = mv_info["url_best"]
		title = mv_info["title"]
		pic_url = mv_info["pic_url"]
		return render_template("dplayer.html",mv_url=mv_url,title=title,mv_id=mv_id,pic_url=pic_url)
	else:
		abort(404)

	return render_template("aplayer.html",songs_info=songs_info,title=title,showlrc=showlrc)
if __name__ == "__main__":
    app.run(port=5010)