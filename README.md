# Terminal

Welcome to the terminal. The main purpose of this terminal is to play audio files for visually impaired students. The terminal is used together with the custom controller for maximal effect.

# Overview

Components of the terminal:

```
1 Raspberrypi 4
1 Monitor
1 USB speaker set
1 Custom Controller 
```

**The controller**

The controller has 4 buttons. 

1. UP - used for navigation between lessons and chapters
2. DOWN - used for navigation between lessons and chapters
3. A - used to choose lessons or to replay chapters
4. B - used to return to the main menu during lessons

**Using the terminal**

To run the terminal, enter `launchterminal` into the terminal.

Upon entering the terminal, a tutorial of the terminal automatically plays. Push the **A** button to replay the tutorial or any other buttons to continue onto the main menu.

Inside the main menu, use the **UP** and **DOWN** buttons to navigate between the different lessons. Once the user has settled on a lesson, Press the **A** button to enter the lesson. 

The chapters of the lesson will automatically start playing. To navigate between the chapters use the **UP** and  **DOWN** buttons. To replay any chapters, use the **A** button. To return to the main menu, use the **B** button. 

Once the user has finished all the chapters in a lesson, he will be automatically directed to a small quiz to test the user's understanding of the content. A short quiz will be read out and options will be given. The user will then use the **A** or **B** button so select the correct option. 

If the correct option is selected, the terminal plays an audio file that congratulates the user. On the other hand, if the wrong option is selected, the terminal explains an audio file explaining the corect answer to the user. 


# File Hierarchy 

This section is ***critical*** to the functionality of terminal.
The autio files and directories within the program must be appropriately named.

### Example Layout 
```
    .
    ├── main.py
    ├── tutorial.mp3
    ├── main_menu_voice.mp3
    └── main_menu 
        ├── lesson 1
        │    ├──example_lesson_1_voice.mp3
        │    ├──lesson_1_chapter_1.mp3
        │    ├──lesson_1_chapter_2.mp3
        │    ├──lesson_1_chapter_3.mp3
        │    ├──quiz_1_answer_A.mp3
        │    ├──quiz_1_correct.mp3
        │    └──quiz_1_wrong.mp3
        └── lesson 2
             ├──example_lesson_2_voice.mp3
             ├──lesson_2_chapter_1.mp3
             ├──lesson_2_chapter_2.mp3
             ├──lesson_2_chapter_3.mp3
             ├──quiz_2_answer_B.mp3
             ├──quiz_2_correct.mp3
             └──quiz_2_wrong.mp3
```

Running `main.py` launches the terminal. 

`tutorial.mp3` and `main_menu_voice.mp3 must remain in the same directory as main.py

Contents in square brackets [ ] can be replaced with whatever the user wishes. 

example

    [name of lesson]_voice.mp3

### Adding lessons
Different lessons can be added to the terminal. This is done by adding a new directory in the *main_menu* directory. Within this new directory, a .mp3 file needs to be added. 

The naming convention is as follows:
    
    [name of lesson]_voice.mp3

***Only 1 \*_voice.mp3 file should be in the direcory***

example

    example_lesson_1_voice.mp3

### Adding chapters

To add chapters to the lesson, appropriately named .mp3 files can be added to the lesson directory. 

The naming convention for the chapters is as follows:

    [lesson name]_chapter_[number].mp3

If more than 1 chapters are added, the number in the name of the file must be in the correct order. 

example

    lesson_1_chapter_1.mp3
    lesson_1_chapter_2.mp3

### Adding quizzes

To add chapters to the lesson, appropriately named .mp3 files can be added to the lesson directory. 

The quiz audio file has the following naming convention:

    quiz_[lesson]_answer_[correct answer].mp3

example

    quiz_1_answer_A.mp3

The correct answer to the quiz (either A or B in this implementation of the terminal) must be in the name of the .mp3 file. 

Furthermore, 2 additional audio files have to be added to the directory. 

The audio file that plays when the user chooses the correct option has the naming convention: 

    quiz_[lesson]_correct.mp3

example

    quiz_1_correct.mp3

The audio file that plays when the user chooses the wrong option has the naming convention: 

    quiz_[lesson]_wrong.mp3

example:

    quiz_1_wrong.mp3

