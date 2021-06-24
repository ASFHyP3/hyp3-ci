def test_hyp3_ci(script_runner):
    ret = script_runner.run('hyp3_ci', '-h')
    assert ret.success


def test_proc_ci(script_runner):
    ret = script_runner.run('proc_ci', '-h')
    assert ret.success
