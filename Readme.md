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

This is ELABLOADER, a simple-to-use, no-bullshit, non bloating, console based software solution for the modern, digitalized lab. It was created to meet the developers requirements of transfering data between the API provided by Elab and the tables provided by the physical lab. It is utilized mainly by reading in prepared XLSX files. Also, its now in Beta and that's pretty sick. Please do report any bugs! Thanks!

## Installation

A simple download of a folder is all it takes. And the usual Python stuff.
We tested on Python 3.9 .
<br>
<br>
This is the official download source, the place to praise and the place to complain:
```
path to git, add on publihing
```

## Getting started

So you want to upload stuff onto the database? Cool, lets get started.

What do I need? <br>
-The Elab API Key (Kindly ask your Admin if unsure)<br>
-The Elab URL (Also, kindly ask your Admin if unsure)<br>
-Category ID in Elab (As you guessed, ask your Admin if you need this ID.)<br>
 
## Data preparation

First, carefully prepare a list of the items to be added in XLSX format (Excel sheet). I strongly suggest using XLSX for comforts sake.
Make sure the mandatory columns and header names are present in the file. These vary between the different types of data you can upload. 
If you are lost, head over to the ./Examples folder.

## Modes

### Everything marked red in the ./Examples Excel files is a mandatory entry and is case SENSITIVE!

### Mode seqp

This mode will upload sequencing primers onto Elab.
Fill out the mandatory columns. It is recommended to also fill out the existing ones, or remove them if not needed.
Any additional columns will be added into the Elab table. Results can vary due to Elab's CSS.

### Mode qpcr

This mode will upload qpcr primers onto Elab.
Fill out the mandatory columns. It is recommended to also fill out the existing ones, or remove them if not needed.
Any additional columns will be added into the Elab table. Results can vary due to Elab's CSS.

### Mode rest

This mode will upload restriction enzymes onto Elab.
Fill out the mandatory columns. It is recommended to also fill out the existing ones, or remove them if not needed.
Any additional columns will be added into the Elab table. Results can vary due to Elab's CSS.

### Mode plas

This mode will upload plasmids onto Elab.
Fill out the mandatory columns. It is recommended to also fill out the existing ones, or remove them if not needed.
Any additional columns will be added into the Elab table. Results can vary due to Elab's CSS.

### Mode cons

This mode will upload consumables (e.g. Chemicals, Tools, etc.) onto Elab.
Fill out the mandatory columns. It is recommended to also fill out the existing ones, or remove them if not needed.
Any additional columns will be added into the Elab table. Results can vary due to Elab's CSS.

## Running 

Download the ELABLOADER folder from GitHub. 
Double-click the "elabloader.py" file (after consulting the /Examples folder if lost).
When the console window pops up and is ready to receive user input, simply enter the command.

## Arguments and Flags

The program needs arguments to work; so-called "Flags". These are instructions you give via a dash.

The following instructions are available and mandatory. Please make sure you do not miss any, or the program will report back an error:
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
(if not in the "ElabLoader" Folder, navigate to it. (cd ForEndusers / cd ElabLoader)

```shell
./elabloader.py [Flags]
```

**Before you ask, here is a pre-fabbed command:**

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

### This Script is published under [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/)

## ELAB LOADER was created by:
### -Luca Fries-
### -Andreas Chiocchetti-
 

