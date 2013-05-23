Title: The ubiquity of error
Date: 2013-05-26 15:00
Tags: scientific software, software, programming, code, reproducible research
Category: general
Slug: ubiquity-of-error
Author: Matthew Brett
Summary: Computers make us forget that make mistakes

I was talking to an esteemed colleague about six months ago about how easy it
was to believe that we do not make errors, unless we check.

He said that he had noticed this change when his students and research
assistants started to use their own computer programs to analyze data.  Before
this, when he and others added up a column of numbers, they would check
several times that they were correct.  After, the student or RA would analyze
some data with a program they had written themselves, and my friend would say
"are you sure the program is right" and they would say "yes I'm sure". My
friend would then go through the results and check; they would often find
mistakes.  He thought that there was something about using a computer that
made it easy to believe that the result was right, even if the process of
getting the result had the same chance of error as a simpler task like adding
numbers.

To quote David Donoho:

> In my own experience, error is ubiquitous in scientific computing, and one needs to work very diligently and energetically to eliminate it. One needs a very clear idea of what has been done in order to know where to look for likely sources of error. I often cannot really be sure what a student or colleague has done from his/her own presentation, and in fact often his/her description does not agree with my own understanding of what has been done, once I look carefully at the scripts. Actually, I find that researchers quite generally forget what they have done and misrepresent their computations.
>
> Computing results are now being presented in a very loose, “breezy” way—in journal articles, in conferences, and in books. All too often one simply takes computations at face value. This is spectacularly against the evidence of my own experience. I would much rather that at talks and in referee reports, the possibility of such error were seriously examined.
>
> -- <cite>David L. Donoho (2010). An invitation to reproducible computational
> research. Biostatistics Volume 11, Issue 3 Pp. 385-388</cite>

There is something about computational science that seems to make the idea of
error less worrying or important:

> In stark contrast to the sciences relying on deduction or empiricism,
computational science is far less visibly concerned with the ubiquity of
error. At conferences and in publications, it’s now completely acceptable for
a researcher to simply say, “here is what I did, and here are my results.”
Presenters devote almost no time to explaining why the audience should believe
that they found and corrected errors in their computations. The presentation’s
core isn’t about the struggle to root out error — as it would be in mature
fields — but is instead a sales pitch: an enthusiastic presentation of ideas
and a breezy demo of an implementation. Computational science has nothing like
the elaborate mechanisms of formal proof in mathematics or meta-analysis in
empirical science. Many users of scientific computing aren’t even trying to
follow a systematic, rigorous discipline that would in principle allow others
to verify the claims they make. How dare we imagine that computational
science, as routinely practiced, is reliable!
>
> -- <cite> David L. Donoho, Arian Maleki, Inam Ur Rahman, Morteza Shahram and
> Victoria Stodden (2009) Reproducible Research in Computational Harmonic
> Analysis.  Computing in Science and Engineering 11(1) pp 8-18
