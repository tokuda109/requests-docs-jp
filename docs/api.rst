.. _api:

Developer Interface
===================

.. module:: requests

.. This part of the documentation covers all the interfaces of Requests. For
   parts where Requests depends on external libraries, we document the most
   important right here and provide links to the canonical documentation.

ドキュメントのこの章では、Requests の全てのインターフェースについて説明します。
Requests が外部のライブラリに依存する部分については、ここでは重要な部分についてのみドキュメント化し、
正式なドキュメントへのリンクを添えます。

.. Main Interface
   --------------

メインインターフェース
-------------------------

.. All of Requests' functionality can be accessed by these 7 methods.
   They all return an instance of the :class:`Response <Response>` object.

全ての Requests の機能には、以下の7つのメソッドにアクセスすることができます。
これらは全て :class:`Response <Response>` オブジェクトのインスタンスを返却します。

.. autofunction:: request

.. autofunction:: head
.. autofunction:: get
.. autofunction:: post
.. autofunction:: put
.. autofunction:: patch
.. autofunction:: delete

.. Exceptions
   ----------

例外
-------------

.. autoexception:: requests.RequestException
.. autoexception:: requests.ConnectionError
.. autoexception:: requests.HTTPError
.. autoexception:: requests.URLRequired
.. autoexception:: requests.TooManyRedirects
.. autoexception:: requests.ConnectTimeout
.. autoexception:: requests.ReadTimeout
.. autoexception:: requests.Timeout


.. Request Sessions
   ----------------

リクエストのセッション
-----------------------------

.. _sessionapi:

.. autoclass:: Session
   :inherited-members:


.. Lower-Level Classes
   -------------------

低レベルのクラス
----------------------

.. autoclass:: requests.Request
   :inherited-members:

.. autoclass:: Response
   :inherited-members:


.. Lower-Lower-Level Classes
   -------------------------

さらに低レベルのクラス
-------------------------

.. autoclass:: requests.PreparedRequest
   :inherited-members:

.. autoclass:: requests.adapters.BaseAdapter
   :inherited-members:

.. autoclass:: requests.adapters.HTTPAdapter
   :inherited-members:

.. Authentication
   --------------

認証
-----------------

.. autoclass:: requests.auth.AuthBase
.. autoclass:: requests.auth.HTTPBasicAuth
.. autoclass:: requests.auth.HTTPProxyAuth
.. autoclass:: requests.auth.HTTPDigestAuth



.. Encodings
   ---------

エンコーディング
------------------

.. autofunction:: requests.utils.get_encodings_from_content
.. autofunction:: requests.utils.get_encoding_from_headers
.. autofunction:: requests.utils.get_unicode_from_response


.. _api-cookies:

Cookies
-------

.. autofunction:: requests.utils.dict_from_cookiejar
.. autofunction:: requests.utils.add_dict_to_cookiejar
.. autofunction:: requests.cookies.cookiejar_from_dict

.. autoclass:: requests.cookies.RequestsCookieJar
   :inherited-members:

.. autoclass:: requests.cookies.CookieConflictError
   :inherited-members:



Status Code Lookup
------------------

.. autoclass:: requests.codes

::

    >>> requests.codes['temporary_redirect']
    307

    >>> requests.codes.teapot
    418

    >>> requests.codes['\o/']
    200



.. Migrating to 1.x
   ----------------

バージョン 1 系への移行
--------------------------------

.. This section details the main differences between 0.x and 1.x and is meant
   to ease the pain of upgrading.

この章では、バージョン 0.x と 1.x の主な違いについて説明し、アップグレードする際の苦痛を和らげることを目的としています。

.. API Changes
   ~~~~~~~~~~~

APIの変更
~~~~~~~~~~~~~~

.. ``Response.json`` is now a callable and not a property of a response.

* ``Response.json`` は呼び出し可能になって、レスポンスのプロパティではなくなりました。

  ::

      import requests
      r = requests.get('https://github.com/timeline.json')
      r.json()   # This *call* raises an exception if JSON decoding fails

.. The ``Session`` API has changed. Sessions objects no longer take parameters.
   ``Session`` is also now capitalized, but it can still be
   instantiated with a lowercase ``session`` for backwards compatibility.

* ``Session`` API が変更されました。
  セッションのオブジェクトはパラメータを受け取りません。
  ``Session`` という名称もキャピタライズされましたが、後方互換製のために ``session`` という
  lowercase でもインスタンスを作成することができます。

  ::

      s = requests.Session()    # formerly, session took parameters
      s.auth = auth
      s.headers.update(headers)
      r = s.get('http://httpbin.org/headers')

.. All request hooks have been removed except 'response'.

* 全てのリクエストのフックは、'response' を除いて削除されました。

.. Authentication helpers have been broken out into separate modules. See
   requests-oauthlib_ and requests-kerberos_.

* 認証ヘルパーは、別のモジュールに分割されています。requests-oauthlib_ と requests-kerberos_ を参照して下さい。

.. _requests-oauthlib: https://github.com/requests/requests-oauthlib
.. _requests-kerberos: https://github.com/requests/requests-kerberos

.. The parameter for streaming requests was changed from ``prefetch`` to
   ``stream`` and the logic was inverted. In addition, ``stream`` is now
   required for raw response reading.

* ストリーミングのリクエストのパラメータは ``prefetch`` から ``stream`` に変更され、ロジックが逆になりました。
  さらに、``stream`` は生のレスポンスを解釈するために必要になりました。

  ::

      # in 0.x, passing prefetch=False would accomplish the same thing
      r = requests.get('https://github.com/timeline.json', stream=True)
      for chunk in r.iter_content(8192):
          ...

.. The ``config`` parameter to the requests method has been removed. Some of
   these options are now configured on a ``Session`` such as keep-alive and
   maximum number of redirects. The verbosity option should be handled by
   configuring logging.

* リクエストのメソッドへの ``config`` パラメータは削除されました。
  これらのオプションの一部は、キープアライブや最大のリダイレクト数等の ``Session`` で設定されるようになりました。
  verbosity optionはロギングを設定することで処理する必要があります。

  ::

      import requests
      import logging

      # Enabling debugging at http.client level (requests->urllib3->http.client)
      # you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
      # the only thing missing will be the response.body which is not logged.
      try: # for Python 3
          from http.client import HTTPConnection
      except ImportError:
          from httplib import HTTPConnection
      HTTPConnection.debuglevel = 1

      logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
      logging.getLogger().setLevel(logging.DEBUG)
      requests_log = logging.getLogger("requests.packages.urllib3")
      requests_log.setLevel(logging.DEBUG)
      requests_log.propagate = True

      requests.get('http://httpbin.org/headers')



Licensing
~~~~~~~~~

.. One key difference that has nothing to do with the API is a change in the
   license from the ISC_ license to the `Apache 2.0`_ license. The Apache 2.0
   license ensures that contributions to Requests are also covered by the Apache
   2.0 license.

API と関係のない変更で大きなものの1つとして、ライセンスが ISC_ ライセンスから `Apache 2.0`_ ライセンスに変更されました。
Apache 2.0 ライセンスは、Requests へのコントリビューションも Apache 2.0 ライセンスの対象となります。

.. _ISC: http://opensource.org/licenses/ISC
.. _Apache 2.0: http://opensource.org/licenses/Apache-2.0


.. Migrating to 2.x
   ----------------

バージョン 2 系への移行
--------------------------------

.. Compared with the 1.0 release, there were relatively few backwards
   incompatible changes, but there are still a few issues to be aware of with
   this major release.

バージョン 1.0 のリリースと比較すると、後方互換性を壊す変更は比較的少なかったが、
このメジャーリリースではいくつか気をつけないといけないことがあります。

.. For more details on the changes in this release including new APIs, links
   to the relevant GitHub issues and some of the bug fixes, read Cory's blog_
   on the subject.

今回のリリースで含まれた新しい API、関連する Github の Issues、いくつかのバグ修正について修正の詳細は、
Cory のブログで詳細を確認して下さい。

.. _blog: http://lukasa.co.uk/2013/09/Requests_20/


.. API Changes
   ~~~~~~~~~~~

APIの変更
~~~~~~~~~~~~~~

.. There were a couple changes to how Requests handles exceptions.
   ``RequestException`` is now a subclass of ``IOError`` rather than
   ``RuntimeError`` as that more accurately categorizes the type of error.
   In addition, an invalid URL escape sequence now raises a subclass of
   ``RequestException`` rather than a ``ValueError``.

* Requests が例外処理をする方法のうち幾つかに変更がありました。
  ``RequestException`` は、エラーの種類をより明確に分類するために ``RuntimeError`` ではなく、
  ``IOError`` のサブクラスになりました。
  さらに、無効な URL のエスケースシーケンスの場合、``ValueError`` ではなく、
  ``RequestException`` のサブクラスとして例外を発生させます。

  ::

      requests.get('http://%zz/')   # raises requests.exceptions.InvalidURL

  .. Lastly, ``httplib.IncompleteRead`` exceptions caused by incorrect chunked
     encoding will now raise a Requests ``ChunkedEncodingError`` instead.

  最後に、不正なチャンクエンコーディングが原因となって発生した ``httplib.IncompleteRead`` の例外は、
  代わりに Requests の ``ChunkedEncodingError`` を発生させます。

.. The proxy API has changed slightly. The scheme for a proxy URL is now
   required.

* プロキシの API が少し変更されました。プロキシ URL のスキームが必要になりました。

  ::

      proxies = {
        "http": "10.10.1.10:3128",    # use http://10.10.1.10:3128 instead
      }

      # In requests 1.x, this was legal, in requests 2.x,
      #  this raises requests.exceptions.MissingSchema
      requests.get("http://example.org", proxies=proxies)


.. Behavioural Changes
   ~~~~~~~~~~~~~~~~~~~~~~~

振る舞いの変化
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Keys in the ``headers`` dictionary are now native strings on all Python
   versions, i.e. bytestrings on Python 2 and unicode on Python 3. If the
   keys are not native strings (unicode on Python 2 or bytestrings on Python 3)
   they will be converted to the native string type assuming UTF-8 encoding.

``headers`` ディクショナリのキーは、全ての Python バージョンのネイティブの文字列になりました。
つまり、Python 2 におけるstr文字列で、Python 3 におけるunicode文字列のことです。
キーがネイティブ文字列(Python 2 におけるunicode文字列やPython 3 におけるstr文字列)ではない場合、
UTF-8 エンコーディングと仮定したネイティブ文字列に変換されます。

.. Values in the ``headers`` dictionary should always be strings. This has
   been the project's position since before 1.0 but a recent change
   (since version 2.11.0) enforces this more strictly. It's advised to avoid
   passing header values as unicode when possible.

``headers`` ディクショナリの値は常に文字列にしなければいけません。
これは 1.0 以前のプロジェクトの振る舞いですが、最近の変更(バージョン 2.11.0 以降)により厳密になりました。
可能であれば、ヘッダーの値を unicode として渡さないようにすることを推奨しています。
