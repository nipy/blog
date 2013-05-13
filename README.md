# nipy blog

Web pages for nipy blog

The website is built using Pelican.

The built web-pages go in the ``gh-pages`` branch of this repo.

The Pelican source for the website goes in the ``master`` branch.

Working on the site goes like:

## First time

1. Install [Pelican](http://github.com/getpelican/pelican)
1. Clone this repo from <http://github.com/matthew-brett/blog> or fork it to
   your own Github account.
1. ``git submodule update --init``


## After that

1. Add any posts in ``content`` as something like ``content/name-of-post.md``
   using the Pelican formatting (see other posts in ``content/`` for examples).
   You can also write posts in ReST, with Pelican-specific formatting at the
   start (see Pelican docs).

1. Add and commit

1. If you don't have write permission to the repo - submit a pull request - we'll merge and build for you.

1. If you do have write permission then ``make github`` should do the trick.
