# -*- coding: utf-8 -*-

"""
requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.
"""
from urllib3.exceptions import HTTPError as BaseHTTPError


class RequestException(IOError):
    """
    .. There was an ambiguous exception that occurred while handling your
       request.

    リクエストの処理中に原因不明な例外が起きた時に送出されます。
    """

    def __init__(self, *args, **kwargs):
        """Initialize RequestException with `request` and `response` objects."""
        response = kwargs.pop('response', None)
        self.response = response
        self.request = kwargs.pop('request', None)
        if (response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request
        super(RequestException, self).__init__(*args, **kwargs)


class HTTPError(RequestException):
    """
    .. An HTTP error occurred.

    HTTP エラーが起きた時に送出されます。
    """


class ConnectionError(RequestException):
    """
    .. A Connection error occurred.

    コネクションエラーが起きた時に送出されます。
    """


class ProxyError(ConnectionError):
    """A proxy error occurred."""


class SSLError(ConnectionError):
    """An SSL error occurred."""


class Timeout(RequestException):
    """
    .. The request timed out.

    リクエストがタイムアウトした時に送出されます。

    .. Catching this error will catch both
       :exc:`~requests.exceptions.ConnectTimeout` and
       :exc:`~requests.exceptions.ReadTimeout` errors.

    このエラーを受け取ると、:exc:`~requests.exceptions.ConnectTimeout` と
    :exc:`~requests.exceptions.ReadTimeout` の2つのエラーを受け取ることになります。
    """


class ConnectTimeout(ConnectionError, Timeout):
    """
    .. The request timed out while trying to connect to the remote server.

    リモートサーバーに接続しようとして、リクエストがタイムアウトした時に送出されます。

    .. Requests that produced this error are safe to retry.

    このエラーが発生したリクエストは、再度実行しても問題ありません。
    """


class ReadTimeout(Timeout):
    """
    .. The server did not send any data in the allotted amount of time.

    サーバーが設定された時間内にデータを返却しなかった場合に送出されます。
    """


class URLRequired(RequestException):
    """
    .. A valid URL is required to make a request.

    リクエストを生成するときに有効な URL が必要です。
    """


class TooManyRedirects(RequestException):
    """
    .. Too many redirects.

    リダイレクト回数が多すぎる時に送出されます。
    """


class MissingSchema(RequestException, ValueError):
    """The URL schema (e.g. http or https) is missing."""


class InvalidSchema(RequestException, ValueError):
    """See defaults.py for valid schemas."""


class InvalidURL(RequestException, ValueError):
    """The URL provided was somehow invalid."""


class InvalidHeader(RequestException, ValueError):
    """The header value provided was somehow invalid."""


class ChunkedEncodingError(RequestException):
    """The server declared chunked encoding but sent an invalid chunk."""


class ContentDecodingError(RequestException, BaseHTTPError):
    """Failed to decode response content"""


class StreamConsumedError(RequestException, TypeError):
    """The content for this response was already consumed"""


class RetryError(RequestException):
    """Custom retries logic failed"""


class UnrewindableBodyError(RequestException):
    """Requests encountered an error when trying to rewind a body"""

# Warnings


class RequestsWarning(Warning):
    """Base warning for Requests."""
    pass


class FileModeWarning(RequestsWarning, DeprecationWarning):
    """A file was opened in text mode, but Requests determined its binary length."""
    pass


class RequestsDependencyWarning(RequestsWarning):
    """An imported dependency doesn't match the expected version range."""
    pass
