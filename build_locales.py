import json, pathlib
root=pathlib.Path(__file__).parent
langs=['ko','en','es','zh','ja','de']
data=r'''title|폴더 납품 목록 생성|Folder Delivery Manifest|Manifiesto de carpeta|文件夹交付清单|フォルダー納品リスト|Ordner-Übergabeliste
badge|브라우저 안에서 처리|Processed in your browser|Procesado en tu navegador|浏览器本地处理|ブラウザー内で処理|Verarbeitung im Browser
hero|납품할 폴더,\n목록까지 깔끔하게.|Your folder,\nready for delivery.|Tu carpeta,\nlista para entregar.|交付文件夹，\n清单一目了然。|納品するフォルダーを、\n一覧まで整える。|Dein Ordner,\nsauber übergeben.
intro|상대 경로·크기·수정시각을 정리하고 SHA-256으로 내용을 확인하세요.|List relative paths, sizes and timestamps. Add SHA-256 when you need a content fingerprint.|Organiza rutas, tamaños y fechas. Añade SHA-256 para identificar el contenido.|整理相对路径、大小和修改时间，按需计算 SHA-256。|相対パス・サイズ・更新日時を整理。必要に応じて SHA-256 を計算します。|Relative Pfade, Größen und Zeitstempel auflisten. Optional SHA-256 berechnen.
choose|폴더를 선택하세요|Choose a folder|Elige una carpeta|选择文件夹|フォルダーを選択|Ordner auswählen
private|원본을 변경하지 않으며 업로드하지 않습니다.|Originals stay unchanged. No uploads.|No se modifican ni suben los originales.|不修改原文件，不上传数据。|元ファイルを変更・送信しません。|Originale bleiben unverändert. Kein Upload.
folder|폴더 선택|Choose folder|Elegir carpeta|选择文件夹|フォルダー選択|Ordner wählen
file|파일 선택|Choose files|Elegir archivos|选择文件|ファイル選択|Dateien wählen
example|예제로 체험|Try an example|Probar ejemplo|试用示例|サンプルを試す|Beispiel laden
limits|최대 2,000개 · 합계 500 MiB · 해시 파일당 100 MiB|Up to 2,000 files · 500 MiB total · 100 MiB per hashed file|Máximo 2.000 archivos · 500 MiB total · 100 MiB por archivo con hash|最多 2,000 个文件 · 总计 500 MiB · 哈希每文件 100 MiB|最大 2,000 件 · 合計 500 MiB · ハッシュは 1 件 100 MiB|Bis 2.000 Dateien · insgesamt 500 MiB · Hash je Datei 100 MiB
exclude|점(.)으로 시작하는 파일·폴더 제외|Exclude dot-prefixed files and folders|Excluir archivos y carpetas que empiezan por punto|排除名称以点开头的文件和文件夹|ドットで始まるファイル・フォルダーを除外|Dateien und Ordner mit Punkt am Anfang ausschließen
hash|SHA-256 계산|Calculate SHA-256|Calcular SHA-256|计算 SHA-256|SHA-256 を計算|SHA-256 berechnen
safe|CSV 수식 시작 문자 보호|Protect CSV formula prefixes|Proteger prefijos de fórmulas CSV|保护 CSV 公式起始字符|CSV の数式開始文字を保護|CSV-Formelanfänge schützen
generate|목록 생성|Generate manifest|Generar lista|生成清单|一覧を作成|Liste erstellen
clear|비우기|Clear|Vaciar|清空|クリア|Leeren
noSelection|선택된 파일 없음|No files selected|Sin archivos seleccionados|尚未选择文件|ファイル未選択|Keine Dateien ausgewählt
initial|예제로 출력 형식을 먼저 확인할 수 있습니다.|Try the example to preview the export format.|Prueba el ejemplo para ver el formato de salida.|可先使用示例查看导出格式。|サンプルで出力形式を確認できます。|Das Beispiel zeigt das Exportformat.
result|파일 목록|File manifest|Lista de archivos|文件清单|ファイル一覧|Dateiliste
csv|CSV 다운로드|Download CSV|Descargar CSV|下载 CSV|CSV ダウンロード|CSV herunterladen
md|Markdown 다운로드|Download Markdown|Descargar Markdown|下载 Markdown|Markdown ダウンロード|Markdown herunterladen
copy|Markdown 복사|Copy Markdown|Copiar Markdown|复制 Markdown|Markdown をコピー|Markdown kopieren
files|파일|files|archivos|个文件|ファイル|Dateien
total|전체 크기|Total size|Tamaño total|总大小|合計サイズ|Gesamtgröße
hashed|해시 계산|Hashed files|Archivos con hash|已计算哈希|ハッシュ計算済み|Hash berechnet
path|상대 경로|Relative path|Ruta relativa|相对路径|相対パス|Relativer Pfad
extension|확장자|Extension|Extensión|扩展名|拡張子|Erweiterung
size|크기|Size|Tamaño|大小|サイズ|Größe
modified|수정시각 (UTC)|Modified (UTC)|Modificado (UTC)|修改时间 (UTC)|更新日時 (UTC)|Geändert (UTC)
placeholder|목록을 생성하면 여기에 표시됩니다.|Your manifest will appear here.|La lista aparecerá aquí.|生成的清单将显示在这里。|作成した一覧が表示されます。|Hier erscheint die erstellte Liste.
preview|미리보기 최대 300행. 다운로드에는 전체 목록이 포함됩니다.|Preview: 300 rows maximum. Downloads include all processed files.|Vista previa: hasta 300 filas. La descarga incluye todos los archivos procesados.|最多预览 300 行，下载包含全部已处理文件。|プレビューは最大 300 行。ダウンロードには全件を含みます。|Vorschau: maximal 300 Zeilen. Downloads enthalten alle verarbeiteten Dateien.
helpTitle|처리 범위와 출처|Scope and sources|Alcance y fuentes|处理范围与来源|処理範囲と出典|Umfang und Quellen
help1|폴더 선택은 브라우저마다 다릅니다. 파일 선택으로 대체하면 폴더 경로가 없습니다. 브라우저가 전달한 파일만 포함하며 빈 폴더·권한 없는 파일·심볼릭 링크는 보장하지 않습니다. 운영체제 숨김 속성은 확인할 수 없어 점(.) 이름만 필터링합니다.|Folder selection depends on the browser. File selection has no folder paths. Only browser-provided files are included; empty folders, inaccessible files and symlinks are not guaranteed. Hidden OS attributes are unavailable; only dot-prefixed names are filtered.|La selección de carpetas depende del navegador. Al elegir archivos no hay rutas de carpeta. Solo se incluyen los archivos entregados por el navegador; no se garantizan carpetas vacías, archivos sin permiso ni enlaces simbólicos. Solo se filtran nombres que empiezan por punto, no atributos ocultos del sistema.|文件夹选择取决于浏览器。单独选择文件时不包含文件夹路径。仅处理浏览器提供的文件，不保证包含空文件夹、无权限文件或符号链接。无法读取系统隐藏属性，仅按点开头的名称筛选。|フォルダー選択はブラウザーによります。ファイル選択ではフォルダーパスがありません。ブラウザーが渡したファイルのみ対象で、空フォルダー・アクセス不可ファイル・シンボリックリンクは保証しません。OS の隠し属性は取得できず、ドット名のみ除外します。|Die Ordnerauswahl hängt vom Browser ab. Die Dateiauswahl liefert keine Ordnerpfade. Nur vom Browser gelieferte Dateien werden erfasst; leere Ordner, unzugängliche Dateien und Symlinks sind nicht garantiert. Versteckte Betriebssystemattribute sind nicht verfügbar; gefiltert werden nur Punktnamen.
help2|수정시각은 UTC입니다. 수식 보호는 공백 뒤 = + - @로 시작하는 값에 작은따옴표를 붙입니다. 원문이 필요하면 끄세요. SHA-256은 HTTPS 또는 localhost가 필요합니다. 입력·결과는 새로고침 시 사라집니다.|Timestamps use UTC. Formula protection prefixes an apostrophe to values starting with = + - @ after whitespace. Disable it for exact text. SHA-256 requires HTTPS or localhost. Reloading clears inputs and results.|Las fechas usan UTC. La protección añade un apóstrofo a valores que empiezan por = + - @ tras espacios. Desactívala para conservar el texto exacto. SHA-256 requiere HTTPS o localhost. Recargar borra entradas y resultados.|时间使用 UTC。公式保护会在空白后以 = + - @ 开头的值前添加单引号；需保留原文时可关闭。SHA-256 需要 HTTPS 或 localhost。刷新会清空输入和结果。|日時は UTC。数式保護は空白の後で = + - @ から始まる値にアポストロフィーを付けます。原文が必要なら解除してください。SHA-256 は HTTPS または localhost が必要です。再読み込みで入力・結果は消えます。|Zeitstempel verwenden UTC. Der Formelschutz setzt ein Apostroph vor Werte, die nach Leerraum mit = + - @ beginnen. Für exakten Text deaktivieren. SHA-256 benötigt HTTPS oder localhost. Neuladen löscht Eingaben und Ergebnisse.
footer|개인 검토용 · 기기에만 머무는 파일|Private review · Files stay on your device|Revisión privada · Los archivos permanecen en tu dispositivo|私人评审 · 文件仅留在本机|非公開レビュー用 · ファイルは端末内のみ|Private Prüfung · Dateien bleiben auf deinem Gerät
language|언어|Language|Idioma|语言|言語|Sprache
selected|옵션을 확인한 뒤 목록 생성을 누르세요.|Review the options, then generate the manifest.|Revisa las opciones y genera la lista.|检查选项后生成清单。|設定を確認して一覧を作成してください。|Optionen prüfen und die Liste erstellen.
cleared|파일 선택을 비웠습니다.|File selection cleared.|Selección vaciada.|已清空文件选择。|ファイル選択をクリアしました。|Dateiauswahl geleert.
changed|옵션이 변경되었습니다. 목록을 다시 생성하세요.|Options changed. Generate the manifest again.|Opciones cambiadas. Vuelve a generar la lista.|选项已更改，请重新生成清单。|設定が変更されました。一覧を再作成してください。|Optionen geändert. Liste erneut erstellen.
noHash|미계산|Not calculated|Sin calcular|未计算|未計算|Nicht berechnet
processing|처리 중|Processing|Procesando|正在处理|処理中|Verarbeitung
complete|완료|Complete|Completado|已完成|完了|Fertig
excludedLabel|제외|Excluded|Excluidos|已排除|除外|Ausgeschlossen
hashDone|SHA-256 계산 완료|SHA-256 complete|SHA-256 completado|SHA-256 已完成|SHA-256 計算完了|SHA-256 berechnet
copied|Markdown 목록을 복사했습니다.|Markdown copied.|Markdown copiado.|已复制 Markdown 清单。|Markdown をコピーしました。|Markdown kopiert.
clipboard|복사할 수 없습니다. 다운로드를 사용하세요.|Cannot copy. Use the download instead.|No se pudo copiar. Usa la descarga.|无法复制，请使用下载。|コピーできません。ダウンロードを使ってください。|Kopieren nicht möglich. Bitte herunterladen.
empty|폴더 또는 파일을 선택하세요.|Choose a folder or files.|Elige una carpeta o archivos.|请选择文件夹或文件。|フォルダーまたはファイルを選択してください。|Ordner oder Dateien auswählen.
countLimit|한 번에 2,000개까지 처리할 수 있습니다.|The limit is 2,000 files per run.|El límite es de 2.000 archivos por operación.|每次最多处理 2,000 个文件。|1 回につき最大 2,000 件です。|Maximal 2.000 Dateien pro Vorgang.
sizeLimit|선택한 파일의 합계가 500 MiB를 초과합니다.|Selected files exceed 500 MiB in total.|Los archivos superan 500 MiB en total.|所选文件总计超过 500 MiB。|選択ファイルの合計が 500 MiB を超えます。|Ausgewählte Dateien überschreiten insgesamt 500 MiB.
secure|SHA-256은 HTTPS 또는 localhost에서 지원됩니다.|SHA-256 requires HTTPS or localhost.|SHA-256 requiere HTTPS o localhost.|SHA-256 需要 HTTPS 或 localhost。|SHA-256 は HTTPS または localhost が必要です。|SHA-256 benötigt HTTPS oder localhost.
hashLimit|해시 계산은 파일당 100 MiB까지 지원합니다.|Hashing supports files up to 100 MiB each.|El hash admite hasta 100 MiB por archivo.|哈希计算每个文件最多支持 100 MiB。|ハッシュは 1 ファイル 100 MiB までです。|Hash-Berechnung unterstützt bis zu 100 MiB je Datei.
excluded|제외 옵션 적용 후 남은 파일이 없습니다.|No files remain after filtering.|No quedan archivos tras filtrar.|筛选后没有剩余文件。|除外後にファイルがありません。|Nach dem Filtern bleiben keine Dateien.
interrupted|입력이 변경되었습니다. 다시 생성하세요.|Input changed. Generate again.|La entrada cambió. Genera de nuevo.|输入已更改，请重新生成。|入力が変更されました。再作成してください。|Eingabe geändert. Erneut erstellen.
readError|파일을 읽을 수 없습니다. 다시 선택하세요.|Cannot read a file. Select files again.|No se pudo leer un archivo. Selecciónalo de nuevo.|无法读取文件，请重新选择。|ファイルを読み取れません。再選択してください。|Datei kann nicht gelesen werden. Erneut auswählen.
exportNote|크기 단위: bytes · 수정시각: UTC · SHA-256 빈칸: 미계산|Size: bytes · Timestamps: UTC · Blank SHA-256: not calculated|Tamaño: bytes · Fechas: UTC · SHA-256 vacío: sin calcular|大小：bytes · 时间：UTC · SHA-256 空白：未计算|サイズ: bytes · 日時: UTC · SHA-256 空欄: 未計算|Größe: bytes · Zeit: UTC · Leeres SHA-256: nicht berechnet'''
catalog={l:{} for l in langs}
for line in data.splitlines():
    key,*values=line.split('|')
    if len(values)!=6: raise ValueError((key,len(values)))
    for l,v in zip(langs,values): catalog[l][key]=v.replace('\\n','\n')
for l in langs:
    t=catalog[l];t['headers']=[t['path'],t['extension'],t['size']+' (bytes)',t['modified'],'SHA-256']
(root/'dist/locales.js').write_text('export const catalog='+json.dumps(catalog,ensure_ascii=False)+';\n',encoding='utf-8')
template='''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><base href="{base}"><title>{title}</title><link rel="stylesheet" href="style.css"></head><body><main><header><a class="brand" href="./">LOCAL / FILE TOOLS</a><span class="badge" data-t="badge"></span><label><span data-t="language"></span> <select id="language" aria-label="{language}"><option value="ko">한국어</option><option value="en">English</option><option value="es">Español</option><option value="zh">简体中文</option><option value="ja">日本語</option><option value="de">Deutsch</option></select></label></header><section class="hero"><p class="eyebrow">FOLDER MANIFEST</p><h1 data-t="hero" style="white-space:pre-line"></h1><p data-t="intro"></p></section><section class="panel"><div class="upload"><div class="folder-icon" aria-hidden="true">▱</div><h2 data-t="choose"></h2><p data-t="private"></p><div class="buttons"><label class="button primary"><span data-t="folder"></span><input id="folder" type="file" webkitdirectory multiple></label><label class="button"><span data-t="file"></span><input id="files" type="file" multiple></label><button id="example" data-t="example"></button></div><small data-t="limits"></small></div><div class="options"><label><input id="exclude" type="checkbox" checked><span data-t="exclude"></span></label><label><input id="hash" type="checkbox"><span data-t="hash"></span></label><label><input id="safe" type="checkbox" checked><span data-t="safe"></span></label></div><div class="actionbar"><button class="primary" id="generate" data-t="generate"></button><button id="clear" data-t="clear"></button><span id="selection" data-t="noSelection"></span></div><p id="status" role="status" aria-live="polite" data-t="initial"></p></section><section class="panel result"><div class="result-top"><div><p class="eyebrow">DELIVERY INDEX</p><h2 data-t="result"></h2></div><div class="buttons"><button id="csv" disabled data-t="csv"></button><button id="md" disabled data-t="md"></button><button id="copy" disabled data-t="copy"></button></div></div><div class="metrics"><div><strong id="count">0</strong><span data-t="files"></span></div><div><strong id="size">0 B</strong><span data-t="total"></span></div><div><strong id="hashed">0</strong><span data-t="hashed"></span></div></div><div class="table-wrap"><table><thead><tr><th data-t="path"></th><th data-t="extension"></th><th data-t="size"></th><th data-t="modified"></th><th>SHA-256</th></tr></thead><tbody id="rows"><tr><td colspan="5" class="empty" data-t="placeholder"></td></tr></tbody></table></div><p class="footnote" data-t="preview"></p></section><details><summary data-t="helpTitle"></summary><p data-t="help1"></p><p data-t="help2"></p><p><a href="https://www.w3.org/TR/WebCryptoAPI/" target="_blank" rel="noreferrer">W3C Web Cryptography API</a> · <a href="https://www.rfc-editor.org/rfc/rfc4180" target="_blank" rel="noreferrer">RFC 4180 (CSV)</a></p></details><footer><span data-t="footer"></span><a href="https://nanalab.kr/apps/">More Apps ↗</a></footer></main><script type="module" src="app.js"></script></body></html>'''
for lang in langs:
    out=root/'dist'/('' if lang=='ko' else lang);out.mkdir(exist_ok=True)
    html=template.replace('{lang}',lang).replace('{base}','./' if lang=='ko' else '../').replace('{title}',catalog[lang]['title']).replace('{language}',catalog[lang]['language'])
    (out/'index.html').write_text(html,encoding='utf-8')
core=root/'dist/core.js';s=core.read_text(encoding='utf-8')
for original,key in [(catalog['ko'][k],k) for k in ['empty','countLimit','sizeLimit','secure','hashLimit']]:s=s.replace("Error('"+original+"')","Error('"+key+"')")
s=s.replace("export function csv(rows,safe=true){return [['경로','확장자','크기(bytes)','수정시각(UTC)','SHA-256']", "export function csv(rows,safe=true,headers=['경로','확장자','크기(bytes)','수정시각(UTC)','SHA-256']){return [headers")
start=s.index('export function markdown(');end=s.index('export function formatBytes',start)
s=s[:start]+'''export function markdown(rows,labels={title:'폴더 납품 목록',note:'크기 단위: bytes · 수정시각: UTC · SHA-256 빈칸: 미계산',headers:['경로','확장자','크기(bytes)','수정시각(UTC)','SHA-256']}){return '# '+labels.title+'\\n\\n'+labels.note+'\\n\\n| '+labels.headers.join(' | ')+' |\\n| --- | --- | ---: | --- | --- |\\n'+rows.map(r=>'| '+[r.path,r.ext,r.size,r.modified,r.hash].map(mdEscape).join(' | ')+' |').join('\\n')+'\\n';}
'''+s[end:]
core.write_text(s,encoding='utf-8')
