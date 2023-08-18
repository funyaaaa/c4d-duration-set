import c4d
import json

def create_project_from_base(base_path, json_path):
    # JSONファイルを開き、データを読み取る
    with open(json_path, 'r') as f:
        content = f.read()
        print(content)
        cuts = json.loads(content)

    # 各カットに対してプロジェクトファイルを作成
    for cut in cuts:
        cut_number = cut['cut_number']
        frame_count = cut['frame_count']

        # 既存のドキュメントをロード
        doc = c4d.documents.LoadDocument(base_path, c4d.SCENEFILTER_0)
        if not doc:
            return False

        # フレーム数を設定
        doc.SetMinTime(c4d.BaseTime(0))
        doc.SetMaxTime(c4d.BaseTime(frame_count, doc.GetFps()))

        # ドキュメントを保存
        save_path = f"/{cut_number}.c4d"  # C4Dファイルの保存先のパスを設定してください
        c4d.documents.SaveDocument(doc, save_path, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)

        print("saved " + cut_number +".c4d")

    return True

# 実行
base_path = f""  # ベースとなるC4Dファイルのパスを指定してください
json_path = f""  # JSONファイルのパスを指定してください
create_project_from_base(base_path, json_path)
