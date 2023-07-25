     ______ _               ____  _      ____          _____  ______ _____  
    |  ____| |        /\   |  _ \| |    / __ \   /\   |  __ \|  ____|  __ \ 
    | |__  | |       /  \  | |_) | |   | |  | | /  \  | |  | | |__  | |__) |
    |  __| | |      / /\ \ |  _ <| |   | |  | |/ /\ \ | |  | |  __| |  _  / 
    | |____| |____ / ____ \| |_) | |___| |__| / ____ \| |__| | |____| | \ \ 
    |______|______/_/    \_\____/|______\____/_/    \_\_____/|______|_|  \_\
# ELAB LOADER Alpha V0.5.8

<!-- TOC -->
* [ELAB LOADER Alpha V0.5.8](#elab-loader-alpha-v058)
  * [Introduction](#introduction)
  * [Installation](#installation)
* [Getting started](#getting-started)
  * [Data preparation](#data-preparation)
    * [Mode Primer](#mode-primer)
    * [Mode Restriction Enzyme](#mode-restriction-enzyme)
    * [Mode Antibodies](#mode-antibodies)
    * [Mode Consumables](#mode-consumables)
  * [Running](#running)
    * [Arguments (Flags)](#arguments--flags-)
    * [Command examples](#command-examples)
* [Legal and Credits](#legal-and-credits)
<!-- TOC -->

<!--- ADD EULA AND LEGAL AT END  --->
<!--- Check numbering and structure of titles  --->
<!--- Fill mode dummies  --->

## Introduction



## Installation

None. Please use this program only on the Nuvolos cloud instance.

```
pererequisites 
und path to git dann 
```

# Getting started

So you want to upload a database item? Cool, lets get started.

What do I need<br>
API Key <br>
URL <br>
Category ID in elab 
 

<br>
<br>
## 1 Data preparation

First, carefully prepare a list of the items to be added in XLSX format (Excel sheet).
Make sure the mandatory columns and header names are present in the file. These vary between the different types of data you can upload. 
If you wish for visual examples, head over to the ./Examples folder.
```plain
## Ausfüllen  
```

## Data preparation 

### Mode Primer

Mandatory columns:
\# auflisten der Spaltennamen \+ was da rein muss 

Any other column 
was passiert mit den andren Saplten 

Example bild 

### Mode Restriction Enzyme

Mandatory columns:

Any other column 
 

### Mode Antibodies 

Mandatory columns:

Any other column 

### Mode Consumables

Mandatory columns:

Any other column 

<br>

## Running 

```
## anpassen so als wie wenn man das direct in ther console laufen lässt (nicht pycharm)
```

To run the program, launch my instance on Nuvolos. Its name is "Luca Testproj".
Simply click on the little monitor on the left sidebar and select the PyCharm application.
Once it is run and you have the pycharm interface, navigate via the project explorer
(the box with the folders on the left) to the folder called "ForEndusers".
Do not touch anything else or I will have to launch you into the sun ;)
Double click the "elabloader.py" file
Now at the bottom, head to "Terminal".

Now for the arguments.

### Arguments (Flags)

The program needs arguments to work; so called "Flags". These are instructions you give via a dash.

The following instructions are available and mandatory. Use in this sequence:
``` 
-k, --apikey        API key as generated on the ElabFTW user panel
                    needs to have write and read access
           
-u, --url           to parse the url of the elab page.
            
-f, --file          <path to file>, File ending accepted is .XLSX

-c, --cat_id        to parse the numeric(int) category ID of the DB type you wish to upload.
                    This can be found out on ELAB. In case of questions ask your administrator.
                    
-m, --mode          to select between type of import.
            
                    Modes available:
                    olig    uploads Oligos for sgRNA generation
                    plas    uploads Plasmid information 
                    rest    uploads restriction enzyme information 
                    seqp    uploads Sequencing primer information
                    qpcr    uploads qpcr primer information
                    cons    uploads consumable information 
                                
                    Each mode needs to be provided with a table one at a time. 
                    The table needs to fulfill all the requirements found
                    in the readme.md and the ./Example folder to work properly.

```

### Command examples

Now that you have learned about the flags, its time to finally send the command.

In the "Terminal", enter the following:
(if not in the "ElabLoader" Folder, navigate to it. (cd ForEndusers / cd ElabLoader)

```shell
./elabloader.py [Flags]
```

**Before you ask, heres a prefabbed command:**

```shell
./elabloader.py --apikey <enteryourkey> \ 
                --url <https://yourelab.yourelabsending/api/v2/> \
                --file </files/ForEndusers/ElabLoader/Input/example.xlsx> \
                --cat_id numberofyourcatid > Debug/output.log
```


For logging, you can dump the output to a file. 

```shell
./elabloader.py --apikey <enteryourkey> \ 
                --url <https://yourelab.yourelabsending/api/v2/> \
                --file </files/ForEndusers/ElabLoader/Input/example.xlsx> \
                --cat_id numberofyourcatid > Debug/output.log
```

# Legal and Credits

ELAB LOADER was created by Luca Fries and Andreas Chiocchetti 
as a custom solution for our lab to fulfill the requirement of uploading specific dataset items to our  ELAB database(s)


