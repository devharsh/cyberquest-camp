# CyberQuest Summer Camp (Free Edition)

A free, five-day, hands-on introduction to cybersecurity for middle and high school students. Every tool used here is free and runs in a web browser. No paid range or special hardware required.


## Who this is for
- Middle and high school students, complete beginners welcome.
- Teachers, club leaders, parents, and volunteers running a camp or after-school program.

## How the week flows
Each day has just two files: an interactive slide deck (`.html`) and a hands-on notebook (`.ipynb`). The slide deck now contains the full day guide too (objectives, vocabulary, news, activities, numericals, multiple choice with an answer key, and the code challenge), so there is nothing else to open.

Open the slide deck and just press the Next arrow from start to finish. Each deck opens with a "Your plan for today" roadmap and is split into clearly labeled Parts (Get oriented, Learn the basics, Code along, Play the free tools, Test yourself, Go deeper, Wrap up). Every Part begins with a divider that says what to do and how many slides it is, so you always know where you are and what is next.

Each day follows the same friendly pattern:
1. **Watch and click**: open the interactive HTML slides to learn the basics and answer knowledge-check questions.
2. **Code along**: when a slide says so, open the Jupyter notebook (`.ipynb`) and run the examples and challenges.
3. **Play**: use two free, fun, interactive tools to practice for real.
4. **Reflect**: the reflection prompts and answer key are built into the slides.

## Daily plan

| Day | Topic | Files | Free tools |
|-----|-------|-------|-----------|
| 1 | Python and the Linux command line | Day1_slides.html, Day1.ipynb | CodeCombat, OverTheWire Bandit |
| 2 | Security foundations and strong passwords | Day2_slides.html, Day2.ipynb | Google Interland, Security.org password tester |
| 3 | Cryptography: codes and ciphers | Day3_slides.html, Day3.ipynb | dcode.fr, CyberChef |
| 4 | Web security and AI security | Day4_slides.html, Day4.ipynb | CTFLearn, Lakera Gandalf |
| 5 | Capstone: Capture The Flag and OSINT | Day5_slides.html, Day5.ipynb | picoCTF, OSINT Framework |

## Suggested daily schedule (09:00 to 16:30)

| Time | Block | What happens |
|------|-------|--------------|
| 09:00 to 09:15 | Morning kickoff | Daily motivation and cybersecurity news of the day |
| 09:15 to 11:15 | Teaching session I | Core concepts and walkthroughs (use the slides) |
| 11:15 to 11:45 | Morning break | Rest and refreshment |
| 11:45 to 13:45 | Teaching session II | Hands-on code labs and the interactive tools |
| 13:45 to 14:45 | Lunch break | Supervised lunch |
| 14:45 to 16:00 | Group project | Team work on the capstone (Days 1 to 4); final briefings on Day 5 |
| 16:00 to 16:15 | Afternoon break | Short break |
| 16:15 to 16:30 | Recap | Summary and preview of the next day |

## Concept map by day
- Day 1: intro to Python, variables, networking basics, HTTP vs HTTPS, Linux command line.
- Day 2: risk, threat, vulnerability, hacker profiles, the Computer Fraud and Abuse Act (CFAA), the CIA triad, brute force, Distributed Denial of Service (DDoS).
- Day 3: encoding, encryption, hashing, digital signatures, phishing, Multi-Factor Authentication (MFA).
- Day 4: SQL Injection (SQLi), prompt engineering, prompt injection, AI model hallucinations, steganography.
- Day 5: Capture The Flag mechanics, Open-Source Intelligence (OSINT), and careers (CompTIA Security+, Certified Ethical Hacker, degrees).

## The free tools (with definitions)
- **CodeCombat** ( https://codecombat.com/ ): learn Python by guiding a hero through a game.
- **OverTheWire Bandit** ( https://overthewire.org/wargames/bandit/bandit0.html ): learn the Linux terminal one level at a time. SSH = Secure Shell.
- **Google Interland** ( https://beinternetawesome.withgoogle.com/en_us/interland ): gamified lessons on passwords and phishing.
- **Security.org password tester** ( https://www.security.org/how-secure-is-my-password/ ): see estimated crack time as you build a password (use made-up passwords only).
- **dcode.fr** ( https://www.dcode.fr/ ): identify and solve classic ciphers.
- **CyberChef** ( https://cyberchef.org/ ): a drag-and-drop data tool, the cyber Swiss-army knife.
- **CTFLearn** ( https://ctflearn.com/ ): beginner Capture The Flag challenges. CTF = Capture The Flag.
- **Lakera Gandalf** ( https://gandalf.lakera.ai/baseline ): a prompt-injection game for AI security. LLM = Large Language Model.
- **picoCTF** ( https://picoctf.org/ ): Carnegie Mellon University's free CTF training platform with hundreds of practice challenges.
- **OSINT Framework** ( https://osintframework.com/ ): a clickable map of open-source investigation tools. OSINT = Open-Source Intelligence.

## How to run the notebooks
No install is needed if you use a free cloud option:
- **Google Colab**: go to https://colab.research.google.com/ , choose Upload, and pick the day notebook.
- Or run locally: install Python, then `pip install jupyter` and run `jupyter notebook`.

The interactive slides are plain HTML. Open `Interactive_Slides.html` for the full combined course deck, which also has a Day decks menu (top right) linking to each per-day interactive deck. You can also open any `DayN/DayN_slides.html` directly. Use arrow keys to move and click the answers.

## Safety, ethics, and accounts
- Only practice on the sites listed here, which are built for learning.
- Never test attacks on systems you do not own or do not have permission to test.
- Never enter a real password into any tester. Use made-up examples.
- Some sites (CTFLearn, picoCTF) ask for a free account. Students under 13 should sign up with a parent or guardian and follow each site's terms.

## License and reuse
This curriculum is provided for educational use. The external tools are owned by their creators and keep their own terms and licenses. Add a LICENSE file (for example MIT or Creative Commons) before publishing if you plan to share widely.

## Repository structure
```
cyberquest-camp/
  README.md
  LICENSE
  CITATION.cff
  Interactive_Slides.html  (full combined deck + Day decks menu)
  resources/case-studies/  (4 one-page breach studies with sources)
  Day1/  Day1_slides.html  Day1.ipynb
  Day2/  Day2_slides.html  Day2.ipynb
  Day3/  Day3_slides.html  Day3.ipynb
  Day4/  Day4_slides.html  Day4.ipynb
  Day5/  Day5_slides.html  Day5.ipynb
```

Each day folder holds two files: the interactive slide deck (`.html`) and the hands-on notebook (`.ipynb`). The slide deck absorbs the full written guide (objectives, vocabulary, news, activities, numericals, multiple choice with answer key, and the code challenge) and tells you exactly when to open and run the notebook. The notebook includes a Supplementary Practical Lab section merged from the earlier curriculum draft.

## Additional bundled materials
- `Interactive_Slides.html`: the full combined course deck, with a Day decks menu linking to each per-day deck.
- `CITATION.cff`: citation metadata.
