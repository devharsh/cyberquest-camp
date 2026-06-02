# Day 1: Foundations - Python and the Linux Command Line

**Duration:** about 3 hours (flexible)
**Goal:** Write your first real code and meet the terminal that powers most of the internet.

---

## Learning objectives
By the end of today you can:
- Explain what Python is and why it is used in cybersecurity.
- Use variables, data types, and a loop.
- Navigate a Linux terminal and read your first hidden password in OverTheWire Bandit.

## Vocabulary (acronyms expanded and defined)
- **Python**: a popular, easy-to-read programming language (named after the comedy group Monty Python, not the snake).
- **CLI = Command Line Interface**: a text-only way to control a computer by typing commands.
- **OS = Operating System**: the software that runs a computer, such as Windows, macOS, or Linux.
- **Linux**: a free, open-source operating system that runs most web servers, phones (Android), and supercomputers.
- **SSH = Secure Shell**: a tool to safely log in to another computer over the network.
- **IDE = Integrated Development Environment**: an app for writing and running code.
- **Syntax**: the grammar rules of a programming language.
- **Variable**: a named box that stores a value.

## Picture it
```
   YOU type a command  ->  [ TERMINAL ]  ->  the computer obeys
        ls                                     shows your files
        cd Desktop                             moves into a folder
        cat secret.txt                         prints a file
```
A loop is like telling a robot: "take a step, repeat 5 times."

## In the news (real and verifiable)
Python is consistently ranked among the most popular programming languages in the world in the annual Stack Overflow Developer Survey and the TIOBE index. Security teams love it because you can automate boring tasks in a few lines. Most websites you visit run on Linux servers, which is why learning the terminal is a real career skill.

## Activity 1: CodeCombat (Python through a game)
Open https://codecombat.com/ and start **Computer Science 1** (free levels).
1. Create a free account or play as a guest.
2. Move your hero with code like `hero.moveRight()`.
3. When you repeat moves, use a loop, the same idea as the notebook.
Aim to clear the first 5 to 8 levels.

## Activity 2: OverTheWire Bandit (Linux terminal levels)
Open https://overthewire.org/wargames/bandit/bandit0.html
- **Bandit Level 0:** log in with SSH. On Windows use the built-in Terminal or PowerShell; on Mac use Terminal.
  - Command: `ssh bandit0@bandit.labs.overthewire.org -p 2220`
  - Password: `bandit0`
- **Bandit Level 0 to 1:** read the file named `readme`.
  - Command: `cat readme`  (this prints the password for the next level)
- Commands you will use a lot: `ls` (list files), `cd` (change directory), `cat` (print a file), `pwd` (where am I).
Write each password you find in a safe note so you can keep climbing.

## Numericals (do these in the notebook)
1. How many times does `for i in range(7):` repeat?
2. What is `2 ** 10` (two to the power ten)?
3. What is `25 % 4` (the remainder)?

## Multiple choice (MCQ)
1. A variable is best described as:
   a) a type of virus  b) a named box that stores a value  c) a website
2. Which command prints the contents of a file in Linux?
   a) `cat`  b) `run`  c) `open`
3. SSH stands for:
   a) Super Secure Hardware  b) Secure Shell  c) System Service Host

## Code challenge
Open **Day1.ipynb** and complete Challenge 1 (mission counter) and Challenge 2 (password length checker).

## Reflection and homework
Write two sentences: what does a loop in code have in common with a maze in CodeCombat? Try one more Bandit level at home if you want a head start.

---
**Answer key.** Numericals: 1) 7 times, 2) 1024, 3) 1. MCQ: 1-b, 2-a, 3-b.


---

# Extended Lecture Notes

# Day 1: Foundational Scripting, Networks, and Linux Environments

## Morning Kickoff: Motivation & News (09:00 AM - 09:15 AM)
* **Case Profile**: The 2014 Sony Pictures Hack. Attackers compromised network architectures using targeted data deletion tools, revealing confidential emails and unreleased files. This illustrates how technical script logic alters international geopolitics.

## Teaching Session I: Core Lecture (09:15 AM - 11:15 AM)

### Introduction to Computer Programming using Python
Python is an interpreted, high-level, general-purpose programming language. Because its syntax focuses heavily on readability, it is the primary industry tool used by security professionals to write automated scanners and network exploit modules.
* **Variables**: Allocated memory addresses holding data values.
* **Syntax**: The grammar rules regulating code configuration.
* **Data Types**: Strings (textual data like `"admin"`), Integers (whole numbers like `80`), and Booleans (logical evaluations representing `True` or `False`).

### Computer Networking Foundations
* **Internet Protocol Address (IP Address)**: A unique numerical identifier assigned to every hardware component interacting on an internet network framework.
* **Data Packet**: A formatted unit of data carried by a packet-switched network. Contains control metadata (headers) and user data payloads.
* **Routing**: The functional process of selecting paths across network nodes to guide packets from their source to their destination.
* **HTTP vs HTTPS**: Hypertext Transfer Protocol (HTTP) transmits network requests in unencrypted plain text. Hypertext Transfer Protocol Secure (HTTPS) uses Transport Layer Security (TLS) cryptographic protocols to encrypt communication channels, preventing eavesdropping.



### The Linux Operating System Command Line Interface (CLI)
Cybersecurity systems, cloud networks, and penetration testing platforms like Kali Linux rely on a text-based command line interface instead of a graphical user interface.
* `pwd` (Print Working Directory): Outputs the full path of the current working folder.
* `ls` (List Directory Contents): Displays files inside the current working folder.
* `cd` (Change Directory): Moves the user into a different directory folder.
* `mkdir` (Make Directory): Generates a brand-new directory folder.
* `echo` (Display text line): Prints arguments to the standard output screen.
* `cat` (Concatenate): Reads file inner text and displays it directly to the terminal.

---

## Teaching Session II: Labs & Interactive Tools (11:45 AM - 01:45 PM)

### Practical Interactive Tools for Today
1.  **CodeCombat**: Navigate programming levels by typing functional Python loops and variable calls.
2.  **OverTheWire Bandit**: Connect via Secure Shell (SSH) and run commands (`ls`, `cd`, `cat`) to search for text-based authentication keys hidden in files.

---

## Knowledge Evaluation Bank (Embedded Assessments)

### Multiple-Choice Questions (MCQ)
1.  An analyst intercepts network traffic and reads user passwords in plain text. What unencrypted protocol was the target web application using?
    * A) HTTPS
    * B) HTTP
    * C) SSH
    * *Answer Key*: B. HTTP transmits payloads without cryptographic protection layers.

2.  Which Linux CLI command displays the contents of a text file on the terminal screen?
    * A) mkdir
    * B) pwd
    * C) cat
    * *Answer Key*: C. `cat` reads and outputs file contents to standard output.

### Numerical Exercise
A network router receives an unfragmented data packet file with a total payload size of 4,500 bytes. If the local network limits the maximum packet transmission size to 1,500 bytes per transmission unit, calculate the exact minimum number of individual packet segments the router must generate to transmit the complete payload data across the network.
* *Solution Step*: $\text{Segments} = \frac{4500 \text{ bytes}}{1500 \text{ bytes/packet}} = 3 \text{ packets}$.

---

## Recap & Tomorrow's Horizon (04:15 PM - 04:30 PM)
* **Summary**: Today we mastered core variables, network routing differences, and basic terminal control commands.
* **Tomorrow Preview**: We will move from basic technical systems to security management frameworks, examining threats, vulnerability analysis, and the legal limits of hacking.
