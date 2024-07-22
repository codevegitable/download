import requests
import re
from pyquery import PyQuery as pq

url = 'http://121.41.73.5:5000'
html = requests.get(url=url).text
doc = pq(html)
items = doc('.download-section').items()
file = open('README.md', 'w', encoding='utf-8')

for item in items:
    item.find('i').remove()

    plugings = item.find('#补丁').find('a').items()
    plugings_text = item.find('#补丁').find('a').items()

    galgame = item.find('#galgame').find('a').items()
    galgame_text = item.find('#galgame').find('a').items()

    benzi = item.find('#本子').find('a').items()
    benzi_text = item.find('#本子').find('a').items()

    with file:
        file.write('''# 补丁

''')
        for files, file_text in zip(plugings, plugings_text):
            file.write(f'''> <a href="{url}{files.attr["href"]}">{file_text.text()}</a>

''')
        file.write(f'''{"=" * 50}

''')
        file.write('''# galgame

''')
        for files, file_text in zip(galgame, galgame_text):
            file.write(f'''> <a href="{url}{files.attr["href"]}">{file_text.text()}</a>

''')
        file.write(f'''{"=" * 50}

''')
        file.write('''# 本子

''')
        for files, file_text in zip(benzi, benzi_text):
            file.write(f'''> <a href="{url}{files.attr["href"]}">{file_text.text()}</a>

''')
        file.write(f'''{"=" * 50}

''')