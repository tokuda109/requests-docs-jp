.. _install:

.. Installation of Requests
   ========================

Requests のインストール方法
===============================

.. This part of the documentation covers the installation of Requests.
   The first step to using any software package is getting it properly installed.

ドキュメントのこの章では、Requests のインストール方法について紹介しています。
ソフトウェア・パッケージを使うための第一歩は正しくインストールすることです。

$ pip install requests
----------------------

.. To install Requests, simply run this simple command in your terminal of choice::

Requests をインストールするには、使っているターミナルで以下のシンプルなコマンドを実行するだけです。::

    $ pip install requests

.. If you don't have `pip <https://pip.pypa.io>`_ installed (tisk tisk!),
   `this Python installation guide <http://docs.python-guide.org/en/latest/starting/installation/>`_
   can guide you through the process.

`pip <https://pip.pypa.io>`_ がまだインストールされていない場合、
`この Python のインストールガイド <http://docs.python-guide.org/en/latest/starting/installation/>`_ をから行ってください。

.. Get the Source Code
   -------------------

ソースコードを取得する
-------------------------

.. Requests is actively developed on GitHub, where the code is
   `always available <https://github.com/requests/requests>`_.

Requests は GitHub 上でアクティブに開発されていて、コードは`常に利用することができます <https://github.com/requests/requests>`_。

.. You can either clone the public repository::

公開されているリポジトリをクローンしてきて使うこともできます。::

    $ git clone git://github.com/requests/requests.git

.. Or, download the `tarball <https://github.com/requests/requests/tarball/master>`_::

もしくは、`tarball <https://github.com/requests/requests/tarball/master>`_ をダウンロードすることもできます。::

    $ curl -OL https://github.com/requests/requests/tarball/master
    # optionally, zipball is also available (for Windows users).

.. Once you have a copy of the source, you can embed it in your own Python
   package, or install it into your site-packages easily::

ソースのコピーを取得したら、Python パッケージに埋め込んだり、簡単に site-packages にインストールすることができます。::

    $ cd requests
    $ pip install .
