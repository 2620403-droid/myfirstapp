import streamlit as st
import random
import urllib.parse


st.set_page_config(
    page_title="MBTI POP PICK",
    page_icon="☀️"
)


st.markdown("""
<style>
body {
    background-color: #fff5fb;
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#ff4f91;
}

.card {
    background:white;
    padding:30px;
    border-radius:25px;
    box-shadow:0 8px 25px rgba(0,0,0,0.12);
}

.badge {
    background:#ffd6ea;
    color:#ff3d8d;
    padding:8px 15px;
    border-radius:20px;
    font-weight:bold;
}

.song {
    color:#8b5cf6;
    font-size:26px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)



mbti_data = {

"ENFP":{
"emoji":"🌈",
"type":"햇살 에너지",
"desc":"새로운 경험과 재미를 좋아하는 자유로운 영혼",
"songs":[
"Sabrina Carpenter - Espresso",
"Surfaces - Sunday Best",
"Rex Orange County - Sunflower",
"beabadoobee - Glue Song",
"BENEE - Supalonely"
]
},

"ESFP":{
"emoji":"✨",
"type":"여름 파티 스타",
"desc":"사람들과 함께 즐거운 순간을 만드는 타입",
"songs":[
"Sabrina Carpenter - Espresso",
"Dua Lipa - Dance The Night",
"Doja Cat - Say So",
"Carly Rae Jepsen - Run Away With Me",
"PinkPantheress - Boy's a liar"
]
},

"INFP":{
"emoji":"🌙",
"type":"감성 드림러",
"desc":"음악과 감정을 깊게 느끼는 몽환적인 타입",
"songs":[
"Taylor Swift - cardigan",
"Laufey - From The Start",
"Lana Del Rey - Say Yes To Heaven",
"Clairo - Sofia",
"Men I Trust - Show Me How"
]
},

"ISFP":{
"emoji":"🎨",
"type":"감성 아티스트",
"desc":"자신만의 취향과 분위기를 가진 타입",
"songs":[
"Harry Styles - Adore You",
"Wave to Earth - Seasons",
"Still Woozy - Goodie Bag",
"Steve Lacy - Bad Habit",
"Vacations - Young"
]
},

"ENTP":{
"emoji":"🔥",
"type":"아이디어 천재",
"desc":"새로운 것을 시도하는 개성 넘치는 타입",
"songs":[
"Glass Animals - Heat Waves",
"COIN - Talk Too Much",
"Dominic Fike - 3 Nights",
"Troye Sivan - Rush",
"Charli XCX - Boom Clap"
]
},

"ESTP":{
"emoji":"🏄",
"type":"모험가",
"desc":"활동적이고 순간을 즐기는 타입",
"songs":[
"Harry Styles - Watermelon Sugar",
"Avicii - Wake Me Up",
"OneRepublic - I Ain't Worried",
"Kygo - Firestone",
"Calvin Harris - Summer"
]
},

"ENTJ":{
"emoji":"👑",
"type":"카리스마 리더",
"desc":"자신감과 목표 의식이 강한 타입",
"songs":[
"Rihanna - Diamonds",
"Dua Lipa - Houdini",
"Beyoncé - CUFF IT",
"Tate McRae - greedy",
"The Weeknd - Starboy"
]
},

"INTJ":{
"emoji":"🖤",
"type":"전략가",
"desc":"차분하고 자신만의 세계가 있는 타입",
"songs":[
"The Weeknd - Blinding Lights",
"Billie Eilish - Therefore I Am",
"Arctic Monkeys - Do I Wanna Know?",
"The Neighbourhood - Sweater Weather",
"Joji - Slow Dancing in the Dark"
]
},

"ISFJ":{
"emoji":"🌷",
"type":"따뜻한 힐링러",
"desc":"주변을 편안하게 만드는 다정한 타입",
"songs":[
"Ed Sheeran - Perfect",
"Bruno Mars - Just The Way You Are",
"HONNE - Day 1",
"Laufey - Valentine",
"John Legend - All of Me"
]
},

"ISTJ":{
"emoji":"📚",
"type":"성실한 완벽주의자",
"desc":"꾸준하고 믿음직한 타입",
"songs":[
"Adele - Easy On Me",
"Taylor Swift - Anti-Hero",
"Coldplay - Yellow",
"Sam Smith - Stay With Me",
"Vance Joy - Riptide"
]
},

"ESTJ":{
"emoji":"⚡",
"type":"추진력 리더",
"desc":"책임감과 실행력이 강한 타입",
"songs":[
"Imagine Dragons - Believer",
"Queen - Don't Stop Me Now",
"David Guetta - Titanium",
"Avicii - The Nights",
"Coldplay - Adventure of a Lifetime"
]
},

"ISTP":{
"emoji":"🕶️",
"type":"쿨한 자유인",
"desc":"자기 방식대로 살아가는 타입",
"songs":[
"Steve Lacy - Bad Habit",
"Dayglow - Can I Call You Tonight?",
"Joji - Sanctuary",
"Wallows - Are You Bored Yet?",
"Tame Impala - The Less I Know The Better"
]
},

"ESFJ":{
"emoji":"💗",
"type":"사랑스러운 분위기 메이커",
"desc":"사람을 행복하게 만드는 타입",
"songs":[
"Maroon 5 - Sugar",
"Ariana Grande - Into You",
"Bruno Mars - Treasure",
"Jason Mraz - I'm Yours",
"Katy Perry - Teenage Dream"
]
},

"INFJ":{
"emoji":"🌌",
"type":"신비로운 몽상가",
"desc":"깊은 생각과 감성을 가진 타입",
"songs":[
"Billie Eilish - ocean eyes",
"Cigarettes After Sex - Apocalypse",
"The 1975 - About You",
"Lana Del Rey - Young and Beautiful",
"Daughter - Youth"
]
},

"ENFJ":{
"emoji":"☀️",
"type":"따뜻한 리더",
"desc":"사람들에게 좋은 영향을 주는 타입",
"songs":[
"Coldplay - Viva La Vida",
"Harry Styles - Adore You",
"Taylor Swift - Love Story",
"Walk The Moon - Shut Up and Dance",
"OneRepublic - Good Life"
]
}

}



st.markdown(
"<div class='title'>☀️ MBTI POP PICK</div>",
unsafe_allow_html=True
)

st.write("💿 나의 성격에 어울리는 여름 팝송 찾기")


user_mbti = st.text_input(
"MBTI 입력 (예: ENFP)"
).upper()



if st.button("✨ 플레이리스트 만들기"):

    if user_mbti in mbti_data:

        data = mbti_data[user_mbti]

        song = random.choice(data["songs"])

        youtube = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(song)
        )


        st.markdown(f"""
        <div class="card">

        <h1>{data['emoji']} {user_mbti}</h1>

        <span class="badge">
        {data['type']}
        </span>

        <br><br>

        <p>{data['desc']}</p>

        <hr>

        🎧 오늘의 추천곡

        <div class="song">
        {song}
        </div>

        </div>
        """,
        unsafe_allow_html=True)


        st.link_button(
            "▶️ YouTube에서 듣기",
            youtube
        )


    else:
        st.error("MBTI 4글자를 정확히 입력해주세요!")



st.caption("☀️ MBTI × Summer Pop Playlist")
