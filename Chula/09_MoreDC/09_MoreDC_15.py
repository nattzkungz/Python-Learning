music = {}
num_of_song = int(input())

for i in range(num_of_song):
    song = input().split(",")
    convert = song[3].split(":")
    song_length_sec = int(convert[0]) * 60 + int(convert[1])
    if song[2] not in music:
        music[song[2]] = song_length_sec
    else:
        music[song[2]] += song_length_sec

music_l = []
for i in music:
    music_l.append([music[i], i])

sort_music_list = sorted(music_l, reverse=True)

for g in sort_music_list:
    count = 0
    duration = g[0]
    if duration > 60:
        duration /= 60
        count += 1
    long = str(duration).split(".")
    sec = str(round(float("0." + long[1])*0.6, 2))[2:]
    g[0] = long[0] + ":" + sec
    if len(sec) < 2:
        g[0] += "0"

song_count = len(sort_music_list)
if song_count <= 3:
    for i in range(song_count):
        print(sort_music_list[i][1] + " --> " + sort_music_list[i][0])
else:
    for i in range(3):
        print(sort_music_list[i][1] + " --> " + sort_music_list[i][0])
