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

- 取り組んだレベル：基礎 
- やったこと：
    MCPサーバーに get_lecture_summsry の追加
- 結果：
    "第2回では何を学びますか？ "
    という質問に対し、
    [tool call]   glossary_get_lecture_summary({'lecture': 2})
    の呼び出し
- 気づき・疑問：
    ツールを追加する前に同じコマンドを実行してみたところ
    [tool call]   glossary_search_glossary({'query': '第2回'})
    が呼び出されていた。
    回答としては、どちらも正しい回答を得ることができたため問題ないのだが、ツールを追加した後ではsearch_glossaryこのツールは呼び出されないのかと疑問に思った。
    演習の時はAWSのことについて質問した際に、上記のツールが呼び出されていたので、今回も呼び出されていてもおかしくないと思っていた。


- 取り組んだレベル：実装 
- やったこと：
    MCPサーバーに make_quiz の追加
    範囲外の回を指定した際に、わかりやすいメッセージを返す
- 結果：
    "第2回のクイズを作って" -> 
    **【確認問題】**
    Q. 「エポック」の意味は何でしょうか？
    💡 **ヒント：**
    ...

    [tool call]   glossary_make_quiz({'lecture': 2})

    "第99回のクイズを作って" ->
    第99回の講義は講座の範囲外となっており、用意されていません。
    現在指定できる講義回は以下の通りです。
    - 第1回
    - 第2回
    - 第3回
    - 第4回
    - 第6回
    もしよろしければ、上記のいずれかの回のクイズを作成いたしますので、ご希望の回をお知らせください！

    [tool call]   glossary_make_quiz({'lecture': 99})

- 気づき・疑問：
    make_quiz は前に作成したものに、load_glossary()　を追加し、MCPサーバーに追加するだけだったのであまり難しくはなかった。
    正常に動くパターンと範囲外を指定したパターンのどちらもうまくいった。
    第5回の表記がなかったため、バグかと思ったら、 data/rag_data/lectures.json に登録されていないだけだった。


- 取り組んだレベル：発展
- やったこと：
    antigravity での MCPサーバーの設定方法
- 結果：
    設定ファイルとファイル名：
        ファイル名：mcp_config.json

        グローバル設定: ~/.gemini/config/mcp_config.json（すべてのプロジェクトに適用されます）。
        ワークスペース設定: <workspace>/.agents/mcp_config.json（該当するワークスペースにのみ適用されます）。
        プラグイン設定も可能：.agents/plugins/<plugin_name>/mcp_config.json　または
                          ~/.gemini/config/plugins/<plugin_name>/mcp_config.json
    設定ファイルの例:
    {
        "mcpServers": {
          "sqlite-explorer": {
            "command": "node",
            "args": ["/usr/local/bin/sqlite-mcp-server.js"],
            "env": {
                "SQLITE_DB_PATH": "/var/data/app.db"
            }
          },
            "my-remote-server": {
            "serverUrl": "https://api.example.com/mcp/",
            "headers": {
                "Authorization": "Bearer YOUR_API_TOKEN"
            }
          }
        }
    }
    コマンドで起動する方法：
        演習と同じく"mcpServers"の下にサーバー名をキーとして"command"（必須）、"args"（任意）、"env"（任意）を書く
    
    URL で接続する書き方：
        演習と同じく、"serverUrl" に接続先 URL を書きます（"url" も可）。
    
    有効になる範囲
        グローバル設定ではすべてのプロジェクトで有効になる。
        ワークスペース設定では該当するワークススペースでのみ有効になる。
        プラグインではグローバル、ワークスペースのどちらも配置可能

    URL：https://antigravity.google/docs/mcp/
        https://antigravity.google/docs/build-plugins/

- 気づき・疑問：
    ファイル構造の書き方は 演習のものとほとんど同じで、サーバー名、コマンド or url で設定できる。
    args などの任意のオプションもあった。
    外部のMCPへの接続も url や serverUrl から接続可能でほとんど同じである。
    設定ファイルがグローバルやワークスペース、プラグインなど自分が望む環境に配置できる点が、より柔軟性がある点だと思った。