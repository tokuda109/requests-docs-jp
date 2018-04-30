.. _advanced:

高度な使い方
=================

.. Advanced Usage
   ==============

.. This document covers some of Requests more advanced features.

このドキュメントは、Requests のより高度な機能をいくつか紹介します。

.. _session-objects:

セッションオブジェクト
------------------------------

.. Session Objects
   ---------------

.. The Session object allows you to persist certain parameters across
   requests. It also persists cookies across all requests made from the
   Session instance, and will use ``urllib3``'s `connection pooling`_. So if
   you're making several requests to the same host, the underlying TCP
   connection will be reused, which can result in a significant performance
   increase (see `HTTP persistent connection`_).

Session オブジェクトは特定のパラメータをリクエスト間で永続化することができます。
``urllib3`` の `connection pooling`_ を使って、
Session インスタンスの全てのリクエストで Cookie が永続化することもできます。
したがって、同じホストに対して複数のリクエストを行う場合、基になる TCP 接続が再利用されるため、
パフォーマンスが大幅に向上します(`HTTP persistent connection`_ を参照して下さい)。

.. A Session object has all the methods of the main Requests API.

Session オブジェクトには、Requests の主な API の全てのメソッドがあります。

.. Let's persist some cookies across requests::

リクエスト間に渡る Cookie の永続化をやってみましょう::

    s = requests.Session()

    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')

    print(r.text)
    # '{"cookies": {"sessioncookie": "123456789"}}'


.. Sessions can also be used to provide default data to the request methods. This
   is done by providing data to the properties on a Session object::

セッションはリクエストのメソッドにデフォルトデータを提供するためにも使用することができます。
これは Session オブジェクトのプロパティにデータを提供することに行われます。::

    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})

    # both 'x-test' and 'x-test2' are sent
    s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})


.. Any dictionaries that you pass to a request method will be merged with the
   session-level values that are set. The method-level parameters override session
   parameters.

リクエストのメソッドに渡す任意のディクショナリは、設定されたセッションレベルの値とマージされます。
メソッドレベルのパラメータは、セッションパラメータを上書きします。

.. Note, however, that method-level parameters will *not* be persisted across
   requests, even if using a session. This example will only send the cookies
   with the first request, but not the second::

注意することとして、セッションを使ってもメソッドレベルのパラメータはリクエスト間で**永続化されません**。
以下の例では、最初のリクエストで Cookie を送信しますが、二回目は送信しません。::

    s = requests.Session()

    r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
    print(r.text)
    # '{"cookies": {"from-my": "browser"}}'

    r = s.get('http://httpbin.org/cookies')
    print(r.text)
    # '{"cookies": {}}'


.. If you want to manually add cookies to your session, use the
   :ref:`Cookie utility functions <api-cookies>` to manipulate
   :attr:`Session.cookies <requests.Session.cookies>`.

セッションに Cookie を手動で追加する場合、:ref:`Cookie utility functions <api-cookies>` を使って、
:attr:`Session.cookies <requests.Session.cookies>` を操作します。

.. Sessions can also be used as context managers::

セッションはコンテキストマネージャーとしても使えます。::

    with requests.Session() as s:
        s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

.. This will make sure the session is closed as soon as the ``with`` block is
   exited, even if unhandled exceptions occurred.

これにより、例外が処理できなかったとしても、
``with`` ブロックが終了するとすぐにセッションを閉じることを保証しています。

.. Remove a Value From a Dict Parameter

    Sometimes you'll want to omit session-level keys from a dict parameter. To
    do this, you simply set that key's value to ``None`` in the method-level
    parameter. It will automatically be omitted.

.. admonition:: 辞書パラメータから値の削除

    場合によっては辞書パラメータからセッションレベルのキーを省略したい場合があります。
    これをするには、メソッドレベルのパラメータでキーの値をシンプルに ``None`` を設定するだけです。
    自動的に省略されます。

.. All values that are contained within a session are directly available to you.
   See the :ref:`Session API Docs <sessionapi>` to learn more.

セッションに含まれている全ての値を直接アクセスすることができます。
詳しくは、:ref:`Session API Docs <sessionapi>` を参照して下さい。

.. _request-and-response-objects:

リクエストとレスポンスのオブジェクト
--------------------------------------------------------

.. Request and Response Objects
   ----------------------------

.. Whenever a call is made to ``requests.get()`` and friends, you are doing two
   major things. First, you are constructing a ``Request`` object which will be
   sent off to a server to request or query some resource. Second, a ``Response``
   object is generated once Requests gets a response back from the server.
   The ``Response`` object contains all of the information returned by the server and
   also contains the ``Request`` object you created originally. Here is a simple
   request to get some very important information from Wikipedia's servers::

``requests.get()`` や類似のメソッドを呼び出すたびに、2つの主要なことをしていることになります。
まず、``Request`` オブジェクトを生成して、リソースをサーバーに要求するために送信します。
次に、Requests がサーバーからのレスポンスを受け取ると ``Response`` オブジェクトが生成されます。
``Response`` オブジェクトは、サーバーから返却された情報が全て含まれていて、
元となった ``Request`` オブジェクトも含まれています。
以下は、Wikipedia のサーバーからいくつかのとても重要な情報を取得するためのシンプルなリクエストです。::

    >>> r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')

.. If we want to access the headers the server sent back to us, we do this::

サーバーから返却されたヘッダーにアクセスするには以下のようにします。::

    >>> r.headers
    {'content-length': '56170', 'x-content-type-options': 'nosniff', 'x-cache':
    'HIT from cp1006.eqiad.wmnet, MISS from cp1010.eqiad.wmnet', 'content-encoding':
    'gzip', 'age': '3080', 'content-language': 'en', 'vary': 'Accept-Encoding,Cookie',
    'server': 'Apache', 'last-modified': 'Wed, 13 Jun 2012 01:33:50 GMT',
    'connection': 'close', 'cache-control': 'private, s-maxage=0, max-age=0,
    must-revalidate', 'date': 'Thu, 14 Jun 2012 12:59:39 GMT', 'content-type':
    'text/html; charset=UTF-8', 'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,
    MISS from cp1010.eqiad.wmnet:80'}

.. However, if we want to get the headers we sent the server, we simply access the
   request, and then the request's headers::

しかし、サーバーから返却されたヘッダーを取得する場合は、リクエストにアクセスし、リクエストのヘッダーにアクセスするだけです。::

    >>> r.request.headers
    {'Accept-Encoding': 'identity, deflate, compress, gzip',
    'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0'}

.. _prepared-requests:

Prepared Requests
-----------------

.. Whenever you receive a :class:`Response <requests.Response>` object
   from an API call or a Session call, the ``request`` attribute is actually the
   ``PreparedRequest`` that was used. In some cases you may wish to do some extra
   work to the body or headers (or anything else really) before sending a
   request. The simple recipe for this is the following::

API や Session の呼び出しから :class:`Response <requests.Response>` オブジェクトを受け取る際に、
``request`` 属性は、その際に使われた ``PreparedRequest`` となっています。
場合によって、リクエストを送信する前にボディやヘッダー(または他のもの)に追加作業をしたいことがあります。
簡単なやりかたは以下のとおりです。::

    from requests import Request, Session

    s = Session()

    req = Request('POST', url, data=data, headers=headers)
    prepped = req.prepare()

    # do something with prepped.body
    prepped.body = 'No, I want exactly this as the body.'

    # do something with prepped.headers
    del prepped.headers['Content-Type']

    resp = s.send(prepped,
        stream=stream,
        verify=verify,
        proxies=proxies,
        cert=cert,
        timeout=timeout
    )

    print(resp.status_code)

.. Since you are not doing anything special with the ``Request`` object, you
   prepare it immediately and modify the ``PreparedRequest`` object. You then
   send that with the other parameters you would have sent to ``requests.*`` or
   ``Session.*``.

``Request`` オブジェクトは特別なことを何もしていないので、すぐに``PreparedRequest`` オブジェクト
それから ``requests.*`` や ``Session.*`` に送信した他のパラメータとともに送信します。

.. However, the above code will lose some of the advantages of having a Requests
   :class:`Session <requests.Session>` object. In particular,
   :class:`Session <requests.Session>`-level state such as cookies will
   not get applied to your request. To get a
   :class:`PreparedRequest <requests.PreparedRequest>` with that state
   applied, replace the call to :meth:`Request.prepare()
   <requests.Request.prepare>` with a call to
   :meth:`Session.prepare_request() <requests.Session.prepare_request>`, like this::

しかし、上記のコードは Requests の :class:`Session <requests.Session>` オブジェクトの利点をいくつか失います。
特に、Cookie のような :class:`Session <requests.Session>` レベルの状態についてはリクエストに適用されません。
その状態が適用された :class:`PreparedRequest <requests.PreparedRequest>` を得るには、
:meth:`Request.prepare() <requests.Request.prepare>` を呼び出して、以下のように
:meth:`Session.prepare_request() <requests.Session.prepare_request>` を呼び出すことで置換します。::

    from requests import Request, Session

    s = Session()
    req = Request('GET',  url, data=data, headers=headers)

    prepped = s.prepare_request(req)

    # do something with prepped.body
    prepped.body = 'Seriously, send exactly these bytes.'

    # do something with prepped.headers
    prepped.headers['Keep-Dead'] = 'parrot'

    resp = s.send(prepped,
        stream=stream,
        verify=verify,
        proxies=proxies,
        cert=cert,
        timeout=timeout
    )

    print(resp.status_code)

.. _verification:

SSL 証明書の検証
---------------------

.. SSL Cert Verification
   ---------------------

.. Requests verifies SSL certificates for HTTPS requests, just like a web browser.
   By default, SSL verification is enabled, and Requests will throw a SSLError if
   it's unable to verify the certificate::

Requests は、ウェブブラウザと同様に、HTTPS のリクエストの際に、SSL 証明書を検証します。
デフォルトでは、SSL 証明書の検証が有効になっていて、Requests が証明書を検証できなかった場合、
SSLError を送出します。

    >>> requests.get('https://requestb.in')
    requests.exceptions.SSLError: hostname 'requestb.in' doesn't match either of '*.herokuapp.com', 'herokuapp.com'

.. I don't have SSL setup on this domain, so it throws an exception. Excellent. GitHub does though::

このドメインの SSL のセットアップを持っていないので、例外が送出されます。
いいですね。GitHub does though::

    >>> requests.get('https://github.com')
    <Response [200]>

.. You can pass ``verify`` the path to a CA_BUNDLE file or directory with certificates of trusted CAs::

信頼できる認証局の証明書の CA_BUNDLE ファイルかディレクトリへのパスを ``verify`` に渡すことができます。::

    >>> requests.get('https://github.com', verify='/path/to/certfile')

.. or persistent::

もしくは永続化するには::

    s = requests.Session()
    s.verify = '/path/to/certfile'

.. If ``verify`` is set to a path to a directory, the directory must have been processed using
   the c_rehash utility supplied with OpenSSL.

.. note:: ``verify`` がディレクトリへのパスに設定されている場合、そのディレクトリは OpenSSL に付属の c_rehash ユーティリティを使用して処理されている必要があります。

.. This list of trusted CAs can also be specified through the ``REQUESTS_CA_BUNDLE`` environment variable.

信頼できる認証局のリストは、``REQUESTS_CA_BUNDLE`` の環境変数で指定することもできます。

.. Requests can also ignore verifying the SSL certificate if you set ``verify`` to False::

``verify`` を False にした場合、Requests は SSL 証明書の検証を無視します。::

    >>> requests.get('https://kennethreitz.org', verify=False)
    <Response [200]>

.. By default, ``verify`` is set to True. Option ``verify`` only applies to host certs.

デフォルトでは、``verify`` は True に設定されています。オプションの ``verify`` はホスト証明書にのみ適用されます。

.. Client Side Certificates
   ------------------------

クライアント側の証明書
---------------------------

.. You can also specify a local cert to use as client side certificate, as a single
   file (containing the private key and the certificate) or as a tuple of both
   files' paths::

1ファイル(秘密鍵と証明書を含む)として指定するか、両ファイルのタプルとして指定するかで
クライアント側の証明書として使用するローカルの証明書を指定することができます。::

    >>> requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
    <Response [200]>

.. or persistent::

もしくは永続化するには::

    s = requests.Session()
    s.cert = '/path/client.cert'

.. If you specify a wrong path or an invalid cert, you'll get a SSLError::

間違ったパスや無効な証明書を指定すると、SSLError が送出されます。::

    >>> requests.get('https://kennethreitz.org', cert='/wrong_path/client.pem')
    SSLError: [Errno 336265225] _ssl.c:347: error:140B0009:SSL routines:SSL_CTX_use_PrivateKey_file:PEM lib

.. The private key to your local certificate *must* be unencrypted.
   Currently, Requests does not support using encrypted keys.

.. warning:: ローカルの証明書の秘密鍵は暗号化されていないようにしておきます。
             現在、Requests は暗号化されたキーを使う機能をサポートしていません。

.. _ca-certificates:

認証局の証明書
------------------

.. CA Certificates
   ---------------

.. By default, Requests bundles a set of root CAs that it trusts, sourced from the
   `Mozilla trust store`_. However, these are only updated once for each Requests
   version. This means that if you pin a Requests version your certificates can
   become extremely out of date.

デフォルトで、Requests は信頼できるルート認証局の一覧を `Mozilla trust store`_ から取得してバンドルしています。
しかし、この一覧は Requests の各バージョンごとに一度更新されます。
これは、Requests のバージョンを固定すると証明書が古くなってしまうかもしれないからです。

.. From Requests version 2.4.0 onwards, Requests will attempt to use certificates
   from `certifi`_ if it is present on the system. This allows for users to update
   their trusted certificates without having to change the code that runs on their
   system.

Requests のバージョン2.4.0からは、証明書がシステム上にある場合は `certifi`_ からの証明書を使うことを試みます。
これにより、システム上で実行されるコードを変更することなく、信頼できる証明書に更新することができます。

.. For the sake of security we recommend upgrading certifi frequently!

セキュリティのために、certifi を頻繁に更新することをお勧めします！

.. _HTTP persistent connection: https://en.wikipedia.org/wiki/HTTP_persistent_connection
.. _connection pooling: http://urllib3.readthedocs.io/en/latest/reference/index.html#module-urllib3.connectionpool
.. _certifi: http://certifi.io/
.. _Mozilla trust store: https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt

.. _body-content-workflow:

ボディコンテンツのワークフロー
--------------------------------------

.. Body Content Workflow
   ---------------------

.. By default, when you make a request, the body of the response is downloaded
   immediately. You can override this behaviour and defer downloading the response
   body until you access the :attr:`Response.content <requests.Response.content>`
   attribute with the ``stream`` parameter::

デフォルトでは、リクエストを行うとレスポンスのボディをすぐにダウンロードします。
この動作を上書きすることができ、:attr:`Response.content <requests.Response.content>` 属性に
``stream`` パラメータを指定してアクセスするまでレスポンスのボディのダウンロードを遅らせることができます。::

    tarball_url = 'https://github.com/requests/requests/tarball/master'
    r = requests.get(tarball_url, stream=True)

.. At this point only the response headers have been downloaded and the connection
   remains open, hence allowing us to make content retrieval conditional::

この時点で、レスポンスヘッダ−のみダウンロードされ、コネクションは接続したままのため、
コンテンツの取得を条件付きで許可するようにすることができます。::

    if int(r.headers['content-length']) < TOO_LONG:
      content = r.content
      ...

.. You can further control the workflow by use of the :meth:`Response.iter_content() <requests.Response.iter_content>`
   and :meth:`Response.iter_lines() <requests.Response.iter_lines>` methods.
   Alternatively, you can read the undecoded body from the underlying
   urllib3 :class:`urllib3.HTTPResponse <urllib3.response.HTTPResponse>` at
   :attr:`Response.raw <requests.Response.raw>`.

:meth:`Response.iter_content() <requests.Response.iter_content>`、および
:meth:`Response.iter_lines() <requests.Response.iter_lines>` メソッドを使うことで
ワークフローをさらにコントロールすることができます。
他の方法として、:attr:`Response.raw <requests.Response.raw>` にある
urllib3 の :class:`urllib3.HTTPResponse <urllib3.response.HTTPResponse>` 配下にある
デコードされていないボディを読むこともできます。

.. If you set ``stream`` to ``True`` when making a request, Requests cannot
   release the connection back to the pool unless you consume all the data or call
   :meth:`Response.close <requests.Response.close>`. This can lead to
   inefficiency with connections. If you find yourself partially reading request
   bodies (or not reading them at all) while using ``stream=True``, you should
   make the request within a ``with`` statement to ensure it's always closed::

リクエストを行う時に ``stream`` に ``True`` を設定すると、全てのデータを消費するか、
:meth:`Response.close <requests.Response.close>` を呼ばないかぎり、
Requests はコネクションをプールして開放することができません。
これによってコネクションを非効率にするかもしれません。
``stream=True`` にしている間、リクエストのボデイを部分的に読み込む(または、まったく読み込まない)場合、
``with`` 文内でリクエストを作成し、コネクションを閉じるようにする必要があります。::

    with requests.get('http://httpbin.org/get', stream=True) as r:
        # Do things with the response here.

.. _keep-alive:

キープアライブ
--------------------

.. Keep-Alive
   ----------

.. Excellent news — thanks to urllib3, keep-alive is 100% automatic within a session!
   Any requests that you make within a session will automatically reuse the appropriate
   connection!

エクセレントなお知らせ - urllib3 のおかげで、キープアライブはセッション内で 100% 自動的に行われます。
セッション内でリクエストを生成すると、適切に接続を自動的に再利用します。

.. Note that connections are only released back to the pool for reuse once all body
   data has been read; be sure to either set ``stream`` to ``False`` or read the
   ``content`` property of the ``Response`` object.

全てのボディデータが読み込まれると、接続は再利用するためにプールされるだけになることに注意して下さい。
``stream`` を ``False`` にセットするか、``Response`` オブジェクトの ``content`` プロパティを解釈するようにして下さい。

.. _streaming-uploads:

ストリーミングアップロード
---------------------------

.. Streaming Uploads
   -----------------

.. Requests supports streaming uploads, which allow you to send large streams or
   files without reading them into memory. To stream and upload, simply provide a
   file-like object for your body::

Requests はストリーミングアップロードをサポートしています。
大きなストリームやファイルをメモリに読み込まずに送信することができます。
ストリーミングとアップロードを行うには、ボディにファイル形式のオブジェクトをシンプルに提供するだけです。 ::

    with open('massive-body', 'rb') as f:
        requests.post('http://some.url/streamed', data=f)

.. It is strongly recommended that you open files in `binary mode`_.
   This is because Requests may attempt to provide the
   ``Content-Length`` header for you, and if it does this value will
   be set to the number of *bytes* in the file. Errors may occur if
   you open the file in *text mode*.

.. warning:: `binary mode`_ でファイルを開くことを強くお勧めしています。
             これは Requests が ``Content-Length`` ヘッダーを提供しようとするので、
             この値はファイルのバイト数に設定されるからです。
             *text mode* でファイルを開くとエラーが発生する場合があります。

.. _binary mode: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

.. _chunk-encoding:

チャンク形式のエンコードされたリクエスト
--------------------------------------------

.. Chunk-Encoded Requests
   ----------------------

.. Requests also supports Chunked transfer encoding for outgoing and incoming requests.
   To send a chunk-encoded request, simply provide a generator (or any iterator without
   a length) for your body::

Requests は入ってくるリクエストと出ていくリクエストのチャンク形式の転送エンコーディングもサポートしています。
チャンク形式でエンコードされたリクエストを送信するには、ボディにジェネレータ(または長さを持たないイテレータ)を提供するだけです。::

    def gen():
        yield 'hi'
        yield 'there'

    requests.post('http://some.url/chunked', data=gen())

.. For chunked encoded responses, it's best to iterate over the data using
   :meth:`Response.iter_content() <requests.Response.iter_content>`. In
   an ideal situation you'll have set ``stream=True`` on the request, in which
   case you can iterate chunk-by-chunk by calling ``iter_content`` with a ``chunk_size``
   parameter of ``None``. If you want to set a maximum size of the chunk,
   you can set a ``chunk_size`` parameter to any integer.

チャンク形式でエンコードされたレスポンスは、:meth:`Response.iter_content() <requests.Response.iter_content>` を
使ってデータを反復処理することをお勧めします。
理想的な状況として、リクエストで ``stream=True`` を設定してから、``chunk_size`` パラメータを
``None`` にして ``iter_content`` を呼び出すことでチャンク単位で反復処理を行うことができます。
チャンクの最大のサイズを設定する場合、``chunk_size`` パラメータを任意の整数で設定することが可能です。

.. _multipart:

複数のマルチパートエンコードされたファイルのPOST
-------------------------------------------------------

.. POST Multiple Multipart-Encoded Files
   -------------------------------------

.. You can send multiple files in one request. For example, suppose you want to
   upload image files to an HTML form with a multiple file field 'images'::

1回のリクエストで複数のファイルを送信することができます。
例えば、画像ファイルを複数のファイルフィールドの 'images' の HTML フォームにアップロードしたい場合::

    <input type="file" name="images" multiple="true" required="true"/>

.. To do that, just set files to a list of tuples of ``(form_field_name, file_info)``::

これを行うにはファイルを ``(form_field_name, file_info)`` のタプルのリストとして設定します。::

    >>> url = 'http://httpbin.org/post'
    >>> multiple_files = [
            ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
            ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
    >>> r = requests.post(url, files=multiple_files)
    >>> r.text
    {
      ...
      'files': {'images': 'data:image/png;base64,iVBORw ....'}
      'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
      ...
    }

.. It is strongly recommended that you open files in `binary mode`_.
   This is because Requests may attempt to provide the
   ``Content-Length`` header for you, and if it does this value will
   be set to the number of *bytes* in the file. Errors may occur if
   you open the file in *text mode*.

.. warning:: `binary mode`_ でファイルを開くことを強くお勧めしています。
             これは Requests が ``Content-Length`` ヘッダーを提供しようとするので、
             この値はファイルのバイト数に設定されるからです。
             *text mode* でファイルを開くとエラーが発生する場合があります。

.. _binary mode: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

.. _event-hooks:

イベントフック
-------------------

.. Event Hooks
   -----------

.. Requests has a hook system that you can use to manipulate portions of
   the request process, or signal event handling.

Requests にはフックシステムがあり、これを使用してリクエストの処理を一部変えたり、イベント処理を通知したりすることができます。

Available hooks:

``response``:
    The response generated from a Request.


.. You can assign a hook function on a per-request basis by passing a
   ``{hook_name: callback_function}`` dictionary to the ``hooks`` request
   parameter::

``{hook_name: callback_function}`` ディクショナリを ``hooks`` リクエストパラメータに渡すことで、
リクエスト毎にフック関数を割り当てることができます。::

    hooks=dict(response=print_url)

.. That ``callback_function`` will receive a chunk of data as its first
   argument.

``callback_function`` は、最初の引数としてデータのチャンクを受け取ります。

::

    def print_url(r, *args, **kwargs):
        print(r.url)

.. If an error occurs while executing your callback, a warning is given.

コールバックの実行中にエラーが発生すると、警告を表示します。

.. If the callback function returns a value, it is assumed that it is to
   replace the data that was passed in. If the function doesn't return
   anything, nothing else is effected.

コールバック関数が値を返す場合、渡されたデータが置換されたものとします。
関数が何も返さない場合、何も影響がありません。

.. Let's print some request method arguments at runtime::

実行中のリクエストのメソッドの引数を出力してみましょう::

    >>> requests.get('http://httpbin.org', hooks=dict(response=print_url))
    http://httpbin.org
    <Response [200]>

.. _custom-auth:

独自の認証
------------------------

.. Custom Authentication
   ---------------------

.. Requests allows you to use specify your own authentication mechanism.

Requests は独自の認証メカニズムを指定することができます。

.. Any callable which is passed as the ``auth`` argument to a request method will
   have the opportunity to modify the request before it is dispatched.

リクエストのメソッドの ``auth`` 引数に渡した任意の呼び出し可能オブジェクトは、
ディスパッチされる前にリクエストを変更する機会があります。

.. Authentication implementations are subclasses of :class:`AuthBase <requests.auth.AuthBase>`,
   and are easy to define. Requests provides two common authentication scheme
   implementations in ``requests.auth``: :class:`HTTPBasicAuth <requests.auth.HTTPBasicAuth>` and
   :class:`HTTPDigestAuth <requests.auth.HTTPDigestAuth>`.

認証の実装方法は :class:`AuthBase <requests.auth.AuthBase>` のサブクラスで、簡単に定義できます。
Requests は、``requests.auth`` に :class:`HTTPBasicAuth <requests.auth.HTTPBasicAuth>` と
:class:`HTTPDigestAuth <requests.auth.HTTPDigestAuth>` の2つの共通の認証スキームの実装を提供しています。

.. Let's pretend that we have a web service that will only respond if the
   ``X-Pizza`` header is set to a password value. Unlikely, but just go with it.

``X-Pizza`` ヘッダーにパスワードの値が設定されている場合のみ応答するウェブサービスがあるとしましょう。
そんなサービスはないと思うかもしれませんが、騙されたと思って見ていきましょう。

::

    from requests.auth import AuthBase

    class PizzaAuth(AuthBase):
        """Attaches HTTP Pizza Authentication to the given Request object."""
        def __init__(self, username):
            # setup any auth-related data here
            self.username = username

        def __call__(self, r):
            # modify and return the request
            r.headers['X-Pizza'] = self.username
            return r

.. Then, we can make a request using our Pizza Auth::

その後、Pizza Auth を使ってリクエストを行うことができます。::

    >>> requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
    <Response [200]>

.. _streaming-requests:

ストリーミングリクエスト
----------------------------

.. Streaming Requests
   ------------------

.. With :meth:`Response.iter_lines() <requests.Response.iter_lines>` you can easily
   iterate over streaming APIs such as the `Twitter Streaming
   API <https://dev.twitter.com/streaming/overview>`_. Simply
   set ``stream`` to ``True`` and iterate over the response with
   :meth:`~requests.Response.iter_lines()`::

:meth:`Response.iter_lines() <requests.Response.iter_lines>` を使って、
`Twitter Streaming API <https://dev.twitter.com/streaming/overview>`_ 等のストリーミング API を簡単にイテレーション処理をすることができます。
``stream`` を ``True`` に設定し、:meth:`~requests.Response.iter_lines()` で応答をイテレーション処理を行います。::

    import json
    import requests

    r = requests.get('http://httpbin.org/stream/20', stream=True)

    for line in r.iter_lines():

        # filter out keep-alive new lines
        if line:
            decoded_line = line.decode('utf-8')
            print(json.loads(decoded_line))

.. When using `decode_unicode=True` with
   :meth:`Response.iter_lines() <requests.Response.iter_lines>` or
   :meth:`Response.iter_content() <requests.Response.iter_content>`, you'll want
   to provide a fallback encoding in the event the server doesn't provide one::

:meth:`Response.iter_lines() <requests.Response.iter_lines>` や
:meth:`Response.iter_content() <requests.Response.iter_content>` で `decode_unicode=True` を使う場合、
サーバーが提供していないイベントでフォールバックエンコーディングを指定することをお勧めします。::

    r = requests.get('http://httpbin.org/stream/20', stream=True)

    if r.encoding is None:
        r.encoding = 'utf-8'

    for line in r.iter_lines(decode_unicode=True):
        if line:
            print(json.loads(line))

.. :meth:`~requests.Response.iter_lines()` is not reentrant safe.
   Calling this method multiple times causes some of the received data
   being lost. In case you need to call it from multiple places, use
   the resulting iterator object instead::

        lines = r.iter_lines()
        # Save the first line for later or just skip it

        first_line = next(lines)

        for line in lines:
            print(line)

.. warning::

    :meth:`~requests.Response.iter_lines()` は、リエントラント安全ではありません。
    このメソッドを複数回呼び出すと、受信したデータの一部が失われます。
    複数の場所から呼び出す必要がある場合、代わりにイテレータオブジェクトの結果を使います。::

        lines = r.iter_lines()
        # Save the first line for later or just skip it

        first_line = next(lines)

        for line in lines:
            print(line)

.. _proxies:

プロキシ
------------

.. Proxies
   -------

.. If you need to use a proxy, you can configure individual requests with the
   ``proxies`` argument to any request method::

プロキシを使用する必要がある場合、
任意のリクエストメソッドの ``proxies`` 引数で個別にリクエストを設定することができます。::

    import requests

    proxies = {
      'http': 'http://10.10.1.10:3128',
      'https': 'http://10.10.1.10:1080',
    }

    requests.get('http://example.org', proxies=proxies)

.. You can also configure proxies by setting the environment variables
   ``HTTP_PROXY`` and ``HTTPS_PROXY``.

プロキシは、環境変数の ``HTTP_PROXY`` と ``HTTPS_PROXY`` を設定することもできます。

::

    $ export HTTP_PROXY="http://10.10.1.10:3128"
    $ export HTTPS_PROXY="http://10.10.1.10:1080"

    $ python
    >>> import requests
    >>> requests.get('http://example.org')

.. To use HTTP Basic Auth with your proxy, use the `http://user:password@host/` syntax::

HTTP Basic 認証をプロキシで使うには、`http://user:password@host/` のような書き方にしてください。::

    proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}

.. To give a proxy for a specific scheme and host, use the
   `scheme://hostname` form for the key.  This will match for
   any request to the given scheme and exact hostname.

特定のスキームやホストにプロキシを指定するには、キーに `scheme://hostname` 形式にします。
これは、指定されたスキームへのリクエストと正しいホスト名と一致します。

::

    proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}

Note that proxy URLs must include the scheme.

SOCKS
^^^^^

.. versionadded:: 2.10.0

.. In addition to basic HTTP proxies, Requests also supports proxies using the
   SOCKS protocol. This is an optional feature that requires that additional
   third-party libraries be installed before use.

基本的な HTTP プロキシに加えて、Requests は SOCKS プロトコルを使ったプロキシもサポートしています。
これはオプションの機能で、使う前に追加のサードパーティのライブラリを必要とします。

.. You can get the dependencies for this feature from ``pip``:

``pip`` から、この機能を使うための依存を取得することができます。:

.. code-block:: bash

    $ pip install requests[socks]

.. Once you've installed those dependencies, using a SOCKS proxy is just as easy
   as using a HTTP one::

これらの依存をインストールしたら、SOCKS プロキシを使うのは、HTTP を使うのと同じくらい簡単です。::

    proxies = {
        'http': 'socks5://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }

.. Using the scheme ``socks5`` causes the DNS resolution to happen on the client, rather than on the proxy server. This is in line with curl, which uses the scheme to decide whether to do the DNS resolution on the client or proxy. If you want to resolve the domains on the proxy server, use ``socks5h`` as the scheme.

``socks5`` スキームを使うと DNS の名前解決がプロキシサーバーではなく、クライアント側で行われます。
これはクライアントやプロキシで DNS の名前解決を行うかどうかを決定するためにこのスキームを curl が使うのと同様です。
プロキシサーバー上のドメインを解決する場合は、スキームとして ``socks5h`` を使います。

.. _compliance:

コンプライアンス
--------------------

.. Compliance
   ----------

.. Requests is intended to be compliant with all relevant specifications and
   RFCs where that compliance will not cause difficulties for users. This
   attention to the specification can lead to some behaviour that may seem
   unusual to those not familiar with the relevant specification.

Requests は、コンプライアンスがユーザーに問題を引き起こさないようにするために、関連する仕様と RFC に準拠すること意図しています。
この仕様の注意点として、関連する仕様に精通していない場合に不思議な挙動だと感じるかもしれません。

.. Encodings
   ^^^^^^^^^

エンコーディング
^^^^^^^^^^^^^^^^^^

.. When you receive a response, Requests makes a guess at the encoding to
   use for decoding the response when you access the :attr:`Response.text
   <requests.Response.text>` attribute. Requests will first check for an
   encoding in the HTTP header, and if none is present, will use `chardet
   <http://pypi.python.org/pypi/chardet>`_ to attempt to guess the encoding.

レスポンスを受け取った際、:attr:`Response.text <requests.Response.text>` 属性にアクセスした時に、
レスポンスをデコードするために、Requests はエンコーディングを推測します。
Requests はまず HTTP ヘッダーのエンコーディングをチェックし、存在しない場合はエンコーディングを推測するために
`chardet <http://pypi.python.org/pypi/chardet>`_ を使います。

.. The only time Requests will not do this is if no explicit charset
   is present in the HTTP headers **and** the ``Content-Type``
   header contains ``text``. In this situation, `RFC 2616
   <http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.7.1>`_ specifies
   that the default charset must be ``ISO-8859-1``. Requests follows the
   specification in this case. If you require a different encoding, you can
   manually set the :attr:`Response.encoding <requests.Response.encoding>`
   property, or use the raw :attr:`Response.content <requests.Response.content>`.

Requests がこのようにしない場合として、HTTP ヘッダーに明確な文字コードがなく、``Content-Type`` ヘッダーに ``text`` が含まれている場合です。
この状況で `RFC 2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.7.1>`_ は、
デフォルトの文字コードが ``ISO-8859-1`` になっていることが想定されています。
この場合、Requests は仕様に従います。別のエンコーディングが必要な場合は、
:attr:`Response.encoding <requests.Response.encoding>` プロパティを手動で設定するか、
生データの :attr:`Response.content <requests.Response.content>` を使用することができます。

.. _http-verbs:

.. HTTP Verbs
   ----------

HTTP メソッド
--------------------

.. Requests provides access to almost the full range of HTTP verbs: GET, OPTIONS,
   HEAD, POST, PUT, PATCH and DELETE. The following provides detailed examples of
   using these various verbs in Requests, using the GitHub API.

Requests は、GET、OPTIONS、HEAD、POST、PUT、PATCH、DELETE
のほぼ全ての HTTP メソッドにアクセスすることができます。
GitHub の API を使って、このメソッドを Requests で使う例を以下で紹介します。

.. We will begin with the verb most commonly used: GET. HTTP GET is an idempotent
   method that returns a resource from a given URL. As a result, it is the verb
   you ought to use when attempting to retrieve data from a web location. An
   example usage would be attempting to get information about a specific commit
   from GitHub. Suppose we wanted commit ``a050faf`` on Requests. We would get it
   like so::

最も一般的に使われる GET の HTTP メソッドで始めましょう。
HTTP の GET は、指定された URL からリソースを受け取る冪等のメソッドです。
その結果、ウェブのロケーションからデータを取得しようとするときに使う HTTP メソッドです。
サンプル例で GitHub から特定のコミットに関する情報を取得しようとするものです。
Requests の ``a050faf`` のコミットを取得したいとします。
以下のようにするとできます。::

    >>> import requests
    >>> r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')

.. We should confirm that GitHub responded correctly. If it has, we want to work
   out what type of content it is. Do this like so::

GitHub が正しく応答したことを確認する必要があります。
正しければ、どのようなタイプのコンテンツだったかの処理をしたいと思います。
以下のようにします。::

    >>> if r.status_code == requests.codes.ok:
    ...     print(r.headers['content-type'])
    ...
    application/json; charset=utf-8

.. So, GitHub returns JSON. That's great, we can use the :meth:`r.json
   <requests.Response.json>` method to parse it into Python objects.::

したがって、GitHub は JSON を返却します。
素晴らしいことですが、:meth:`r.json <requests.Response.json>` メソッドを使って解析することで、
Python のオブジェクトにします。::

    >>> commit_data = r.json()

    >>> print(commit_data.keys())
    [u'committer', u'author', u'url', u'tree', u'sha', u'parents', u'message']

    >>> print(commit_data[u'committer'])
    {u'date': u'2012-05-10T11:10:50-07:00', u'email': u'me@kennethreitz.com', u'name': u'Kenneth Reitz'}

    >>> print(commit_data[u'message'])
    makin' history

.. So far, so simple. Well, let's investigate the GitHub API a little bit. Now,
   we could look at the documentation, but we might have a little more fun if we
   use Requests instead. We can take advantage of the Requests OPTIONS verb to
   see what kinds of HTTP methods are supported on the url we just used.::

これまでのところ、とても簡単です。次は GitHub の API について少し調べてみましょう。
ドキュメントを見ることができますが、代わりに Requests を使ってみるとさらに面白いかもしれません。
Requests の OPTIONS の HTTP メソッドを利用して、今リクエストした URL でサポートしている HTTP メソッドの種類を確認することができます。::

    >>> verbs = requests.options(r.url)
    >>> verbs.status_code
    500

.. Uh, what? That's unhelpful! Turns out GitHub, like many API providers, don't
   actually implement the OPTIONS method. This is an annoying oversight, but it's
   OK, we can just use the boring documentation. If GitHub had correctly
   implemented OPTIONS, however, they should return the allowed methods in the
   headers, e.g.::

ええっと、何が起こったのでしょう?
使えませんね!
多くの API プロバイダと同様に、GitHub は実際には OPTIONS メソッドを実装していません。
見落としていましたが、問題ありません。
ドキュメントで確認することができます。
しかし、GitHub が正しく OPTIONS を実装しているなら、ヘッダーで許可するメソッドを返却しないといけません。

    >>> verbs = requests.options('http://a-good-website.com/api/cats')
    >>> print(verbs.headers['allow'])
    GET,HEAD,POST,OPTIONS

.. Turning to the documentation, we see that the only other method allowed for
   commits is POST, which creates a new commit. As we're using the Requests repo,
   we should probably avoid making ham-handed POSTS to it. Instead, let's play
   with the Issues feature of GitHub.

ドキュメントに目を向けると、コミットで許可している唯一のメソッドは POST で、
これは新しいコミットを作成することを意味しています。
Requests のリポジトリを使っているので、ham-handed POSTS を作成することは避けて下さい。
代わりに GitHub の Issues 機能を試してみましょう。

.. This documentation was added in response to
   `Issue #482 <https://github.com/requests/requests/issues/482>`_. Given that
   this issue already exists, we will use it as an example. Let's start by getting it.::

この文章は、`Issue #482 <https://github.com/requests/requests/issues/482>`_ に対応するために追加されました。
この問題は、既知の問題なので例として使います。再現してみましょう。::

    >>> r = requests.get('https://api.github.com/repos/requests/requests/issues/482')
    >>> r.status_code
    200

    >>> issue = json.loads(r.text)

    >>> print(issue[u'title'])
    Feature any http verb in docs

    >>> print(issue[u'comments'])
    3

.. Cool, we have three comments. Let's take a look at the last of them.::

Cool、コメントが3つあります。コメントの最後を見てみましょう。::

    >>> r = requests.get(r.url + u'/comments')
    >>> r.status_code
    200

    >>> comments = r.json()

    >>> print(comments[0].keys())
    [u'body', u'url', u'created_at', u'updated_at', u'user', u'id']

    >>> print(comments[2][u'body'])
    Probably in the "advanced" section

.. Well, that seems like a silly place. Let's post a comment telling the poster
   that he's silly. Who is the poster, anyway?::

見る場所が良くなかったみたいですね。
投稿者にふざけていることを教えるコメントを投稿してみましょう。
投稿者は誰だろう？::

    >>> print(comments[2][u'user'][u'login'])
    kennethreitz

.. OK, so let's tell this Kenneth guy that we think this example should go in the
   quickstart guide instead. According to the GitHub API doc, the way to do this
   is to POST to the thread. Let's do it.::

この例をクイックスタートのガイドに入れることを Kenneth に伝えましょう。
GitHub の API のドキュメントによると、これを行う方法はスレッドに POST することです。
やってみましょう。::

    >>> body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
    >>> url = u"https://api.github.com/repos/requests/requests/issues/482/comments"

    >>> r = requests.post(url=url, data=body)
    >>> r.status_code
    404

.. Huh, that's weird. We probably need to authenticate. That'll be a pain, right?
   Wrong. Requests makes it easy to use many forms of authentication, including
   the very common Basic Auth.

う〜ん、おかしいなぁ。
多分認証する必要がありそうですね。
面倒ですよね？大丈夫ですよ。
Requests は、とても一般的な Basic 認証を含む様々な認証方法を簡単に使うことができます。

::

    >>> from requests.auth import HTTPBasicAuth
    >>> auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')

    >>> r = requests.post(url=url, data=body, auth=auth)
    >>> r.status_code
    201

    >>> content = r.json()
    >>> print(content[u'body'])
    Sounds great! I'll get right on it.

.. Brilliant. Oh, wait, no! I meant to add that it would take me a while, because
   I had to go feed my cat. If only I could edit this comment! Happily, GitHub
   allows us to use another HTTP verb, PATCH, to edit this comment. Let's do
   that.

いいですね。
ちょっと待った！
ネコに餌をあげないといけないので、しばらく時間がかかるということを追加したいとします。
もしこのコメントを編集できたら。
幸いにも、GitHub はこのコメントを編集するための PATCH という別の HTTP メソッドを使うことができます。
ではやってみましょう。

::

    >>> print(content[u"id"])
    5804413

    >>> body = json.dumps({u"body": u"Sounds great! I'll get right on it once I feed my cat."})
    >>> url = u"https://api.github.com/repos/requests/requests/issues/comments/5804413"

    >>> r = requests.patch(url=url, data=body, auth=auth)
    >>> r.status_code
    200

.. Excellent. Now, just to torture this Kenneth guy, I've decided to let him
   sweat and not tell him that I'm working on this. That means I want to delete
   this comment. GitHub lets us delete comments using the incredibly aptly named
   DELETE method. Let's get rid of it.

素晴らしい。
では、Kenneth という方を焦らせてしまうので、この作業をしているということを知られないようにしようと決めました。
つまり、このコメントを削除したいということです。
GitHub は適切な名前が付けられている DELETE メソッドを使ってコメントを削除してみましょう。
では取り除いてみましょう。

::

    >>> r = requests.delete(url=url, auth=auth)
    >>> r.status_code
    204
    >>> r.headers['status']
    '204 No Content'

.. Excellent. All gone. The last thing I want to know is how much of my ratelimit
   I've used. Let's find out. GitHub sends that information in the headers, so
   rather than download the whole page I'll send a HEAD request to get the
   headers.

素晴らしい。
全てなくなりました。
あと知りたいことは、使ったレートリミットです。
確認してみましょう。
GitHub はその情報をヘッダーに追加して送信してくるので、
ページ全体をダウンロードせず、HEAD リクエストを送信してヘッダーを取得します。

::

    >>> r = requests.head(url=url, auth=auth)
    >>> print(r.headers)
    ...
    'x-ratelimit-remaining': '4995'
    'x-ratelimit-limit': '5000'
    ...

.. Excellent. Time to write a Python program that abuses the GitHub API in all
   kinds of exciting ways, 4995 more times.

素晴らしい。
4995回以上のエキサイティングな方法で GitHub API を使う Python プログラムを書くことができる回数です。

.. _custom-verbs:

独自の HTTP メソッド
------------------------

.. Custom Verbs
   ------------

.. From time to time you may be working with a server that, for whatever reason,
   allows use or even requires use of HTTP verbs not covered above. One example of
   this would be the MKCOL method some WEBDAV servers use. Do not fret, these can
   still be used with Requests. These make use of the built-in ``.request``
   method. For example::

ときには何らかの理由で、上記で扱われていない HTTP メソッドを使用する必要があったり、使用しているサーバーで作業する場合があります。
この場合の1例として、一部の WEBDAV サーバーが使用している MKCOL 方式があります。
心配しなくても、これらは Requests と一緒に使うことが可能です。
これは組み込みの ``.request`` メソッドを使用します。例として::

    >>> r = requests.request('MKCOL', url, data=data)
    >>> r.status_code
    200 # Assuming your call was correct

.. Utilising this, you can make use of any method verb that your server allows.

これを利用すると、サーバーが認めている任意の HTTP メソッドを使うことができます。

.. _link-headers:

リンクヘッダー
------------------

.. Link Headers
   ------------

.. Many HTTP APIs feature Link headers. They make APIs more self describing and
   discoverable.

多くの HTTP API にはリンクヘッダーがあります。それらは API を発見しやすくします。

.. GitHub uses these for `pagination <http://developer.github.com/v3/#pagination>`_
   in their API, for example::

GitHub は API の `pagination <http://developer.github.com/v3/#pagination>`_ にこれを使用します。
例として::

    >>> url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
    >>> r = requests.head(url=url)
    >>> r.headers['link']
    '<https://api.github.com/users/kennethreitz/repos?page=2&per_page=10>; rel="next", <https://api.github.com/users/kennethreitz/repos?page=6&per_page=10>; rel="last"'

.. Requests will automatically parse these link headers and make them easily consumable::

Requests は自動的にリンクヘッダーを解析し、簡単に使えるようにします。::

    >>> r.links["next"]
    {'url': 'https://api.github.com/users/kennethreitz/repos?page=2&per_page=10', 'rel': 'next'}

    >>> r.links["last"]
    {'url': 'https://api.github.com/users/kennethreitz/repos?page=7&per_page=10', 'rel': 'last'}

.. _transport-adapters:

トランスポートアダプタ
--------------------------

.. Transport Adapters
   ------------------

.. As of v1.0.0, Requests has moved to a modular internal design. Part of the
   reason this was done was to implement Transport Adapters, originally
   `described here`_. Transport Adapters provide a mechanism to define interaction
   methods for an HTTP service. In particular, they allow you to apply per-service
   configuration.

v1.0.0 以降、Requests はモジュール化された内部組み込みの設計に移行しました。
これが行われた理由の１つとして、もともとは `described here`_ で説明したトランスポートアダプタを実装することです。
トランスポートアダプタは、HTTP サービスで対話する方法を定義するメカニズムを提供します。
特にサービスごとの設定を適用することが可能です。

.. Requests ships with a single Transport Adapter, the :class:`HTTPAdapter
   <requests.adapters.HTTPAdapter>`. This adapter provides the default Requests
   interaction with HTTP and HTTPS using the powerful `urllib3`_ library. Whenever
   a Requests :class:`Session <requests.Session>` is initialized, one of these is
   attached to the :class:`Session <requests.Session>` object for HTTP, and one
   for HTTPS.

Requests は、トランスポートアダプタである :class:`HTTPAdapter <requests.adapters.HTTPAdapter>` が付属しています。
このアダプタは強力な `urllib3`_ ライブラリを使って、HTTP と HTTPS とのデフォルトの Requests の対話を提供しています。
Requests の :class:`Session <requests.Session>` が初期化すると、これらのうちの１つが
HTTP の :class:`Session <requests.Session>` オブジェクトに、HTTPS の Session オブジェクトにアタッチされます。

.. Requests enables users to create and use their own Transport Adapters that
   provide specific functionality. Once created, a Transport Adapter can be
   mounted to a Session object, along with an indication of which web services
   it should apply to.

Requests は、特定の機能を提供する独自のトランスポートアダプタを作成して、使うことが可能です。
作成されたトランスポートアダプタは、どのウェブサービスを適用するかの指定を Session オブジェクトにマウントすることができます。

::

    >>> s = requests.Session()
    >>> s.mount('http://www.github.com', MyAdapter())

.. The mount call registers a specific instance of a Transport Adapter to a
   prefix. Once mounted, any HTTP request made using that session whose URL starts
   with the given prefix will use the given Transport Adapter.

mount の呼び出しをトランスポートアダプタの特定のインスタンスをプレフィックスに登録します。
マウントされると、URL が指定されたプレフィックスで始まるセッションを使用して行われた HTTP リクエストは、
指定されたトランスポートアダプタを使用します。

.. Many of the details of implementing a Transport Adapter are beyond the scope of
   this documentation, but take a look at the next example for a simple SSL use-
   case. For more than that, you might look at subclassing the
   :class:`BaseAdapter <requests.adapters.BaseAdapter>`.

トランスポートアダプタを実装する詳細の多くは、このドキュメントの範囲を超えていますが、単純な SSL のユースケースの次の例を見て下さい。
それ以上の場合は、:class:`BaseAdapter <requests.adapters.BaseAdapter>` のサブクラス化を参照して下さい。

.. Example: Specific SSL Version
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

例: 特定のSSLバージョン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. The Requests team has made a specific choice to use whatever SSL version is
   default in the underlying library (`urllib3`_). Normally this is fine, but from
   time to time, you might find yourself needing to connect to a service-endpoint
   that uses a version that isn't compatible with the default.

Requests チームは基礎となるライブラリ(`urllib3`_)にデフォルトの SSL バージョンを使用するような選択をしました。
通常これは問題となりませんが、時にはデフォルトと互換性のないバージョンを使用するサービスのエンドポイントに
接続する必要があるかもしれません。

.. You can use Transport Adapters for this by taking most of the existing
   implementation of HTTPAdapter, and adding a parameter *ssl_version* that gets
   passed-through to `urllib3`. We'll make a Transport Adapter that instructs the
   library to use SSLv3::

HTTPAdapter の既存の実装の大部分を引き継ぎ、`urllib3` に渡す *ssl_version* パラメータを追加することでトランスポートアダプタを使うことができます。
ライブラリに SSLv3 を使うように指定するトランスポートアダプタを作成します。::

    import ssl

    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.poolmanager import PoolManager


    class Ssl3HttpAdapter(HTTPAdapter):
        """"Transport adapter" that allows us to use SSLv3."""

        def init_poolmanager(self, connections, maxsize, block=False):
            self.poolmanager = PoolManager(
                num_pools=connections, maxsize=maxsize,
                block=block, ssl_version=ssl.PROTOCOL_SSLv3)

.. _`described here`: http://www.kennethreitz.org/essays/the-future-of-python-http
.. _`urllib3`: https://github.com/shazow/urllib3

.. _blocking-or-nonblocking:

ブロッキングかノンブロッキングか？
------------------------------------

.. Blocking Or Non-Blocking?
   -------------------------

.. With the default Transport Adapter in place, Requests does not provide any kind
   of non-blocking IO. The :attr:`Response.content <requests.Response.content>`
   property will block until the entire response has been downloaded. If
   you require more granularity, the streaming features of the library (see
   :ref:`streaming-requests`) allow you to retrieve smaller quantities of the
   response at a time. However, these calls will still block.

デフォルトのトランスポートアダプタを適切に設定すると、Requests はいかなる種類のノンブロッキングの IO も提供していません。
:attr:`Response.content <requests.Response.content>` プロパティはレスポンス全体がダウンロードされるまでブロックされます。
より細分化する必要があるなら、ライブラリのストリーミング機能(:ref:`streaming-requests` を参照)を使用して、
一回に少しずつのレスポンスを受け取ることができます。
しかし、これらの呼び出しはブロックされます。

.. If you are concerned about the use of blocking IO, there are lots of projects
   out there that combine Requests with one of Python's asynchronicity frameworks.
   Two excellent examples are `grequests`_ and `requests-futures`_.

ブロッキング IO を使うことが不安なら、Python の非同期フレームワークと Requests を組み合わせているプロジェクトがたくさんあります。
`grequests`_ と `requests-futures`_ の2つはいい例です。

.. _`grequests`: https://github.com/kennethreitz/grequests
.. _`requests-futures`: https://github.com/ross/requests-futures

.. Header Ordering
   ---------------

ヘッダーの順番
------------------

.. In unusual circumstances you may want to provide headers in an ordered manner. If you pass an ``OrderedDict`` to the ``headers`` keyword argument, that will provide the headers with an ordering. *However*, the ordering of the default headers used by Requests will be preferred, which means that if you override default headers in the ``headers`` keyword argument, they may appear out of order compared to other headers in that keyword argument.

特殊な状況では、順序を守ってヘッダーを提供しなければいけない場合があります。
``headers`` キーワード引数に ``OrderedDict`` を渡すと、ヘッダーを順序を指定することができます。
*しかし*、Requests で使用するデフォルトのヘッダーの順序が優先されます。
つまり、``headers`` キーワード引数のデフォルトのヘッダーを上書きすると、
そのキーワード引数の他のヘッダーと比較するので、順序がおかしくなるかもしれません。

.. If this is problematic, users should consider setting the default headers on a :class:`Session <requests.Session>` object, by setting :attr:`Session <requests.Session.headers>` to a custom ``OrderedDict``. That ordering will always be preferred.

これに問題がある場合は、:class:`Session <requests.Session>` オブジェクトのデフォルトヘッダーを設定することを検討してみてもいいかもしれません。
設定した順序が優先されます。

.. _timeouts:

タイムアウト
----------------

.. Timeouts
   --------

.. Most requests to external servers should have a timeout attached, in case the
   server is not responding in a timely manner. By default, requests do not time
   out unless a timeout value is set explicitly. Without a timeout, your code may
   hang for minutes or more.

サーバーがすぐに応答できない場合のマナーとして、外部サーバーへのほとんどのリクエストはタイムアウトが設定されている必要があります。
デフォルトでは、明示的に設定されていない限り、リクエストはタイムアウトしません。
タイムアウトしなければ、コードは数分以上停止することができます。

.. The **connect** timeout is the number of seconds Requests will wait for your
   client to establish a connection to a remote machine (corresponding to the
   `connect()`_) call on the socket. It's a good practice to set connect timeouts
   to slightly larger than a multiple of 3, which is the default `TCP packet
   retransmission window <http://www.hjp.at/doc/rfc/rfc2988.txt>`_.

**コネクション** のタイムアウトは、クライアントがリモートマシンへの接続を確立するまで Requests が待機する秒数のことです。
コネクションのタイムアウトをデフォルトの `TCP パケットの再転送のウィンドウサイズ <http://www.hjp.at/doc/rfc/rfc2988.txt>`_ を、
3の倍数よりほんの少し大きくすることをお勧めします。

.. Once your client has connected to the server and sent the HTTP request, the
   **read** timeout is the number of seconds the client will wait for the server
   to send a response. (Specifically, it's the number of seconds that the client
   will wait *between* bytes sent from the server. In 99.9% of cases, this is the
   time before the server sends the first byte).

クライアントがサーバーに接続して HTTP のリクエストを送ると、
読み込みのタイムアウト時間は、サーバーがレスポンスを送信するまでの待機する秒数です。
(具体的には、クライアントがサーバーから送られてくるバイトデータ間の待機する秒数です。
99.9% のケースでは、これはサーバーが最初のバイトデータを送るまでの時間です。)

.. If you specify a single value for the timeout, like this::

タイムアウトに1つの値を指定する場合、以下のようになります。::

    r = requests.get('https://github.com', timeout=5)

.. The timeout value will be applied to both the ``connect`` and the ``read``
   timeouts. Specify a tuple if you would like to set the values separately::

タイムアウトの値は、``接続`` と ``読み込み`` の両方のタイムアウトに適用されます。
値を個別にセットする場合は、タプルで指定します。

    r = requests.get('https://github.com', timeout=(3.05, 27))

.. If the remote server is very slow, you can tell Requests to wait forever for
   a response, by passing None as a timeout value and then retrieving a cup of
   coffee.

リモートサーバーが非常に遅い場合、タイムアウトの値として None を渡して、retrieving a cup of coffee をして、
Requests にレスポンスが返ってくるまでずっと待機するように指示することができます。

::

    r = requests.get('https://github.com', timeout=None)

.. _`connect()`: http://linux.die.net/man/2/connect
