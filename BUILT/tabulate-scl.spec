%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name tabulate
%define version 0.7.7
%define unmangled_version 0.7.7
%define unmangled_version 0.7.7
%define release 1

Summary: Pretty-print tabular data
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}tabulate
Version: %{version}
Release: %{release}
Source0: tabulate-%{unmangled_version}.tar.gz
License: GPL

Group: Development/Libraries
BuildRoot: %{_tmppath}/tabulate-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Sergey Astanin <s.astanin@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://bitbucket.org/astanin/python-tabulate


%description
===============
python-tabulate
===============

Pretty-print tabular data in Python, a library and a command-line
utility.

The main use cases of the library are:

* printing small tables without hassle: just one function call,
  formatting is guided by the data itself

* authoring tabular data for lightweight plain-text markup: multiple
  output formats suitable for further editing or transformation

* readable presentation of mixed textual and numeric data: smart
  column alignment, configurable number formatting, alignment by a
  decimal point


Installation
------------

To install the Python library and the command line utility, run::

    pip install tabulate

The command line utility will be installed as ``tabulate`` to ``bin`` on Linux
(e.g. ``/usr/bin``); or as ``tabulate.exe`` to ``Scripts`` in your Python
installation on Windows (e.g. ``C:\Python27\Scripts\tabulate.exe``).

You may consider installing the library only for the current user::

    pip install tabulate --user

In this case the command line utility will be installed to ``~/.local/bin/tabulate``
on Linux and to ``%APPDATA%\Python\Scripts\tabulate.exe`` on Windows.

To install just the library on Unix-like operating systems::

    TABULATE_INSTALL=lib-only pip install tabulate

On Windows::

    set TABULATE_INSTALL=lib-only
    pip install tabulate


Library usage
-------------

The module provides just one function, ``tabulate``, which takes a
list of lists or another tabular data type as the first argument,
and outputs a nicely formatted plain-text table::

    >>> from tabulate import tabulate

    >>> table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
    ...          ["Moon",1737,73.5],["Mars",3390,641.85]]
    >>> print tabulate(table)
    -----  ------  -------------
    Sun    696000     1.9891e+09
    Earth    6371  5973.6
    Moon     1737    73.5
    Mars     3390   641.85
    -----  ------  -------------

The following tabular data types are supported:

* list of lists or another iterable of iterables
* list or another iterable of dicts (keys as columns)
* dict of iterables (keys as columns)
* two-dimensional NumPy array
* NumPy record arrays (names as columns)
* pandas.DataFrame

Examples in this file use Python2. Tabulate supports Python3 too.


Headers
~~~~~~~

The second optional argument named ``headers`` defines a list of
column headers to be used::

    >>> print tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"])
    Planet      R (km)    mass (x 10^29 kg)
    --------  --------  -------------------
    Sun         696000           1.9891e+09
    Earth         6371        5973.6
    Moon          1737          73.5
    Mars          3390         641.85

If ``headers="firstrow"``, then the first row of data is used::

    >>> print tabulate([["Name","Age"],["Alice",24],["Bob",19]],
    ...                headers="firstrow")
    Name      Age
    ------  -----
    Alice      24
    Bob        19


If ``headers="keys"``, then the keys of a dictionary/dataframe, or
column indices are used. It also works for NumPy record arrays and
lists of dictionaries or named tuples::

    >>> print tabulate({"Name": ["Alice", "Bob"],
    ...                 "Age": [24, 19]}, headers="keys")
      Age  Name
    -----  ------
       24  Alice
       19  Bob


Row Indices
~~~~~~~~~~~

By default, only pandas.DataFrame tables have an additional column
called row index. To add a similar column to any other type of table,
pass ``showindex="always"`` or ``showindex=True`` argument to
``tabulate()``. To suppress row indices for all types of data, pass
``showindex="never"`` or ``showindex=False``.  To add a custom row
index column, pass ``showindex=rowIDs``, where ``rowIDs`` is some
iterable::

    >>> print(tabulate([["F",24],["M",19]], showindex="always"))
    -  -  --
    0  F  24
    1  M  19
    -  -  --


Table format
~~~~~~~~~~~~

There is more than one way to format a table in plain text.
The third optional argument named ``tablefmt`` defines
how the table is formatted.

Supported table formats are:

- "plain"
- "simple"
- "grid"
- "fancy_grid"
- "pipe"
- "orgtbl"
- "jira"
- "psql"
- "rst"
- "mediawiki"
- "moinmoin"
- "html"
- "latex"
- "latex_booktabs"
- "textile"

``plain`` tables do not use any pseudo-graphics to draw lines::

    >>> table = [["spam",42],["eggs",451],["bacon",0]]
    >>> headers = ["item", "qty"]
    >>> print tabulate(table, headers, tablefmt="plain")
    item      qty
    spam       42
    eggs      451
    bacon       0

``simple`` is the default format (the default may change in future
versions).  It corresponds to ``simple_tables`` in `Pandoc Markdown
extensions`::

    >>> print tabulate(table, headers, tablefmt="simple")
    item      qty
    ------  -----
    spam       42
    eggs      451
    bacon       0

``grid`` is like tables formatted by Emacs' `table.el`
package.  It corresponds to ``grid_tables`` in Pandoc Markdown
extensions::

    >>> print tabulate(table, headers, tablefmt="grid")
    +--------+-------+
    | item   |   qty |
    +========+=======+
    | spam   |    42 |
    +--------+-------+
    | eggs   |   451 |
    +--------+-------+
    | bacon  |     0 |
    +--------+-------+

``fancy_grid`` draws a grid using box-drawing characters::

    >>> print tabulate(table, headers, tablefmt="fancy_grid")
    ╒════════╤═══════╕
    │ item   │   qty │
    ╞════════╪═══════╡
    │ spam   │    42 │
    ├────────┼───────┤
    │ eggs   │   451 │
    ├────────┼───────┤
    │ bacon  │     0 │
    ╘════════╧═══════╛

``psql`` is like tables formatted by Postgres' psql cli::

    >>> print tabulate.tabulate()
    +--------+-------+
    | item   |   qty |
    |--------+-------|
    | spam   |    42 |
    | eggs   |   451 |
    | bacon  |     0 |
    +--------+-------+

``pipe`` follows the conventions of `PHP Markdown Extra` extension.  It
corresponds to ``pipe_tables`` in Pandoc. This format uses colons to
indicate column alignment::

    >>> print tabulate(table, headers, tablefmt="pipe")
    | item   |   qty |
    |:-------|------:|
    | spam   |    42 |
    | eggs   |   451 |
    | bacon  |     0 |

``orgtbl`` follows the conventions of Emacs `org-mode`, and is editable
also in the minor `orgtbl-mode`. Hence its name::

    >>> print tabulate(table, headers, tablefmt="orgtbl")
    | item   |   qty |
    |--------+-------|
    | spam   |    42 |
    | eggs   |   451 |
    | bacon  |     0 |

``jira`` follows the conventions of Atlassian Jira markup language::

    >>> print tabulate(table, headers, tablefmt="jira")
    || item   ||   qty ||
    | spam   |    42 |
    | eggs   |   451 |
    | bacon  |     0 |

``rst`` formats data like a simple table of the `reStructuredText` format::

    >>> print tabulate(table, headers, tablefmt="rst")
    ======  =====
    item      qty
    ======  =====
    spam       42
    eggs      451
    bacon       0
    ======  =====

``mediawiki`` format produces a table markup used in `Wikipedia` and on
other MediaWiki-based sites::

    >>> print tabulate(table, headers, tablefmt="mediawiki")
    {| class="wikitable" style="text-align: left;"
    |+ <!-- caption -->
    |-
    ! item   !! align="right"|   qty
    |-
    | spam   || align="right"|    42
    |-
    | eggs   || align="right"|   451
    |-
    | bacon  || align="right"|     0
    |}

``moinmoin`` format produces a table markup used in `MoinMoin`
wikis::

    >>> print tabulate(d,headers,tablefmt="moinmoin")
    || ''' item   ''' || ''' quantity   ''' ||
    ||  spam    ||  41.999      ||
    ||  eggs    ||  451         ||
    ||  bacon   ||              ||

``textile`` format produces a table markup used in `Textile` format::

    >>> print tabulate(table, headers, tablefmt='textile')
    |_.  item   |_.   qty |
    |<. spam    |>.    42 |
    |<. eggs    |>.   451 |
    |<. bacon   |>.     0 |

``html`` produces standard HTML markup::

    >>> print tabulate(table, headers, tablefmt="html")
    <table>
    <tbody>
    <tr><th>item  </th><th style="text-align: right;">  qty</th></tr>
    <tr><td>spam  </td><td style="text-align: right;">   42</td></tr>
    <tr><td>eggs  </td><td style="text-align: right;">  451</td></tr>
    <tr><td>bacon </td><td style="text-align: right;">    0</td></tr>
    </tbody>
    </table>

``latex`` format creates a ``tabular`` environment for LaTeX markup::

    >>> print tabulate(table, headers, tablefmt="latex")
    \begin{tabular}{lr}
    \hline
     item   &   qty \\
    \hline
     spam   &    42 \\
     eggs   &   451 \\
     bacon  &     0 \\
    \hline
    \end{tabular}

``latex_booktabs`` creates a ``tabular`` environment for LaTeX markup
using spacing and style from the ``booktabs`` package.


.. _Pandoc Markdown extensions: http://johnmacfarlane.net/pandoc/README.html#tables
.. _PHP Markdown Extra: http://michelf.ca/projects/php-markdown/extra/#table
.. _table.el: http://table.sourceforge.net/
.. _org-mode: http://orgmode.org/manual/Tables.html
.. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables
.. _Textile: http://redcloth.org/hobix.com/textile/
.. _Wikipedia: http://www.mediawiki.org/wiki/Help:Tables


Column alignment
~~~~~~~~~~~~~~~~

``tabulate`` is smart about column alignment. It detects columns which
contain only numbers, and aligns them by a decimal point (or flushes
them to the right if they appear to be integers). Text columns are
flushed to the left.

You can override the default alignment with ``numalign`` and
``stralign`` named arguments. Possible column alignments are:
``right``, ``center``, ``left``, ``decimal`` (only for numbers), and
``None`` (to disable alignment).

Aligning by a decimal point works best when you need to compare
numbers at a glance::

    >>> print tabulate([[1.2345],[123.45],[12.345],[12345],[1234.5]])
    ----------
        1.2345
      123.45
       12.345
    12345
     1234.5
    ----------

Compare this with a more common right alignment::

    >>> print tabulate([[1.2345],[123.45],[12.345],[12345],[1234.5]], numalign="right")
    ------
    1.2345
    123.45
    12.345
     12345
    1234.5
    ------

For ``tabulate``, anything which can be parsed as a number is a
number. Even numbers represented as strings are aligned properly. This
feature comes in handy when reading a mixed table of text and numbers
from a file:

::

    >>> import csv ; from StringIO import StringIO
    >>> table = list(csv.reader(StringIO("spam, 42\neggs, 451\n")))
    >>> table
    [['spam', ' 42'], ['eggs', ' 451']]
    >>> print tabulate(table)
    ----  ----
    spam    42
    eggs   451
    ----  ----



Number formatting
~~~~~~~~~~~~~~~~~

``tabulate`` allows to define custom number formatting applied to all
columns of decimal numbers. Use ``floatfmt`` named argument::


    >>> print tabulate([["pi",3.141593],["e",2.718282]], floatfmt=".4f")
    --  ------
    pi  3.1416
    e   2.7183
    --  ------


Wide (fullwidth CJK) symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To properly align tables which contain wide characters (typically fullwidth
glyphs from Chinese, Japanese or Korean languages), the user should install
``wcwidth`` library. To install it together with ``tabulate``::

    pip install tabulate[widechars]

Wide character support is enabled automatically if ``wcwidth`` library is
already installed.  To disable wide characters support without uninstalling
``wcwidth``, set the global module-level flag ``WIDE_CHARS_MODE``::

    import tabulate
    tabulate.WIDE_CHARS_MODE = False


Usage of the command line utility
---------------------------------

::

    Usage: tabulate [options] [FILE ...]

    FILE                      a filename of the file with tabular data;
                              if "-" or missing, read data from stdin.

    Options:

    -h, --help                show this message
    -1, --header              use the first row of data as a table header
    -o FILE, --output FILE    print table to FILE (default: stdout)
    -s REGEXP, --sep REGEXP   use a custom column separator (default: whitespace)
    -F FPFMT, --float FPFMT   floating point number format (default: g)
    -f FMT, --format FMT      set output table format; supported formats:
                              plain, simple, grid, fancy_grid, pipe, orgtbl,
                              rst, mediawiki, html, latex, latex_booktabs, tsv
                              (default: simple)


Performance considerations
--------------------------

Such features as decimal point alignment and trying to parse everything
as a number imply that ``tabulate``:

* has to "guess" how to print a particular tabular data type
* needs to keep the entire table in-memory
* has to "transpose" the table twice
* does much more work than it may appear

It may not be suitable for serializing really big tables (but who's
going to do that, anyway?) or printing tables in performance sensitive
applications. ``tabulate`` is about two orders of magnitude slower
than simply joining lists of values with a tab, coma or other
separator.

In the same time ``tabulate`` is comparable to other table
pretty-printers. Given a 10x10 table (a list of lists) of mixed text
and numeric data, ``tabulate`` appears to be slower than
``asciitable``, and faster than ``PrettyTable`` and ``texttable``

::

    =================================  ==========  ===========
    Table formatter                      time, μs    rel. time
    =================================  ==========  ===========
    csv to StringIO                          25.3          1.0
    join with tabs and newlines              33.6          1.3
    asciitable (0.8.0)                      590.0         23.4
    tabulate (0.7.7)                       1403.5         55.6
    tabulate (0.7.7, WIDE_CHARS_MODE)      2156.6         85.4
    PrettyTable (0.7.2)                    3377.0        133.7
    texttable (0.8.6)                      3986.3        157.8
    =================================  ==========  ===========


Version history
---------------

- 0.8: FUTURE RELEASE
- 0.7.6: Bug fixes. New table formats (``psql``, ``jira``, ``moinmoin``, ``textile``).
  Wide character support. Printing from database cursors.
  Option to print row indices. Boolean columns. Ragged rows.
  Option to disable number parsing.
- 0.7.5: Bug fixes. ``--float`` format option for the command line utility.
- 0.7.4: Bug fixes. ``fancy_grid`` and ``html`` formats. Command line utility.
- 0.7.3: Bug fixes. Python 3.4 support. Iterables of dicts. ``latex_booktabs`` format.
- 0.7.2: Python 3.2 support.
- 0.7.1: Bug fixes. ``tsv`` format. Column alignment can be disabled.
- 0.7: ``latex`` tables. Printing lists of named tuples and NumPy
  record arrays. Fix printing date and time values. Python <= 2.6.4 is supported.
- 0.6: ``mediawiki`` tables, bug fixes.
- 0.5.1: Fix README.rst formatting. Optimize (performance similar to 0.4.4).
- 0.5: ANSI color sequences. Printing dicts of iterables and Pandas' dataframes.
- 0.4.4: Python 2.6 support.
- 0.4.3: Bug fix, None as a missing value.
- 0.4.2: Fix manifest file.
- 0.4.1: Update license and documentation.
- 0.4: Unicode support, Python3 support, ``rst`` tables.
- 0.3: Initial PyPI release. Table formats: ``simple``, ``plain``,
  ``grid``, ``pipe``, and ``orgtbl``.


How to contribute
-----------------

Contributions should include tests and an explanation for the changes they
propose. Documentation (examples, docstrings, README.rst) should be updated
accordingly.

This project uses `nose` testing framework and `tox` to automate testing in
different environments. Add tests to one of the files in the ``test/`` folder.

To run tests on all supported Python versions, make sure all Python
interpreters, ``nose`` and ``tox`` are installed, then run ``tox`` in
the root of the project source tree.

On Linux ``tox`` expects to find executables like ``python2.6``,
``python2.7``, ``python3.4`` etc. On Windows it looks for
``C:\Python26\python.exe``, ``C:\Python27\python.exe`` and
``C:\Python34\python.exe`` respectively.

To test only some Python environements, use ``-e`` option. For
example, to test only against Python 2.7 and Python 3.4, run::

    tox -e py27,py34

in the root of the project source tree.

To enable NumPy and Pandas tests, run::

    tox -e py27-extra,py34-extra

(this may take a long time the first time, because NumPy and Pandas
will have to be installed in the new virtual environments)

See ``tox.ini`` file to learn how to use ``nosetests`` directly to
test individual Python versions.

.. _nose: https://nose.readthedocs.org/
.. _tox: http://tox.testrun.org/


Contributors
------------

Sergey Astanin, Pau Tallada Crespí, Erwin Marsi, Mik Kocikowski, Bill Ryder,
Zach Dwiel, Frederik Rietdijk, Philipp Bogensberger, Greg (anonymous),
Stefan Tatschner, Emiel van Miltenburg, Brandon Bennett, Amjith Ramanujam,
Jan Schulz, Simon Percivall, Javier Santacruz López-Cepero, Sam Denton,
Alexey Ziyangirov, acaird, Cesar Sanchez, naught101, John Vandenberg,
Zack Dever.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n tabulate-%{unmangled_version} -n tabulate-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
