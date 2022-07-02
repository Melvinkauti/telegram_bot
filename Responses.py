from datetime import datetime


def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am WuubaLubbaDubDubbot"

    if user_message in ("tell me a joke", "make me laugh", "tell me something funny"):
        return "Helvetica and New Times Roman walk into a bar, Get out of here shouts the bar tender. we dont serve your type"

    if user_message in ("recommend music for me", "play music", "playlist"):
        return "https://open.spotify.com/playlist/0GnetKTkAzly6IWhEYRusq?si=5e495c6849ad4fb3 " \
               "https://open.spotify.com/playlist/3rdroUK46p4nh5VCCDxnnB?si=ed0c732caa3b4187"

    if user_message in ("time", "time?"):
        # get local time
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you"
