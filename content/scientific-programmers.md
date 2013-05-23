Title: Unscientific programming
Date: 2013-05-26 15:30
Tags: scientific software, software, programming, code
Category: general
Slug: unscientific-programming
Author: Matthew Brett
Summary: Scientific programming is programming

We various of the Berkeley NIPY crowd were in a Mexican restaurant yesterday
lunchtime. We discussed the IPython notebook and scientific programming and
reproducible research.

One question struck me as fundamental: *do scientists have to learn to be
software engineers?*

I think the common answer to this is "No - scientific coding is different".
The "No" camp points out that scientists use code in a different way to
software engineers.  Science is exploration, and so is scientific coding.
Scientific code is provisional, often changing.  There is no specfication,
there is no production system that must *just work*.  We are trying stuff out,
seeing what works, adjusting to our better understanding of the data and the
ideas.

Maybe the scientist's idea of the canonical software engineer is someone who
writes and hosts a web application with some database behind it.

Accepting the "No", we look at things that software engineers should learn:

1. Version control.  Essential for a software engineer, apparently, because
   they need to be able to rollback their changes, and keep track of released
   and development versions.  Desirable maybe for a scientist, but not
   essential, because the code never goes into production, and we always use
   the latest version of the code.
2. Testing.  Essential for a software engineer, otherwise they may release
   code that corrupts a database of financial transactions or delivers the
   wrong item to your address.  Desirable maybe for a scientist, but not
   essential because the nature of the code changes so often that it would
   only slow things down to write exhaustive tests, only for the code to
   change track and make the tests obsolete.
3. Code review.  Essential for a software engineer, because they work in teams
   with other software engineers.  This is their job, to write code, and they
   can learn from each other. Desirable maybe for a scientist, but not
   essential because each scientist owns their own problem and so only they
   can understand their code.  Explaining the code is time-consuming and slows
   progress in developing new ideas.  Others in the lab are not software
   engineers, so they are not trained to review code, they will not enjoy it
   and they will not do a good job.
4. Releases.  Essential for a software engineer because they may be paid to
   provide code that others can use.  The release labels code that can be
   used.  The software engineer can and should make sure the code works as
   advertised.  Desirable maybe for a scientist, but not essential, because
   the code changes often, and the code may be written to solve a very
   specific problem that could not be of much interest to another researcher.
   If the other researcher is interested, they should make the effort to work
   out how to use the code, that is not the job of the author-scientist, they
   are not paid to support software, but to produce science.
5. Documentation.  Essential for a software engineer because they want their
   code to be used correctly by other people.  Desirable but not essential for
   the scientist because scientific code is not for distribution except to
   other scientists who must take responsibility for the code themselves.

I think that these set of beliefs lie at the heart of the problem for
reproducible science.

The beliefs rest on the following model of writing scientific code:

## A folk model of scientific code

A scientist named A writes some code.  They check the code.  They confirm it
is working.  Most likely this means the code is free of major errors.

Another scientist named B is reading some results published by A. They can
assume that the results are free of major errors.

## Living with the folk model

Now everything makes sense.  Version control, testing, code review, releases,
documentation are great, of course, but if we can assume there are no major
errors, then - why would B want to see my code?  If B gets my code, why would
she need to understand it?  Why would she need to know what version it was, or
how that related to my paper?  She should assume that there are no major
errors.

## Rejecting the folk model

The folk model is not just too simple, it is flat-out wrong.  We [make
mistakes](|filename|ubiquity-of-error.md) all the time.  *All the time*.  If
you know that, then you know that B needs to check your stuff.  They can't do
science without checking your stuff.  If they need to check your stuff, you
need to write your code *for production*.  Then, nothing is optional.  We all
need; version control, testing, code review, releases, documentation.

<!-- vim:ft=markdown
-->

