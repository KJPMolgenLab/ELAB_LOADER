# Populate resources in eLabFTW using the API

This manual will explain step by step how to use the API of eLabFTW to automatically upload entries to the resources in a specific team using the eLab\_loader: https://github.com/KJPMolgenLab/ELAB\_LOADER
You can use the script and execute it via the terminal of your device or with a source code editor. 
The first step explains how to install the source code editor Visual Studio Code (VS Code). If this is not relevant to you, you can continue directly with Step 3

## 1\. Installing the programming environment

Installing VS Code, Git and Python on your PC:<ol><li>Download VS Code: <a href="https://code.visualstudio.com/download">https://code.visualstudio.com/download</a></li></ol>

* <li>Start installation and select default settings</li>* <li>Install Git on the PC <a href="https://git-scm.com/downloads">https://git-scm.com/downloads</a></li>* <li>Install Python on the PC <a href="https://www.python.org/downloads/windows/">https://www.python.org/downloads/windows/</a><ol><li><strong>Important</strong> installation setting: Click on 'Add python to Path'</li></ol></li>* <li>Start VS Code</li>## 2\. Setting up VS Code<ol><li>First you have to chose a theme</li><li>Click "<- Welcome" at the top left to get to the main page</li><li>There you click on 'Open Folder'<ol><li>Now select a folder in which you want to save everything</li><li>Create a folder and name it as it makes sense to you</li></ol></li><li>The folder now appears on the left in VS Code</li></ol>

## 3\. Clone the elab\_loader and install packages

In VS Code the Terminal is accessible via the menu bar, click on "new terminal"<ol><li>Move to the folder you want to work with. Therefore you can use the command cd and the name of the folder to get there.</li><li>In the correct folder, type in the following command to clone the eLab\_Loader project<ol><li>git clone https://github.com/KJPMolgenLab/ELAB\_LOADER.git</li></ol></li><li>After a few seconds (depending on how fast your computer is) a new folder (in your folder) with the name "ELAB\_LOADER" will be created</li><li>Use the command cd to get into this new folder</li><li>In the next step, the required packages will be installed, therefore type in the following command<ol><li>pip install -r requirements.txt</li></ol></li></ol>

 Everything you need should be installed now. We will continue to run the script.

## 4\. Run the script and populate your eLabFTW resources with consumables

We are still in the terminal in the "ELAB\_LOADER" folder<ol><li>Type in the following command to run the script<ol><li>./elabloader.py</li></ol></li><li>If nothing happens and the next command line will appear, then the script is started. Otherwise, an error message will be displayed</li><li>Next we need to type in a long command to use the script, beforehand a few things need to be prepared<ol><li>Prepare the excel list with your chemicals (consumables)</li><li>Therefore open the "example" folder and the edit the "example\_cons" file</li><li>Take care that the red marked columns are mandatory, but you are allowed to have as many white columns you need next to the excisting ones</li><li>Then you need an API key in the team in eLabFTW where you work, so please generate it with read and write permissions</li><li>You also need the ID of the category in eLabFTW to which you want to upload this Excel list.</li></ol></li><li>The command to run the script for consumable might look like this:</li> ./elabloader.py --apikey "enter your key" --url "https://yourelab.yourelabsending.lab/api/v2/" --file ./Example/Example\_cons.xlsx --cat\_id "numberofyourcatid"</ol>

With this you will be able to populate the resources in eLabFTW. However it is recommended to first try this out with a few test entries.

## How to find out which ID my category has?

There a several ways to find out which ID you category in eLabFTW has.<ol><li>You have access to the admin panel in eLabFTW<ol><li>Call up the categories in the admin panel and click on "edit" of the category where you want to get the ID.</li><li>Now check out the URL, the last number is the ID of the category</li></ol></li><li>You don't have access to the admin panel<ol><li>Go to resources in eLabFTW and create a new empty entry in the category.</li><li>Back to the resources,the new entry is displayed and now you click on the category name above the title of the entry</li><li>In the URL (the first number) is your category ID, it is indicated by "cat=..."</li></ol></li><li>Use F12 in your Browser and open the developer tools interface<ol><li>Go to resources in eLabFTW and create a new empty entry in the category.</li><li>Back to the resources,the new entry is displayed and now you click on the "F12" button of your keyboard</li><li>The developer tools of your browser appears, use the picker and click on the name of the category (above the title of the entry)</li><li>A line of code will be highlighted and there it's written "data-value=..."</li></ol></li></ol>

#### Tested for eLabFTW v5.0.4 and API v2