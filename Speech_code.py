import speech_recognition as sr
import webbrowser
import time
import pyautogui

# Function to recognize speech commands
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to open the YouTube liked videos playlist
def open_youtube_liked_videos():
    liked_videos_url = "https://www.youtube.com/playlist?list=LL"
    webbrowser.open(liked_videos_url)

# Function to click on the first video in the liked videos playlist and make it full screen
def click_first_video_and_fullscreen():
    time.sleep(5)  # Wait for the page to load completely
    # These coordinates should be adjusted based on your screen resolution and browser layout
    first_video_coords = (400, 300)  # Example coordinates, adjust these accordingly
    pyautogui.click(first_video_coords)
    time.sleep(4)  # Wait for the video to start playing
    pyautogui.press("f")  # Press 'f' to enter full screen

# Function to control YouTube video playback
def control_video(action):
    actions = {
        "forward": "right",
        "backward": "left",
        "volume up": "up",
        "volume down": "down",
        "stop": "space",
        "play": "space"
    }
    if action in actions:
        pyautogui.press(actions[action])
    else:
        print("Invalid control action.")

# Main loop
def main():
    while True:
        command = recognize_speech()
        if command:
            if command == "exit":
                print("Exiting...")
                break
            elif command == "play youtube":
                print("Playing YouTube liked videos...")
                open_youtube_liked_videos()
                click_first_video_and_fullscreen()
            elif any(cmd in command for cmd in ["forward", "backward", "volume", "stop", "play"]):
                control_video(command)
            else:
                print("Invalid command. Please say again.")

if __name__ == "__main__":
    main()
