## General file arrangement

LaTeX project is organized into *preamble* and nested *environments* and contain commands and text.

The preamble contains commands to:

  - define document class, e.g. `\documentclass{article}` for scholarly papers
  - load packages to add functionality, e.g. `\usepackage{amsmath}` for advanced math formatting
  - define document metadata, e.g. `\title{Name of this report}`
  - define custom commands (see below)
  
There is single root environment called *document*.

  - starts with `\begin{document}` and contains everything to `\end{document}`
  - can contain text, commands and other environments
  - all other environments are defined in a similar manner

Commands start with `\`, than have command name and argument, e.g. `\section{My first heading h1}`
orders *My first heading h1* to be printed appropriately formatted as heading (`\section`) . All document metadata are printed with `\maketitle` command

Multiple text files (pure text or text with commands and environments) could be imported in the main document:
  
  - `\include{Chapter3}` (top level, no nesting)
  - `\input{./Chapter3/Introduction}`

  
## Syntax

*Properly write nonstandard function name*

```latex
\mathrm{rect}  % Directly in math environment

\DeclareMathOperator{\rect}{rect} % Define the new function name in the preamble
\rect % use as standard function in math environment
```

*Define new commands*

```latex
\providecommand{\abs}[1]{\lvert#1\rvert}  % in the preamble
\abs{y_i(t)}  % in math environment
% instead of:
\lvert y_i(t) \rvert
```

*Brackets*

```latex
\left(   % opening bracket of type (
\right]  % closing bracket of type ]
\right.  % no closing bracket
```

*Equations*

  - basic formula, block: `\[  ax+b \]`, inline: `$ax+b$` or just `$a$`
  - environment for single equation, numbered: `equation`, unnumbered: `equation*`
  - environment for splitting single equation on multiple lines: `split` (should be defined in equation environment)
  - environment for multiple equations: `align` (you can add `\label{eqn:Y}` for each line)



## Examples
Properly write nonstandard function name:

```latex
\[  
  H(f) = \rect \left(\frac{f}{B}\right) \cos 5 
\]
\[  
  H(f) = \mathrm{rect} \left(\frac{f}{B}\right) \cos 5 
\]
```

*Big brackets, mbox, matrices*

```latex
\[
\rect \left( \frac{t}{T} \right) =  \left\{
\begin{matrix}
1, &\lvert t \rvert \leq \frac{T}{2} \\
0, &\mbox{otherwise}
\end{matrix} \right.
\]
```
