---
title: Latex Snippet
categories: Latex
tag: Snippet
date: 2017-12-18 20:36:00 +0800
published: false

---

# Math
## Align
``` latex
\begin{align}
  f(x) &= x^2\\
  g(x) &= \frac{1}{x}\\
  F(x) &= \int^a_b \frac{1}{3}x^3
\end{align}
```
## Matrix
``` latex
\left[
\begin{matrix}
1 & 0\\
0 & 1
\end{matrix}
\right]
```
## Picture
### Add Picture
``` latex
\usepackage{graphicx}

\begin{figure}
  \includegraphics[width=\linewidth]{boat.jpg}
  \caption{A boat.}
  \label{fig:boat1}
\end{figure}

Figure \ref{fig:boat1} shows a boat.
```
### Fix Picture Position
``` latex
%...
\begin{figure}[h!]
%...
```
where
- h (here) - same location
- t (top) - top of page
- b (bottom) - bottom of page
- p (page) - on an extra page
- ! (override) - will force the specified location
### Subpicture
``` latex
\usepackage{graphicx}
\usepackage{subcaption}
%...

\begin{figure}[h!]
  \centering
  \begin{subfigure}[b]{0.4\linewidth}
    \includegraphics[width=\linewidth]{coffee.jpg}
    \caption{Coffee.}
  \end{subfigure}
  \begin{subfigure}[b]{0.4\linewidth}
    \includegraphics[width=\linewidth]{coffee.jpg}
    \caption{More coffee.}
  \end{subfigure}
  \caption{The same cup of coffee. Two times.}
  \label{fig:coffee}
\end{figure}

%...
```
## Content-like
### Content
``` latex
\tableofcontents
```
### Tables and Figures List
``` latex
\begin{appendix}
  \listoffigures
  \listoftables
\end{appendix}
```

