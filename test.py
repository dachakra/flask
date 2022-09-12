import sentry_sdk


sentry_sdk.init(
    dsn="https://e5b8d8f5f3dc4b42b87b71e64b7ec1bc@o87286.ingest.sentry.io/6399892",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # traces_sample_rate=1.0,
)


def main():
    foo();

if __name__ == "__main__":
    main()