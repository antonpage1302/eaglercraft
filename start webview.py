import webview

window = webview.create_window(
    'Local Dev App', 
    'http://localhost:1302'
)

webview.start()
