import re, sys

# ---------------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------------

def esc(s):
    """Escape LaTeX special characters in plain text."""
    return (s.replace('\\', r'\textbackslash{}')
             .replace('#', r'\#').replace('$', r'\$').replace('%', r'\%')
             .replace('&', r'\&').replace('_', r'\_').replace('^', r'\^{}')
             .replace('{', r'\{').replace('}', r'\}')
             .replace('<', r'\textless{}').replace('>', r'\textgreater{}')
             # Unicode chars that must be in ASCII for esc() callers
             .replace('✓', r'\checkmark{}')
             .replace('✗', r'$\times$')
             .replace('≡', r'$\equiv$')
             .replace('≈', r'$\approx$')
             .replace('≤', r'$\leq$')
             .replace('≥', r'$\geq$')
             .replace('≠', r'$\neq$')
             .replace('→', r'$\rightarrow$')
             .replace('←', r'$\leftarrow$')
             .replace('×', r'$\times$')
             .replace('•', r'\textbullet{}')
             .replace('’', r"'").replace('‘', r"'")
             .replace('“', r"``").replace('”', r"''")
             .replace('–', '--').replace('—', '---'))

def strip_tags(html):
    return re.sub(r'<(?:[a-zA-Z/!?][^>]*|)>', '', html)

def unescape(s):
    return (s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
             .replace('&nbsp;', ' ').replace('&#39;', "'").replace('&quot;', '"')
             .replace('&mdash;', '---').replace('&ndash;', '--'))

def clean_js(html):
    # JS template literal: \$ is a literal dollar (not a template placeholder start)
    html = html.replace('\\$', '$')
    # Stray backslash before an HTML tag (e.g. \<span> used as $ prefix in slide sources)
    html = re.sub(r'\\(</?[a-zA-Z])', r'\1', html)
    # Remove ${...} template expressions (8 passes handles nesting up to depth 8)
    for _ in range(8):
        html = re.sub(r'\$\{[^{}]*\}', '', html)
    # Remove lines that are just JS punctuation
    html = re.sub(r'(?m)^[ \t]*[\'\")(}{]+[ \t]*$', '', html)
    return html

# ---------------------------------------------------------------------------
# Pre-escaper: apply esc(unescape()) to text nodes only, leaving tags intact
# ---------------------------------------------------------------------------

def _esc_text_nodes(html):
    """Escape LaTeX special chars in all text nodes (between HTML tags)."""
    result = []
    pos = 0
    for m in re.finditer(r'<(?:[a-zA-Z/!?][^>]*|)>', html):
        if m.start() > pos:
            result.append(esc(unescape(html[pos:m.start()])))
        result.append(m.group(0))   # tag kept verbatim
        pos = m.end()
    if pos < len(html):
        result.append(esc(unescape(html[pos:])))
    return ''.join(result)

# ---------------------------------------------------------------------------
# Main converter
# ---------------------------------------------------------------------------

def html_to_tex(html):
    if not html or not html.strip():
        return ''
    html = clean_js(html)

    html = re.sub(r'<button[^>]*>.*?</button>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div[^>]*class=["\']feedback[^>]*>.*?</div>', '', html, flags=re.DOTALL)

    SVG_REPL = ('\n' + r'\begin{center}\textit{[Interactive diagram'
                r' --- see \url{https://camp.com.puter.tips}]}\end{center}' + '\n')
    html = re.sub(r'<svg[^>]*>.*?</svg>', lambda _: SVG_REPL, html, flags=re.DOTALL)

    # Save code blocks before escaping text nodes (verbatim content must stay raw)
    BOX_ASCII = str.maketrans({
        '\u2500': '-',  '\u2501': '-',  '\u2502': '|',  '\u2503': '|',
        '\u250C': '+',  '\u2510': '+',  '\u2514': '+',  '\u2518': '+',
        '\u251C': '|',  '\u2524': '|',  '\u252C': '+',  '\u2534': '+',
        '\u253C': '+',  '\u2550': '-',  '\u2551': '|',  '\u2560': '+',
        '\u2563': '+',  '\u2566': '+',  '\u2569': '+',  '\u256C': '+',
        '\u2574': '-',  '\u2575': '|',  '\u2576': '-',  '\u2577': '|',
        '\u2578': '-',  '\u2579': '|',  '\u257A': '-',  '\u257B': '|',
    })

    code_blocks = []
    def save_code(m):
        raw = unescape(m.group(1) if m.lastindex else m.group(0))
        raw = raw.translate(BOX_ASCII)
        ph = 'CODEBLOCK{}ENDCODE'.format(len(code_blocks))
        code_blocks.append(raw)
        return ph
    html = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', save_code, html, flags=re.DOTALL)
    html = re.sub(r'<pre[^>]*>(.*?)</pre>', save_code, html, flags=re.DOTALL)

    # PRE-ESCAPE: all text nodes are now LaTeX-safe
    html = _esc_text_nodes(html)

    # From here: text content already escaped; handlers just use strip_tags()

    # Inline code — content is pre-escaped, just wrap
    html = re.sub(r'<code>(.*?)</code>',
        lambda m: r'\texttt{' + strip_tags(m.group(1)) + '}',
        html, flags=re.DOTALL)

    # Headings
    def _sec(cmd):
        return lambda m: '\n' + cmd + '{' + strip_tags(m.group(1)) + '}\n'
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', _sec(r'\section*'),    html, flags=re.DOTALL)
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', _sec(r'\subsection*'), html, flags=re.DOTALL)
    html = re.sub(r'<h3[^>]*>(.*?)</h3>', _sec(r'\subsubsection*'), html, flags=re.DOTALL)

    # Special <p class=...> variants
    html = re.sub(r"<p[^>]*class=['\"]partbadge['\"][^>]*>(.*?)</p>",
        lambda m: '\n' + r'\vspace{4pt}\noindent\textsc{' + strip_tags(m.group(1)) + '}\n\n',
        html, flags=re.DOTALL)
    html = re.sub(r'<p[^>]*class=["\']muted["\'][^>]*>(.*?)</p>',
        lambda m: r'{\small\itshape\color{gray}' + strip_tags(m.group(1)) + '}\n\n',
        html, flags=re.DOTALL)

    # Inline formatting
    html = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>',
        lambda m: r'\textbf{' + strip_tags(m.group(1)) + '}', html, flags=re.DOTALL)
    html = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>',
        lambda m: r'\textit{' + strip_tags(m.group(1)) + '}', html, flags=re.DOTALL)

    # Tables
    def convert_table(m):
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', m.group(1), re.DOTALL)
        if not rows:
            return ''
        tex_rows, ncols = [], 0
        for i, row in enumerate(rows):
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
            ct = [strip_tags(c).strip() for c in cells]
            if not ct:
                continue
            if i == 0:
                ncols = len(ct)
                tex_rows.append(r'\textbf{' + r'} & \textbf{'.join(ct) + r'} \\ \midrule')
            else:
                tex_rows.append(' & '.join(ct) + r' \\')
        if not ncols:
            return ''
        w = str(round(13.0 / ncols, 1))
        spec = ('p{' + w + 'cm}') * ncols
        return ('\n' + r'\begin{center}\small\begin{tabular}{' + spec + r'}\toprule' + '\n'
                + '\n'.join(tex_rows) + '\n'
                + r'\bottomrule\end{tabular}\end{center}' + '\n')
    html = re.sub(r'<table[^>]*>(.*?)</table>', convert_table, html, flags=re.DOTALL)

    # Lists
    def cvt_list(tag, env, h):
        def _outer(m):
            items = re.sub(r'<li[^>]*>(.*?)</li>',
                lambda x: '  ' + r'\item ' + strip_tags(x.group(1)).strip() + '\n',
                m.group(1), flags=re.DOTALL)
            return '\n' + r'\begin{' + env + '}\n' + items + r'\end{' + env + '}' + '\n'
        return re.sub(r'<' + tag + r'[^>]*>(.*?)</' + tag + r'>', _outer, h, flags=re.DOTALL)
    html = cvt_list('ul', 'itemize', html)
    html = cvt_list('ol', 'enumerate', html)

    # HR
    HR = '\n' + r'\medskip\noindent\rule{\linewidth}{0.4pt}\medskip' + '\n'
    html = re.sub(r'<hr\s*/?>', lambda _: HR, html)

    # Strip remaining block wrappers
    html = re.sub(r'<p[^>]*>(.*?)</p>',   lambda m: '\n' + m.group(1) + '\n', html, flags=re.DOTALL)
    html = re.sub(r'<div[^>]*>(.*?)</div>', lambda m: '\n' + m.group(1) + '\n', html, flags=re.DOTALL)
    html = re.sub(r'<span[^>]*>(.*?)</span>', lambda m: m.group(1), html, flags=re.DOTALL)
    html = re.sub(r'<(?:[a-zA-Z/!?][^>]*|)>', '', html)

    # Restore code blocks
    for idx, code in enumerate(code_blocks):
        html = html.replace('CODEBLOCK{}ENDCODE'.format(idx),
            '\n' + r'\begin{lstlisting}' + '\n' + code + r'\end{lstlisting}' + '\n')

    html = re.sub(r'\n{4,}', '\n\n', html)
    return html.strip()

# ---------------------------------------------------------------------------
# JS slide object extraction helpers
# ---------------------------------------------------------------------------

def get_prop(js_obj, key):
    pattern = re.compile(r'\b' + re.escape(key) + r'\s*:\s*`')
    m = pattern.search(js_obj)
    if not m:
        return None
    start = m.end()
    i, depth = start, 0
    while i < len(js_obj):
        ch = js_obj[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '$' and i + 1 < len(js_obj) and js_obj[i + 1] == '{':
            depth += 1
            i += 2
            continue
        if ch == '}' and depth > 0:
            depth -= 1
            i += 1
            continue
        if ch == '`' and depth == 0:
            return js_obj[start:i]
        i += 1
    return None

def extract_s_calls(js):
    calls = []
    i = 0
    while i < len(js):
        idx = js.find('S({', i)
        if idx == -1:
            break
        brace_depth, backtick, j = 0, False, idx + 2
        while j < len(js):
            ch = js[j]
            if ch == '\\' and backtick:
                j += 2
                continue
            if ch == '`':
                backtick = not backtick
            if not backtick:
                if ch == '{':
                    brace_depth += 1
                elif ch == '}':
                    brace_depth -= 1
                    if brace_depth == 0:
                        calls.append(js[idx + 2:j + 1])
                        i = j + 1
                        break
            j += 1
        else:
            break
    return calls
