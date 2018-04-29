.. _faq:

.. Frequently Asked Questions
   ==========================

よくある質問
==========================

.. This part of the documentation answers common questions about Requests.

ドキュメントのこの章では Requests についての一般的な質問について答えます。

.. Encoded Data?
   -------------

エンコードされたデータ
--------------------------

.. Requests automatically decompresses gzip-encoded responses, and does
   its best to decode response content to unicode when possible.

Requests は、gzip エンコードされたレスポンスを自動的に解凍し、
可能な限り Unicode に対応するレスポンスコンテンツにデコードしようとします。

.. You can get direct access to the raw response (and even the socket),
   if needed as well.

必要に応じて、生のレスポンス(さらにはソケット)に直接アクセスすることができます。

.. Custom User-Agents?
   -------------------

独自のユーザーエージェント
------------------------------

.. Requests allows you to easily override User-Agent strings, along with
   any other HTTP Header.

Requests は、他の HTTP ヘッダーと同じように User-Agent 文字列を簡単に上書きすることができます。

.. Why not Httplib2?
   -----------------

なぜHttplib2ではないのですか?
----------------------------------

.. Chris Adams gave an excellent summary on
   `Hacker News <http://news.ycombinator.com/item?id=2884406>`_:

Chris Adamsさんは、`Hacker News <http://news.ycombinator.com/item?id=2884406>`_ の投稿で、
すばらしい見解を与えてくれました。

    httplib2 is part of why you should use requests: it's far more respectable
    as a client but not as well documented and it still takes way too much code
    for basic operations. I appreciate what httplib2 is trying to do, that
    there's a ton of hard low-level annoyances in building a modern HTTP
    client, but really, just use requests instead. Kenneth Reitz is very
    motivated and he gets the degree to which simple things should be simple
    whereas httplib2 feels more like an academic exercise than something
    people should use to build production systems[1].

    Disclosure: I'm listed in the requests AUTHORS file but can claim credit
    for, oh, about 0.0001% of the awesomeness.

    1. http://code.google.com/p/httplib2/issues/detail?id=96 is a good example:
    an annoying bug which affect many people, there was a fix available for
    months, which worked great when I applied it in a fork and pounded a couple
    TB of data through it, but it took over a year to make it into trunk and
    even longer to make it onto PyPI where any other project which required "
    httplib2" would get the working version.


.. Python 3 Support?
   -----------------

Python 3はサポートしていますか？
----------------------------------

.. Yes! Here's a list of Python platforms that are officially
   supported:

はい！公式にサポートしている Python のプラットフォームは以下の通りです。:

* Python 2.6
* Python 2.7
* Python 3.4
* Python 3.5
* Python 3.6
* PyPy

.. What are "hostname doesn't match" errors?
   -----------------------------------------

"hostname doesn't match" というエラーは何ですか？
--------------------------------------------------------

.. These errors occur when :ref:`SSL certificate verification <verification>`
   fails to match the certificate the server responds with to the hostname
   Requests thinks it's contacting. If you're certain the server's SSL setup is
   correct (for example, because you can visit the site with your browser) and
   you're using Python 2.6 or 2.7, a possible explanation is that you need
   Server-Name-Indication.

これらのエラーは、:ref:`SSL certificate verification <verification>` で、
Requests がアクセス使用しているサーバーのホスト名の証明書と一致しない時に発生します。
サーバーの SSL 設定が正しい(例として、ブラウザでサイトにアクセスできるか)ことが確認できた場合に、
Python 2.6 か 2.7 を使っている場合は、Server-Name-Indication が必要です。

.. `Server-Name-Indication`_, or SNI, is an official extension to SSL where the
   client tells the server what hostname it is contacting. This is important
   when servers are using `Virtual Hosting`_. When such servers are hosting
   more than one SSL site they need to be able to return the appropriate
   certificate based on the hostname the client is connecting to.

`Server-Name-Indication`_ (SNI)は、クライアントがサーバーにどのホスト名に接続しているかを伝える SSL の正式な拡張です。
サーバーが `Virtual Hosting`_ を使っている場合は、これは重要です。
このようなサーバーが1つ以上の SSL サイトをホストしている場合、
クライアントが接続しているホスト名に基いて適切な証明書を返却する必要があります。

.. Python3 and Python 2.7.9+ include native support for SNI in their SSL modules.
   For information on using SNI with Requests on Python < 2.7.9 refer to this
   `Stack Overflow answer`_.

Python3 と Python 2.7.9 以上には SSL モジュールの SNI のネイティブサポートが含まれています。
Python 2.7.9 未満の Requests で SNI を使う方法については、`Stack Overflow answer`_ を参照して下さい。

.. _`Server-Name-Indication`: https://en.wikipedia.org/wiki/Server_Name_Indication
.. _`virtual hosting`: https://en.wikipedia.org/wiki/Virtual_hosting
.. _`Stack Overflow answer`: https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484
