import requests
import time
import pygame

def check_api():
    try:
        response = requests.get("https://api-my.sa.gov.ge/api/v1/DrivingLicensePracticalExams2/DrivingLicenseExamsDates2?CategoryCode=4&CenterId=15")
        print(response.text)
        if response.status_code == 200 and response.text!="[]":
            return True
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    return False

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for music to finish playing
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    music_file_path = "C:/Users/User/Desktop/myShit/soflis.mp3"  # Update this with the path to your music file
    while True:
        if check_api():
            print("API is up! Playing music...")
            play_music(music_file_path)
            break
        else:
            print("API is down. Retrying in 15 seconds...")
            time.sleep(15)
