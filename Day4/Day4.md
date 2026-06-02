# Day 4: Web Security and AI Security

**Duration:** about 3 hours
**Goal:** See how websites work, find your first web flags, and learn why AI assistants can be tricked.

---

## Learning objectives
- Break a URL into its parts and explain an HTTP request.
- Describe two common web attacks and how sites defend against them.
- Explain prompt injection and try the Gandalf challenge.

## Vocabulary (acronyms expanded and defined)
- **HTTP = HyperText Transfer Protocol**: the language browsers and servers use to talk.
- **HTTPS = HTTP Secure**: HTTP with encryption so others cannot read your traffic.
- **URL = Uniform Resource Locator**: the address of a page, such as https://example.com.
- **HTML = HyperText Markup Language**: the code that builds web pages.
- **XSS = Cross-Site Scripting**: tricking a site into running attacker code in your browser.
- **SQL = Structured Query Language**: the language used to talk to databases.
- **SQLi = SQL Injection**: smuggling commands into a site that trusts user input.
- **API = Application Programming Interface**: a way for programs to talk to each other.
- **AI = Artificial Intelligence**; **LLM = Large Language Model**: an AI trained on text that follows instructions.

## Picture it
```
  Browser  --- HTTP request --->  Web server  --->  Database
           <-- HTML response ---             <---
  If the server trusts bad input, an attacker can sneak commands through.
```

## In the news (real and verifiable)
The Open Worldwide Application Security Project (OWASP) publishes the OWASP Top 10, the most critical web risks, and injection flaws like SQL injection have appeared on that list for many years. OWASP also released a Top 10 for Large Language Model applications, and prompt injection is listed as the number one risk. In other words, the bugs you learn today are exactly what professionals worry about.

## Activity 1: CTFLearn
Open https://ctflearn.com/
- Make a free account and open the **Easy** challenges in the Web category.
- Use your skills from Day 3: inspect URLs, decode Base64, and look at page source.

## Activity 2: Lakera Gandalf
Open https://gandalf.lakera.ai/baseline
- Your goal: convince the AI named Gandalf to reveal its secret password.
- Each level adds a stronger defense, teaching you how prompt injection works and how it is blocked.

## Numericals and puzzles (do these in the notebook)
1. In the URL https://shop.example.com/search?q=shoes&page=2, what is the value of `page`?
2. Decode the Base64 cookie in the notebook to reveal a flag.
3. Count: how many parts does a full URL have (scheme, host, path, query)?

## Multiple choice (MCQ)
1. HTTPS adds what compared to HTTP?
   a) faster ads  b) encryption and verified identity  c) bigger images
2. SQL injection happens when:
   a) a site trusts user input and runs it as a command  b) the wifi is slow  c) the password is short
3. Prompt injection targets:
   a) databases  b) an AI model that follows instructions in text  c) printers

## Code challenge
Open **Day4.ipynb**: run the URL parser, the input validation simulator, and strengthen the AI guard function.

## Reflection and homework
Name one real defense against SQL injection (hint: parameterized queries) and one reason prompt injection is hard to fully stop.

---
**Answer key.** Numericals: 1) 2, 2) flag{web_basics_unlocked}, 3) four. MCQ: 1-b, 2-a, 3-b.


---

# Extended Lecture Notes

# Day 4: Web Application Vulnerabilities, Blockchain, and AI Safety

## Morning Kickoff: Motivation & News (09:00 AM - 09:15 AM)
* **Case Profile**: The 2017 Equifax Data Breach. Attackers exploited an unpatched vulnerability in an open-source web framework, gaining unauthorized access to the personal data of over 140 million people. This shows why secure input parsing is a critical layer of web defense.

## Teaching Session I: Core Lecture (09:15 AM - 11:15 AM)

### Web Application Deficiencies and SQL Injection (SQLi)
Web applications rely on database backends to store information. If user inputs are concatenated directly into database commands without verification, applications become vulnerable to injection attacks.
* **Structured Query Language (SQL)**: The standard programming language used to manage and manipulate relational databases.
* **SQL Injection (SQLi)**: An attack where malicious SQL statements are inserted into web form input fields. This fools the database into executing unauthorized commands, allowing attackers to bypass authentication or leak database data.



### Blockchain and Cryptocurrency Fundamentals
* **Blockchain**: A decentralized, distributed ledger technology that securely records transactions across a peer-to-peer network.
* **Cryptocurrency**: A digital currency that uses cryptographic principles to secure transactions, control the creation of additional units, and verify the transfer of assets on an immutable ledger.

### Steganography
* **Definition**: The practice of concealing a secret message, file, or image within another ordinary file (such as hiding text inside the pixel data of a digital image). Unlike encryption, which hides the *meaning* of data, steganography hides the *existence* of the communication.

### Artificial Intelligence and Large Language Model (AI/LLM) Security
As applications integrate Large Language Models, new vulnerabilities emerge at the prompt interface layer.
* **Prompt Engineering**: Designing and optimizing text prompts to guide an LLM into generating specific, accurate outputs.
* **Prompt Injection**: An attack where a user crafts malicious input prompts to override an LLM's system instructions, forcing it to ignore safety rules or leak confidential data.
* **Hallucination**: A phenomenon where an AI model confidently generates outputs that are factually incorrect, fabricated, or completely disconnected from reality.

---

## Teaching Session II: Labs & Interactive Tools (11:45 AM - 01:45 PM)

### Practical Interactive Tools for Today
1.  **CTFLearn**: Solve beginner-friendly web application challenges focused on identifying hidden parameters and basic injection vulnerabilities.
2.  **Lakera Gandalf AI Challenge**: Use creative prompt injection techniques to trick an LLM into revealing a secret passport code across increasingly secure protection layers.

---

## Knowledge Evaluation Bank (Embedded Assessments)

### Multiple-Choice Questions (MCQ)
1.  An attacker enters characters like `' OR '1'='1` into a login form, successfully bypassing authentication without a password. What vulnerability did they exploit?
    * A) Steganography
    * B) Structured Query Language Injection (SQLi)
    * C) Multi-Factor Authentication Bypass
    * *Answer Key*: B. Failing to validate inputs allows raw SQL commands to be processed directly by the database backend.

2.  When an AI model generates factually incorrect information but presents it as a confident, accurate statement, this behavior is called what?
    * A) Prompt Injection
    * B) Data Encryption
    * C) Hallucination
    * *Answer Key*: C. Hallucinations occur when an LLM outputs fabricated claims due to statistical training patterns.

### Numerical Exercise
A steganography tool hides secret data bytes inside the least significant bits of an image file. The target uncompressed image has a resolution of $1,000 \times 1,000$ pixels. If each pixel contains 3 color channels (Red, Green, Blue) and the tool can alter 1 bit per channel, calculate the maximum storage capacity of hidden data in bytes.
* *Solution Steps*:
    * $$\text{Total color channels} = 1000 \times 1000 \times 3 = 3,000,000 \text{ channels}$$
    * $$\text{Available space in bits} = 3,000,000 \text{ channels} \times 1 \text{ bit/channel} = 3,000,000 \text{ bits}$$
    * $$\text{Convert to bytes} = \frac{3,000,000 \text{ bits}}{8 \text{ bits/byte}} = 375,000 \text{ bytes (or } 375 \text{ KB)}$$

---

## Recap & Tomorrow's Horizon (04:15 PM - 04:30 PM)
* **Summary**: Today we analyzed SQL Injection web vulnerabilities, explored blockchain structures, and experimented with prompt injection attacks against LLMs.
* **Tomorrow Preview**: We will enter the Capture the Flag team arena and explore professional career paths, certifications, and academic degrees in cybersecurity.
