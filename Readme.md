![LOGO](GitResources/loaderlogo.png)
# ELAB LOADER Beta V 1.6.0

<!-- TOC -->
* [ELAB LOADER Alpha V0.5.8](#elab-loader-alpha-v058)
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Getting started](#getting-started)
  * [Data preparation](#data-preparation)
  * [Modes](#modes)
    * [Mode seqp](#mode-seqp)
    * [Mode qpcr](#mode-qpcr)
    * [Mode rest](#mode-rest)
    * [Mode plas](#mode-plas)
    * [Mode cons](#mode-cons)
  * [Running](#running)
  * [Arguments and Flags](#arguments-and-flags)
    * [Command examples](#command-examples)
  * [Legal and Credits](#legal-and-credits)
<!-- TOC -->

<!--- ADD EULA AND LEGAL AT END  --->
<!--- Check numbering and structure of titles  --->
<!--- Fill mode dummies  --->

## Introduction

This is ELABLOADER, a simple-to-use, no-bullshit, non bloating, console based solution to transfer data between the API provided by [elabFTW](https://www.elabftw.net/) and tables provided by the physical lab. 
It is utilized mainly by reading in prepared XLSX, CSV, or TXT files. 
Current version is under development. 
Please do report any bugs! Thanks!

Only works with [elabFTW](https://www.elabftw.net/) installed 
A demo version of [elabFTW](https://www.elabftw.net/) is available at https://demo.elabftw.net/

## Installation

You must have Python 3.9 with the following libraries installed

* elabapi_python
* pandas 
* numpy 

Github is the official download source, the place to praise and the place to complain:
Simply clone the project and you shouldbe good to go. 

```
git clone https://github.com/KJPMolgenLab/ELAB_LOADER.git 
```

## Getting started

What do I need? 
- The elabFTW URL to the API 
  - e.g. ```https://demo.elabftw.net/api/v2```
  - Also, kindly ask your Admin if unsure
    <br><br>
- an API Key 
  - can be generated in the user panel 
  - needs to have write permisseion
  - Online information see [Info](https://doc.elabftw.net/user-guide.html#api-keys-tab)
  - Kindly ask your Admin if unsure
  <br><br>

- The Category ID of the type of item you want to update in Elab: 
  - The type of item has to be predefined in the labbook 
  - If you select the type of item in your database view you can get the id from the url 
  - e.g. ```https://demo.elabftw.net/database.php?q=&cat=7&mode=show&limit=15``` gives category 7 
  - And you guessed it ask your Admin if unsure
 
## Data preparation

First, carefully prepare a list of the items to be added in XLSX format (Excel sheet). 
We strongly suggest using XLSX for comforts sake.
Make sure the mandatory columns and header names are present in the file. 
These vary between the different types of data you can upload. 
For the different modes we provided templates in the Example folders

**Everything marked red in the ./Examples Excel files is a mandatory entry and is case SENSITIVE!**

You can add as many columns as you wish, they will be added to the items in tabular format

Fill out the mandatory columns. It is recommended to also fill out the existing ones, or remove them if not needed.
Any additional columns will be added into the Elab table. 
Results can vary due to Elab's CSS.

## Modes

### Mode seqp
This mode will upload sequencing primers onto Elab.
The algorithm will check if the primer sequence already exists in the database, if yes the program does not upload or change the primer again 
and give you feedback about it 
If the Primer sequence cannot be identified a new entry is generated

### Mode qpcr
This mode will upload qpcr primers onto Elab.
The template here assumes a primer pair and a Probe
If you do not have a Probe in your qPCR designs just leave the column empty

Similarity check will be done on the sequences of the primers and the probe 
Identical items will be patched, i.e. replaced by the information in the table 
If no item can be identified to be similar a new entry is generated

### Mode rest
This mode will upload restriction enzymes onto Elab.
Similarity check will be done based on the Supplier and the Ordernumber
If the Restriction enzyme cannot be identified a new entry is generated, otherwise the item is skipped with a feedback

### Mode plas

This mode will upload plasmids onto Elab.
Similarity check will be done based on the Name/title of the entry
If the Plasmid cannot be identified a new entry is generated, otherwise the item is skipped with a feedback

### Mode cons

This mode will upload consumables (e.g. Chemicals, Tools, etc.) onto Elab.
Similarity check will be done based on the Supplier and the Ordernumber.
If the Restriction enzyme cannot be identified a new entry is generated, otherwise the item is skipped with a feedback

## Running the algorithm

to test if your program runs go to a command line terminal move to the folder of the 
Elabloader and check is the elabloader.py file is executable

```commandline
cd <PathtoElabloader>
./elabloader.py
```
if all libraries are installed successfully the following message should appear

```commandline
            All libraries loaded and ready 

             ______ _               ____  _      ____          _____  ______ _____  
            |  ____| |        /\   |  _ \| |    / __ \   /\   |  __ \|  ____|  __ \ 
            | |__  | |       /  \  | |_) | |   | |  | | /  \  | |  | | |__  | |__) |
            |  __| | |      / /\ \ |  _ <| |   | |  | |/ /\ \ | |  | |  __| |  _  / 
            | |____| |____ / ____ \| |_) | |___| |__| / ____ \| |__| | |____| | \ \ 
            |______|______/_/    \_\____/|______\____/_/    \_\_____/|______|_|  \_\

            
no arguments provided
type --help for more information

```

## Arguments and Flags

The program needs arguments to work; so-called "Flags". These are instructions you give via a dash.
The following instructions are available and mandatory. 

Please make sure you do not miss any, or the program will report back an error:


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

Now that you have learned about the flags, it's time to finally send the command.
In the "Terminal", enter the following:

```shell
./elabloader.py [Flags]
```

**Before you ask, here is a pre-fabbed command:**

```shell
./elabloader.py --apikey <enteryourkey> \ 
                --url <https://yourelab.yourelabsending.lab/api/v2/> \
                --file <./Example/Example_cons.xlsx> \
                --cat_id <numberofyourcatid
```

For logging, you can dump the output to a file.
```shell
./elabloader.py --apikey <enteryourkey> \ 
                --url <https://yourelab.yourelabsending/api/v2/> \
                --file </files/ForEndusers/ElabLoader/Input/example.xlsx> \
                --cat_id numberofyourcatid > Debug/output.log
```

# Legal and Credits

**This Script is published under [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/)**

## ELABLOADER was created by:

* [achiocch](https://github.com/achiocch)
* [LF-KGU](https://github.com/LF-KGU)

