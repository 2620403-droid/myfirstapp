import streamlit as st
import random
import urllib.parse


st.set_page_config(
    page_title="MBTI POP PICK",
    page_icon="☕",
    layout="centered"
)


# 디자인
st.markdown("""
<style>

body {
    background:#fff4fa;
}

.title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    color:#ff4f91;
}

.subtitle {
    text-align:center;
    color:#777;
    font-size:18px;
}

.card {
    background:white;
    padding:35px;
    border-radius:30px;
    box-shadow:0 10px 25px rgba(0,0,0,0.1);
}

.badge {
    background:#ffe0ef;
    color:#ff3d8d;
    padding:8px 18px;
    border-radius:20px;
    font-weight:bold;
}

.song {
    font-size:27px;
    font-weight:900;
    color:#8b5cf6;
}

</style>
""", unsafe_allow_html=True)



# MBTI 데이터
mbti_data = {

"ENFP":{
"emoji":"🌈",
"type":"인간 비타민",
"desc":"밝은 에너지와 새로운 설렘을 좋아하는 타입",
"songs":[
"Sabrina Carpenter - Espresso",
"Sabrina Carpenter - Feather",
"Dua Lipa - Dance The Night",
"Tate McRae - greedy",
"Doja Cat - Say So"
]
},


"ESFP":{
"emoji":"✨",
"type":"파티 스타",
"desc":"즐거움과 자신만의 매력을 뽐내는 타입",
"songs":[
"Sabrina Carpenter - Espresso",
"Ariana Grande - 7 rings",
"Lady Gaga - Just Dance",
"Rihanna - Only Girl (In The World)",
"Katy Perry - Teenage Dream"
]
},


"INFP":{
"emoji":"🌸",
"type":"감성 큐레이터",
"desc":"예쁜 분위기와 음악 속 감정을 사랑하는 타입",
"songs":[
"Laufey - Bewitched",
"Lana Del Rey - Say Yes To Heaven",
"Taylor Swift - cardigan",
"Conan Gray - Heather",
"Harry Styles - Adore You"
]
},


"ENTP":{
"emoji":"🔥",
"type":"아이디어 폭주러",
"desc":"새로운 도전과 재미를 추구하는 타입",
"songs":[
"Charli XCX - Boom Clap",
"Doja Cat - Kiss Me More",
"Lady Gaga - Poker Face",
"Avicii - Wake Me Up",
"Troye Sivan - Rush"
]
},


"ISFJ":{
"emoji":"🌷",
"type":"따뜻한 힐링러",
"desc":"포근하고 다정한 분위기를 가진 타입",
"songs":[
"Harry Styles - Watermelon Sugar",
"Ed Sheeran - Perfect",
"Bruno Mars - Just The Way You Are",
"Laufey - From The Start",
"Ariana Grande - pov"
]
},


"INTJ":{
"emoji":"🖤",
"type":"쿨한 전략가",
"desc":"자신만의 취향과 스타일이 확실한 타입",
"songs":[
"Dua Lipa - Houdini",
"The Weeknd - Starboy",
"Billie Eilish - Therefore I Am",
"Rihanna - Diamonds",
"Tate McRae - exes"
]
}

}



# 없는 MBTI 기본값
for mbti in [
"ISTJ","ESTJ","ISTP","ESTP",
"ISFP","ESFJ","INFJ","ENTJ"
]:

    mbti_data[mbti]={
    "emoji":"⭐",
    "type":"유니크한 스타일",
    "desc":"자신만의 개성을 가진 특별한 타입",
    "songs":[
    "Sabrina Carpenter - Espresso",
    "Dua Lipa - Houdini",
    "Harry Styles - Adore You",
    "NewJeans - Super Shy",
    "Carly Rae Jepsen - Call Me Maybe"
    ]
    }



# 화면

st.markdown(
"<div class='title'>☕ MBTI POP PICK</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>나의 성격에 어울리는 인스타 감성 팝송 찾기 🎧</div>",
unsafe_allow_html=True
)


st.write("")


user_mbti = st.text_input(
"💗 MBTI 입력",
placeholder="예 : ENFP"
).upper()



if st.button("✨ 내 팝 카드 만들기"):

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

        ☕ 오늘의 감성 플레이리스트

        <div class="song">
        {song}
        </div>


        </div>

        """,
        unsafe_allow_html=True)


        st.link_button(
            "▶️ YouTube로 듣기",
            youtube
        )


    else:

        st.error(
            "MBTI 4글자를 입력해주세요!"
        )



st.caption(
"💿 MBTI × POP × Instagram Mood"
)
