"""Practical guide to large language models for software engineers.

This script provides simple educational examples for:
- what an LLM is
- tokens and context windows
- training vs inference
- parameters and temperature
- prompts, system vs user messages
- hallucination causes
- LLM vs traditional ML
"""

from __future__ import annotations


def estimate_tokens(text: str, chars_per_token: float = 4.0) -> int:
    """Approximate token count using a simple English rule-of-thumb.

    This is educational and intentionally approximate. Real tokenization is model-specific.
    """
    if not text:
        return 0
    return max(1, round(len(text) / chars_per_token))


def print_section(title: str) -> None:
    print(f"\n{'=' * 80}\n{title}\n{'=' * 80}")


def explain_llm() -> None:
    print("An LLM is a neural model trained to predict the next token in a sequence.")
    print("In simple terms, it learns patterns in language and uses them to generate text, code, and structured output.")
    print("It is best seen as a probability model over language, not as a source of guaranteed truth.")


def show_tokens() -> None:
    examples = {
        "Short prompt": "Write a Python function to sum a list.",
        "Code sample": "def add_numbers(values):\n    return sum(values)",
        "Longer doc": "Large language models use transformer architectures to process sequences of tokens and predict the next token.",
    }

    print("Token estimation examples (rough rule of thumb: ~4 chars per token):")
    for label, text in examples.items():
        count = estimate_tokens(text)
        print(f"- {label}: {len(text)} chars -> ~{count} tokens")


def show_context_window() -> None:
    context_examples = {
        "Small model": 4096,
        "Mid-size model": 32768,
        "Long-context model": 128000,
    }

    print("Example context windows (token budgets):")
    for name, tokens in context_examples.items():
        print(f"- {name}: {tokens:,} tokens")

    prompt = (
        "System: You are a helpful engineering assistant.\n"
        "User: Explain how context windows work in LLM systems.\n"
        "User: Keep the answer concise but clear."
    )
    print(f"Prompt size estimate: {estimate_tokens(prompt)} tokens")


def show_training_vs_inference() -> None:
    print("Training: expensive offline process that learns model weights from large datasets.")
    print("Inference: using the trained model to respond to live requests and generate outputs.")
    print("Typical production design: train once, serve many inferences efficiently.")


def show_parameters() -> None:
    models = {
        "Small": 7_000_000_000,
        "Large": 70_000_000_000,
        "Enterprise-scale": 405_000_000_000,
    }

    print("Example parameter counts (approximate):")
    for name, params in models.items():
        print(f"- {name}: {params:,} parameters")

    print("More parameters can increase expressiveness, but data quality, training procedure, and system design matter too.")


def show_temperature() -> None:
    temps = {
        "0.1": "Precise, deterministic, ideal for extraction and classification",
        "0.4": "Mostly stable, still useful for general assistance",
        "0.8": "More creative and varied output",
        "1.2": "High diversity but more risk of drift or hallucination",
    }

    print("Temperature controls randomness:")
    for value, description in temps.items():
        print(f"- {value}: {description}")


def show_prompt_examples() -> None:
    system = (
        "You are a senior software engineer. Be concise, factual, and say 'unknown' "
        "when the answer is not supported by the provided context."
    )
    user = (
        "Given this deployment log, summarize the likely causes of latency and provide "
        "the top 3 remediation steps."
    )

    print("Example system message:")
    print(system)
    print("\nExample user message:")
    print(user)


def show_hallucination_reasons() -> None:
    reasons = [
        "The model predicts likely text, not verified facts.",
        "It can infer patterns even when evidence is weak or missing.",
        "High temperature or vague prompts increase drift.",
        "It may sound confident while inventing details.",
    ]

    print("Why hallucinations happen:")
    for reason in reasons:
        print(f"- {reason}")

    print("Mitigations: retrieval grounding, citations, structured schemas, validation, and explicit uncertainty handling.")


def show_llm_vs_traditional_ml() -> None:
    print("Traditional ML:")
    print("- Narrow tasks, explicit labels, focused feature engineering")
    print("- Great for classification, forecasting, and ranking")
    print("- Usually trained for a specific objective")

    print("\nLLMs:")
    print("- General-purpose language interface")
    print("- Flexible across tasks through prompting and tool use")
    print("- Strong at summarization, code generation, and language interaction")
    print("- Require careful control for factual reliability and safety")


def main() -> None:
    print_section("What Is an LLM? A Practical Guide for Software Engineers")
    explain_llm()

    print_section("Tokens")
    show_tokens()

    print_section("Context Window")
    show_context_window()

    print_section("Training vs Inference")
    show_training_vs_inference()

    print_section("Parameters")
    show_parameters()

    print_section("Temperature")
    show_temperature()

    print_section("Prompt and Role Messages")
    show_prompt_examples()

    print_section("Why LLMs Hallucinate")
    show_hallucination_reasons()

    print_section("LLM vs Traditional ML")
    show_llm_vs_traditional_ml()

    print("\nEngineering takeaway: use LLMs as reasoning assistants, not as unquestioned truth sources. Ground them, validate them, and control context and output quality.")


if __name__ == "__main__":
    main()
