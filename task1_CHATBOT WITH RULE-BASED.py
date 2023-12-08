import streamlit as st
import random

def get_random_fun_fact(sign):
    # Fun facts about astrological signs
    fun_facts = {
        "aries": "Fun Fact: Aries individuals are known for their courage and determination.",
        "taurus": "Fun Fact: Taurus is ruled by Venus, the planet of love and beauty.",
        "gemini": "Fun Fact: Geminis are known for their quick-witted and adaptable nature.",
        "cancer": "Fun Fact: Cancer is ruled by the Moon, emphasizing emotions and intuition.",
        "leo": "Fun Fact: Leos are natural leaders and often enjoy being the center of attention.",
        "virgo": "Fun Fact: Virgos are detail-oriented and strive for perfection in all they do.",
        "libra": "Fun Fact: Libras are known for their love of harmony and balance.",
        "scorpio": "Fun Fact: Scorpios are intense and determined, with a magnetic personality.",
        "sagittarius": "Fun Fact: Sagittarians are adventurous and always up for a new challenge.",
        "capricorn": "Fun Fact: Capricorns are disciplined and ambitious, working towards their goals.",
        "aquarius": "Fun Fact: Aquarians are independent thinkers with a strong humanitarian streak.",
        "pisces": "Fun Fact: Pisceans are compassionate dreamers with a vivid imagination.",
    }

    return fun_facts.get(sign, "Fun Fact: Unfortunately, I don't have a fun fact for that sign.")

def stellar_signs_chatbot(user_input):
    # Predefined responses for astrological signs
    sign_responses = {
        "aries": "Aries: You're a natural-born leader with a lot of energy and enthusiasm!",
        "taurus": "Taurus: You value stability and are known for your practicality and reliability.",
        "gemini": "Gemini: Your curiosity and adaptability make you a great communicator.",
        "cancer": "Cancer: Your nurturing and empathetic nature is one of your greatest strengths.",
        "leo": "Leo: You're confident, passionate, and love being in the spotlight.",
        "virgo": "Virgo: Known for your attention to detail, you're a reliable and practical friend.",
        "libra": "Libra: You seek balance and harmony, and you have a natural charm.",
        "scorpio": "Scorpio: Your intensity and determination set you apart in everything you do.",
        "sagittarius": "Sagittarius: Your adventurous spirit and optimism make you a great companion.",
        "capricorn": "Capricorn: You're disciplined and hardworking, with a strong sense of responsibility.",
        "aquarius": "Aquarius: Your originality and humanitarian nature make you a unique and caring individual.",
        "pisces": "Pisces: Your empathy and creativity contribute to your compassionate personality.",
    }

  
    user_input_lower = user_input.lower()

    
    for sign, response in sign_responses.items():
        if sign in user_input_lower:
            return response + "\n\n" + get_random_fun_fact(sign)

    
    return "I'm sorry, I don't have information on that astrological sign. Please enter a valid sign (e.g., Aries, Leo, Cancer)."


def main():
    st.title("StellarSigns - Your Astrological Sign Guide 🌟")
    st.write("Discover insights about your astrological sign!")

    user_input = st.text_input("Enter your astrological sign:", "")
    submit_button = st.button("Submit")

    if submit_button:
        if user_input:
            greeting = f"Hello, {user_input.capitalize()}!"
            response = stellar_signs_chatbot(user_input)
            closing_message = "Feel free to explore more signs or ask about your friends' signs!"
            st.success(f"{greeting}\n\n{response}\n\n{closing_message}")
        else:
            st.warning("Please enter your astrological sign before submitting.")

if __name__ == "__main__":
    main()
