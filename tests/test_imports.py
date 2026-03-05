def test_imports() -> None:
    import gogi_bot
    import gogi_bot.analytics.performance
    import gogi_bot.backtest.vectorbt_runner
    import gogi_bot.connectors.base
    import gogi_bot.connectors.ccxt_connector
    import gogi_bot.dex.dydx_v4_client
    import gogi_bot.dex.hyperliquid_client
    import gogi_bot.marketdata.cryptofeed_adapter
    import gogi_bot.orderbook.book
    import gogi_bot.orderbook.features
    import gogi_bot.risk.guards
    import gogi_bot.strategies.base
    import gogi_bot.strategies.examples

    assert gogi_bot.__version__

