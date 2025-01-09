<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <h1>Music-album-folder-manager</h1>
  <p>
    The script will automatically create album folders and put music files inside it, so you won't have to.
  </p>

  <h2>How does it work?</h2>
  <p>
    It takes all the <code>.flac</code>, <code>.mp3</code>, <code>.ogg</code> or <code>.wav</code> files inside the folder specified in the last line of the code, and creates a folder representing the album of the music.
    <br>
    I chose this format for the album folder: <code>ALBUMARTIST - ALBUM</code> but you can change it, adding more information such as the year.
    <br>
    Here is the <a href="https://mutagen.readthedocs.io/en/latest/">documentation</a> of Mutagen, the library used in the script if you want to know more.
    <br><br>
    The script will extract from each file in the given path its <code>ALBUM</code> and <code>ALBUMARTIST</code> tags. It will then proceed to create a folder with the given format.
    <br>
    If the folder name contains invalid characters, such as <code>(r'<>:"/\|?*')</code> it will ignore the characters during the creation of the folder.
  </p>

  <h2>Usage</h2>
  <p>Just change the last line of code with your path.</p>
  Be sure to have metadata in your files, otherwise the script won't work.

  <h2>Examples</h2>
  <!--><h4>Example 1</h4><-->
  <p>These files don't have their album folder yet:</p>
  <img src="https://github.com/user-attachments/assets/d07bc6c2-aaf7-4d4f-92b0-0c4c6bca3297" alt="Unable to load image">
  <p>After running the script, they will be inside a single folder, since their <code>ALBUM</code> tag is the same:</p>
  <img src="https://github.com/user-attachments/assets/0fe39bd6-657a-4998-b526-fcc502e69729" alt="Unable to load image">
  <p>This is how my music folder looks like after running the script in a folder with more or less 200 music files</p>
  <img src="https://github.com/user-attachments/assets/0ca6f8e0-5067-46f5-8a6c-beed323ebbde" alt="Unable to load image">
</body>
</html>
