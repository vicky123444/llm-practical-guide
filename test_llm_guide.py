import sys
import subprocess

from llm_guide import estimate_tokens


def test_estimate_tokens_empty():
    assert estimate_tokens("") == 0


def test_estimate_tokens_hello():
    # 'hello' is 5 chars -> round(5/4) == 1, and function uses max(1, ...)
    assert estimate_tokens("hello", chars_per_token=4.0) == 1


def test_estimate_tokens_long():
    text = "a" * 400
    assert estimate_tokens(text, chars_per_token=4.0) == round(len(text) / 4.0)


def test_script_runs():
    # Run the script as a smoke test using the current Python interpreter
    subprocess.run([sys.executable, "llm_guide.py"], check=True)
