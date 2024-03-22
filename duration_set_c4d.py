import c4d
import json
import os

def create_project_from_base(base_path, json_path, output_folder):
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
        doc.SetMaxTime(c4d.BaseTime(frame_count / doc.GetFps()))

        # ドキュメントを保存
        save_path = os.path.join(output_folder, f"{cut_number}.c4d")
        if c4d.documents.SaveDocument(doc, save_path, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT):
            print(f"saved {save_path}")
        else:
            return False  # ドキュメントの保存に失敗した場合は、処理を終了

    return True  # すべてのファイルの保存に成功した場合

def main():
    base_path = c4d.storage.LoadDialog(title="ベースとなるC4Dファイルを選択してください", flags=c4d.FILESELECT_LOAD)
    if not base_path:
        print("ベースファイルの選択がキャンセルされました。")
        return

    json_path = c4d.storage.LoadDialog(title="JSONファイルを選択してください", flags=c4d.FILESELECT_LOAD)
    if not json_path:
        print("JSONファイルの選択がキャンセルされました。")
        return

    output_folder = c4d.storage.LoadDialog(title="出力先のフォルダを選択してください", flags=c4d.FILESELECT_DIRECTORY)
    if not output_folder:
        print("出力先フォルダの選択がキャンセルされました。")
        return

    if create_project_from_base(base_path, json_path, output_folder):
        c4d.gui.MessageDialog('全てのC4Dファイルの出力が完了しました。')
    else:
        c4d.gui.MessageDialog('C4Dファイルの出力中にエラーが発生しました。')

# スクリプトの実行
if __name__=='__main__':
    main()
