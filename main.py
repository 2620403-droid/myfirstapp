import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI Pop Pick 🎧",
    page_icon="🎵",
    layout="centered"
)

# 스타일(CSS)
st.markdown("""
<style>
body {
    background-color: #fff5fb;
}

.main {
    background: linear-gradient(135deg, #ffe6f7, #e6f0ff);
    border-radius: 20px;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: 900;
    background: linear-gradient(90deg,#ff4ecd,#6c63ff);
    -webkit-background-clip: text;
    color: transparent;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.song {
    font-size: 28px;
    font-weight: bold;
    color: #ff4b91;
}

.tag {
    background: #ffe0f0;
    padding: 8px 15px;
    border-radius: 20px;
    display: inline-block;
    color: #d63384;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# 데이터
mbti_data = {
    "INFP": {
        "emoji":"🌙",
        "type":"감성적인 꿈꾸는 예술가",
        "desc":"상상력이 풍부하고 자신의 세계가 뚜렷해요. 음악과 이야기에 깊게 빠지는 스타일!",
        "songs":["Taylor Swift - cardigan",
                 "Billie Eilish - ocean eyes",
                 "Adele - Easy On Me"]
    },

    "ENFP": {
        "emoji":"🌈",
        "type":"에너지 넘치는 자유로운 영혼",
        "desc":"새로운 경험을 좋아하고 사람들에게 긍정 에너지를 주는 타입!",
        "songs":["Dua Lipa - Levitating",
                 "Katy Perry - Firework",
                 "Coldplay - A Sky Full of Stars"]
    },

    "INTJ": {
        "emoji":"🖤",
        "type":"전략적인 천재 플래너",
        "desc":"목표를 세우고 깊게 생각하는 분석가 스타일!",
        "songs":["The Weeknd - Blinding Lights",
                 "Imagine Dragons - Believer",
                 "Sia - Unstoppable"]
    },

    "ENTP": {
        "emoji":"🔥",
        "type":"아이디어 폭발 토론가",
        "desc":"재치 있고 새로운 것을 시도하는 창의적인 타입!",
        "songs":["Imagine Dragons - Thunder",
                 "Bruno Mars - 24K Magic",
                 "Lady Gaga - Poker Face"]
    },

    "ISFJ": {
        "emoji":"🌷",
        "type":"따뜻한 배려왕",
        "desc":"주변 사람을 잘 챙기고 안정감을 주는 타입!",
        "songs":["Ed Sheeran - Perfect",
                 "Ariana Grande - pov",
                 "Sam Smith - Stay With Me"]
    },

    "ESFP": {
        "emoji":"✨",
        "type":"파티의 중심 스타",
        "desc":"즐거움을 찾고 분위기를 밝게 만드는 타입!",
        "songs":["Justin Bieber - Sorry",
                 "Maroon 5 - Sugar",
                 "Sabrina Carpenter - Espresso"]
    }
}


# 나머지 MBTI 기본 처리
all_mbti = [
    "ISTJ","ESTJ","ISTP","ESTP",
    "ISFP","ESFJ","INFJ","ENTJ"
]

for m in all_mbti:
    if m not in mbti_data:
        mbti_data[m] = {
            "emoji":"⭐",
            "type":"특별한 개성을 가진 사람",
            "desc":"자신만의 방식으로 세상을 바라보는 매력적인 타입!",
            "songs":[
                "Harry Styles - As It Was",
                "Olivia Rodrigo - vampire",
                "The Weeknd - Starboy"
            ]
        }


# 화면
st.markdown("<div class='title'>🎧 MBTI POP PICK</div>",
            unsafe_allow_html=True)

st.write("")

st.markdown(
"💗 **나의 MBTI를 입력하면 나와 어울리는 팝송을 찾아줘요!**"
)

mbti = st.text_input(
    "MBTI 입력 (예: INFP)",
    placeholder="INFP"
).upper()


if st.button("✨ 내 플레이리스트 보기"):

    if mbti in mbti_data:

        data = mbti_data[mbti]
        song = random.choice(data["songs"])

        st.balloons()

        st.markdown(f"""
        <div class='card'>

        <h1>{data['emoji']} {mbti}</h1>

        <div class='tag'>
        {data['type']}
        </div>

        <br><br>

        <p>{data['desc']}</p>

        <hr>

        🎵 당신에게 추천하는 오늘의 팝송

        <div class='song'>
        {song}
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.caption("💿 당신만의 감성 플레이리스트가 완성됐어요!")

    else:
        st.error("MBTI 4글자를 정확히 입력해주세요! (예: ENFP)")


st.write("")
st.markdown(
"📸 Made with 💗 for MBTI music lovers"
)
