function exportToJSON() {
    // padStartの代替関数
    function padStart(string, targetLength, padString) {
        string = String(string);
        padString = String((typeof padString !== 'undefined' ? padString : ' '));

        while (string.length < targetLength) {
            string = padString + string;
        }

        return string;
    }

    // コンポジションを取得
    var comp = app.project.activeItem;

    // 無効なコンポジションかをチェック
    if (!comp || !(comp instanceof CompItem)) {
        alert("有効なコンポジションが選択されていません。");
        return;
    }

    // 結果を保存するための配列
    var result = [];

    // レイヤーをループして情報を収集
    var count = 1;  // カウンター変数を導入
    for (var i = comp.layers.length; i > 0; i--) {
        var layer = comp.layers[i];

        var cutNumber = padStart(count, 3, '0'); // カウンター変数を使用
        var frameCount = layer.outPoint * comp.frameRate - layer.inPoint * comp.frameRate; // フレーム数を計算

        result.push({
            "cut_number": "cut" + cutNumber,
            "frame_count": Math.round(frameCount)
        });

        count++;  // カウンター変数を増加
    }

    // JSONデータを文字列として取得
    var jsonString = JSON.stringify(result, null, 4);

    // ファイルを保存
    var file = new File(Folder.desktop.fsName + "/output.json");
    if (file.open('w')) {
        file.write(jsonString);
        file.close();
        alert("JSONがデスクトップに保存されました。");
    } else {
        alert("ファイルの保存に失敗しました。");
    }
}

exportToJSON();  // 関数を呼び出して実行
