# Day 5: Capstone - Capture The Flag and OSINT

**Duration:** about 3 hours
**Goal:** Combine every skill, compete on picoCTF, and learn ethical open-source investigation.

---

## Learning objectives
- Solve real CTF challenges on picoCTF using your week of skills.
- Explain what OSINT is and the ethics that govern it.
- Read file metadata and complete the multi-step capstone flag.

## Vocabulary (acronyms expanded and defined)
- **CTF = Capture The Flag**: a security game where you find hidden flags by solving challenges.
- **OSINT = Open-Source Intelligence**: gathering information from public sources only.
- **EXIF = Exchangeable Image File Format**: hidden data inside photos, such as time and sometimes location.
- **GPS = Global Positioning System**: satellite location data.
- **White hat**: an ethical hacker who always has permission.

## Ethics first
OSINT uses only information that is already public, and only on targets you are allowed to investigate: a practice account, a fictional persona, or yourself. Never harass anyone, never try to access private accounts, and always have permission. This rule is what separates a security professional from a criminal.

## Picture it
```
  Skills you built this week  ->  CAPSTONE
  Linux + Python  +  Passwords  +  Crypto  +  Web  +  AI  =  a junior cyber analyst
```

## In the news (real and verifiable)
picoCTF, created by security experts at Carnegie Mellon University, is one of the largest free Capture The Flag programs and has introduced hundreds of thousands of students to cybersecurity. Capture The Flag is also a headline event at major security conferences such as DEF CON, where professional teams compete.

## Activity 1: picoCTF
Open https://picoctf.org/
- Open **picoGym** (practice anytime, free).
- Start with the **General Skills** and **Cryptography** categories. Many challenges use exactly what you learned this week.

## Activity 2: OSINT Framework
Open https://osintframework.com/
- Explore the clickable map of free investigation tools.
- Pick one branch (for example Username or Images) and explain in one line what it helps you find.

## Numericals and puzzles (do these in the notebook)
1. Decode the Base64 flag in the notebook to read a picoCTF flag.
2. Solve the multi-step capstone (XOR then Base64) to recover the final flag.
3. List two pieces of information EXIF data can reveal about a photo.

## Multiple choice (MCQ)
1. OSINT means:
   a) Offline System Internal Network Test  b) Open-Source Intelligence  c) Online Secret Internet Tool
2. Before investigating a target with OSINT you must:
   a) have permission and use only public data  b) hack their email  c) guess their password
3. A picoCTF flag usually looks like:
   a) `picoCTF{...}`  b) `www.example.com`  c) `192.168.0.1`

## Code challenge
Open **Day5.ipynb**: read the metadata example, decode the warm-up flag, and solve the capstone.

## Where to go next
Keep your free picoCTF account, join or start a cyber club, and look into the CyberPatriot program and local CTF events. Free continued practice: picoGym, OverTheWire, and CTFLearn.

## Reflection
Which day was your favorite, and what is one cyber skill you want to keep building?

---
**Answer key.** Numericals: 1) picoCTF{osint_and_crypto_master}, 2) picoCTF{x0r_osint_pro}, 3) any two of: date/time taken, camera model, GPS location. MCQ: 1-b, 2-a, 3-a.


---

# Extended Lecture Notes

# Day 5: Capture the Flag Arenas and Professional Cybersecurity Pathways

## Morning Kickoff: Motivation & News (09:00 AM - 09:15 AM)
* **Case Profile**: The DEF CON Capture the Flag Finals. Every year, global teams compete in continuous attack-and-defense challenges, showcasing how gamified exercises prepare professionals to handle real-world threat incidents.

## Teaching Session I: Core Lecture (09:15 AM - 11:15 AM)

### Capture the Flag (CTF) Competition Frameworks
* **Jeopardy-Style CTF**: A cybersecurity competition format where participants choose challenges from distinct categories (such as Cryptography, Reverse Engineering, Web Exploitation, Forensic Analysis, and Open-Source Intelligence). Solving a challenge reveals a hidden text string called a **flag**, which players submit to a scoreboard to earn points.

### Professional Industry Certifications
* **CompTIA Security+**: A globally recognized, vendor-neutral foundational certification that validates the baseline technical skills required to perform core security functions and pursue an entry-level IT security career.
* **Certified Ethical Hacker (CEH)**: A credential issued by the EC-Council that validates a professional's understanding of how to look for weaknesses and vulnerabilities in target systems using the same tools and techniques as malicious hackers, but in a lawful and ethical manner.

### Higher Education Academic Pathways
* **University Certificate**: Short-term, intensive training programs (typically 6 to 12 months) focused on specific technical skill sets like incident response or digital forensics.
* **Cybersecurity Minor**: A supplementary block of technical courses completed alongside a major degree program (such as Computer Science or Data Analytics) to build baseline security knowledge.
* **Associate Degree (A.S. or A.A.)**: A 2-year undergraduate degree program, often offered by community colleges, that focuses on foundational technical training and hands-on skills for network helpdesk roles.
* **Bachelor Degree (B.S. or B.A.)**: A comprehensive 4-year undergraduate degree program that provides deep theoretical, mathematical, and architectural foundations in computer science, software engineering, and systems security.

---

## Teaching Session II: Labs & Interactive Tools (11:45 AM - 01:45 PM)

### Practical Interactive Tools for Today
1.  **picoCTF**: Compete in Carnegie Mellon's beginner-friendly educational hacking platform to solve interactive problems and harvest flags.
2.  **OSINT Framework**: Navigate an interactive index of open-source intelligence gathering tools to learn how public information is gathered for security footprint analysis.

---

## Knowledge Evaluation Bank (Embedded Assessments)

### Multiple-Choice Questions (MCQ)
1.  Which foundational, vendor-neutral certification is widely considered the industry standard entry point for starting a career as a junior security analyst?
    * A) Certified Ethical Hacker (CEH)
    * B) CompTIA Security+
    * C) Associate Degree
    * *Answer Key*: B. CompTIA Security+ is the standard certification benchmark for entry-level infosec jobs.

2.  In a Jeopardy-style Capture the Flag competition, what is the primary goal of solving a challenge?
    * A) Writing a complete software application patch.
    * B) Finding a unique text string called a flag to submit for points.
    * C) Running a distributed denial of service attack against the scoreboard.
    * *Answer Key*: B. Challenges hide specific flag tokens that validate a successful exploit or analysis.

### Numerical Exercise
A 5-member team competes in a Jeopardy-style CTF challenge lasting exactly 2 hours (120 minutes). The team earns points by solving tasks across three categories:
* 3 Cryptography tasks at 100 points each.
* 2 Web exploit tasks at 250 points each.
* 1 Forensic task worth 400 points.

Calculate the team's total final score and their average point acquisition rate per minute over the course of the competition.
* *Solution Steps*:
    * $$\text{Total Points} = (3 \times 100) + (2 \times 250) + (1 \times 400) = 300 + 500 + 400 = 1,200 \text{ points}$$
    * $$\text{Acquisition Rate} = \frac{1,200 \text{ points}}{120 \text{ minutes}} = 10 \text{ points per minute}$$

---

## Recap & Camp Graduation (04:15 PM - 04:30 PM)
* **Summary**: Today we put our skills to the test in the CTF arena, explored professional certification roadmaps, and mapped out university degree pathways.
* **Congratulations**: You have completed all curriculum modules for the Cyber Squad Summer Camp! Keep learning, practice ethically, and help defend the digital frontier.


---

# Capstone Project Handout

# Capstone Group Project Handout & Case Analysis Matrix

Every afternoon from **02:45 PM to 04:00 PM** (1 hour 15 minutes), teams of 2 to 3 students work on a deep-dive analysis of a real-world cybersecurity breach. On Day 5, teams deliver a 10-minute presentation detailing their chosen case study.

---

## Daily Project Milestones

* **Day 1: Team Assembly and Case Selection** - Form teams, choose a case study, and outline a project scope summary.
* **Day 2: Threat and Vulnerability Analysis** - Identify the specific assets targeted, the vulnerabilities exploited, and the impact on the **CIA Triad**.
* **Day 3: Defensive Architecture Redesign** - Propose technical security controls (such as firewalls, encryption, or Multi-Factor Authentication) to prevent similar breaches.
* **Day 4: Slide Creation and Presentation Dry-Run** - Finalize an 8-slide presentation deck and practice timing and speaker transitions.
* **Day 5: Final Presentations & Briefings** - Deliver a 10-minute presentation to the camp instructors and answer technical questions from peers.

---

## Real-World Case Study Options

### 1. Change Healthcare Ransomware Attack (February 2024)
* **Summary**: Threat actors exploited a remote entry portal that lacked multi-factor authentication, deploying ransomware that disrupted health payment processing systems nationwide.
* **Core Themes**: Critical infrastructure availability, ransomware operations, and identity protection controls.

### 2. Salt Typhoon Cyber Espionage Campaign (2024-2025)
* **Summary**: A sophisticated state-sponsored threat group compromised access points deep within national telecommunications providers, targeting core systems used for lawful interception requests.
* **Core Themes**: Advanced Persistent Threats (APTs), national security espionage, and infrastructure hardening.

### 3. MGM Resorts Vishing Breach (September 2023)
* **Summary**: Attackers used voice phishing (vishing) to trick an IT support helpdesk operator into resetting login credentials for a high-privilege employee, leading to massive operational disruptions.
* **Core Themes**: Social engineering vulnerabilities, helpdesk authentication policies, and user awareness training.

---

## Evaluation Rubric (100-Point Scale)

* **Technical Accuracy (25 Points)**: Correct use of security terminology, vulnerability frameworks, and incident details.
* **Threat Mapping Depth (25 Points)**: Clear explanation of how the vulnerability was exploited and its impact on the CIA Triad.
* **Remediation and Defense Design (20 Points)**: Feasibility and technical logic of the proposed security controls.
* **Presentation Quality & Teamwork (20 Points)**: Equal participation among team members, clear communication, and slide professional design.
* **Q&A Engagement (10 Points)**: Accuracy and clarity when answering questions from instructors and peers during the post-presentation review.
