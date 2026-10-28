"""第1回: 会話履歴を保ちながらLLMに質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールを持たない「素の」呼び出し。
初回の質問後は、追加の質問を入力すると同じ会話の履歴を使って回答する。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
import time

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def ask(chat: genai.chats.Chat, question: str) -> str:
    started_at = time.perf_counter()
    response = chat.send_message(message=question)
    elapsed_seconds = time.perf_counter() - started_at

    print(f"[応答時間] {elapsed_seconds:.2f}秒")
    usage = response.usage_metadata
    print(
        f"[使用量] 入力トークン数: {usage.prompt_token_count}, "
        f"出力トークン数: {usage.candidates_token_count}"
    )

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    client = genai.Client(api_key=get_api_key())
    chat = client.chats.create(model=MODEL)

    try:
        question = args.question
        while True:
            print(f"[質問] {question}\n")
            print(ask(chat, question))
            print("\n続けて質問できます（終了するには空行）。")
            try:
                question = input("> ").strip()
            except EOFError:
                break
            if not question:
                break
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
