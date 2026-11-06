# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
    素のLLMは用語種を参照しないため、学習時にない情報について詳しく答えられず、
    "AIE2026の講座の宿題にある「3レベル」とは何ですか？"
    という質問には、最もらしい答えが返ってきた。
    しかし、agent は search_glossary という tool を呼び出しており、
    data/glossary.json から必要な用語を検索して、適切な回答が返ってきた。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
    [tool call]   search_glossary({'query': '3レベル'})
    [tool return] search_glossary -> [{"term": "宿題の3レベル", "lecture": 1, "definition": "AIE2026の宿題の構成。「基礎（講義内容の確認）」「実装（自分でコードを書く）」「発展（調査や試行）」の3段階があり、どれか1つに取り組…
    [usage] RunUsage(cost=Decimal('0.0006417'), details={'text_prompt_tokens': 939}, input_text_tokens=939, input_tokens=939, output_tokens=144, requests=2, tool_calls=1)
- 1つの質問での LLM 呼び出し回数（`requests`）：2回
- 追加したツールと、docstring に書いた説明：
    make_quiz という指定した回の用語を、用語集の中からランダムで1つクイズとして出力するツールを追加した。
    docstring は講義で例として扱われていた内容が適切だったため、そのままの説明を書いた。
    """指定した回の用語から 1つを選び、確認問題と答えを返す。「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。"""

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
