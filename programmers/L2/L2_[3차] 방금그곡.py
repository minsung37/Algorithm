# [3차] 방금그곡
# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    music_convert = {"C#": "H", "D#": "I", "F#": "J", "G#": "K", "A#": "L"}
    for convert in music_convert:
        if convert in m:
            m = m.replace(convert, music_convert[convert])

    def time_calculate(start, end):
        start_min, start_second = start.split(":")
        end_min, end_second = end.split(":")
        return (int(end_min) * 60 + int(end_second)) - (int(start_min) * 60 + int(start_second))

    dic_music = {}
    music_order = []
    for musicinfo in musicinfos:
        start_time, end_time, name, sound = musicinfo.split(",")
        for convert in music_convert:
            if convert in sound:
                sound = sound.replace(convert, music_convert[convert])
        length = time_calculate(start_time, end_time)
        music = sound * (length // len(sound) + 1)
        dic_music[name] = music[:length]
        music_order.append(name)

    count = []
    for music in dic_music:
        if m in dic_music[music]:
            count.append([music, len(dic_music[music]), music_order.index(music)])
    if count:
        count = sorted(count, key=lambda x: (-x[1], x[2]))
        return count[0][0]
    return "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))