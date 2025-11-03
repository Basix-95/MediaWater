from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for, send_file
import shutil
import os
import zipfile
import io
app = Flask(__name__)
app.secret_key = 'supersecret'  # Needed for flash messages

upload_folder = 'uploads'
os.makedirs(upload_folder, exist_ok=True)


@app.route('/')
def home():
    return render_template("main.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        if 'files' in request.files:
            uploaded_files = request.files.getlist('files')
            for f in uploaded_files:
                if f.filename:
                    filepath = os.path.join(upload_folder, os.path.normpath(f.filename))
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    f.save(filepath)

        if 'file' in request.files:
            single_file = request.files['file']
            if single_file.filename:
                filepath = os.path.join(upload_folder, single_file.filename)
                single_file.save(filepath)

        flash('Upload completed successfully!')
        return redirect(url_for('upload'))

    return render_template('upload.html')

@app.route('/files')
def list_files():
    """Lists all files in the upload folder."""
    items = os.listdir(upload_folder)
    files = []
    folders = []

    for item in items:
        path = os.path.join(upload_folder, item)
        if os.path.isdir(path):
            folders.append(item)
        else:
            files.append(item)

    return render_template('download.html', files=files, folders=folders)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(upload_folder, filename, as_attachment=True)


@app.route('/download_folder/<path:foldername>')
def download_folder(foldername):
    folder_path = os.path.join(upload_folder, foldername)

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        flash("Folder not found!")
        return redirect(url_for('list_files'))

    EXCLUDE_DIRS = {'venv', '__pycache__', '.git', '.idea', '.vscode'}

    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(folder_path):
            # remove excluded directories from traversal
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                file_path = os.path.join(root, file)
                # use a relative path inside the ZIP (relative to the folder being downloaded)
                arcname = os.path.relpath(file_path, folder_path)

                # only include real files (skip broken symlinks / missing files)
                if os.path.isfile(file_path):
                    try:
                        z.write(file_path, arcname)
                    except FileNotFoundError:
                        app.logger.warning(f"Skipping missing file: {file_path}")
                        continue

    memory_file.seek(0)
    return send_file(
        memory_file,
        download_name=f"{foldername}.zip",
        as_attachment=True
    )


@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    path = os.path.join(upload_folder, filename)
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        flash(f"{filename} deleted successfully!")
    else:
        flash("File not found!")
    return redirect(url_for('list_files'))


@app.route('/delete_folder/<path:foldername>', methods=['POST'])
def delete_folder(foldername):
    folder_path = os.path.join(upload_folder, foldername)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        flash(f"Folder '{foldername}' deleted successfully!")
    else:
        flash("Folder not found!")
    return redirect(url_for('list_files'))


if __name__ == '__main__':
    app.run(debug=True)

