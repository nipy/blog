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
1. ``git submodule update --init --recursive``

## After that

1. Add any posts in ``content`` as something like ``content/name-of-post.md``
   using the Pelican formatting (see other posts in ``content/`` for examples).
   You can also write posts in ReST, with Pelican-specific formatting at the
   start (see Pelican docs).

1. Add and commit

1. If you don't have write permission to the repo - submit a pull request - we'll merge and build for you.

If you do have write permission then:

### If you are working on a clone of nipy/blog.git

1. ``make github`` should build the html pages to ``output``, commit them to
   the gh-pages branch and push this branch up to ``nipy/blog:gh-pages`` from
   which the pages are hosted.

### If you are working on your own fork of nipy/blog.git

1. ``make github`` will build the html pages to ``output``, commit them to the
   gh-pages branch and push this branch up to ``<origin>/blog:gh-pages``.
   ``origin`` is the git remote.  If ``origin`` happens to point to
   ``git@github.com:nipy/blog.git`` then this will work fine.

   If `origin` doesn't point to `git@github.com:nipy/blog.git`` and you have
   another remote that does point there, add that remote to the ``make``
   command, e.g ``make github-upstream-rw`` where ``upstream-rw`` is a remote
   pointing to ``git@github.com:nipy/blog.git``
