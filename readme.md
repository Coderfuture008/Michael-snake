# Snake Classification

This project is about classifying snake: the name of the snake is given and whether or not it is venomous.

 The impact of this project is that many people are scared of snakes due to some snakes being venomous. My project is about letting people classify the snakes and then outputting whether the snake is venomous or not. This will allow people outside to know if they are in danger. Also, if a person has been bitten, they will know if the bite is deadly or not. This will allow some people to know if they need medical attention because they have just been bitten by a venomous and perhaps save their life.

![Screenshot (11)](https://github.com/Coderfuture008/Michael-snake/assets/140195616/b674b858-9287-45f5-8437-f80bf28c9d89)

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 
This project used resnet-18 model to classify snakes. The model already had many different species of snakes trained so I didn't need to retrain it. I then researched the snakes and split them into two lists which are safe and dangerous. Then, I used a for loop at the end to match the identified snake to a snake in of the list. If it belonged in the safe list, then the program outputed "This snake is not venomous.". If it was in the dangerous list, then I outputed "This snake is venomous. If you are bitten, please seek medical attention."

## Running this project

1. It is necessary that users have resnet-18 downloaded on their Jetson Nano.
2. Python 3 and other files should have come with the Jetson Nano in VScode.
3. Download Project.py onto the computer.
4. Create a folder called Project by clicking the button create folder.
5. Then upload Project.py into the Project folder.
6. Find images on the web and download them. If they are in a zipped folder than unzip them.
7. Drag the images or folder into the folder called Project in vscode.
8. Go to the Project by doing cd Project
9. Run the program by doing: python3 Project.py [imagename] if it is an image in Project folder.If image is in a folder in Project folder, then do python3 Project.py [foldername]/[imagename] to run correctly. Do not forget the .png, .jpg or something else after the imagename.

# Video
https://youtu.be/jD3wRStoLdo
