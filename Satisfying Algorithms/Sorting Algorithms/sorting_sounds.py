import winsound

import sys
import os

# Get the absolute path of the parent directory (main_folder)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Access the Sounds Files
import Sounds.Notifications
import Sounds.Swoops

# def playthis():
#     sound_file = os.path.join("..", "Sounds", "473868__erokia__synth-loop-26-90-bpm.wav")
#     winsound.PlaySound(sound_file, winsound.SND_FILENAME)

def play_SwoopOne():
    script_dir = os.path.dirname(__file__)  # Get the directory path of the current script
    sound_file = os.path.join(script_dir, "..", "Sounds", "Swoops", "473868__erokia__synth-loop-26-90-bpm.wav")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_NotificationOne():
    script_dir = os.path.dirname(__file__)  # Get the directory path of the current script
    sound_file = os.path.join(script_dir, "..", "Sounds", "Notifications", "186669__fordps3__computer-boop.wav")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_NotificationTwo():
    script_dir = os.path.dirname(__file__)  # Get the directory path of the current script
    sound_file = os.path.join(script_dir, "..", "Sounds", "Notifications", "221363__waveplaysfx__perc-tom-click.wav")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_NotificationThree():
    script_dir = os.path.dirname(__file__)  # Get the directory path of the current script
    sound_file = os.path.join(script_dir, "..", "Sounds", "Notifications", "523422__andersmmg__ding-1.wav")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_NotificationFour():
    script_dir = os.path.dirname(__file__)  # Get the directory path of the current script
    sound_file = os.path.join(script_dir, "..", "Sounds", "Notifications", "quick_blip.mp3")
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

def test_sound_effect_path():
    script_dir = os.path.dirname(__file__)  # Get the directory path of the current script
    sound_file = os.path.join(script_dir, "..", "Sounds", "Swoops", "473868__erokia__synth-loop-26-90-bpm.wav")
    if os.path.isfile(sound_file):
        print("Sound effect file found.")
    else:
        print("Sound effect file not found.")


        
# # Drive code to test above
# if __name__ == "__main__":
#     test_sound_effect_path()
#     #play_SwoopOne()
#     play_NotificationTwo()