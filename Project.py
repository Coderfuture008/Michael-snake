#!/usr/bin/python3


Safe = ["thunder snake, worm snake, Carphophis amoenus", 
"ringneck snake, ring-necked snake, ring snake", 
"hognose snake, puff adder, sand viper", "green snake, grass snake", 
"king snake, kingsnake", "garter snake, grass snake", "water snake", 
"night snake, Hypsiglena torquata", 
"boa constrictor, Constrictor constrictor", 
"rock python, rock snake, Python sebae"]

Dangerous = ["vine snake", "Indian cobra, Naja naja", "green mamba", 
"sea snake", " sidewinder, horned rattlesnake, Crotalus cerastes", 
"diamondback, diamondback rattlesnake, Crotalus adamanteus"]

import jetson_inference
import jetson_utils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="resnet-18", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()

img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(opt.network)

class_idx, confidence = net.Classify(img)

class_desc = net.GetClassDesc(class_idx)
print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))


for i in Safe:
    if i == class_desc:
        print("This snake is not venomous.")
for i in Dangerous:
    if i == class_desc:
        print("This snake is venomous. If you are bitten, please seek medical attention.")
