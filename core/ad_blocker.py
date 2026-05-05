from playwright.sync_api import BrowserContext, Route

_AD_PATTERNS = [
    "**/googlesyndication.com/**",
    "**/pagead2.googlesyndication.com/**",
    "**/doubleclick.net/**",
    "**/google-analytics.com/**",
    "**/googletagmanager.com/**",
    "**/googleadservices.com/**",
    "**/adservice.google.com/**",
    "**/*ads*",
    "**/analytics.js",
    "**/gtag/js",
]


def _abort(route: Route) -> None:
    route.abort()


def register_ad_blocker(context: BrowserContext) -> None:
    for pattern in _AD_PATTERNS:
        context.route(pattern, _abort)
