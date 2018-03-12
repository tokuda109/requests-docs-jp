.. How to Help
   ===========

サポート方法
==============

.. Requests is under active development, and contributions are more than welcome!

Requests は活発に開発されていて、コントリビューターをさらに歓迎します！

.. Check for open issues or open a fresh issue to start a discussion around a bug.
   There is a Contributor Friendly tag for issues that should be ideal for people who are not very
   familiar with the codebase yet.
.. Fork `the repository <https://github.com/requests/requests>`_ on GitHub and start making your
   changes to a new branch.
.. Write a test which shows that the bug was fixed.
.. Send a pull request and bug the maintainer until it gets merged and published. :)
   Make sure to add yourself to `AUTHORS <https://github.com/requests/requests/blob/master/AUTHORS.rst>`_.

#. バグに関するディスカッションを開始するための新規の Issues を作成するか、既に Issues があるかチェックしてみて下さい。
   まだコードに慣れていない方にぴったりの Contributor Friendly タグがあります。
#. GitHub の `リポジトリ <https://github.com/requests/requests>`_ をフォークして、新しいブランチで作業を始めて下さい。
#. バグが修正されたことを示すためのテストを書いて下さい。
#. プルリクエストを送り、マージされて公開されるまでバグをメンテナンスして下さい。
   `AUTHORS <https://github.com/requests/requests/blob/master/AUTHORS.rst>`_ に自身の名前を追加して下さい。

.. Feature Freeze
   --------------

機能のフリーズ
-----------------

.. As of v1.0.0, Requests has now entered a feature freeze. Requests for new
   features and Pull Requests implementing those features will not be accepted.

v1.0.0 以降、Requests は新規機能の停止をしました。
新しい機能の要望やプルリクエストは受け付けていません。

Development Dependencies
------------------------

.. You'll need to install py.test in order to run the Requests' test suite::

Requests のテストスイートを実行するには、py.test をインストールする必要があります。::

    $ venv .venv
    $ source .venv/bin/activate

    $ make
    $ python setup.py test
    ============================= test session starts ==============================
    platform darwin -- Python 3.4.4, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
    ...
    collected 445 items

    tests/test_hooks.py ...
    tests/test_lowlevel.py ............
    tests/test_requests.py ...........................................................
    tests/test_structures.py ....................
    tests/test_testserver.py ...........
    tests/test_utils.py ..s...........................................................

    ============== 442 passed, 1 skipped, 2 xpassed in 46.48 seconds ===============

.. You can also run ``$ make tests`` to run against all supported Python versions, using tox/detox.

サポートしている全ての Python バージョンに対して、tox/detox を使ってテスト実行することもできて、``$ make tests`` を実行して下さい。

.. Runtime Environments
   --------------------

ランタイム環境
--------------------

.. Requests currently supports the following versions of Python:

Requests は、現在以下の Python バージョンをサポートしています。:

- Python 2.6
- Python 2.7
- Python 3.4
- Python 3.5
- Python 3.6
- PyPy

.. Google AppEngine is not officially supported although support is available
   with the `Requests-Toolbelt`_.

Google AppEngine では、公式にはサポートしていませんが、`Requests-Toolbelt`_ を使うことで有効にできます。

.. _Requests-Toolbelt: http://toolbelt.readthedocs.io/
