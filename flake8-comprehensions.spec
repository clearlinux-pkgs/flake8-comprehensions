#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC7125C934883BE5 (me@adamj.eu)
#
Name     : flake8-comprehensions
Version  : 3.2.2
Release  : 16
URL      : https://files.pythonhosted.org/packages/8c/9b/26d0d2ab67e16500c8e68db07e66335f4a51fa1236a794e21ba670ac0dc4/flake8-comprehensions-3.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/8c/9b/26d0d2ab67e16500c8e68db07e66335f4a51fa1236a794e21ba670ac0dc4/flake8-comprehensions-3.2.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/8c/9b/26d0d2ab67e16500c8e68db07e66335f4a51fa1236a794e21ba670ac0dc4/flake8-comprehensions-3.2.2.tar.gz.asc
Summary  : A flake8 plugin to help you write better list/set/dict comprehensions.
Group    : Development/Tools
License  : ISC
Requires: flake8-comprehensions-python = %{version}-%{release}
Requires: flake8-comprehensions-python3 = %{version}-%{release}
Requires: flake8
BuildRequires : buildreq-distutils3
BuildRequires : flake8

%description
=====================
flake8-comprehensions
=====================

.. image:: https://img.shields.io/pypi/v/flake8-comprehensions.svg
        :target: https://pypi.org/project/flake8-comprehensions/

.. image:: https://img.shields.io/travis/adamchainz/flake8-comprehensions.svg
        :target: https://travis-ci.org/adamchainz/flake8-comprehensions

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

A `flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin that
helps you write better list/set/dict comprehensions.

Installation
------------

Install from ``pip`` with:

.. code-block:: sh

     pip install flake8-comprehensions

Python 3.5 to 3.8 supported.

When installed it will automatically be run as part of ``flake8``; you can
check it is being picked up with:

.. code-block:: sh

    $ flake8 --version
    3.7.8 (flake8-comprehensions: 3.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.8.0 on Linux


Rules
-----

==== ====
Code Rule
==== ====
C400 Unnecessary generator - rewrite as a list comprehension.
C401 Unnecessary generator - rewrite as a set comprehension.
C402 Unnecessary generator - rewrite as a dict comprehension.
C403 Unnecessary list comprehension - rewrite as a set comprehension.
C404 Unnecessary list comprehension - rewrite as a dict comprehension.
C405 Unnecessary (list/tuple) literal - rewrite as a set literal.
C406 Unnecessary (list/tuple) literal - rewrite as a dict literal.
C407 Unnecessary (dict/list) comprehension - '<builtin>' can take a generator.
C408 Unnecessary (dict/list/tuple) call - rewrite as a literal.
C409 Unnecessary (list/tuple) passed to tuple() - (remove the outer call to tuple()/rewrite as a tuple literal).
C410 Unnecessary (list/tuple) passed to list() - (remove the outer call to list()/rewrite as a list literal).
C411 Unnecessary list call - remove the outer call to list().
C412 Unnecessary (dict/list/set) comprehension - 'in' can take a generator.
C413 Unnecessary list call around sorted().
C413 Unnecessary reversed call around sorted() - (use sorted(..., reverse=(True/False))/toggle reverse argument to sorted()).
C414 Unnecessary (list/reversed/set/sorted/tuple) call within list/set/sorted/tuple().
C415 Unnecessary subscript reversal of iterable within reversed/set/sorted().
C416 Unnecessary (list/set) comprehension - rewrite using list/set().
==== ====

Examples
--------

C400-402: Unnecessary generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to use ``list``, ``set``, or ``dict`` around a generator
expression, since there are equivalent comprehensions for these types. For
example:

* Rewrite ``list(f(x) for x in foo)`` as ``[f(x) for x in foo]``
* Rewrite ``set(f(x) for x in foo)`` as ``{f(x) for x in foo}``
* Rewrite ``dict((x, f(x)) for x in foo)`` as ``{x: f(x) for x in foo}``

C403-404: Unnecessary list comprehension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to use a list comprehension inside a call to ``set`` or
``dict``, since there are equivalent comprehensions for these types. For
example:

* Rewrite ``set([f(x) for x in foo])`` as ``{f(x) for x in foo}``
* Rewrite ``dict([(x, f(x)) for x in foo])`` as ``{x: f(x) for x in foo}``

C405-406,C409-410: Unnecessary list/tuple literal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to use a list or tuple literal within a call to ``tuple``,
``list``, ``set``, or ``dict`` since there is literal syntax for these types.
For example:

* Rewrite ``tuple([1, 2])`` or ``tuple((1, 2))`` as ``(1, 2)``
* Rewrite ``tuple([])`` as ``()``
* Rewrite ``list([1, 2])`` or ``list((1, 2))`` as ``[1, 2]``
* Rewrite ``list([])`` as ``[]``
* Rewrite ``set([1, 2])`` or ``set((1, 2))`` as ``{1, 2}``
* Rewrite ``set([])`` as ``set()``
* Rewrite ``dict([(1, 2)])`` or ``dict(((1, 2),))`` as ``{1: 2}``
* Rewrite ``dict([])`` as ``{}``

C407: Unnecessary list comprehension - '<builtin>' can take a generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to pass a list comprehension to some builtins that can take
generators instead. For example:

* Rewrite ``sum([x ** 2 for x in range(10)])`` as
  ``sum(x ** 2 for x in range(10))``
* Rewrite ``all([foo.bar for foo in foos])`` as
  ``all(foo.bar for foo in foos)``
* Rewrite ``filter(lambda x: x % 2 == 0, [x ** 3 for x in range(10)])`` as
  ``filter(lambda x: x % 2 == 0, (x ** 3 for x in range(10)))``

The list of builtins that are checked for are:

* ``all``
* ``any``
* ``enumerate``
* ``filter``
* ``frozenset``
* ``map``
* ``max``
* ``min``
* ``sorted``
* ``sum``
* ``tuple``

C408: Unnecessary (dict/list/tuple) call - rewrite as a literal.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's slower to call e.g. ``dict()`` than using the empty literal, because the
name ``dict`` must be looked up in the global scope in case it has been
rebound. Same for the other two basic types here. For example:

* Rewrite ``dict()`` as ``{}``
* Rewrite ``list()`` as ``[]``
* Rewrite ``tuple()`` as ``()``

C411: Unnecessary list call - remove the outer call to list().
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to use a ``list`` around list comprehension, since it is
equivalent without it. For example:

* Rewrite ``list([f(x) for x in foo])`` as ``[f(x) for x in foo]``

C412: Unnecessary (dict/list/set) comprehension - 'in' can take a generator.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to pass a dict/list/set comprehension to 'in' that can take a
generator instead. For example:

* Rewrite ``y in [f(x) for x in foo]`` as ``y in (f(x) for x in foo)``
* Rewrite ``y in {x ** 2 for x in foo}`` as ``y in (x ** 2 for x in foo)``

C413: Unnecessary list/reversed call around sorted().
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to use ``list()`` around ``sorted()`` as it already returns a
list. It is also suboptimal to use ``reversed()`` around ``sorted()`` as the
latter has a ``reverse`` argument. For example:

* Rewrite ``list(sorted([2, 3, 1]))`` as ``sorted([2, 3, 1])``
* Rewrite ``reversed(sorted([2, 3, 1]))`` as ``sorted([2, 3, 1], reverse=True)``
* Rewrite ``reversed(sorted([2, 3, 1], reverse=True))`` as ``sorted([2, 3, 1])``

C414: Unnecessary (list/reversed/set/sorted/tuple) call within list/set/sorted/tuple().
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to change the type of the iterable or change the order of
elements within certain other function calls that will themselves define the
order of the iterable or the type that is output. For example:

* Rewrite ``list(list(iterable))`` as ``list(iterable)``
* Rewrite ``list(tuple(iterable))`` as ``list(iterable)``
* Rewrite ``tuple(list(iterable))`` as ``tuple(iterable)``
* Rewrite ``tuple(tuple(iterable))`` as ``tuple(iterable)``
* Rewrite ``set(set(iterable))`` as ``set(iterable)``
* Rewrite ``set(list(iterable))`` as ``set(iterable)``
* Rewrite ``set(tuple(iterable))`` as ``set(iterable)``
* Rewrite ``set(sorted(iterable))`` as ``set(iterable)``
* Rewrite ``set(reversed(iterable))`` as ``set(iterable)``
* Rewrite ``sorted(list(iterable))`` as ``sorted(iterable)``
* Rewrite ``sorted(tuple(iterable))`` as ``sorted(iterable)``
* Rewrite ``sorted(sorted(iterable))`` as ``sorted(iterable)``
* Rewrite ``sorted(reversed(iterable))`` as ``sorted(iterable)``

C415: Unnecessary subscript reversal of iterable within reversed/set/sorted().
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to reverse the order of an iterable using a ``[::-1]`` before
passing it into ``set()`` which will randomize the order, ``sorted()`` which
will return a new sorted list, or ``reversed()`` which will effectively return
the original iterable. For example:

* Rewrite ``set(iterable[::-1])`` as ``set(iterable)``
* Rewrite ``sorted(iterable[::-1])`` as ``sorted(iterable, reverse=True)``
* Rewrite ``reversed(iterable[::-1])`` as ``iterable``

C416: Unnecessary (list/set) comprehension - rewrite using list/set().
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's unnecessary to use a list comprehension if the elements are unchanged. The
iterable should be wrapped in ``list()`` or ``set()`` instead. For example:

* Rewrite ``[x for x in iterable]`` as ``list(iterable)``
* Rewrite ``{x for x in iterable}`` as ``set(iterable)``

=======
History
=======

3.2.2 (2020-01-20)
------------------

* Remove check for dict comprehensions in rule C407 as it would also change the
  results for certain builtins such as ``sum()``.

3.2.1 (2020-01-20)
------------------

* Remove check for set comprehensions in rule C407 as it would change the
  results for certain builtins such as ``sum()``.

3.2.0 (2020-01-20)
------------------

* Add ``filter`` and ``map`` to rule C407.
* Check for dict and set comprehensions in rules C407 and C412.

3.1.4 (2019-11-20)
------------------

* Remove the tuple/unpacking check from C416 to prevent false positives where
  the type of the iterable is changed from some iterable to a tuple.

3.1.3 (2019-11-19)
------------------

* Ensure the fix for false positives in ``C416`` rule for asynchronous
  comprehensions runs on Python 3.6 too.

3.1.2 (2019-11-18)
------------------

* Fix false positives in ``C416`` rule for list comprehensions returning
  tuples.

3.1.1 (2019-11-16)
------------------

* Fix false positives in ``C416`` rule for asynchronous comprehensions.

3.1.0 (2019-11-15)
------------------

* Update Python support to 3.5-3.8.
* Fix false positives for C404 for list comprehensions not directly creating
  tuples.
* Add ``C413`` rule that checks for unnecessary use of ``list()`` or
  ``reversed()`` around ``sorted()``.
* Add ``C414`` rule that checks for unnecessary use of the following:
    * ``list()``, ``reversed()``, ``sorted()``, or ``tuple()``  within ``set``
      or ``sorted()``
    * ``list()`` or ``tuple()``  within ``list()`` or ``tuple()``
    * ``set()``  within ``set``
* Add ``C415`` rule that checks for unnecessary reversal of an iterable via
  subscript within ``reversed()``, ``set()``, or ``sorted()``.
* Add ``C416`` rule that checks for unnecessary list or set comprehensions that
  can be rewritten using ``list()`` or ``set()``.

3.0.1 (2019-10-28)
------------------

* Fix version display on ``flake8 --version`` (removing dependency on
  ``cached-property``). Thanks to Jon Dufresne.

3.0.0 (2019-10-25)
------------------

* Update Flake8 support to 3.0+ only. 3.0.0 was released in 2016 and the plugin
  hasn't been tested with it since.

2.3.0 (2019-10-25)
------------------

* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``importlib.metadata.version("flake8-comprehensions")``
  (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ /
  `backport <https://pypi.org/project/importlib-metadata/>`__).
* Add dependencies on ``cached-property`` and ``importlib-metadata``.
* Fix false negatives in ``C407`` for cases when ``enumerate`` and ``sum()``
  are passed more than one argument.

2.2.0 (2019-08-12)
------------------

* Update Python support to 3.5-3.7, as 3.4 has reached its end of life.
* ``C412`` rule that complains about using list comprehension with ``in``.

2.1.0 (2019-03-01)
------------------

* Add missing builtin ``enumerate`` to ``C407``.

2.0.0 (2019-02-02)
------------------

* Drop Python 2 support, only Python 3.4+ is supported now.

1.4.1 (2017-05-17)
------------------

* Fix false positives in ``C408`` for calls using ``*args`` or ``**kwargs``.

1.4.0 (2017-05-14)
------------------

* Plugin now reserves the full ``C4XX`` code space rather than just ``C40X``
* ``C408`` rule that complains about using ``tuple()``, ``list()``, or
  ``dict()`` instead of a literal.
* ``C409`` and ``C410`` rules that complain about an unnecessary list or tuple
  that could be rewritten as a literal.
* ``C411`` rule that complains about using list comprehension inside a
  ``list()`` call.

1.3.0 (2017-05-01)
------------------

* Don't allow installation with Flake8 3.2.0 which doesn't enable the plugin.
  This bug was fixed in Flake8 3.2.1.
* Prevent false positives of ``C402`` from generators of expressions that
  aren't two-tuples.
* ``C405`` and ``C406`` now also complain about unnecessary tuple literals.

1.2.1 (2016-06-27)
------------------

* ``C407`` rule that complains about unnecessary list comprehensions inside
  builtins that can work on generators.

1.2.0 (2016-07-11)
------------------

* Split all rule codes by type. This allows granular selection of the rules in
  flake8 configuration.

1.1.1 (2016-04-06)
------------------

* Fix crash on method calls

1.1.0 (2016-04-06)
------------------

* ``C401`` rule that complains about unnecessary list comprehensions inside
  calls to ``set()`` or ``dict()``.
* ``C402`` rule that complains about unnecessary list literals inside calls to
  ``set()`` or ``dict()``.

1.0.0 (2016-04-05)
------------------

* ``C400`` rule that complains about an unnecessary usage of a generator when a
  list/set/dict comprehension would do.

%package python
Summary: python components for the flake8-comprehensions package.
Group: Default
Requires: flake8-comprehensions-python3 = %{version}-%{release}

%description python
python components for the flake8-comprehensions package.


%package python3
Summary: python3 components for the flake8-comprehensions package.
Group: Default
Requires: python3-core
Provides: pypi(flake8-comprehensions)

%description python3
python3 components for the flake8-comprehensions package.


%prep
%setup -q -n flake8-comprehensions-3.2.2
cd %{_builddir}/flake8-comprehensions-3.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582923722
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
