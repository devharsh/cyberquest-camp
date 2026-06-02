# Day 2: Cyber Foundations and the Math of Passwords

**Duration:** about 3 hours
**Goal:** Understand the core goals of security and prove with math why long passwords win.

---

## Learning objectives
- State the three goals of security (the CIA triad).
- Explain why password length beats complexity.
- Use a password tester responsibly and estimate crack time.

## Vocabulary (acronyms expanded and defined)
- **CIA triad = Confidentiality, Integrity, Availability**: keep data secret, keep it correct, keep it reachable.
- **MFA = Multi-Factor Authentication**: proving who you are with two or more things (a password plus a phone code).
- **2FA = Two-Factor Authentication**: MFA with exactly two factors.
- **PIN = Personal Identification Number**: a short numeric code.
- **Phishing**: a fake message that tricks you into giving up a password.
- **Keyspace**: the total number of possible passwords; bigger is harder to guess.
- **Brute force**: trying every possible password until one works.

## Picture it
```
  Something you KNOW (password)
  Something you HAVE (phone, key)   ->  combine two = Multi-Factor Authentication
  Something you ARE  (fingerprint)
```

## In the news (real and verifiable)
Every year, password managers such as NordPass publish a list of the most common passwords, and weak choices like 123456 and password appear at the top again and again. These take well under a second for a computer to guess. The lesson security pros repeat: length and unpredictability matter far more than swapping an a for an @.

## Activity 1: Google Interland
Open https://beinternetawesome.withgoogle.com/en_us/interland
- Play **Tower of Treasure** to practice building strong passwords.
- Play **Reality River** to spot phishing and scams.

## Activity 2: Security.org password tester (math you can see)
Open https://www.security.org/how-secure-is-my-password/
- Type made-up passwords only. Never type a real password you actually use.
- Add one character at a time and watch the estimated crack time jump. This is the keyspace growing.

## Numericals (do these in the notebook)
1. How many 4-digit PINs are possible (digits 0 to 9)?
2. An 8-character lowercase password: how many combinations (26 to the power 8)?
3. If an attacker tries 1 billion guesses per second, roughly how long to try all 8-character all-symbol passwords? (The notebook computes this.)

## Multiple choice (MCQ)
1. The C in the CIA triad stands for:
   a) Control  b) Confidentiality  c) Computer
2. Which is stronger?
   a) `P@ss1!`  b) `purple-kite-river-stone`
3. MFA improves security because:
   a) it makes passwords shorter  b) an attacker needs more than just your password  c) it hides your screen

## Code challenge
Open **Day2.ipynb** and finish the password strength meter and the passphrase keyspace calculation.

## Reflection and homework
Turn on MFA on one of your own accounts with a parent or guardian. Write one sentence on why a passphrase of four random words can beat a short symbol password.

---
**Answer key.** Numericals: 1) 10,000 PINs, 2) 208,827,064,576 (about 2.09 x 10^11), 3) see notebook (a few hours, which is why 8 chars is no longer safe). MCQ: 1-b, 2-b, 3-b.


---

# Extended Lecture Notes

# Day 2: Risk Frameworks, Threat Matrices, and Legal Controls

## Morning Kickoff: Motivation & News (09:00 AM - 09:15 AM)
* **Case Profile**: The 2024 Change Healthcare Ransomware Attack. Cybercriminals exploited an unauthenticated entry portal, halting health payment infrastructure nationwide. This underscores why missing security controls present catastrophic operational risks.

## Teaching Session I: Core Lecture (09:15 AM - 11:15 AM)

### Cybersecurity Governance Terminology
* **Asset**: Any high-value resource, hardware appliance, or data segment owned by an organization (e.g., patient health records database records).
* **Threat**: Any potential event or entity capable of causing harm or unauthorized access to an asset (e.g., a ransomware gang).
* **Vulnerability**: A flaw or operational weakness in system architecture, software code, or physical access controls that can be exploited by an attacker.
* **Risk**: The mathematical probability that a specific threat will exploit a vulnerability, multiplied by the operational impact or financial loss ($Risk = Probability \times Impact$).
* **Security Assessment**: A comprehensive technical evaluation of an infrastructure's defensive posture to identify vulnerabilities before attackers do.

### The Threat Actor Spectrum
* **White Hat Hackers**: Security professionals who perform penetration testing with legal authorization to help defend networks.
* **Black Hat Hackers**: Malicious cybercriminals who breach infrastructure unlawfully for financial gain or disruption.
* **Gray Hat Hackers**: Individuals who find vulnerabilities without authorization but report them without malicious intent, operating outside strict legal boundaries.
* **Script Kiddies**: Amateurs who launch pre-made exploit tools and scripts without understanding their underlying code mechanics.
* **Hacktivists**: Politically or ideologically motivated actors who deface web systems or leak files to draw attention to a social cause.

### Legal Frameworks and Core Governance Matrix
* **Ethical Hacking Rules**: Requires **explicit written permission**, a clearly defined **scope** of testing targets, and adhering to **responsible disclosure** policies by reporting vulnerabilities privately to owners.
* **Computer Fraud and Abuse Act (CFAA)**: The primary United States federal computer crime statute. It criminalizes accessing a protected computer system without authorization or exceeding authorized access bounds.

### The CIA Security Triad Core Properties
* **Confidentiality**: Ensuring data is accessible only to authorized entities. Attacks include **Brute-Force Password Cracking**.
* **Integrity**: Safeguarding data from unauthorized modification or tampering.
* **Availability**: Ensuring information networks are reliably accessible to users. Attacks include **Denial-of-Service (DoS)** and **Distributed Denial-of-Service (DDoS)** attacks, which flood bandwidth to crash systems.



---

## Teaching Session II: Labs & Interactive Tools (11:45 AM - 01:45 PM)

### Practical Interactive Tools for Today
1.  **Google Interland**: Complete gamified interactive paths focused on evaluating threat links, phishing recognition, and risk management parameters.
2.  **Security.org Password Tool**: Input testing phrases to see how expanding character lengths affects brute-force cracking time metrics.

---

## Knowledge Evaluation Bank (Embedded Assessments)

### Multiple-Choice Questions (MCQ)
1.  A hacker leaks corporate database documents to protest a company's environmental policy. This actor belongs to which category?
    * A) Script Kiddie
    * B) Hacktivist
    * C) White Hat Hacker
    * *Answer Key*: B. Hacktivists use technical exploits to drive ideological or political messages.

2.  An attacker floods an e-commerce platform with 500,000 automated requests per second, causing the web servers to crash. Which component of the CIA Triad is compromised?
    * A) Confidentiality
    * B) Integrity
    * C) Availability
    * *Answer Key*: C. Flooding infrastructure with requests causes a denial of service, violating system Availability.

### Numerical Exercise
An executive calculates that a corporate server holding customer records faces an asset evaluation cost of \$200,000. Risk analysts determine a threat group has an annual rate of occurrence matching 0.5 (once every two years). If an exploit occurs, the exposure factor damage is 40% of the total asset value. Calculate the Single Loss Expectancy (SLE) and Annualized Loss Expectancy (ALE) values using these metrics.
* *Solution Steps*:
    * $$\text{SLE} = \text{Asset Value} \times \text{Exposure Factor} = \$200,000 \times 0.40 = \$80,000$$
    * $$\text{ALE} = \text{SLE} \times \text{Annual Rate of Occurrence} = \$80,000 \times 0.5 = \$40,000 \text{ loss per year}$$

---

## Recap & Tomorrow's Horizon (04:15 PM - 04:30 PM)
* **Summary**: Today we broke down risk, mapped threat profiles, analyzed the CFAA, and explored how brute-force and DDoS attacks disrupt the CIA Triad.
* **Tomorrow Preview**: We will explore defensive mechanics, covering encoding, hashing, encryption, and strategies to resist social engineering.
