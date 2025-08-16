"""
File: q1Mystery.py

This file contains the script for Question 1 of Homework 1

Fall 2025
Author: <your name here>
"""
# TODO: Put your name above!

# ----------------------------------------------------------------------------------------------
# Question 1: Mystery script. Figure out what this is doing and annotate it
# TODO: Add a comment here that summarizes the purpose of the script below:
# TODO: what does it do?

# TODO: Annotated each line of code below as shown in the example, describing what it does


lenStr = input("How long (in inches) is your fish tank: ")
widStr = input("How wide (in inches) is your fish tank: ")
hgtStr = input("How tall (in inches) is your fish tank: ")

length = float(lenStr)
width = float(lenStr)
height = float(hgtStr)

tankVolume1 = length * width * height
tankGallons = tankVolume1 / 231

print("This tank holds", tankGallons, "gallons of water.")

volForFish = max(0.0, tankGallons - 10)
numFish1 = volForFish // 10
numFish = int(numFish1)

print("This tank can hold", numFish, "common goldfish.")
