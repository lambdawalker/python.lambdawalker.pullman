def test_smoke():
    from lambdawalker.pullman.pullman import Orchestrator, BaseWorker
    assert Orchestrator is not None
    print("pullman OK")
