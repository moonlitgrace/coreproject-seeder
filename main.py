import webview

if __name__ == '__main__':
	webview.create_window('Seeder', 'build/index.html', min_size=(600, 450), text_select=True)
	webview.start(debug=True)
