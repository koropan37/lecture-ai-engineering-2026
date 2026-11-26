# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：
    app.agent --list-tools
    モデルに見えているツール: 3 個
    [search_materials], [make_quiz], [save_learning_log]

    app.mcp_agent --list-tools
    モデルに見えているツール: 1 個
    [glossary_search_glossary]

- STEP 2 の [tool call]：
    [tool call]   glossary_search_glossary({'query': '3レベル'})

- STEP 3 の [tool call]：
    [tool call]   fetch_fetch({'url': 'https://modelcontextprotocol.io/'})

- STEP 4 の [tool call]：
    [tool call]   aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Amazon S3 バージョニング 概要'})
    [tool call]   aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Using versioning in S3 buckets overview'})
    [tool call]   glossary_search_glossary({'query': 'Amazon S3'})

- 気づき・疑問：
    外部や公開されているMCPサーバーを利用する際には、その安全性を確かめないと、自分で中身が確認できないことがあるので、出どころの信用は大事たと感じる。
    今回の演習で気になったことは、最後のAWSのツールを呼び出す時に、一緒に glossary_search_glossary も呼び出されていることが気になった。
    全部のMCPを起動してどのツールを使うのかを判断しているのはモデルだが、1、2回目のツールの呼び出しで必要な情報は手に入れられたのではないか、また起動順にツールが呼び出されるのではなく、最後に呼び出されて必要な情報は見つかりませんでした。という結果だったので、なぜ呼び出したのだろうと気になった。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
