.. _authentication:

.. Authentication
   ==============

認証
==============

.. This document discusses using various kinds of authentication with Requests.

このドキュメントでは、Requests で様々な種類の認証を使用する方法について説明します。

.. Many web services require authentication, and there are many different types.
   Below, we outline various forms of authentication available in Requests, from
   the simple to the complex.

多くのウェブサービスでは認証が必要となり、様々な認証方法があります。
以下で、シンプルなものから複雑なものまで Requests で利用できる様々な認証方法についての概要を説明します。

.. Basic Authentication
   --------------------

Basic認証
--------------------

.. Many web services that require authentication accept HTTP Basic Auth. This is
   the simplest kind, and Requests supports it straight out of the box.

認証が必要な多くのウェブサービスでは、HTTP Basic認証を受け付けています。
これは最も簡単な認証で、Requests はサポートしています。

.. Making requests with HTTP Basic Auth is very simple::

HTTP Basic認証でリクエストを生成するのは、とても簡単です。 ::

    >>> from requests.auth import HTTPBasicAuth
    >>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
    <Response [200]>

.. In fact, HTTP Basic Auth is so common that Requests provides a handy shorthand
   for using it::

実際、HTTP Basic認証はとても一般的なので、Requests は省略して書く方法を提供しています。

    >>> requests.get('https://api.github.com/user', auth=('user', 'pass'))
    <Response [200]>

.. Providing the credentials in a tuple like this is exactly the same as the
   ``HTTPBasicAuth`` example above.

このようなタプルによる認証情報を付与することで、上記の ``HTTP Basic認証`` の例と同じように動作します。

.. netrc Authentication
   ~~~~~~~~~~~~~~~~~~~~

netrc による認証
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. If no authentication method is given with the ``auth`` argument, Requests will
   attempt to get the authentication credentials for the URL's hostname from the
   user's netrc file. The netrc file overrides raw HTTP authentication headers
   set with `headers=`.

``auth`` 引数で認証方法が指定されていない場合、Requests はユーザーの netrc ファイルから URL のホスト名の認証クレデンシャルを得ようとします。
netrc ファイルは `headers=` でセットされた生の HTTP の認証ヘッダーを上書きします。

.. If credentials for the hostname are found, the request is sent with HTTP Basic
   Auth.

ホスト名のクレデンシャルが見つかった場合、リクエストは HTTP Basic 認証で送信されます。

.. Digest Authentication
   ---------------------

Digest認証
------------------------

.. Another very popular form of HTTP Authentication is Digest Authentication,
   and Requests supports this out of the box as well::

HTTP 認証の別の一般的な認証方法として、Digest 認証があり、Requests はサポートしています。

    >>> from requests.auth import HTTPDigestAuth
    >>> url = 'http://httpbin.org/digest-auth/auth/user/pass'
    >>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
    <Response [200]>


.. OAuth 1 Authentication
   ----------------------

OAuth1.0 認証
----------------------

.. A common form of authentication for several web APIs is OAuth. The ``requests-oauthlib``
   library allows Requests users to easily make OAuth 1 authenticated requests::

いくつかのウェブAPIにおいて、一般的な認証方法は OAuth です。
``requests-oauthlib`` ライブラリは、OAuth 1.0 認証のリクエストを生成するのが簡単にできます。 ::

    >>> import requests
    >>> from requests_oauthlib import OAuth1

    >>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
    ...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

    >>> requests.get(url, auth=auth)
    <Response [200]>

.. For more information on how to OAuth flow works, please see the official `OAuth`_ website.
   For examples and documentation on requests-oauthlib, please see the `requests_oauthlib`_
   repository on GitHub

OAuth フローの仕組みの詳細については、公式の `OAuth`_ ウェブサイトを参照して下さい。
requests-oauthlib のサンプルとドキュメントについては、GitHub の `requests_oauthlib`_ リポジトリを参照して下さい。

.. OAuth 2 and OpenID Connect Authentication
   -----------------------------------------

OAuth2.0 と OpenID Connect 認証
--------------------------------------------

.. The ``requests-oauthlib`` library also handles OAuth 2, the authentication mechanism
   underpinning OpenID Connect. See the `requests-oauthlib OAuth2 documentation`_ for
   details of the various OAuth 2 credential management flows:

``requests-oauthlib`` ライブラリは、OpenID Connect の基盤となる認証機構である OAuth2.0 も処理します。
様々な OAuth2.0 認証情報の管理フローの詳細については `requests-oauthlib OAuth2 documentation`_ を参照して下さい。

* `Web Application Flow`_
* `Mobile Application Flow`_
* `Legacy Application Flow`_
* `Backend Application Flow`_

.. Other Authentication
   --------------------

その他の認証
-----------------------

.. Requests is designed to allow other forms of authentication to be easily and
   quickly plugged in. Members of the open-source community frequently write
   authentication handlers for more complicated or less commonly-used forms of
   authentication. Some of the best have been brought together under the
   `Requests organization`_, including:

Requests は他の認証方法を簡単で手っ取り早く拡張できるように作られています。
オープンソースコミュニティのメンバーは、より複雑であまり一般的に使われない認証方法のための認証用の処理をよく作ります。
これらの認証方法の中から以下の良かったものは、`Requests organization`_ アカウントの下で管理されるようになりました。

- Kerberos_
- NTLM_

.. If you want to use any of these forms of authentication, go straight to their
   GitHub page and follow the instructions.

これらの認証方法を使う場合は、GitHub ページを参照して、やり方に従って下さい。

.. New Forms of Authentication
   ---------------------------

新しい認証方法
------------------------------

.. If you can't find a good implementation of the form of authentication you
   want, you can implement it yourself. Requests makes it easy to add your own
   forms of authentication.

望むような認証方法を実装したものが見つからない場合、自身で実装することができます。
Requests は独自の認証方法を簡単に追加することができます。

.. To do so, subclass :class:`AuthBase <requests.auth.AuthBase>` and implement the
  ``__call__()`` method::

実装するには、サブクラスを :class:`AuthBase <requests.auth.AuthBase>` にして、
``__call__()`` メソッドを実装して下さい。 ::

    >>> import requests
    >>> class MyAuth(requests.auth.AuthBase):
    ...     def __call__(self, r):
    ...         # Implement my authentication
    ...         return r
    ...
    >>> url = 'http://httpbin.org/get'
    >>> requests.get(url, auth=MyAuth())
    <Response [200]>

.. When an authentication handler is attached to a request,
   it is called during request setup. The ``__call__`` method must therefore do
   whatever is required to make the authentication work. Some forms of
   authentication will additionally add hooks to provide further functionality.

認証処理がリクエストに付与されると、リクエストのセットアップ中に呼び出されます。
``__call__`` メソッドは、認証作業を行うために必要となる処理の全てを行う必要があります。
いくつかの認証方法は、さらに機能を提供するためにフックが追加されています。

.. Further examples can be found under the `Requests organization`_ and in the
   ``auth.py`` file.

その他のサンプルは、`Requests organization`_ アカウントにあり、``auth.py`` ファイルの中にあります。

.. _OAuth: http://oauth.net/
.. _requests_oauthlib: https://github.com/requests/requests-oauthlib
.. _requests-oauthlib OAuth2 documentation: http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html
.. _Web Application Flow: http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#web-application-flow
.. _Mobile Application Flow: http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#mobile-application-flow
.. _Legacy Application Flow:  http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#legacy-application-flow
.. _Backend Application Flow:  http://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#backend-application-flow
.. _Kerberos: https://github.com/requests/requests-kerberos
.. _NTLM: https://github.com/requests/requests-ntlm
.. _Requests organization: https://github.com/requests
