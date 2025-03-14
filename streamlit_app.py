import streamlit as st
import random

def get_questions():
    return [
        {"question": "Siapa hero pertama yang diberikan secara gratis di Mobile Legends?", "options": ["Layla", "Miya", "Zilong", "Alucard"], "answer": "Layla"},
        {"question": "Apa role utama dari hero Tigreal?", "options": ["Marksman", "Tank", "Mage", "Assassin"], "answer": "Tank"},
        {"question": "Item apa yang memberikan efek lifesteal terbesar untuk hero physical attack?", "options": ["Blade of Despair", "Endless Battle", "Bloodlust Axe", "Haas's Claws"], "answer": "Haas's Claws"},
        {"question": "Berapa jumlah pemain dalam satu tim di mode klasik Mobile Legends?", "options": ["3", "4", "5", "6"], "answer": "5"},
        {"question": "Siapa hero yang dikenal sebagai 'King of the Jungle'?", "options": ["Alucard", "Ling", "Fanny", "Helcurt"], "answer": "Ling"},
        {"question": "Apa item terbaik untuk meningkatkan magic power?", "options": ["Divine Glaive", "Blade of Despair", "Athena's Shield", "Immortality"], "answer": "Divine Glaive"},
        {"question": "Siapa hero yang memiliki skill ultimate 'Brilliance'?", "options": ["Lunox", "Harith", "Esmeralda", "Gusion"], "answer": "Lunox"},
        {"question": "Apa fungsi utama item 'Athena's Shield'?", "options": ["Menambah Attack", "Mengurangi Cooldown", "Memberikan Magic Defense", "Menambah Movement Speed"], "answer": "Memberikan Magic Defense"},
        {"question": "Siapa hero yang memiliki skill 'Way of the Dragon'?", "options": ["Chou", "Paquito", "Masha", "Aldous"], "answer": "Chou"},
        {"question": "Apa tier tertinggi dalam sistem ranked Mobile Legends?", "options": ["Legend", "Mythic", "Epic", "Grandmaster"], "answer": "Mythic"},
    ]

def main():
    st.title("🎮 Game Kuis Mobile Legends")
    st.write("Uji pengetahuanmu tentang Mobile Legends dengan menjawab pertanyaan berikut!")
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.questions = random.sample(get_questions(), len(get_questions()))

    if st.session_state.q_index < len(st.session_state.questions):
        q_data = st.session_state.questions[st.session_state.q_index]
        st.write(f"**{q_data['question']}**")
        choice = st.radio("Pilih jawaban:", q_data["options"], key=f"q{st.session_state.q_index}")
        
        if st.button("Submit"):
            if choice == q_data["answer"]:
                st.session_state.score += 1
                st.success("✅ Jawaban benar!")
            else:
                st.error(f"❌ Jawaban salah! Jawaban yang benar adalah {q_data['answer']}")
            
            st.session_state.q_index += 1
            st.experimental_rerun()
    else:
        st.write(f"### 🎉 Permainan selesai! Skor akhir: {st.session_state.score}/{len(st.session_state.questions)}")
        if st.button("Main lagi"):
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.session_state.questions = random.sample(get_questions(), len(get_questions()))
            st.experimental_rerun()

if __name__ == "__main__":
    main()
