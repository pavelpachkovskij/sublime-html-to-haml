# HTML to Haml plugin for Sublime Text 2
====================

Converts files, selection and clipboard content from HTML or ERB to HAML using http://html2haml.heroku.com API

## Install
The easiest wat to get HTML2Haml is to install it from **Sublime Package Control** though you still can install it from **Git repository**

Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/pavelpachkovskij/sublime-html-to-haml.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

## Usage

* **Convert hole ERB or HTML file** `Shift+Alt+F` - creates new file in the same folder using the same name as the source ending with '.html.haml'.
* **Convert selection** `Shift+Alt+S` - replaces selection of HTML or ERB with HAML content.
* **Convert clipboard content** `Shift+Alt+V` - inserts HAML of converted clipboard HTML or ERB content.

### In Command Palette:

* **HTML2Haml: Convert file**
* **HTML2Haml: Convert selection**
* **HTML2Haml: Convert clipboard content**

## Sublime Text 3

### Git installation

Follow the instruction from [Sublime Text 3 branch](https://github.com/pavelpachkovskij/sublime-html-to-haml/tree/SublimeText3)

### Sublime Package Control

In your command Pallette choose **Package Control: Add Repository** and add Sublime Text 3 branch

    https://github.com/pavelpachkovskij/sublime-html-to-haml/tree/SublimeText3

Then simply (re)install HTML2Haml plugin.