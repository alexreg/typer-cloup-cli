import os
import subprocess


def test_script_completion_run():
    result = subprocess.run(
        ["coverage", "run", "-m", "typer_cloup_cli"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_PYTHON _M TYPER_CLOUP_CLI_COMPLETE": "bash_complete",
            "COMP_WORDS": "typer tests/assets/sample.py",
            "COMP_CWORD": "2",
            "_TYPER_COMPLETE_TESTING": "True",
        },
    )
    assert "run" in result.stdout
