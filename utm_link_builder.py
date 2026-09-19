#!/usr/bin/env python3
"""Build a URL with UTM query parameters."""

from __future__ import annotations

import argparse
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


def build_utm_url(
    url: str,
    source: str,
    medium: str,
    campaign: str,
    content: str | None = None,
    term: str | None = None,
) -> str:
    parts = urlsplit(url.strip())
    if not parts.scheme or not parts.netloc:
        raise ValueError("URL must be absolute (include https://)")

    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query["utm_source"] = source.strip()
    query["utm_medium"] = medium.strip()
    query["utm_campaign"] = campaign.strip()
    if content:
        query["utm_content"] = content.strip()
    if term:
        query["utm_term"] = term.strip()

    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Append UTM params to a base URL")
    parser.add_argument("--url", required=True, help="Absolute base URL")
    parser.add_argument("--source", required=True, help="utm_source")
    parser.add_argument("--medium", required=True, help="utm_medium")
    parser.add_argument("--campaign", required=True, help="utm_campaign")
    parser.add_argument("--content", default=None, help="utm_content (optional)")
    parser.add_argument("--term", default=None, help="utm_term (optional)")
    args = parser.parse_args(argv)

    try:
        print(build_utm_url(args.url, args.source, args.medium, args.campaign, args.content, args.term))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
