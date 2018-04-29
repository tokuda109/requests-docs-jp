.. Vulnerability Disclosure
   ========================

脆弱性の開示
===========================

.. If you think you have found a potential security vulnerability in requests,
   please email `sigmavirus24 <mailto:graffatcolmingov@gmail.com>`_ and
   `Lukasa <mailto:cory@lukasa.co.uk>`_ directly. **Do not file a public issue.**

Requests に潜在的なセキュリティ上の脆弱性があると思われる場合、
`sigmavirus24 <mailto:graffatcolmingov@gmail.com>`_ と `Lukasa <mailto:cory@lukasa.co.uk>`_ に
直接メールしてください。**一般的な Issue は送らないで下さい。**

.. Our PGP Key fingerprints are:

PGP キーのフィンガープリントは以下のとおりです。:

- 0161 BB7E B208 B5E0 4FDC  9F81 D9DA 0A04 9113 F853 (@sigmavirus24)

- 90DC AE40 FEA7 4B14 9B70  662D F25F 2144 EEC1 373D (@lukasa)

.. If English is not your first language, please try to describe the problem and
   its impact to the best of your ability. For greater detail, please use your
   native language and we will try our best to translate it using online services.

英語が母国語ではない場合、不具合を可能な限り伝わるように説明することを心がけて下さい。
詳細については、母国語を使用して下さい。
オンラインサービスを使って翻訳することをお勧めします。

.. Please also include the code you used to find the problem and the shortest
   amount of code necessary to reproduce it.

不具合を探すために使ったコードと、再現するために必要な短いコードも含めるようにして下さい。

.. Please do not disclose this to anyone else. We will retrieve a CVE identifier
   if necessary and give you full credit under whatever name or alias you provide.
   We will only request an identifier when we have a fix and can publish it in a
   release.

これは誰にも開示しないで下さい。
必要に応じて、CVE 識別子を取得し、提供する名前やエイリアスに基いてクレジットするようにします。
フィックスされる場合のみ識別子を要求し、リリースで公開することができます。

.. We will respect your privacy and will only publicize your involvement if you
   grant us permission.

私たちはプライバシーを尊重し、許可してもらった場合のみ関与したことを公開するようにします。

.. Process
   -------

プロセス
--------------

.. This following information discusses the process the requests project follows
   in response to vulnerability disclosures. If you are disclosing a
   vulnerability, this section of the documentation lets you know how we will
   respond to your disclosure.

以下の情報は、Requests プロジェクトが脆弱性の開示への対応に対するプロセスについて説明しています。
脆弱性を開示している場合、ドキュメントのこの章で、開示にどのように対応するか案内します。

.. Timeline
   ~~~~~~~~

タイムライン
~~~~~~~~~~~~~~~~

.. When you report an issue, one of the project members will respond to you within
   two days *at the outside*. In most cases responses will be faster, usually
   within 12 hours. This initial response will at the very least confirm receipt
   of the report.

不具合を報告すると、プロジェクトメンバーの1人が*遅くとも*2日以内に返答します。
ほとんどの場合、返答は早く、通常は12時間以内になります。
最初の返答は、レポートを受け取ったことの確認だけは少なくとも行います。

.. If we were able to rapidly reproduce the issue, the initial response will also
   contain confirmation of the issue. If we are not, we will often ask for more
   information about the reproduction scenario.

不具合を簡単に再現できた場合、最初の返答で不具合の確認が含まれることもあります。
そうでない場合、再現するための方法について説明を求めることもあります。

.. Our goal is to have a fix for any vulnerability released within two weeks of
   the initial disclosure. This may potentially involve shipping an interim
   release that simply disables function while a more mature fix can be prepared,
   but will in the vast majority of cases mean shipping a complete release as soon
   as possible.

私達の目標は、最初の開示から2週間以内にリリースされた脆弱性に対するフィックスを行うことです。
これは、きちんと時間をかけて不具合を修正するまでの間、機能を無効にする暫定リリースとして公開する可能性があります。
しかし、可能な限り早く完全なリリースとして公開することをほとんどの方が望みます。

.. Throughout the fix process we will keep you up to speed with how the fix is
   progressing. Once the fix is prepared, we will notify you that we believe we
   have a fix. Often we will ask you to confirm the fix resolves the problem in
   your environment, especially if we are not confident of our reproduction
   scenario.

フィックスするプロセスの全体として、修正がどのように進んでいるかを把握します。
修正済みが準備されたら、修正されたと信じて通知します。
特に再現する方法がわからない場合、自身の環境では不具合が解決されているか確認することもあります。

.. At this point, we will prepare for the release. We will obtain a CVE number
   if one is required, providing you with full credit for the discovery. We will
   also decide on a planned release date, and let you know when it is. This
   release date will *always* be on a weekday.

この時点で、リリースの準備をします。
必要なら CVE 番号を取得し、発見に対する報酬を支払います。
リリース日の計画を決め、決まった時点でお知らせします。
リリース日は*常に*平日になります。

.. At this point we will reach out to our major downstream packagers to notify
   them of an impending security-related patch so they can make arrangements. In
   addition, these packagers will be provided with the intended patch ahead of
   time, to ensure that they are able to promptly release their downstream
   packages. Currently the list of people we actively contact *ahead of a public
   release* is:

この時点で、パッケージ担当者に連絡して差し迫ったセキュリティ関連のパッチだということを通知し、手配します。
さらにパッケージ担当者はパッケージを素早くリリースできるようにパッチを提供します。
現在、一般公開前にアクティブに連絡している人のリストは以下のとおりです。:

- Jeremy Cline, Red Hat (@jeremycline)
- Daniele Tricoli, Debian (@eriol)

.. We will notify these individuals at least a week ahead of our planned release
   date to ensure that they have sufficient time to prepare. If you believe you
   should be on this list, please let one of the maintainers know at one of the
   email addresses at the top of this article.

準備に十分な時間があることを確認するために予定されたリリース日より少なくとも1週間前に個人宛に通知します。
このリストに掲載されるべきだと思うなら、この記事の一番上にあるメールアドレスの1つを使って、メンテナに知らせてください。

.. On release day, we will push the patch to our public repository, along with an
   updated changelog that describes the issue and credits you. We will then issue
   a PyPI release containing the patch.

リリース日に、公開リポジトリにパッチをプッシュし、不具合の説明とクレジットを更新する変更履歴を追加します。
パッチを含む PyPI リリースを公開します。

.. At this point, we will publicise the release. This will involve mails to
   mailing lists, Tweets, and all other communication mechanisms available to the
   core team.

この時点で、リリースされることを公表します。
これには、メーリングリスト、ツイート、コアチームが利用しているコミュニケーションツールが含まれています。

.. We will also explicitly mention which commits contain the fix to make it easier
   for other distributors and users to easily patch their own versions of requests
   if upgrading is not an option.

アップグレードがオプションではない場合、他のディストリビューターやユーザーが使っている Requests のバージョンに
パッチをあてやすくするために、どのコミットに修正が含まれているかを明示します。

.. Previous CVEs
   -------------

以前の CVE
----------------

- Fixed in 2.6.0

  - `CVE 2015-2296 <http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-2296>`_,
    reported by Matthew Daley of `BugFuzz <https://bugfuzz.com/>`_.

- Fixed in 2.3.0

  - `CVE 2014-1829 <http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2014-1829>`_

  - `CVE 2014-1830 <http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2014-1830>`_
