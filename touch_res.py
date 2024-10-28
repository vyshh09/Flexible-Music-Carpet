import serial
import time
import pygame

# Initialize Pygame mixer
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

# Load the music files
sound_files = {
    "do": pygame.mixer.Sound('C3.mp3'),
    "re": pygame.mixer.Sound('D3.mp3'),
    "mi": pygame.mixer.Sound('E3.mp3')
}

# Open serial port (adjust the port name and baud rate accordingly)
ser = serial.Serial('COM15', 9600)  # Replace 'COM15' with your Arduino's serial port
time.sleep(2)  # Wait for the serial connection to initialize

# Define a threshold for detecting a touch
TOUCH_THRESHOLD = 1.5 # Adjust this value based on your setup
TOUCH_DETECTED = [False, False, False]  # Keep track of touch state for A0, A1, A2

def read_voltages():
    """Reads the voltage from the serial input and parses it into three float values."""
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            parts = line.split("|")  # Split based on '|' separator
            voltages = [float(part.split(":")[1].strip()) for part in parts[1:4]]  # Extract the voltages for V0, V1, V2
            return voltages
        except:
            return None
        
# Create a Pygame window (optional, for event handling)
# screen = pygame.display.set_mode((400, 300))
running = True


try:
    while running:

        #     # Handle events
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        
            # # Check if a key is pressed
            # if event.type == pygame.KEYDOWN:
            #     # Play the music when the 'P' key is pressed
            #         if event.key == pygame.K_a:
            #             print("Playing 'C3.mp3' for A0")
            #             sound_files["do"].play()
            #         elif event.key == pygame.K_s:
            #             print("Playing 'D3.mp3' for A1")
            #             sound_files["re"].play()
            #         elif event.key == pygame.K_d:
            #             print("Playing 'mi.mp3' for A2")
            #             sound_files["mi"].play()

        voltages = read_voltages()  # Get voltages for A0, A1, A2
        if voltages is not None:
            # print(f"Voltages: A0={voltages[0]}V, A1={voltages[1]}V, A2={voltages[2]}V")

            # Check each voltage and play the sound only once per touch
            for i, voltage in enumerate(voltages):
                if voltage < TOUCH_THRESHOLD and not TOUCH_DETECTED[i]:
                    # Mark the touch as detected
                    TOUCH_DETECTED[i] = True

                    # Play the corresponding sound for each voltage input
                    if i == 0:
                        print("Playing 'C3.mp3' for A0")
                        sound_files["do"].play()
                    elif i == 1:
                        print("Playing 'D3.mp3' for A1")
                        sound_files["re"].play()
                    elif i == 2:
                        print("Playing 'mi.mp3' for A2")
                        sound_files["mi"].play()

                # Reset the touch detection when voltage goes above the threshold
                if voltage >= TOUCH_THRESHOLD and TOUCH_DETECTED[i]:
                    TOUCH_DETECTED[i] = False  # Reset touch state
                    print(f"Touch reset for A{i}, ready for next touch.")

        # time.sleep(0.1)

except KeyboardInterrupt:
    ser.close()
    pygame.mixer.quit()
    print("Program terminated.")
