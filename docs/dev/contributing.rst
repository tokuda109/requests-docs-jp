.. _contributing:

.. Contributor's Guide
   ===================

コントリビューター用のガイド
===================================

.. If you're reading this, you're probably interested in contributing to Requests.
   Thank you very much! Open source projects live-and-die based on the support
   they receive from others, and the fact that you're even considering
   contributing to the Requests project is *very* generous of you.

これを読んでいるなら、おそらく Requests に貢献することに興味があるのかもしれません。
ありがとうございます！
オープンソースのプロジェクトは、他の方からのサポートを基にして成り立っていて、
Requests プロジェクトに貢献することを考えているということは、*very* generous of you

.. This document lays out guidelines and advice for contributing to this project.
   If you're thinking of contributing, please start by reading this document and
   getting a feel for how contributing to this project works. If you have any
   questions, feel free to reach out to either `Ian Cordasco`_ or `Cory Benfield`_,
   the primary maintainers.

このドキュメントは、このプロジェクトに貢献するためのガイドラインとアドバイスについて説明しています。
貢献することを考えているなら、まずはこのドキュメントを読んで、このプロジェクトにどのように貢献していけるかを感じてみて下さい。
不明な点があるなら、主要メンテナの `Ian Cordasco`_ か `Cory Benfield`_ のどちらかに気軽に聞いて下さい。

.. _Ian Cordasco: http://www.coglib.com/~icordasc/
.. _Cory Benfield: https://lukasa.co.uk/about

.. If you have non-technical feedback, philosophical ponderings, crazy ideas, or
   other general thoughts about Requests or its position within the Python
   ecosystem, the BDFL, `Kenneth Reitz`_, would love to hear from you.

技術的なこと以外のフィードバック、哲学的な考え、クレイジーなアイデア、Python エコシステム内での位置づけや Requests についてのその他の一般的な考えがある場合、
BDFL である `Kenneth Reitz`_ は、あなたからの意見に耳を傾けます。

.. The guide is split into sections based on the type of contribution you're
   thinking of making, with a section that covers general guidelines for all
   contributors.

このガイドは、作成しようと考えているコントリビューションの方法によって分類され、
全てのコントリビューター用の標準のガイドラインを網羅している分野のどこかに属します。

.. _Kenneth Reitz: mailto:me@kennethreitz.org

Be Cordial
----------

    **Be cordial or be on your way**. *—Kenneth Reitz*

.. Requests has one very important rule governing all forms of contribution,
   including reporting bugs or requesting features. This golden rule is
   "`be cordial or be on your way`_".

Requests は、バグ報告や機能要望を含む全ての形式のコントリビューションを管理するためのとても重要なルールが1つあります。
このゴールデンルールは、「`be cordial or be on your way`_」です。。

.. **All contributions are welcome**, as long as
   everyone involved is treated with respect.

関係する全ての人に対して敬意を払っている限り、**全てのコントリビューションは歓迎します**。

.. _be cordial or be on your way: http://kennethreitz.org/be-cordial-or-be-on-your-way/

.. _early-feedback:

早めにフィードバックをもらいましょう
------------------------------------

.. Get Early Feedback
   ------------------

.. If you are contributing, do not feel the need to sit on your contribution until
   it is perfectly polished and complete. It helps everyone involved for you to
   seek feedback as early as you possibly can. Submitting an early, unfinished
   version of your contribution for feedback in no way prejudices your chances of
   getting that contribution accepted, and can save you from putting a lot of work
   into a contribution that is not suitable for the project.

プロジェクトに参加している場合、完璧になるまで作業を完了させるまで努力しようとする必要性を感じないで下さい。
プロジェクトに関わっている人のだれかが、できるだけ早くフィードバックを得れるようにサポートしてくれます。
フィードバックを受けるための未完成版のコントリビューションを早めに送ることで、
コントリビューションが受け入れられる可能性があるかどうかを判断する機会があり、
プロジェクトに適さないコントリビューションに多くの労力を費やすことを防いでくれます。

Contribution Suitability
------------------------

.. Our project maintainers have the last word on whether or not a contribution is
   suitable for Requests. All contributions will be considered carefully, but from
   time to time, contributions will be rejected because they do not suit the
   current goals or needs of the project.

プロジェクトのメンテナは、コントリビューションが Requests に適しているかどうかの最終権限を持っています。
全てのコントリビューションは慎重に検討され、プロジェクトの現在の目標やニーズにあわない場合に拒否されます。

.. If your contribution is rejected, don't despair! As long as you followed these
   guidelines, you will have a much better chance of getting your next
   contribution accepted.

コントリビューションが拒否された場合、絶望しないで下さい！
これらのガイドラインに従っている限り、次のコントリビューションが受け入れられるさらなるチャンスがあると思います。

.. Code Contributions
   ------------------

コードへのコントリビューション
------------------------------------

.. Steps for Submitting Code
   ~~~~~~~~~~~~~~~~~~~~~~~~~

修正したコードを送る際のステップ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. When contributing code, you'll want to follow this checklist:

コードへのコントリビューションを行う際は、以下のチェックリストに従う必要があります。:

.. Fork the repository on GitHub.
.. Run the tests to confirm they all pass on your system. If they don't, you'll
   need to investigate why they fail. If you're unable to diagnose this
   yourself, raise it as a bug report by following the guidelines in this
   document: :ref:`bug-reports`.
.. Write tests that demonstrate your bug or feature. Ensure that they fail.
.. Make your change.
.. Run the entire test suite again, confirming that all tests pass *including
   the ones you just added*.
.. Send a GitHub Pull Request to the main repository's ``master`` branch.
   GitHub Pull Requests are the expected method of code collaboration on this
   project.

1. GitHub のリポジトリをフォークします。
2. テストを実行して、全てのシステムが問題なく通ることを確認して下さい。
   テストが通らなかった場合、なぜテストが失敗するのか調べる必要があります。
   調べてもわからなかった場合、このドキュメントのガイドラインに従って :ref:`bug-reports` の報告をして下さい。
3. バグや機能のデモをするためのテストを書いて下さい。テストが失敗することを確認してください。
4. 変更を加えます。
5. テストスイート全体を再度実行して、*追加したばかりのテスト* が全て通ったことを確認して下さい。
6. メインリポジトリの ``master`` ブランチにプルリクエストを送ります。
   GitHub のプルリクエストは、このプロジェクトで必要とされているコードのコラボレーション方法を提供している機能です。

.. The following sub-sections go into more detail on some of the points above.

以下の章では、以上の幾つかのポイントについて詳細に説明しています。

.. Code Review
   ~~~~~~~~~~~

コードレビュー
~~~~~~~~~~~~~~~~

.. Contributions will not be merged until they've been code reviewed. You should
   implement any code review feedback unless you strongly object to it. In the
   event that you object to the code review feedback, you should make your case
   clearly and calmly. If, after doing so, the feedback is judged to still apply,
   you must either apply the feedback or withdraw your contribution.

プロジェクトへのコントリビューションは、コードレビューされるまで、マージされません。
強く反対しない限り、コードへのレビューのフィードバックは修正する必要があります。
コードレビューへのフィードバックに異議を唱える場合、状況を整理して、落ち着いて下さい。
その後、フィードバックが有効だと判断された場合は、フィードバックを適用するか、コントリビューションを取り消す必要があります。

.. New Contributors
   ~~~~~~~~~~~~~~~~

新規のコントリビューター
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. If you are new or relatively new to Open Source, welcome! Requests aims to
   be a gentle introduction to the world of Open Source. If you're concerned about
   how best to contribute, please consider mailing a maintainer (listed above) and
   asking for help.

オープンソースプロジェクトへの参加を比較的最近はじめた人であれば、歓迎します！
Requests はオープンソースの世界への第一歩となることを目指しています。
どのように参加するかが心配しているなら、(上で掲載している)メンテナにメールを送って、助けになることがあるか聞いてみて下さい。

.. Please also check the :ref:`early-feedback` section.

:ref:`early-feedback` の章もあるので、確認してみて下さい。

.. Kenneth Reitz's Code Style™
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kenneth Reitz のコードスタイル™
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. The Requests codebase uses the `PEP 8`_ code style.

Requests は、`PEP 8`_ のコードスタイルを基にしています。

.. In addition to the standards outlined in PEP 8, we have a few guidelines:

PEP 8 で述べられている基準に加えて、いくつかのガイドラインがあります。:

.. Line-length can exceed 79 characters, to 100, when convenient.
.. Line-length can exceed 100 characters, when doing otherwise would be *terribly* inconvenient.
.. Always use single-quoted strings (e.g. ``'#flatearth'``), unless a single-quote occurs within the string.

- 行の長さは、状況によって79文字を超えて、100文字までにすることができます。
- 行の長さは、100文字を超えることができ、そうしないと不便なことがあります。
- 文字列内にシングルクォートが含まれていない限り、文字列はシングルクォートを使って下さい(例: ``'#flatearth'``)。

.. Additionally, one of the styles that PEP8 recommends for `line continuations`_
   completely lacks all sense of taste, and is not to be permitted within
   the Requests codebase::

さらに、`line continuations`_ として PEP8 が推奨しているスタイルの1つは全然良くなくて、
Requests のコードでは許可していません。::

    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

.. No. Just don't. Please.

良くないです、お願いですからそのように書かないで下さい。

.. Docstrings are to follow the following syntaxes::

Docstrings は、以下のようなシンタックスにしてください。::

    def the_earth_is_flat():
        """NASA divided up the seas into thirty-three degrees."""
        pass

::

    def fibonacci_spiral_tool():
        """With my feet upon the ground I lose myself / between the sounds
        and open wide to suck it in. / I feel it move across my skin. / I'm
        reaching up and reaching out. / I'm reaching for the random or
        whatever will bewilder me. / Whatever will bewilder me. / And
        following our will and wind we may just go where no one's been. /
        We'll ride the spiral to the end and may just go where no one's
        been.

        Spiral out. Keep going...
        """
        pass

.. All functions, methods, and classes are to contain docstrings. Object data
   model methods (e.g. ``__repr__``) are typically the exception to this rule.

すべての関数、メソッド、クラスに、Docstrings が含まれています。
通常のオブジェクトのデータモデルのメソッド(例: ``__repr__``)は、このルールの適用外です。

.. Thanks for helping to make the world a better place!

世の中が良くなるために協力してくれて有難うございます！

.. _PEP 8: http://pep8.org
.. _line continuations: https://www.python.org/dev/peps/pep-0008/#indentation

.. Documentation Contributions
   ---------------------------

ドキュメントへの貢献
--------------------------------

.. Documentation improvements are always welcome! The documentation files live in
   the ``docs/`` directory of the codebase. They're written in
   `reStructuredText`_, and use `Sphinx`_ to generate the full suite of
   documentation.

ドキュメントの改善は、いつでも歓迎します！
ドキュメントのファイルは、コードの ``docs/`` ディレクトリにあります。
ドキュメントのファイルは、`reStructuredText`_ で書かれていて、
`Sphinx`_ を使ってドキュメント全体を生成しています。

.. When contributing documentation, please do your best to follow the style of the
   documentation files. This means a soft-limit of 79 characters wide in your text
   files and a semi-formal, yet friendly and approachable, prose style.

ドキュメントに貢献する際は、ドキュメントファイルのスタイルに極力従うようにして下さい。
これは、テキストファイルの半角79文字幅の、半分正式ですが親しみやすい書式の、
ゆるい制限があることを意味しています。

.. When presenting Python code, use single-quoted strings (``'hello'`` instead of
   ``"hello"``).

Python コードを表示する際は、
シングルクォーテーションの文字列(``"hello"`` ではなく ``'hello'``)にしてください。

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org/index.html


.. _bug-reports:

バグレポート
----------------

.. Bug Reports
   -----------

.. Bug reports are hugely important! Before you raise one, though, please check
   through the `GitHub issues`_, **both open and closed**, to confirm that the bug
   hasn't been reported before. Duplicate bug reports are a huge drain on the time
   of other contributors, and should be avoided as much as possible.

バグレポートはとても重要です！
しかし、バグが既に報告されていないことを確認するために、
`GitHub issues`_ の **Open と Closed** をチェックして下さい。
重複したバグレポートは、他のコントリビューターの時間の大幅な無駄になるので、できるだけ避けたいです。

.. _GitHub issues: https://github.com/requests/requests/issues


.. Feature Requests
   ----------------

機能要望
-------------------

.. Requests is in a perpetual feature freeze, only the BDFL can add or approve of
   new features. The maintainers believe that Requests is a feature-complete
   piece of software at this time.

Requests は機能追加を停止していて、BDFL のみが新しい機能を追加、承認することができます。
メンテナは、Requests は現時点では機能を満たしたソフトウェアであると考えています。

.. One of the most important skills to have while maintaining a largely-used
   open source project is learning the ability to say "no" to suggested changes,
   while keeping an open ear and mind.

幅広く使われているオープンソースのプロジェクトを維持し続けるための重要なスキルの1つとして、
耳を傾ける心を保ちながら、提案されたことに「NO」と言えるようになることです。

.. If you believe there is a feature missing, feel free to raise a feature
   request, but please do be aware that the overwhelming likelihood is that your
   feature request will not be accepted.

機能が不足していると思った場合、機能要望を気軽にお寄せ下さい。
しかし、機能要望が受け入れられないこともあることにも注意して下さい。
