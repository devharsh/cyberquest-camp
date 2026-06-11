import re, sys
sys.path.insert(0, '/sessions/optimistic-dazzling-cerf/mnt/outputs/cyberquest-pdf')
from extract import html_to_tex, extract_s_calls, get_prop, esc, strip_tags, reset_counters

# ── Paths ──────────────────────────────────────────────────────────────────
BASE = '/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity'
MAIN = '/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity/Bowie/cyberquest-camp/Interactive_Slides.html'

DAY_TITLES = {
    1: ("Python and the Linux Terminal",
        "Day 1 equips students with the foundational technical skills needed throughout the week: "
        "basic Python programming (variables, loops, functions, file I/O), navigation of the Linux "
        "command line, the OSI seven-layer model, IPv4 addressing, and URL anatomy."),
    2: ("Threats, Risk, and the CIA Triad",
        "Day 2 covers the strategic side of security: the CIA and DAD triads, the Parkerian Hexad, "
        "threat actor taxonomy (script kiddies through nation-state APTs), quantitative risk analysis "
        "using ALE, password entropy, and the legal framework of the Computer Fraud and Abuse Act."),
    3: ("Cryptography and TLS",
        "Day 3 explores how mathematics protects information: classical ciphers and frequency analysis, "
        "the one-time pad, AES block cipher modes (ECB vs CBC), hash functions and the birthday paradox, "
        "RSA public-key cryptography worked numerically, digital signatures, and the TLS handshake."),
    4: ("Web Security and AI Attacks",
        "Day 4 examines how web applications are attacked and defended: raw HTTP, the OWASP Top 10, "
        "SQL injection, cross-site scripting, session hijacking, CSRF, and emerging AI attack vectors "
        "including prompt injection, data poisoning, and deepfake social engineering."),
    5: ("CTF Competitions and Career Roadmap",
        "Day 5 ties the week together with Capture the Flag competitions: CTF category taxonomy, "
        "OSINT methodology, Google dorks, EXIF metadata analysis, cryptographic CTF demos, "
        "and a certification and career roadmap mapping skills to professional roles."),
}

# ── Read main deck ─────────────────────────────────────────────────────────
try:
    with open(MAIN) as f:
        main_content = f.read()
    main_script = re.search(r'<script[^>]*>(.*?)</script>', main_content, re.DOTALL).group(1)
    main_slides = extract_s_calls(main_script)
    print(f"Main deck: {len(main_slides)} slides", file=sys.stderr)
except Exception as e:
    print(f"Could not read main deck: {e}", file=sys.stderr)
    main_slides = []

# ── Read day decks ─────────────────────────────────────────────────────────
day_slides = {}
for day in [1,2,3,4,5]:
    path = f'{BASE}/Bowie/cyberquest-camp/Day{day}/Day{day}_slides.html'
    try:
        with open(path) as f:
            c = f.read()
    except FileNotFoundError:
        path = (f'/sessions/optimistic-dazzling-cerf/mnt/Users/devharsh/Documents'
                f'/cyberquest-camp/Day{day}/Day{day}_slides.html')
        with open(path) as f:
            c = f.read()
    chunks = []
    for m in re.finditer(
            r"<div class='slide'>(.*?)(?=<div class='slide'>|</div>\s*<div class=\"progress\">|$)",
            c, re.DOTALL):
        inner = m.group(1).strip()
        text  = re.sub(r'<[^>]+>', '', inner).strip()
        if len(text) > 4:
            chunks.append(inner)
    day_slides[day] = chunks
    print(f"Day {day}: {len(chunks)} slides", file=sys.stderr)

# ── Main deck -> chapter sections ──────────────────────────────────────────
def main_deck_section(section_name, slides):
    lines = []
    for obj in slides:
        sec_m = re.search(r"sec\s*:\s*['\"]([^'\"]+)['\"]", obj)
        if not sec_m or sec_m.group(1) != section_name:
            continue
        html       = get_prop(obj, 'html')
        title      = get_prop(obj, 'title') or get_prop(obj, 'kick') or ''
        slide_type = get_prop(obj, 't') or ''

        if slide_type in ('cover', 'divider', 'toc'):
            tex = html_to_tex(html)
            if tex:
                lines.append(tex + '\n')
        else:
            if title:
                lines.append('\\subsubsection*{' + esc(strip_tags(title)) + '}\n')
            tex = html_to_tex(html)
            if tex:
                lines.append(tex + '\n')
        lines.append('\n')
    return '\n'.join(lines)

# ── Day deck -> section ────────────────────────────────────────────────────
def day_deck_section(chunks):
    lines = []
    for chunk in chunks:
        tex = html_to_tex(chunk)
        if tex.strip():
            lines.append(tex)
            lines.append('\n\\medskip\n')
    return '\n'.join(lines)

# ── Assemble LaTeX ─────────────────────────────────────────────────────────
PREAMBLE = r"""\documentclass[12pt,openany]{book}
\usepackage{cmap}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in,top=1.1in,bottom=1.1in]{geometry}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{amssymb}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{longtable}
\usepackage{listings}
\usepackage{upquote}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{tocloft}
\usepackage{fancyhdr}
\PassOptionsToPackage{hyphens}{url}
\usepackage{hyperref}
\usepackage{url}
\usepackage{float}
\usepackage{graphicx}
\graphicspath{{/sessions/optimistic-dazzling-cerf/mnt/Cybersecurity/Bowie/cyberquest-camp/book/figs/}}
\usepackage{tcolorbox}
\usepackage{setspace}
\usepackage{accsupp}

% Widow and orphan line suppression
\widowpenalty=10000
\clubpenalty=10000
\setlength{\emergencystretch}{3em}

\setlength{\headheight}{14.5pt}

\definecolor{accent}{HTML}{2563EB}
\definecolor{accent2}{HTML}{7C3AED}
\definecolor{accentlt}{HTML}{DBEAFE}
\definecolor{codebg}{HTML}{F1F5FF}
\definecolor{gray}{HTML}{5A6B8C}
\definecolor{coverdark}{HTML}{1E3A5F}
\definecolor{covermid}{HTML}{2563EB}
\definecolor{coverpurp}{HTML}{7C3AED}

\hypersetup{
  unicode=true, colorlinks=true, linkcolor=accent, urlcolor=accent, citecolor=accent2,
  pdfcreator={pdfLaTeX}, pdfproducer={TeX Live 2022},
  pdfdisplaydoctitle=true,
  pdflang={en-US}, pdftitle={CyberQuest Summer Camp 2026},
  pdfauthor={Devharsh Trivedi},
  pdfsubject={Cybersecurity Education},
  pdfkeywords={cybersecurity, CTF, cryptography, web security, AI security, Python}
}

\lstset{
  basicstyle=\ttfamily\small,
  backgroundcolor=\color{codebg},
  frame=single, framerule=0.4pt, rulecolor=\color{accent!40},
  breaklines=true, breakatwhitespace=true,
  keepspaces=true, columns=flexible,
  showstringspaces=false,
  xleftmargin=6pt, xrightmargin=6pt,
  aboveskip=8pt, belowskip=8pt
}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{accent}}
  {\chaptertitlename\ \thechapter}{18pt}{\Huge}
\titleformat{\section}{\normalfont\Large\bfseries\color{accent2}}{}{0pt}{}
\titleformat{\subsection}{\normalfont\large\bfseries\color{accent}}{}{0pt}{}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries}{}{0pt}{}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\textit{\leftmark}}
\fancyhead[LO]{\textit{\rightmark}}
\renewcommand{\headrulewidth}{0.4pt}

\setlist[itemize]{noitemsep, topsep=4pt}
\setlist[enumerate]{noitemsep, topsep=4pt}
\onehalfspacing
"""

# ── TikZ cover page (1 page, colorful, ORCID, version 1.1.0, no email/room) ─
TITLE_PAGE = r"""
\begin{titlepage}
\begin{tikzpicture}[remember picture, overlay]
  % Deep navy background fills the entire page
  \fill[coverdark] (current page.north west) rectangle (current page.south east);
  % Blue highlight band across the middle third
  \fill[covermid, opacity=0.80]
    ([yshift=-0.34\paperheight]current page.north west)
    rectangle
    ([yshift=-0.63\paperheight]current page.north east);
  % Large decorative circle -- bottom right
  \fill[coverpurp, opacity=0.22]
    ([xshift=0.74\paperwidth, yshift=0.14\paperheight]current page.south west)
    circle [radius=0.40\paperwidth];
  % Smaller accent circle -- top left
  \fill[covermid, opacity=0.18]
    ([xshift=-0.05\paperwidth, yshift=-0.07\paperheight]current page.north west)
    circle [radius=0.26\paperwidth];
  % Thin top and bottom edge stripes
  \fill[white, opacity=0.07]
    ([yshift=-0.33\paperheight]current page.north west)
    rectangle
    ([yshift=-0.36\paperheight]current page.north east);
  \fill[white, opacity=0.07]
    ([yshift=0.08\paperheight]current page.south west)
    rectangle
    ([yshift=0.05\paperheight]current page.south east);
\end{tikzpicture}%
%
\color{white}%
\centering
\vspace{1.2cm}

{\small\textsc{Bowie State University \textbullet{} Department of Computer Science}}\\[1.0cm]

{\fontsize{40}{44}\selectfont\bfseries CyberQuest}\\[4pt]
{\fontsize{24}{28}\selectfont\bfseries Summer Camp}\\[0.5cm]
{\large\color{accentlt} 2026 Curriculum Book}\\[0.55cm]

{\color{white!45!covermid}\rule{0.55\linewidth}{0.5pt}}\\[0.55cm]

{\normalsize
  A five-day cybersecurity course for middle and high school students.\\[3pt]
  Hands-on Python, ethical hacking, cryptography, web security, and AI attacks.
}\\[1.0cm]

{\large\bfseries Devharsh Trivedi, Ph.D., CISSP}\\[5pt]
{\small
  Department of Computer Science, Bowie State University\\[2pt]
  Washington D.C., 20003\\[4pt]
  ORCID: \href{https://orcid.org/0000-0001-6374-7249}{\textcolor{accentlt}{0000-0001-6374-7249}}
}\\[0.85cm]

{\small
  \href{https://camp.com.puter.tips}{\textcolor{accentlt}{camp.com.puter.tips}}
  \quad\textbullet\quad
  \href{https://github.com/devharsh/cyberquest-camp}{\textcolor{accentlt}{github.com/devharsh/cyberquest-camp}}
}\\[0.65cm]

{\small Version 1.1.0 \quad\textbullet\quad \today}
\end{titlepage}
"""

DEDICATION = r"""
\frontmatter
\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
This curriculum book is the companion document to the CyberQuest Summer Camp interactive
slide decks, available at \href{https://camp.com.puter.tips}{\texttt{camp.com.puter.tips}}. It is structured in two parts:

\textbf{Part~I} reproduces the main course deck (\textit{Interactive Slides}), which is the
primary teaching vehicle presented to students during each day's opening session.
Each of its six chapters corresponds to a thematic section of the week.

\textbf{Part~II} contains the five daily companion decks. These slides are used during
teaching sessions, labs, and review periods. They expand on the main deck with worked
examples, Python code, mathematical derivations, and knowledge checks drawn from
\textit{Introduction to Cybersecurity} (Trivedi), cited by chapter and section throughout.

\vspace{1em}
\noindent\textbf{License.} This work is released under CC~BY~4.0. You may reproduce,
adapt, and redistribute it with attribution.

\vspace{1em}
\noindent\textbf{Citation.} See the \texttt{CITATION.cff} file in the repository or
the Zenodo record for the preferred citation format.
"""

# ── Further Resources appendix ─────────────────────────────────────────────
FURTHER_RESOURCES = r"""
\chapter*{Further Resources}
\addcontentsline{toc}{chapter}{Further Resources}
\markboth{Further Resources}{Further Resources}

The following free, browser-based platforms are referenced throughout the camp slides.
Students are encouraged to explore them during and after the program.

\section*{Capture the Flag and Wargames}

\begin{description}[leftmargin=0pt, labelindent=0pt, style=nextline]

\item[\href{https://picoctf.org/}{picoctf.org}]
PicoCTF is a free, beginner-friendly CTF competition hosted by Carnegie Mellon University.
It features hundreds of challenges across forensics, cryptography, web exploitation,
reverse engineering, and binary exploitation, organized by difficulty level.

\item[\href{https://ctflearn.com/}{ctflearn.com}]
CTFlearn is a community-driven practice platform with user-submitted challenges.
Good for self-paced skill building after completing Day 5 of the camp.

\item[\href{https://overthewire.org/wargames/bandit/bandit0.html}{overthewire.org --- Bandit}]
OverTheWire Bandit is a wargame that teaches Linux command-line skills through
progressively harder puzzles accessed over SSH --- a direct extension of Day 1 content.

\end{description}

\section*{Cryptography and Encoding Tools}

\begin{description}[leftmargin=0pt, labelindent=0pt, style=nextline]

\item[\href{https://cyberchef.org/}{cyberchef.org}]
CyberChef is the GCHQ \textquotedblleft Cyber Swiss Army Knife\textquotedblright{} ---
a browser-based tool for encoding, decoding, encrypting, and analyzing data.
Used in Day 3 for Base64, hex, and XOR exercises.

\item[\href{https://www.dcode.fr/}{dcode.fr}]
dCode provides solvers for hundreds of classical and modern ciphers, including Caesar,
Vigenere, and frequency-analysis tools used in Day 3 CTF challenges.

\end{description}

\section*{OSINT and Reconnaissance}

\begin{description}[leftmargin=0pt, labelindent=0pt, style=nextline]

\item[\href{https://osintframework.com/}{osintframework.com}]
OSINT Framework maps open-source intelligence techniques and tools to a visual tree.
Referenced in Day 5 when covering Google dorks and metadata-based reconnaissance.

\end{description}

\section*{Password and Security Awareness}

\begin{description}[leftmargin=0pt, labelindent=0pt, style=nextline]

\item[\href{https://www.security.org/how-secure-is-my-password/}{security.org --- How Secure Is My Password?}]
An interactive password strength estimator that demonstrates entropy concepts from
Day 2 in real time. Students can test how long different password patterns take to crack.

\end{description}

\section*{AI Safety and Prompt Injection}

\begin{description}[leftmargin=0pt, labelindent=0pt, style=nextline]

\item[\href{https://gandalf.lakera.ai/baseline}{gandalf.lakera.ai/baseline}]
Gandalf is an interactive prompt-injection challenge where students try to extract
a secret password from an LLM with progressively stronger guardrails. Directly
reinforces the AI attack content in Day 4.

\end{description}

\section*{Interactive Learning Games}

\begin{description}[leftmargin=0pt, labelindent=0pt, style=nextline]

\item[\href{https://beinternetawesome.withgoogle.com/en_us/interland}{beinternetawesome.withgoogle.com --- Interland}]
Google's Interland teaches phishing recognition, password safety, and online privacy
through four mini-games. Suitable for Day 1 and Day 2 warm-up activities.

\item[\href{https://codecombat.com/}{codecombat.com}]
CodeCombat teaches Python through a role-playing game where students write code to
control a hero. A natural extension of the Day 1 Python primer for students who want
additional coding practice.

\end{description}
"""

def build():
    reset_counters()   # reset figure/table counters for a clean build
    out = [PREAMBLE, r'\begin{document}', TITLE_PAGE, DEDICATION,
           r'\clearpage',
           r'\tableofcontents',
           r'\clearpage',
           r'\listoffigures',
           r'\clearpage',
           r'\listoftables',
           r'\mainmatter']

    # PART I - Main Deck
    out.append(r'\part{Main Course Deck}')
    out.append(r'\chapter{Welcome and Course Overview}')
    out.append(main_deck_section('Welcome', main_slides))

    for day in [1,2,3,4,5]:
        title, _ = DAY_TITLES[day]
        out.append(f'\\chapter{{Day {day}: {esc(title)}}}')
        out.append(main_deck_section(f'Day {day}', main_slides))

    # PART II - Daily Companion Decks
    out.append(r'\part{Daily Companion Decks}')
    for day in [1,2,3,4,5]:
        title, intro = DAY_TITLES[day]
        out.append(f'\\chapter{{Day {day} Companion: {esc(title)}}}')
        out.append(esc(intro) + '\n')
        out.append(day_deck_section(day_slides[day]))

    # Appendix: Further Resources
    out.append(FURTHER_RESOURCES)

    out.append(r'\end{document}')
    tex = '\n'.join(out)

    # ── Targeted content corrections (post-processing on generated tex) ───────

    # Remove author contact block that leaks from the main-deck cover slide
    # (the slide contains Room 221 and the old address; we strip the whole line)
    tex = re.sub(
        r'Devharsh Trivedi, Ph\.D\., CISSP - Department of Computer Science,'
        r' Bowie State UniversityComputer Science Building, Room 221[^\n]*\n',
        '', tex
    )
    # Belt-and-suspenders: remove any stray Room 221 reference
    tex = re.sub(r'[^\n]*Room 221[^\n]*\n', '', tex)
    # Remove any stray devharsh email that leaked from slide content
    tex = re.sub(r'[^\n]*devharsh\.1592@gmail\.com[^\n]*\n', '', tex)

    # Break long monospace strings that overflow margins
    tex = tex.replace(
        r'\texttt{Interactive\_Slides.html}',
        r'\texttt{Interactive\allowbreak\_Slides.html}'
    )
    tex = tex.replace(
        r'\texttt{secrets.token\_bytes()}',
        r'\texttt{secrets.\allowbreak token\_bytes()}'
    )
    tex = tex.replace(
        r'picoCTF\{osint\_and\_crypto\_master\}',
        r'picoCTF\{\allowbreak osint\_and\_crypto\_master\}'
    )
    tex = tex.replace(
        r'picoCTF\{x0r\_osint\_pro\}',
        r'picoCTF\{\allowbreak x0r\_osint\_pro\}'
    )

    # HTTPS: expand to full name on first occurrence only
    tex = tex.replace(
        r'HTTPS = HTTP Secure',
        r'HTTPS = HyperText Transfer Protocol Secure',
        1
    )

    # Day 3 N/L notation: insert clarifying parenthetical where first defined
    # The tex will have: L=26\}) ... N=5
    # We add: "where L denotes alphabet size and N denotes password length"
    tex = re.sub(
        r'(L=26\\\})\)',
        r'\1) --- here $L$ is the alphabet size and $N$ is the password length',
        tex,
        count=1
    )

    return tex

tex = build()
with open('/sessions/optimistic-dazzling-cerf/mnt/outputs/cyberquest-pdf/main.tex', 'w') as f:
    f.write(tex)
print(f"Wrote main.tex ({len(tex)} bytes, ~{len(tex.split(chr(10)))} lines)", file=sys.stderr)
