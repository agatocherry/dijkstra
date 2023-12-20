#!/bin/bash

# * Run the program for simple.txt
echo -e "\e[31m• Run for: graphs/simple.txt •\e[0m
"
python3 srcs/main.py graphs/simple.txt

# * Run the program for hard.txt
echo -e "

\e[31m• Run for: graphs/hard.txt •\e[0m
"
python3 srcs/main.py graphs/hard.txt

# * Run the program for prof.txt
echo -e "

\e[31m• Run for: graphs/prof.txt •\e[0m
"
python3 srcs/main.py graphs/prof.txt
