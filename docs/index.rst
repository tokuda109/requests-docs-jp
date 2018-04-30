.. Requests documentation master file, created by
   sphinx-quickstart on Sun Feb 13 23:54:25 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Requests: HTTP for Humans
=========================

Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://img.shields.io/pypi/l/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://img.shields.io/pypi/wheel/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://img.shields.io/pypi/pyversions/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://codecov.io/github/requests/requests/coverage.svg?branch=master
    :target: https://codecov.io/github/requests/requests
    :alt: codecov.io

.. image:: https://img.shields.io/badge/Say%20Thanks!-🦉-1EAEDB.svg
    :target: https://saythanks.io/to/kennethreitz


.. **Requests** is the only *Non-GMO* HTTP library for Python, safe for human
   consumption.

**Requests** は、人が使いやすいように考慮された Python 用の *遺伝子組み換えがされていない* HTTP ライブラリです。

.. *Warning: Recreational use of the Python standard library for HTTP may result in dangerous side-effects,
   including: security vulnerabilities, verbose code, reinventing the wheel,
   constantly reading documentation, depression, headaches, or even death.*

*警告: Python の HTTP 用の標準ライブラリを気軽に使うと、
セキュリティ上の脆弱性、コードの冗長化、車輪の再発明等の危険な副作用が生じる可能性があります。*

-------------------

.. **Behold, the power of Requests**::

**Requests の良さを御覧ください**::

    >>> import requests
    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'private_gists': 419, u'total_private_repos': 77, ...}

.. See `similar code, sans Requests <https://gist.github.com/973705>`_.

`Requests を使わない場合のコード <https://gist.github.com/973705>`_ も参照してみて下さい。

.. **Requests** allows you to send *organic, grass-fed* HTTP/1.1 requests, without the
   need for manual labor. There's no need to manually add query strings to your
   URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling
   are 100% automatic, thanks to `urllib3 <https://github.com/shazow/urllib3>`_.

**Requests** を使用すると、手作業を必要とせずに、*organic, grass-fed* な HTTP/1.1 リクエストを送信することができます。
クエリ文字列を URL に追加したり、POST データをフォームエンコードしたりを手動でする必要はありません。
Keep-alive と HTTP のコネクションプールは、`urllib3 <https://github.com/shazow/urllib3>`_ のおかげで100%自動で行われます。

.. User Testimonials
   -----------------

推薦文
-----------------

.. Twitter, Spotify, Microsoft, Amazon, Lyft, BuzzFeed, Reddit, The NSA, Her Majesty's Government, Google, Twilio, Runscope, Mozilla, Heroku,
   PayPal, NPR, Obama for America, Transifex, Native Instruments, The Washington
   Post, SoundCloud, Kippt, Sony, and Federal U.S.
   Institutions that prefer to be unnamed claim to use Requests internally.

Twitter、Spotify、Microsoft、Amazon、Lyft、BuzzFeed、Reddit、NSA、イギリス政府、Google、
Twilio、Runscope、Mozilla、Heroku、PayPal、NPR、Obama for America、Transifex、Native Instruments、
ワシントン・ポスト、SoundCloud、Kippt、Sony、アメリカ合衆国連邦政府は、公表していませんが内部的に Requests を使っています。

**Armin Ronacher**—
    .. *Requests is the perfect example how beautiful an API can be with the
       right level of abstraction.*

    *Requests は、どれくらい API が適切な抽象レベルで美しくできるかの完璧な例です。*

**Matt DeBoard**—
    .. *I'm going to get Kenneth Reitz's Python requests module tattooed
       on my body, somehow. The whole thing.*

    *Kenneth Reitz の Python のリクエストモジュールの入れ墨を体に入れようと思います。以上。*

**Daniel Greenfeld**—
    .. *Nuked a 1200 LOC spaghetti code library with 10 lines of code thanks to
       Kenneth Reitz's request library. Today has been AWESOME.*

    *Kenneth Reitz のリクエストライブラリのおかげで10行のコードで1200行のスパゲッティコードと同じことができます。すばらしい時代になりました。*

**Kenny Meyers**—
    .. *Python HTTP: When in doubt, or when not in doubt, use Requests. Beautiful,
       simple, Pythonic.*

    *Python HTTP: 使うか迷った時も、迷わなかった時も、Requests を使います。美しく、シンプルで、Pythonic です。*

.. Requests is one of the most downloaded Python packages of all time, pulling in
   over 11,000,000 downloads every month. All the cool kids are doing it!

Requests は最も多くダウンロードされている Python パッケージの1つで、毎月11,000,000回以上ダウンロードされています。
賢い人はみんな使っています！

.. Beloved Features
   ----------------

愛する機能
----------------

.. Requests is ready for today's web.

Requestsは、今日(こんにち)のウェブに欠かせない機能を持っています。

.. Keep-Alive & Connection Pooling
.. International Domains and URLs
.. Sessions with Cookie Persistence
.. Browser-style SSL Verification
.. Automatic Content Decoding
.. Basic/Digest Authentication
.. Elegant Key/Value Cookies
.. Automatic Decompression
.. Unicode Response Bodies
.. HTTP(S) Proxy Support
.. Multipart File Uploads
.. Streaming Downloads
.. Connection Timeouts
.. Chunked Requests
.. ``.netrc`` Support

- キープアライブとコネクションプール
- ドメインとURLの国際化
- Cookie によるセッションの永続化
- ブラウザスタイルの SSL 検証
- 自動のコンテンツデコード
- Basic/Digest 認証
- 自動な解凍
- エレガントなキーと値の Cookies
- Unicode レスポンスボディ
- HTTP(S) プロキシのサポート
- マルチパートのファイルアップロード
- ストリーミング形式のダウンロード
- コネクションのタイムアウト
- チャンク化されたリクエスト
- ``.netrc`` のサポート

.. Requests officially supports Python 2.6–2.7 & 3.4–3.7, and runs great on PyPy.

Requests は公式に Python 2.6〜2.7 と 3.4〜3.7をサポートしていて、PyPyでも動きます。

.. The User Guide
   --------------

ユーザーガイド
--------------

.. This part of the documentation, which is mostly prose, begins with some
   background information about Requests, then focuses on step-by-step
   instructions for getting the most out of Requests.

ドキュメントのこの章では、Requests に関するバックグランドをいくつか紹介します。
それから、Requests を最大限使いこなすための説明をステップ・バイ・ステップで説明しています。

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/advanced
   user/authentication


.. The Community Guide
   -------------------

コミュニティガイド
----------------------

.. This part of the documentation, which is mostly prose, details the
   Requests ecosystem and community.

ドキュメントのこの章では、Requests のエコシステムやコミュニティについて紹介します。

.. toctree::
   :maxdepth: 1

   community/faq
   community/recommended
   community/out-there
   community/support
   community/vulnerabilities
   community/updates
   community/release-process

.. The API Documentation / Guide
   -----------------------------

APIドキュメント / ガイド
--------------------------------

.. If you are looking for information on a specific function, class, or method,
   this part of the documentation is for you.

特定の関数、クラス、メソッドの情報を探しているなら、ドキュメントのこの章が役に立つと思います。

.. toctree::
   :maxdepth: 2

   api


.. The Contributor Guide
   ---------------------

コントリビューターの方のガイド
---------------------------------

.. If you want to contribute to the project, this part of the documentation is for
   you.

プロジェクトに参加する場合、以下のドキュメントが役に立つと思います。

.. toctree::
   :maxdepth: 3

   dev/contributing
   dev/philosophy
   dev/todo
   dev/authors

.. There are no more guides. You are now guideless.
   Good luck.

これ以上の説明はありませんし、もう必要ないと思います。グッド・ラック。
