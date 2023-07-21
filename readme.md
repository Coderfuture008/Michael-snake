# Snake Classification

 This project is about classifying snake: the name of the snake is given and whether or not it is venomous.

 The impact of this project is that many people are scared of snakes due to some snakes being venomous. My project is about letting people classify the snakes and then outputting whether the snake is venomous or not. This will allow people outside to know if they are in danger. Also, if a person has been bitten, they will know if the bite is deadly or not. This will allow some people to know if they need medical attention because they have just been bitten by a venomous and perhaps save their life.

![add image descrition here](direct image link here)

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 
This project used resnet-18 model to classify snakes. The model already had many different species of snakes trained so I didn't need to retrain it. I then researched the snakes and split them into two lists which are safe and dangerous. Then, I used a for loop at the end to match the identified snake to a snake in of the list. If it belonged in the safe list, then the program outputed "This snake is not venomous.". If it was in the dangerous list, then I outputed "This snake is venomous. If you are bitten, please seek medical attention."

## Running this project

1. It is necessary that users have resnet-18 downloaded on their Jetson Nano.
2. Python 3 and other files should have come with the Jetson Nano in VScode.
3. Download the test folder and Project.py onto the computer
4. Create a folder called Project by clicking the button create folder.
5. Unzip the test folder and drag it into Project.
6. Then upload Project.py into the Project folder.
7. Go to the Project by doing cd Project
8. Run the program by doing 

[View a video explanation here](video link)
