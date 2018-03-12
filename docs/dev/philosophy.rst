.. Development Philosophy
   ======================

開発哲学
=========================

Requests is an open but opinionated library, created by an open but opinionated developer.

.. Management Style
   ~~~~~~~~~~~~~~~~

マネジメントスタイル
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. `Kenneth Reitz <http://kennethreitz.org>`_ is the BDFL. He has final say in any decision related to the Requests project. Kenneth is responsible for the direction and form of the library, as well as its presentation. In addition to making decisions based on technical merit, he is responsible for making decisions based on the development philosophy of Requests.

`Kenneth Reitz <http://kennethreitz.org>`_ は BDFL です。
彼は Requests プロジェクトに関する最終的な発言権を持っています。
Kenneth はライブラリの方向性や形式、プレゼンテーションを担当しています。
技術的な優位性に基づいて意思決定を行うほか、Requests の開発哲学に基づいて意思決定を行う責任があります。

.. `Ian Cordasco <http://www.coglib.com/~icordasc/>`_ and `Cory Benfield <https://lukasa.co.uk/about/>`_ are the core contributors. They are responsible for triaging bug reports, reviewing pull requests and ensuring that Kenneth is kept up to speed with developments around the library. The day-to-day managing of the project is done by the core contributors. They are responsible for making judgements about whether or not a feature request is likely to be accepted by Kenneth. Their word is, in some ways, more final than Kenneth's.

`Ian Cordasco <http://www.coglib.com/~icordasc/>`_ と `Cory Benfield <https://lukasa.co.uk/about/>`_ はコアコントリビューターです。
彼らは、バグレポートの審査、プルリクエストのレビュー、Kenneth がライブラリ関連の開発のスピードを上げることを担保する責任があります。
プロジェクトの日常的な管理は、コアコントリビューターによって行われます。
機能要望があった場合に Kenneth に受け入れられるかどうかを判断する責任があります。
彼らの言葉は、ある意味では Kenneth の言葉よりも最終的なものとなります。

.. Values
   ~~~~~~

価値観
~~~~~~~~~~~~

.. Simplicity is always better than functionality.
.. Listen to everyone, then disregard it.
.. The API is all that matters. Everything else is secondary.
.. Fit the 90% use-case. Ignore the nay-sayers.

- シンプルさは機能的なことより優れています。
- 様々な意見に耳を傾け、受け流して下さい。
- API はすべてのことより重要です、これ以外のことは2番目です。
- 90％のユースケースに当てはまり、Ignore the nay-sayers.

.. Semantic Versioning
   ~~~~~~~~~~~~~~~~~~~

セマンティックバージョニング
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. For many years, the open source community has been plagued with version number dystonia. Numbers vary so greatly from project to project, they are practically meaningless.

長年に渡り、オープンソースコミュニティはバージョン番号のストレスに悩まされてきました。
数字はプロジェクトごとに大きく異なるため無意味です。

.. Requests uses `Semantic Versioning <http://semver.org>`_. This specification seeks to put an end to this madness with a small set of practical guidelines for you and your colleagues to use in your next project.

Requests は `Semantic Versioning <http://semver.org>`_ を採用しています。
This specification seeks to put an end to this madness with a small set of practical guidelines for you and your colleagues to use in your next project.

.. Standard Library?
   ~~~~~~~~~~~~~~~~~

標準ライブラリ?
~~~~~~~~~~~~~~~~~~~~

.. Requests has no *active* plans to be included in the standard library. This decision has been discussed at length with Guido as well as numerous core developers.

Requests は標準ライブラリに含まれるという *具体的な* 計画はありません。
これは Guido や数多くのコア開発者によって長らく議論されて出た結論です。

.. Essentially, the standard library is where a library goes to die. It is appropriate for a module to be included when active development is no longer necessary.

本質的に、標準ライブラリはライブラリの成長が止まるところです。
アクティブな開発が必要ない時にモジュールに組み込まれることが適切です。

.. Linux Distro Packages
   ~~~~~~~~~~~~~~~~~~~~~

Linux ディストリビューションパッケージ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Distributions have been made for many Linux repositories, including: Ubuntu, Debian, RHEL, and Arch.

Ubuntu、Debian、RHEL、Arch を含むディストリビューションは数多くの Linux のリポジトリから配布されています。

.. These distributions are sometimes divergent forks, or are otherwise not kept up-to-date with the latest code and bugfixes. PyPI (and its mirrors) and GitHub are the official distribution sources; alternatives are not supported by the Requests project.

これらのディストリビューションは時には分岐フォークであるか、あるいは最新のコードとバグ修正で最新の状態に保たれていないことがあります。 PyPI（およびそのミラー）とGitHubは公式の配布元です。 代替案はRequestsプロジェクトではサポートされていません。
