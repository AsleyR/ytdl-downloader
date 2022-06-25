from winds.main_w import MainWindow
from winds.about_w import AboutWindow
from winds.custom_command import CustomYoutubeDlCommandWindow
from winds.download_windows.video_winds.download_video_w import VideoDownloadWindow
from winds.download_windows.save_winds.save_w import SaveLocationWindow

def main_program():
    AUDIO_YOUTUBEDL_COMMAND = "-x --audio-format mp3"

    try:
        while True:
            program_version = "1.1.1"

            # Init MainWindow
            main_program = MainWindow("Youtube-dl Terminal Gui", program_version)
            user_input = main_program.init_program()
            print(f"You chose: {user_input}")

            # Save Window
            if user_input == '1':
                download_video_w = VideoDownloadWindow()
                download_video_w.init_window()
            
            elif user_input == "2":
                save_window = SaveLocationWindow(AUDIO_YOUTUBEDL_COMMAND)
                save_window.init_window()

            elif user_input == "3":
                custom_command_w = CustomYoutubeDlCommandWindow()
                custom_command_w.init_window()

            elif user_input == '4':
                about_w = AboutWindow("Asley R.", program_version)
                about_w.print_about()

            elif user_input == '6':
                # Exit program
                main_program.exit()

    except KeyboardInterrupt: # Control C keyboard interrupt
        main_program.exit()

# Init script
if __name__ == "__main__":
    main_program()

