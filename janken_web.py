import streamlit as st
import random

st.title("✊✌🖐 じゃんけんゲーム")

options = ['グー', 'チョキ', 'パー']
user_choice = st.radio("あなたの手を選んでね：", options)

if st.button("じゃんけんぽん！"):
    computer_choice = random.choice(options)
    st.write(f"あなた：{user_choice}")
    st.write(f"コンピュータ：{computer_choice}")

    if user_choice == computer_choice:
        result = "あいこ！"
    elif (user_choice == 'グー' and computer_choice == 'チョキ') or \
         (user_choice == 'チョキ' and computer_choice == 'パー') or \
         (user_choice == 'パー' and computer_choice == 'グー'):
        result = "あなたの勝ち！🎉"
    else:
        result = "あなたの負け…😢"

    st.subheader(result)
