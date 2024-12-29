import random
import streamlit as st

def generate_lotto_numbers(excluded_numbers=None):
    if excluded_numbers is None:
        excluded_numbers = []
    
    available_numbers = [num for num in range(1, 46) if num not in excluded_numbers]
    
    if len(available_numbers) < 6:
        raise ValueError("생성 가능한 숫자가 부족합니다. 제외 숫자를 줄여주세요.")
    
    return sorted(random.sample(available_numbers, 6))

def generate_multiple_lotto_games(game_count, excluded_numbers=None):
    return [generate_lotto_numbers(excluded_numbers) for _ in range(game_count)]

# Streamlit UI
st.title("로또 번호 추첨기")

# 게임 수 입력
game_count = st.number_input("생성할 게임 수를 입력하세요:", min_value=1, step=1, value=1)

# 제외 숫자 입력
excluded_input = st.text_input("제외할 숫자를 입력하세요 (띄어쓰기로 구분):")
if excluded_input:
    try:
        excluded_numbers = list(set(map(int, excluded_input.split())))
        if any(num < 1 or num > 45 for num in excluded_numbers):
            st.error("입력한 숫자는 1~45 사이여야 합니다.")
            excluded_numbers = []
    except ValueError:
        st.error("잘못된 입력입니다. 숫자를 띄어쓰기로 구분해 입력해주세요.")
        excluded_numbers = []
else:
    excluded_numbers = []

# 추첨 버튼
if st.button("추첨 시작"):
    try:
        results = generate_multiple_lotto_games(game_count, excluded_numbers)
        st.write("### 결과:")
        for idx, game in enumerate(results, start=1):
            st.write(f"게임 {idx}: {game}")
    except ValueError as e:
        st.error(f"오류: {e}")

# Footer with "Made by Kuki"
st.markdown("---")
st.markdown("**Made by Kuki**")