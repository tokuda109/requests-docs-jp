.. _quickstart:

.. Quickstart
   ==========

クイックスタート
================

.. module:: requests.models

.. Eager to get started? This page gives a good introduction in how to get started
   with Requests.

それでははじめましょう。
このページでは、Requests の使い方についての紹介をします。

.. First, make sure that:

最初に、以下を確認して下さい。:

.. Requests is :ref:`installed <install>`
.. Requests is :ref:`up-to-date <updates>`

* Requestsが :ref:`インストールされている <install>`
* Requestsが :ref:`最新版にされている <updates>`

.. Let's get started with some simple examples.

いくつかの簡単なサンプルをやってみましょう。

.. Make a Request
   --------------

リクエストの生成
-----------------

.. Making a request with Requests is very simple.

Requests を使ってリクエストを生成することはとても簡単です。

.. Begin by importing the Requests module::

Requests モジュールをインポートすることから始まります。::

    >>> import requests

.. Now, let's try to get a webpage. For this example, let's get GitHub's public
   timeline::

ではウェブページを取得してみましょう。
このサンプルでは、GitHub の公開されているタイムラインを取得してみましょう。

    >>> r = requests.get('https://api.github.com/events')

.. Now, we have a :class:`Response <requests.Response>` object called ``r``. We can
   get all the information we need from this object.

現在 ``r`` という :class:`Response` オブジェクトがあります。
このオブジェクトから必要な情報を全て取得することができます。

.. Requests' simple API means that all forms of HTTP request are as obvious. For
   example, this is how you make an HTTP POST request::

Requests のシンプルなAPIは、HTTP リクエストの全ての形式が明白であることを示しています。
例えば、以下のようにして HTTP の POST リクエストを作成することができます。

    >>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})

.. Nice, right? What about the other HTTP request types: PUT, DELETE, HEAD and
   OPTIONS? These are all just as simple::

問題ないですか？
PUT、DELETE、HEAD、OPTIONSなどの他の HTTP リクエストについてはどうするのでしょう？
これらも本当にシンプルです。::

    >>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
    >>> r = requests.delete('http://httpbin.org/delete')
    >>> r = requests.head('http://httpbin.org/get')
    >>> r = requests.options('http://httpbin.org/get')

.. That's all well and good, but it's also only the start of what Requests can
   do.

上手くいくと思いますが、これらは Requests ができることのほんの少しのことしか紹介していません。

.. Passing Parameters In URLs
   --------------------------

URLにパラメータを渡す
--------------------------

.. You often want to send some sort of data in the URL's query string. If
   you were constructing the URL by hand, this data would be given as key/value
   pairs in the URL after a question mark, e.g. ``httpbin.org/get?key=val``.
   Requests allows you to provide these arguments as a dictionary of strings,
   using the ``params`` keyword argument. As an example, if you wanted to pass
   ``key1=value1`` and ``key2=value2`` to ``httpbin.org/get``, you would use the
   following code::

URL のクエリ文字列に何らかのデータを付けて送信することがよくあります。
手動で URL を作る場合、このデータはクエスチョン記号の後のURLにキー/値のペアで付与して下さい。
例として、``httpbin.org/get?key=val`` のようになります。
Requests は ``params`` キーワード引数に、文字列のディクショナリとして渡す方法が用意されています。
例えば、``key1=value1`` と ``key2=value2`` を ``httpbin.org/get`` に渡す場合、以下のコードのようになります。::

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get('http://httpbin.org/get', params=payload)

.. You can see that the URL has been correctly encoded by printing the URL::

URL を表示すると、URL が正しくエンコードされていることが分かります。

    >>> print(r.url)
    http://httpbin.org/get?key2=value2&key1=value1

.. Note that any dictionary key whose value is ``None`` will not be added to the
   URL's query string.

値が ``None`` のディクショナリのキーは、URL のクエリ文字列に追加されません。

.. You can also pass a list of items as a value::

キー/値のアイテムのリストを値として渡すこともできます。::

    >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

    >>> r = requests.get('http://httpbin.org/get', params=payload)
    >>> print(r.url)
    http://httpbin.org/get?key1=value1&key2=value2&key2=value3

.. Response Content
   ----------------

レスポンスコンテンツ
---------------------------

.. We can read the content of the server's response. Consider the GitHub timeline
   again::

サーバーからのレスポンスの内容を見ることができます。
再度、GitHub のタイムラインで見てみましょう。::

    >>> import requests

    >>> r = requests.get('https://api.github.com/events')
    >>> r.text
    u'[{"repository":{"open_issues":0,"url":"https://github.com/...

.. Requests will automatically decode content from the server. Most unicode
   charsets are seamlessly decoded.

Requests はサーバーからのレスポンスの内容を自動的にデコードします。
ほとんどの Unicode 文字列はシームレスにデコードされています。

.. When you make a request, Requests makes educated guesses about the encoding of
   the response based on the HTTP headers. The text encoding guessed by Requests
   is used when you access ``r.text``. You can find out what encoding Requests is
   using, and change it, using the ``r.encoding`` property::

リクエストを行うと、Requests は HTTP ヘッダーの内容に基づいてレスポンスのエンコーディングの推測を行います。
Requests が推測するテキストのエンコーディングは、``r.text`` にアクセスする時に使われます。
``r.encoding`` プロパティを使って Requests が使っているエンコーディングを確認し、変更することができます。::

    >>> r.encoding
    'utf-8'
    >>> r.encoding = 'ISO-8859-1'

.. If you change the encoding, Requests will use the new value of ``r.encoding``
   whenever you call ``r.text``. You might want to do this in any situation where
   you can apply special logic to work out what the encoding of the content will
   be. For example, HTTP and XML have the ability to specify their encoding in
   their body. In situations like this, you should use ``r.content`` to find the
   encoding, and then set ``r.encoding``. This will let you use ``r.text`` with
   the correct encoding.

エンコーディングを変更した場合、Requests は ``r.text`` を呼び出すたびに ``r.encoding`` の新しい値を使用します。
特別なロジックを適用してコンテンツのエンコーディングがどのようなものになるかといった状況を把握したいこともあるかもしれません。
例として、HTTP と XML にはエンコーディングを指定する機能があります。
このような状況において、``r.content`` を使ってエンコーディングを見つけ、``r.encoding`` をセットする必要があります。
これにより、``r.text`` を正しいエンコーディングで使うことができるようになります。

.. Requests will also use custom encodings in the event that you need them. If
   you have created your own encoding and registered it with the ``codecs``
   module, you can simply use the codec name as the value of ``r.encoding`` and
   Requests will handle the decoding for you.

Requests は必要に応じて独自のエンコーディングを使うこともできます。
独自のエンコーディングを作成して ``codecs`` モジュールに登録した場合、
コーデック名を ``r.encoding`` の値として使うだけの簡単な方法で、Requests がデコード処理をやってくれます。

.. Binary Response Content
   -----------------------

バイナリのレスポンスコンテンツ
------------------------------

.. You can also access the response body as bytes, for non-text requests::

テキスト以外のリクエストの場合は、レスポンスボディにバイトとしてアクセスすることもできます。::

    >>> r.content
    b'[{"repository":{"open_issues":0,"url":"https://github.com/...

.. The ``gzip`` and ``deflate`` transfer-encodings are automatically decoded for you.

``gzip`` と ``deflate`` の転送コーディングは自動的にデコードされます。

.. For example, to create an image from binary data returned by a request, you can
   use the following code::

例として、リクエストすることで返却されたバイナリデータから画像を作成するには、以下のコードを使います。::

    >>> from PIL import Image
    >>> from io import BytesIO

    >>> i = Image.open(BytesIO(r.content))


.. JSON Response Content
   ---------------------

JSON のレスポンスコンテンツ
------------------------------

.. There's also a builtin JSON decoder, in case you're dealing with JSON data::

JSON データを扱うことも想定して、組み込みの JSON デコーダーもあります。::

    >>> import requests

    >>> r = requests.get('https://api.github.com/events')
    >>> r.json()
    [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

.. In case the JSON decoding fails, ``r.json()`` raises an exception. For example, if
   the response gets a 204 (No Content), or if the response contains invalid JSON,
   attempting ``r.json()`` raises ``ValueError: No JSON object could be decoded``.

JSON のデコードに失敗した場合、``r.json()`` は例外を発生させます。
例として、レスポンスが 204 (No Content) だった場合や、レスポンスに無効な JSON が含まれていた場合は、
``r.json()`` は ``ValueError: No JSON object could be decoded`` を発生させます。

.. It should be noted that the success of the call to ``r.json()`` does **not**
   indicate the success of the response. Some servers may return a JSON object in a
   failed response (e.g. error details with HTTP 500). Such JSON will be decoded
   and returned. To check that a request is successful, use
   ``r.raise_for_status()`` or check ``r.status_code`` is what you expect.

``r.json()`` のメソッド呼び出しが問題なかったとしても、レスポンスが正しかったということにならないことに注意して下さい。
一部のサーバーでは、レスポンスを返却する処理が失敗した時に JSON オブジェクトを返す場合があります(HTTP 500 の時のエラーの詳細等)。
そのような JSON はデコードされて、返却されます。
リクエストが成功したことを確認するには、``r.raise_for_status()`` を使うか、``r.status_code`` が期待したものかどうかを確認して下さい。

.. Raw Response Content
   --------------------

生のレスポンスコンテンツ
---------------------------

.. In the rare case that you'd like to get the raw socket response from the
   server, you can access ``r.raw``. If you want to do this, make sure you set
   ``stream=True`` in your initial request. Once you do, you can do this::

ごく稀に、サーバーから生のソケットレスポンスを取得したい場合に ``r.raw`` にアクセスすることができます。
これを行う場合は、最初のリクエスト時に ``stream=True`` をセットして下さい。
一度セットすると、可能になります。::

    >>> r = requests.get('https://api.github.com/events', stream=True)

    >>> r.raw
    <requests.packages.urllib3.response.HTTPResponse object at 0x101194810>

    >>> r.raw.read(10)
    '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'

.. In general, however, you should use a pattern like this to save what is being
   streamed to a file::

しかし、一般的にはこのようなパターンを使ってファイルにストリーミングされているものを保存する必要があります。

    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

.. Using ``Response.iter_content`` will handle a lot of what you would otherwise
   have to handle when using ``Response.raw`` directly. When streaming a
   download, the above is the preferred and recommended way to retrieve the
   content. Note that ``chunk_size`` can be freely adjusted to a number that
   may better fit your use cases.

``Response.iter_content`` を使うことで、直接 ``Response.raw`` を使う時にやらなければいけないことがたくさんあります。
When streaming a
download, the above is the preferred and recommended way to retrieve the
content. Note that ``chunk_size`` can be freely adjusted to a number that
may better fit your use cases.

.. Custom Headers
   --------------

独自のヘッダー
-----------------------

.. If you'd like to add HTTP headers to a request, simply pass in a ``dict`` to the
   ``headers`` parameter.

リクエストに HTTP ヘッダーを追加する場合は、シンプルに ``headers`` パラメータに ``ディクショナリ`` を渡します。

.. For example, we didn't specify our user-agent in the previous example::

例として、前のサンプルではユーザーエージェントを指定していませんでした。::

    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}

    >>> r = requests.get(url, headers=headers)

.. Note: Custom headers are given less precedence than more specific sources of information. For instance:

注意点: 独自のヘッダーとして追加された情報は、より具体的な情報より優先度は低くなります。例として:

.. Authorization headers set with `headers=` will be overridden if credentials
   are specified in ``.netrc``, which in turn will be overridden by the  ``auth=``
   parameter.
.. Authorization headers will be removed if you get redirected off-host.
.. Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
.. Content-Length headers will be overridden when we can determine the length of the content.

* `headers=` として設定された認証ヘッダーは、クレデンシャルが ``.netrc`` で指定されている場合は上書きされ、
  ``auth=`` パラメータによって上書きされます。
* Authorization headers will be removed if you get redirected off-host.
* Proxy-Authorization ヘッダーは、URL で提供されたプロキシのクレデンシャルによって更新されます。
* Content-Length ヘッダーは、コンテンツの長さが決まった時に更新されます。

.. Furthermore, Requests does not change its behavior at all based on which custom headers are specified. The headers are simply passed on into the final request.

さらに、Requests は独自のヘッダーが指定されたことによって振る舞いが変わることはありません。
ヘッダーは単純に最終的なリクエストに渡されるだけです。

.. Note: All header values must be a ``string``, bytestring, or unicode. While permitted, it's advised to avoid passing unicode header values.

注意点: 全てのヘッダーの値は、``string``、バイト文字列、Unicode でなければいけません。
許可されている間は、Unicode のヘッダーの値を渡さないようにすることをお勧めしています。

.. More complicated POST requests
   ------------------------------

さらに複雑なPOSTリクエスト
---------------------------------

.. Typically, you want to send some form-encoded data — much like an HTML form.
   To do this, simply pass a dictionary to the ``data`` argument. Your
   dictionary of data will automatically be form-encoded when the request is made::

通常、フォーム形式のデータを HTML 形式と同様に送信します。
これをするには、シンプルに ``data`` 引数にディクショナリを渡します。
リクエストが行われると、データのディクショナリは自動的にフォームエンコードされます。::

    >>> payload = {'key1': 'value1', 'key2': 'value2'}

    >>> r = requests.post("http://httpbin.org/post", data=payload)
    >>> print(r.text)
    {
      ...
      "form": {
        "key2": "value2",
        "key1": "value1"
      },
      ...
    }

.. You can also pass a list of tuples to the ``data`` argument. This is particularly
   useful when the form has multiple elements that use the same key::

``data`` 引数にタプルのリストを渡すこともできます。
これは、フォームに同じキーを使う複数の要素がある場合に特に便利です。

    >>> payload = (('key1', 'value1'), ('key1', 'value2'))
    >>> r = requests.post('http://httpbin.org/post', data=payload)
    >>> print(r.text)
    {
      ...
      "form": {
        "key1": [
          "value1",
          "value2"
        ]
      },
      ...
    }

.. There are times that you may want to send data that is not form-encoded. If
   you pass in a ``string`` instead of a ``dict``, that data will be posted directly.

フォームエンコードされていないデータを送信したい場合がよくあります。
``dict`` の代わりに ``string`` を渡すと、そのデータは直接ポストされます。

For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data::

    >>> import json

    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, data=json.dumps(payload))

Instead of encoding the ``dict`` yourself, you can also pass it directly using
the ``json`` parameter (added in version 2.4.2) and it will be encoded automatically::

    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, json=payload)


POST a Multipart-Encoded File
-----------------------------

Requests makes it simple to upload Multipart-encoded files::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': open('report.xls', 'rb')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "<censored...binary...data>"
      },
      ...
    }

You can set the filename, content_type and headers explicitly::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "<censored...binary...data>"
      },
      ...
    }

If you want, you can send strings to be received as files::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "some,data,to,send\\nanother,row,to,send\\n"
      },
      ...
    }

In the event you are posting a very large file as a ``multipart/form-data``
request, you may want to stream the request. By default, ``requests`` does not
support this, but there is a separate package which does -
``requests-toolbelt``. You should read `the toolbelt's documentation
<https://toolbelt.readthedocs.io>`_ for more details about how to use it.

For sending multiple files in one request refer to the :ref:`advanced <advanced>`
section.

.. warning:: It is strongly recommended that you open files in `binary mode`_.
             This is because Requests may attempt to provide the
             ``Content-Length`` header for you, and if it does this value will
             be set to the number of *bytes* in the file. Errors may occur if
             you open the file in *text mode*.

.. _binary mode: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files


.. Response Status Codes
   ---------------------

レスポンスのステータスコード
-----------------------------------

.. We can check the response status code::

レスポンスのステータスコードを確認することができます。::

    >>> r = requests.get('http://httpbin.org/get')
    >>> r.status_code
    200

.. Requests also comes with a built-in status code lookup object for easy
   reference::

Requests は、簡単に参照できるようにされている組み込みのステータスコードもあります。

    >>> r.status_code == requests.codes.ok
    True

.. If we made a bad request (a 4XX client error or 5XX server error response), we
   can raise it with
   :meth:`Response.raise_for_status() <requests.Response.raise_for_status>`::

不正なリクエスト(4XX クライアントエラーか 5XX サーバーエラーのレスポンス)の場合、
:meth:`Response.raise_for_status() <requests.Response.raise_for_status>` の例外が発生します。

    >>> bad_r = requests.get('http://httpbin.org/status/404')
    >>> bad_r.status_code
    404

    >>> bad_r.raise_for_status()
    Traceback (most recent call last):
      File "requests/models.py", line 832, in raise_for_status
        raise http_error
    requests.exceptions.HTTPError: 404 Client Error

.. But, since our ``status_code`` for ``r`` was ``200``, when we call
   ``raise_for_status()`` we get::

しかし、``r`` の ``status_code`` が ``200`` の場合、
``raise_for_status()`` を呼び出すと以下の結果を得ることができます。::

    >>> r.raise_for_status()
    None

.. All is well.

全て上手くいきました。


.. Response Headers
   ----------------

レスポンスヘッダー
-----------------------

.. We can view the server's response headers using a Python dictionary::

Python のディクショナリで実装されたサーバーのレスポンスヘッダーを表示することができます。::

    >>> r.headers
    {
        'content-encoding': 'gzip',
        'transfer-encoding': 'chunked',
        'connection': 'close',
        'server': 'nginx/1.0.4',
        'x-runtime': '148ms',
        'etag': '"e1ca502697e5c9317743dc078f67693f"',
        'content-type': 'application/json'
    }

.. The dictionary is special, though: it's made just for HTTP headers. According to
   `RFC 7230 <http://tools.ietf.org/html/rfc7230#section-3.2>`_, HTTP Header names
   are case-insensitive.

ディクショナリとはいえ特別で、HTTP ヘッダーのためだけに実装されています。
`RFC 7230 <http://tools.ietf.org/html/rfc7230#section-3.2>`_ によると、HTTP ヘッダーは大文字と小文字を区別しません。

So, we can access the headers using any capitalization we want::

    >>> r.headers['Content-Type']
    'application/json'

    >>> r.headers.get('content-type')
    'application/json'

It is also special in that the server could have sent the same header multiple
times with different values, but requests combines them so they can be
represented in the dictionary within a single mapping, as per
`RFC 7230 <http://tools.ietf.org/html/rfc7230#section-3.2>`_:

    A recipient MAY combine multiple header fields with the same field name
    into one "field-name: field-value" pair, without changing the semantics
    of the message, by appending each subsequent field value to the combined
    field value in order, separated by a comma.

Cookies
-------

.. If a response contains some Cookies, you can quickly access them::

レスポンスに Cookie がある場合、簡単にアクセスすることができます。::

    >>> url = 'http://example.com/some/cookie/setting/url'
    >>> r = requests.get(url)

    >>> r.cookies['example_cookie_name']
    'example_cookie_value'

.. To send your own cookies to the server, you can use the ``cookies``
   parameter::

Cookie をサーバーに送信するには、``cookies`` パラメータを使います。::

    >>> url = 'http://httpbin.org/cookies'
    >>> cookies = dict(cookies_are='working')

    >>> r = requests.get(url, cookies=cookies)
    >>> r.text
    '{"cookies": {"cookies_are": "working"}}'

.. Cookies are returned in a :class:`~requests.cookies.RequestsCookieJar`,
   which acts like a ``dict`` but also offers a more complete interface,
   suitable for use over multiple domains or paths.  Cookie jars can
   also be passed in to requests::

Cookie は ``ディクショナリ`` のように振る舞う :class:`~requests.cookies.RequestsCookieJar` から返却され、
複数のドメインやパスでの使用に適したより完全なインターフェースも提供しています。
CookieJar をリクエストに渡すこともできます。::

    >>> jar = requests.cookies.RequestsCookieJar()
    >>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    >>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
    >>> url = 'http://httpbin.org/cookies'
    >>> r = requests.get(url, cookies=jar)
    >>> r.text
    '{"cookies": {"tasty_cookie": "yum"}}'


.. Redirection and History
   -----------------------

リダイレクトと履歴
--------------------------

.. By default Requests will perform location redirection for all verbs except
   HEAD.

デフォルトでは、Requests は HEAD を除く全ての HTTP メソッドに対してリダイレクトを実行できます。

.. We can use the ``history`` property of the Response object to track redirection.

リダイレクトの履歴を追跡するために、Response オブジェクトの ``history`` プロパティを使えます。

.. The :attr:`Response.history <requests.Response.history>` list contains the
   :class:`Response <requests.Response>` objects that were created in order to
   complete the request. The list is sorted from the oldest to the most recent
   response.

:attr:`Response.history <requests.Response.history>` のリストには、
リクエストを完了するために作成された :class:`Response <requests.Response>` オブジェクトが含まれています。
リストは、最も古いレスポンスから最も新しいレスポンス順に並んでいます。

.. For example, GitHub redirects all HTTP requests to HTTPS::

例として、GitHub は全ての HTTP リクエストを HTTPS にリダイレクトします。::

    >>> r = requests.get('http://github.com')

    >>> r.url
    'https://github.com/'

    >>> r.status_code
    200

    >>> r.history
    [<Response [301]>]


.. If you're using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable
   redirection handling with the ``allow_redirects`` parameter::

GET、OPTIONS、POST、PUT、PATCH、DELETE を使う場合、
``allow_redirects`` パラメータでリダイレクト処理を向こうにできます。::

    >>> r = requests.get('http://github.com', allow_redirects=False)

    >>> r.status_code
    301

    >>> r.history
    []

.. If you're using HEAD, you can enable redirection as well::

HEAD を使う場合、リダイレクトを有効にすることができます。::

    >>> r = requests.head('http://github.com', allow_redirects=True)

    >>> r.url
    'https://github.com/'

    >>> r.history
    [<Response [301]>]


.. Timeouts
   --------

タイムアウト
-------------

.. You can tell Requests to stop waiting for a response after a given number of
   seconds with the ``timeout`` parameter. Nearly all production code should use
   this parameter in nearly all requests. Failure to do so can cause your program
   to hang indefinitely::

``timeout`` パラメータに秒数の数字を渡すと、渡した秒数後に Requests がレスポンスの待ち受けを止めるように指示することができます。
ほぼ全てのプロダクションのコードでは、ほぼ全てのリクエストでこのパラメータを使う必要があります。
それをしておかないと、プログラムが無期限にハングする原因になります。

    >>> requests.get('http://github.com', timeout=0.001)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)


.. admonition:: Note

    ``timeout`` is not a time limit on the entire response download;
    rather, an exception is raised if the server has not issued a
    response for ``timeout`` seconds (more precisely, if no bytes have been
    received on the underlying socket for ``timeout`` seconds). If no timeout is specified explicitly, requests do
    not time out.


.. Errors and Exceptions
   ---------------------

エラーと例外
---------------------

.. In the event of a network problem (e.g. DNS failure, refused connection, etc),
   Requests will raise a :exc:`~requests.exceptions.ConnectionError` exception.

ネットワークの問題(DNSの障害、接続拒否等)が発生した場合、Requests は :exc:`~requests.exceptions.ConnectionError` の例外を発生させます。

.. :meth:`Response.raise_for_status() <requests.Response.raise_for_status>` will
   raise an :exc:`~requests.exceptions.HTTPError` if the HTTP request
   returned an unsuccessful status code.

:meth:`Response.raise_for_status() <requests.Response.raise_for_status>` は、
HTTP リクエストが失敗のステータスコードを返すと、:exc:`~requests.exceptions.HTTPError` を発生させます。

.. If a request times out, a :exc:`~requests.exceptions.Timeout` exception is
   raised.

リクエストがタイムアウトした場合、:exc:`~requests.exceptions.Timeout` の例外を発生させます。

.. If a request exceeds the configured number of maximum redirections, a
   :exc:`~requests.exceptions.TooManyRedirects` exception is raised.

リクエストが設定されている最大のリダイレクト数を超えると、
:exc:`~requests.exceptions.TooManyRedirects` の例外を発生させます。

.. All exceptions that Requests explicitly raises inherit from
   :exc:`requests.exceptions.RequestException`.

Requests が明示的に発生させる全ての例外は、:exc:`requests.exceptions.RequestException` を継承しています。

-----------------------

Ready for more? Check out the :ref:`advanced <advanced>` section.
