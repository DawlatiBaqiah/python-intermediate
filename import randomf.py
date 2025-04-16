import random
import time

def typing_speed_test():
    words = ["Paracetamol", "Coronavirus", "Assemblywomen", "Antiferromagnetism", "Thermoregulation", "Miscommunication", "lymphangiomyomatosis"]
    word = random.choice(words)

    print("Welcome to Typing Speed Test!")
    print(f"Type the followwing word as fast as you can: {word}")
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input("Type here: ")
    if user_input == word:
        time_taken = round(end_time - start_time, 2)
        print(f"Great Job! You took {time_taken} seconds.")
    else:
        print(f"Ooops! You typed it incorrectly, the correct word was '{word}'. Try Again!")

if __name__ == "__main__":
     typing_speed_test()