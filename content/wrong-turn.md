Title: A separation too early
Date: 2013-05-27 12:00
Tags: scientific software, software engineering, programming, code
Category: General
Slug: science-joins-software
Author: Matthew Brett
Summary: Sofware engineering became a separate discipline and orphaned expertise in scientific programming

I followed a Google+ link to an article that has just come out in Science
magazine. The article is "Troubling Trends in Scientific
Software Use" by Lucas Joppa and others [^joppa].

[^joppa]: Joppa, Lucas N., et al. "Troubling Trends in Scientific Software
    Use." Science 340.6134 (2013): 814-815.

I did not find Joppa's article very satisfying, but there were some
interesting references.  For example (from Joppa *et al*):

> From fields such as high-performance computing, we learn key insights and
> best practices for how to develop, standardize, and implement software (11)

Reference 11 is an article by Victor Basili and others on "Understanding the
High-Performance-Computing Community" [^basili]. It is a thoughtful reflection
on the experience of academic software engineers working with scientists using
massively parallel computing. The message I took from the article was that
scientists may have good reasons to reject suggestions from academic software
engineers.  This is often because the solutions are too general to be useful
for a particular problem.  The last sentence from the article is "We've much
to learn from each other".

[^basili]: Basili, Victor R., et al. "Understanding the
    High-Performance-Computing Community." (2008).

Another couple of sentences in the Joppa article led me to interesting places:

> Reliance on personal recommendations and trust is a strategy with risks to
> science and scientist. "End-user developers" commonly create scientific
> software (17, 21, 22) [^joppa]

Reference (22) is "A Software Chasm: Software Engineering and Scientific
Computing" by Diane Kelley [^kelly]. Kelley also has some interesting thoughts
on the separation of science and software engineering:

[^kelly]: Kelly, Diane F. "A software chasm: Software engineering and
    scientific computing." Software, IEEE 24.6 (2007): 120-119.

>Creating the chasm
>
>In a 1997 paper, Iris Vessey described a shift in computing philosophy that
>occurred in the late 1960s. She quoted George E. Forsyth, the ACM's president
>at that time, as stating that computer science was a field of its own,
>separate from the application domains. The result, as Vessey points out, was
>the insistence that anyone who wanted to be taken seriously in the field of
>computing, and software engineering, must develop domain-independent
>techniques, methods, and paradigms. The pressure was such that claims of
>broad applicability became commonplace. So, the bridge between software
>engineering and any application domain became a single massive structure that
>everyone had to use.

This is the relevant quote from Vessey (1997)[^vessey]:

>Then followed a debate, which endured for over a decade, that pitted
>academia against the computing profession. The notions of traditional
>computer scientists steeped in the notion of theory and the stigma of all
>things "applied" led to the following statement by George E. Forsyth,
>President of ACM, in 1965: "... the core of computer science has become
>and will remain a field of its own, ahead of, and separate from the
>application domain specialists." This philosophy led, not only to the
>creation of generic "solutions" to problems, but also to claims that any
>"creation" was applicable in all situations, because to state otherwise
>would have branded the creator as lacking in academic respectability.

[^vessey]: Vessey, Iris. "Problems versus solutions: the role of the application
    domain in software." Papers presented at the seventh workshop on Empirical
    studies of programmers. ACM, 1997.

I wonder if this separation has had a larger effect on our thinking than we
recognize.

For example, our original NIPY grant application asked for salaries for two
full-time programmers to help us apply software engineering methods to writing
neuroimaging software.  We did hire two programmers but we had given them an
impossible job.  To do a good job, they had to now become experts in a
scientific field they did not know. Useful code and documentation had to be
written so that other scientists in the field would find it easy to follow.
To do this, you need to know the field.  We scientists spend more time than we
think working out how to talk to our colleagues. That experience is very hard
to teach.

These articles gave me a new way to think about the false separation of
"software" and "science". It is mysterious that we make this separation,
because my whole experience tells me they are closely linked. I wonder whether
we make this separation because we have come under the unconscious influence
of the movement that Kelley and Vessey describe.  It is easy to see how
tempting it is.   How easy life would be if we really could pay a programmer
to write up our ideas as we sketch them airily on a white-board and retire to
the garden, to think great thoughts.
