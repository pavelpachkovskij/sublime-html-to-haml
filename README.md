# HTML to Haml plugin for Sublime Text 2
====================

Converts files, selection and clipboard content from HTML or ERB to HAML using http://html2haml.heroku.com API

## Install
**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/pavelpachkovskij/sublime-html-to-haml.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

## Usage

* **Convert whole ERB or HTML file** `Shift+Alt+F` - creates new file in the same folder using the same name as the source ending with '.html.haml'.
* **Convert selection** `Shift+Alt+S` - replaces selection of HTML or ERB with HAML content.
* **Convert clipboard content** `Shift+Alt+V` - inserts HAML of converted clipboard HTML or ERB content.

### In Command Palette:

* **HTML2Haml: Convert file**
* **HTML2Haml: Convert selection**
* **HTML2Haml: Convert clipboard content**