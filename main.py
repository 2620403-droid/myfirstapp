import streamlit as st
import random
import urllib.parse

st.set_page_config(
    page_title="MBTI POP CARD",
    page_icon="🎧"
)

st.markdown("""
<style>
body {
    background:#fff0f8;
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:900;
    color:#ff4f9a;
}

.card {
    background:white;
    padding:30px;
    border-radius:30px;
    box-shadow:0 10px 30px rgba(0,0,0,0.12);
    margin-top:20px;
}

.badge {
    background:#ffdded;
    color:#e91e63;
    padding:8px 18px;
    border-radius:20px;
    font-weight:bold;
}

.song {
    font-size:25px;
    font-weight:bold;
    color:#6c63ff;
}

.small {
    color:#777;
}
</style>
""", unsafe_allow_html=True)



mbti_data = {

"INFP":{
"emoji":"🌙",
"name":"감성적인 드림러",
"desc":"상상력이 풍부하고 음악으로 감정을 표현하는 타입",
"songs":[
"Taylor Swift - cardigan",
"Billie Eilish - ocean eyes",
"Adele - Easy On Me",
"Laufey - From The Start",
"Conan Gray - Heather"
]
},


"ENFP":{
"emoji":"🌈",
"name":"긍정 에너지 폭발러",
"desc":"새로운 경험과 설렘을 좋아하는 자유로운 영혼",
"songs":[
"Dua Lipa - Levitating",
"Katy Perry - Firework",
"Coldplay - A Sky Full of Stars",
"Harry Styles - As It Was",
"OneRepublic - I Ain't Worried"
]
},


"INTJ":{
"emoji":"🖤",
"name":"전략적인 마스터마인드",
"desc":"목표가 뚜렷하고 깊게 생각하는 분석가",
"songs":[
"The Weeknd - Blinding Lights",
"Imagine Dragons - Believer",
"Sia - Unstoppable",
"Billie Eilish - Therefore I Am",
"Arctic Monkeys - Do I Wanna Know?"
]
},


"ENTP":{
"emoji":"🔥",
"name":"아이디어 천재",
"desc":"새로운 것을 시도하고 재미를 만드는 타입",
"songs":[
"Bruno Mars - 24K Magic",
"Lady Gaga - Poker Face",
"Imagine Dragons - Thunder",
"Maroon 5 - Moves Like Jagger",
"Avicii - Wake Me Up"
]
},


"ESFP":{
"emoji":"✨",
"name":"무대 위 주인공",
"desc":"사람들과 함께하는 순간을 사랑하는 분위기 메이커",
"songs":[
"Sabrina Carpenter - Espresso",
"Ariana Grande - Into You",
"Justin Bieber - Sorry",
"Maroon 5 - Sugar",
"Rihanna - Diamonds"
]
},


"ISFJ":{
"emoji":"🌷",
"name":"따뜻한 힐링러",
"desc":"배려심 많고 안정감을 주는 다정한 타입",
"songs":[
"Ed Sheeran - Perfect",
"Ariana Grande - pov",
"Sam Smith - Stay With Me",
"Bruno Mars - Just The Way You Are",
"John Legend - All of Me"
]
}

}


# 나머지 MBTI 자동 생성
all_types=[
"ISTJ","ESTJ","ISTP","ESTP",
"ISFP","ESFJ","INFJ","ENTJ"
]

for t in all_types:
    if t not in mbti_data:
        mbti_data[t]={
        "emoji":"⭐",
        "name":"특별한 개성의 소유자",
        "desc":"자신만의 스타일과 취향이 확실한 타입",
        "songs":[
        "Taylor Swift - Anti-Hero",
        "Olivia Rodrigo - vampire",
        "The Weeknd - Starboy",
        "Ariana Grande - yes, and?",
        "Harry Styles - Adore You"
        ]
        }



st.markdown(
"<div class='title'>🎧 MBTI POP CARD</div>",
unsafe_allow_html=True
)

st.write("")

mbti=st.text_input(
"💗 MBTI 입력",
placeholder="예 : ENFP"
).upper()


if st.button("✨ 나의 팝 카드 만들기"):

    if mbti in mbti_data:

        data=mbti_data[mbti]

        song=random.choice(data["songs"])

        youtube_url=(
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(song)
        )


        st.markdown(f"""
        <div class="card">

        <h1>{data['emoji']} {mbti}</h1>

        <span class="badge">
        {data['name']}
        </span>

        <br><br>

        <p>{data['desc']}</p>

        <hr>

        🎵 오늘의 추천곡

        <div class="song">
        {song}
        </div>

        <br>

        <p class="small">
        당신의 성향과 어울리는 감성 플레이리스트
        </p>

        </div>
        """,
        unsafe_allow_html=True)


        st.link_button(
        "▶️ YouTube에서 듣기",
        youtube_url
        )


    else:
        st.error(
        "MBTI 4글자를 정확하게 입력해주세요!"
        )


st.caption("💿 MBTI × POP MUSIC | Instagram style playlist")
