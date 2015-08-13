
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
