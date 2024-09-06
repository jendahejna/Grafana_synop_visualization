from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)


ALLOWED_EXTENSIONS = {'png'}
ALLOWED_FILES = {
    '0.png', '4.png', '5.png', '10.png', '20.png', '21.png', '22.png', '23.png', '24.png',
    '25.png', '30.png', '31.png', '32.png', '33.png', '34.png', '40.png', '41.png', '42.png',
    '50.png', '51.png', '52.png', '53.png', '54.png', '55.png', '56.png', '60.png', '61.png',
    '62.png', '63.png', '64.png', '65.png', '66.png', '67.png', '68.png', '70.png', '71.png',
    '72.png', '73.png', '74.png', '75.png', '76.png', '80.png', '81.png', '82.png', '83.png',
    '84.png', '85.png', '86.png', '87.png'
}


def is_safe_path(base_path, target):
    base_path = os.path.abspath(base_path)
    target = os.path.abspath(os.path.join(base_path, target))
    return os.path.commonpath([base_path]) == os.path.commonpath([base_path, target])


@app.route('/Icons/<filename>')
def get_image(filename):

    if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        filename_with_extension = f"{filename}.png"

        icons_directory = os.path.join(app.root_path, 'Icons')
        if is_safe_path(icons_directory, filename_with_extension):
            if filename_with_extension in ALLOWED_FILES:
                return send_from_directory(icons_directory, filename_with_extension)
            else:
                return abort(403)
        else:
            return abort(403)
    else:
        return abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
