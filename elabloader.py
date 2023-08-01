#!/usr/bin/env python

import elabapi_python
import pandas as pd
from elabapi_python.rest import ApiException
import numpy as np
from typing import Union
import urllib3
import sys
import os
import getopt
from progress.bar import Bar


class BatchImporter(object):
    def __init__(self, verify_ssl=True, debug=False, api_key_elab="", api_url="") -> None:
        self.body = None
        self.API_KEY = api_key_elab
        self.API_HOST_URL = api_url

        configuration = elabapi_python.Configuration()
        configuration.api_key["api_key"] = self.API_KEY
        configuration.api_key_prefix["api_key"] = "Authorization"
        configuration.host = self.API_HOST_URL
        configuration.debug = debug
        configuration.verify_ssl = verify_ssl

        self.api_client = elabapi_python.ApiClient(configuration)

        self.api_client.set_default_header(
            header_name="Authorization", header_value=self.API_KEY
        )

        if not verify_ssl:
            urllib3.disable_warnings()

    def post_item_with_body(self, categoryid: int, title: str = "new created item",
                            content: str = "new entry", ) -> str:
        """
           Posts items via API

        """
        self.body = {
            "category_id": categoryid}

        try:

            response = elabapi_python.ItemsApi(self.api_client).post_item_with_http_info(
                body={'category_id': categoryid})

            location_header_in_response = response[2].get('Location')
            item_id = int(location_header_in_response.split('/').pop())

            response = elabapi_python.ItemsApi(self.api_client).patch_item(item_id,
                                                                           body={'title': title, 'body': content})
            location_header_in_response = response.sharelink
            return location_header_in_response

        except ApiException as error:
            print(error)

    def patch_item(self, item_id: int, body: str, title: str) -> str:
        try:
            response = elabapi_python.ItemsApi(self.api_client).patch_item(item_id, body={'title': title, 'body': body})
            location_header_in_response = response.sharelink
            return location_header_in_response
        except ApiException as error:
            print(error)

    def get_id(self, key: str) -> Union:
        try:
            items_dataentry = elabapi_python.ItemsApi(self.api_client).read_items(q=key)
            if len(items_dataentry) == 0:
                itemid = None
            else:
                li = [item.id for item in items_dataentry]
                itemid = li
            return itemid

        except ApiException as error:
            print(error)
            print('\033[31m' + "Error: Key not found. Check if the key exists! " + '\x1b[0m')
            return None


def create_body_oligos(entry):
    primer = "<table>" \
             "<tr><th> </th><th><b>forward</b></th><th><b>reverse</b></th>" \
             "</tr><tr><td><b>Name</b></td><td>" + str(entry["Primer_fwd"]) + "</td><td>" + \
             str(entry["Primer_rev"]) + "</td>" \
                                        "</tr><tr><td><b>Sequence</b></td><td>" + \
             str(entry["Seq_fwd"]) + "</td><td>" + str(entry["Seq_rev"]) + "</td></tr>" \
                                                                           "</table>"

    rows = "<tr><th><b>Details</b></th><th></th></tr>"
    for k in entry.drop(["title", "Primer_fwd", "Seq_fwd", "Primer_rev", "Seq_rev"]).keys():
        rows = rows + "<tr><td><b>" + str(k) + "</b></td><td>" + str(entry[k]) + "</td></tr>"
    tableentry = "<table>" + rows + "</table>"

    html_body = tableentry + "<p><br></p>" + primer
    return html_body


def create_body_consumables(entry):
    rows = "<tr><th><b>Details</b></th><th></th></tr>"
    for h in entry.drop(["title"]).index:
        rows = rows + "<tr><td><b>" + str(h) + "</b></td><td>" + str(entry[h]) + "</td></tr>"
    tableentry = "<table>" + rows + "</table>"
    return tableentry


def create_body_plasmids(entry):
    rows = "<tr><th><b>Details</b></th><th></th></tr>"
    for h in entry.drop(["title"]).index:
        rows = rows + "<tr><td><b>" + str(h) + "</b></td><td>" + str(entry[h]) + "</td></tr>"
    tableentry = "<table>" + rows + "</table>"
    return tableentry


def create_body_qpcr_primers(entry):
    primer = "<table>" \
             "<tr><th> </th><th>" \
             "<b>forward</b></th><th><b>reverse</b></th><th><b>UPL Probe</b>" \
             "</th></tr>" \
             "<tr><td>" \
             "<b>Name</b>" \
             "</td><td>" + str(entry["Primer_fwd"]) + "</td>" \
                                                      "<td>" + str(entry["Primer_rev"]) + "</td>" \
                                                                                          "<td>" + \
             str(entry["UPL_Probe"]) + " </td></tr>" \
                                       "<tr><td>" \
                                       "<b>Sequence&nbsp;</b>" \
                                       "</td><td>" + str(entry["Seq_fwd"]) + "&nbsp;</td>" \
                                                                             "<td>" + \
             str(entry["Seq_rev"]) + "&nbsp;</td>" \
                            "<td>" + \
             str(entry["SeqUPL"]) + "</td></tr>" \
                                    "</table>"

    rows = "<tr><th><b>Details</b></th><th></th></tr>"
    for u in entry.drop(
            ["title", "Primer_fwd", "Seq_fwd", "Primer_rev", "Seq_rev", "Details", "UPL_Probe", "SeqUPL"], ).keys():
        rows = rows + "<tr><td><b>" + str(u) + "</b></td><td>" + str(entry[u]) + "</td></tr>"
    tableentry = "<table style='width: 25%'>" + rows + "</table>"

    description = ""
    for u in ["Details"]:
        description = description + "<h3>" + str(u) + "</h3><p>" + str(entry[u]) + "</p><p><br></p>"

    html_body = tableentry + "<p><br></p>" + primer + "<p><br></p>" + description
    return html_body


def create_body_seqprimer(entry):
    rows = "<tr><th><b>Details</b></th><th></th></tr>"
    for h in entry.drop(["title"]).index:
        rows = rows + "<tr><td><b>" + str(h) + "&nbsp;</b></td><td>" + str(entry[h]) + "&nbsp;</td></tr>"
    tableentry = "<table>" + rows + "</table>"
    return tableentry


def create_body_restriction_enzymes(entry):
    description = ""
    for z in ["RestrictionSite", "RecognitionSeq"]:
        description = description + "<h3>" + str(z) + "</h3><p>" + str(entry[z]) + "</p><p><br></p>"

    rows = "<tr><th><b>Details</b></th><th></th></tr>"
    for z in entry.drop(["title", "RestrictionSite", "RecognitionSeq"]).keys():
        rows = rows + "<tr><td><b>" + str(z) + "</b></td><td>" + str(entry[z]) + "</td></tr>"
    tableentry = "<table>" + rows + "</table>"

    html_body = tableentry + "<p><br></p>" + description
    return html_body


if __name__ == "__main__":

    argv = sys.argv[1:]

    if len(argv) == 0:
        titleasci = "\033[92m" + r"""
            All libraries loaded and ready 

             ______ _               ____  _      ____          _____  ______ _____  
            |  ____| |        /\   |  _ \| |    / __ \   /\   |  __ \|  ____|  __ \ 
            | |__  | |       /  \  | |_) | |   | |  | | /  \  | |  | | |__  | |__) |
            |  __| | |      / /\ \ |  _ <| |   | |  | |/ /\ \ | |  | |  __| |  _  / 
            | |____| |____ / ____ \| |_) | |___| |__| / ____ \| |__| | |____| | \ \ 
            |______|______/_/    \_\____/|______\____/_/    \_\_____/|______|_|  \_\

            """ + "\x1b[0m"
        print(titleasci)
        print("no arguments provided")
        print("type --help for more information")
        exit(0)

    short_opts = "kufcmh:"
    long_opts = ["apikey=", "url=", "file=", "cat_id=", "mode=", "help"]
    args = []

    try:
        args, opts = getopt.getopt(argv, short_opts, long_opts)
    except getopt.error as err:
        print(str(err))
        exit(0)

    for current_argument, current_value in args:
        if current_argument in ("-h", "--help"):
            helpmsg = r"""
            ------------------------------

            Usage: ./elabloader.py [OPTIONS]
            
            This program uploads information from an excel sheet to an elabFTW database.
            
            OPTIONS MANDATORY
            
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
                            
            The program will now exit. Have a productive day.
            
            Program written by L. Fries and A.G. Chiocchetti under CC BY4.0  
            ___________________________________________________
            """
            print(helpmsg)
            exit(0)
        # retreives arguemnts
        elif current_argument in ("-k", "--apikey"):
            API_KEY_ELAB = current_value
        elif current_argument in ("-u", "--url"):
            API_HOST_URL_ELAB = current_value
        elif current_argument in ("-f", "--file"):
            FILE_TO_READ = current_value
        elif current_argument in ("-c", "--cat_id"):
            CAT_ID = int(current_value)
        elif current_argument in ("-m", "--mode"):
            MODE = current_value

    # start importer Class
    importer = BatchImporter(verify_ssl=False, api_key_elab=API_KEY_ELAB, api_url=API_HOST_URL_ELAB)

    # read file
    root_ext_pair = os.path.splitext(FILE_TO_READ)

    # check file type and read respective file
    if (str(root_ext_pair[1]) == ".xlsx") | (str(root_ext_pair[1]) == ".xls"):
        try:
            file = pd.read_excel(FILE_TO_READ)
        except Exception as e:
            print(e)

    elif root_ext_pair[1] == ".csv":
        try:
            file = pd.read_csv(FILE_TO_READ)
        except Exception as e:
            print(e)

    elif root_ext_pair[1] == ".txt":
        try:
            file = pd.read_table(FILE_TO_READ)
        except Exception as e:
            print(e)
    else:
        print("invalid type of table format, csv, xlsx, xls or txt accepted")

    # start import
    titleasci = "\033[92m" + r"""
    File and Modes accepted welcome to 
    
     ______ _               ____  _      ____          _____  ______ _____  
    |  ____| |        /\   |  _ \| |    / __ \   /\   |  __ \|  ____|  __ \ 
    | |__  | |       /  \  | |_) | |   | |  | | /  \  | |  | | |__  | |__) |
    |  __| | |      / /\ \ |  _ <| |   | |  | |/ /\ \ | |  | |  __| |  _  / 
    | |____| |____ / ____ \| |_) | |___| |__| / ____ \| |__| | |____| | \ \ 
    |______|______/_/    \_\____/|______\____/_/    \_\_____/|______|_|  \_\
    
    """ + "\x1b[0m"
    print(titleasci)

    # initialize loading bar
    bar = Bar('Completed entries: ', max=len(file.index))

    # select mode

    if "olig" == str(MODE):  # updates new oligos (sgRNA oligos)
        for i in file.index:
            body_new = create_body_oligos(file.iloc[i, :])
            try:
                seqfwd = file.iloc[i, ]["Seq_fwd"]
                seqrev = file.iloc[i, ]["Seq_rev"]
            except KeyError:
                print('\033[31m' + "ERROR: Could not find Seq_fwd or Seq_rev in submitted table, "
                                   "\nplease check Readme.md for further details" + '\x1b[0m')
                exit(1)

            a = np.array(importer.get_id(seqfwd))
            b = np.array(importer.get_id(seqrev))

            try:
                existingids = np.intersect1d(a, b)
            except TypeError as e:
                existingids = []

            if len(existingids) == 1:
                message = file.title[i] + " has been found, nothing done"
                url = "item number " + str(existingids)
                bar.next()
                print(" ")

            elif not existingids:
                url = importer.post_item_with_body(categoryid=CAT_ID, title=file.title[i], content=body_new)
                message = file.title[i] + " has been created"
                bar.next()
            else:
                message = file.title[i] + " has multiple entries"
                url = "check items " + str(existingids)
                bar.next()

            print(message)
            print(url)

    elif "plas" == str(MODE):
        for i in file.index:
            # create html entry for the plasmid
            plasmid_body_new = create_body_plasmids(file.iloc[i, :])

            # check if the plasmid already exists
            try:
                seq1 = file.iloc[i, ]["title"]
            except KeyError:
                print('\033[31m' + "ERROR: Could not find title in submitted table, "
                                   "\nplease check Readme.md for further details" + '\x1b[0m')
                exit(1)

            exist = importer.get_id(seq1)

            if not exist:
                url = importer.post_item_with_body(categoryid=CAT_ID, title=file.title[i], content=plasmid_body_new)
                bar.next()
                message = file.title[i] + " item created"
            elif len(exist) == 1:
                message = file.title[i] + " item exists nothing done"
                url = "item item_id is " + str(exist)
                bar.next()
            else:
                message = file.title[i] + " matches multiple items"
                url = "item numbers " + str(exist)
                bar.next()
            print(message)
            print(url)

    elif "rest" == str(MODE):
        for i in file.index:
            restrict_body_new = create_body_restriction_enzymes(file.iloc[i, :])
            try:
                supp = file.iloc[i, ]["Supplier"]
                nume = file.iloc[i, ]["No"]
            except KeyError:
                print('\033[31m' + "ERROR: Could not find Supplier or No in submitted table, "
                                   "\nplease check Readme.md for further details" + '\x1b[0m')
                exit(1)

            a = np.array(importer.get_id(supp))
            b = np.array(importer.get_id(nume))
            try:
                existingids = np.intersect1d(a, b)
            except TypeError as e:
                existingids = []
            if len(existingids) == 1:
                message = file.title[i] + " item exists nothing done"
                url = "item number " + str(existingids)
                bar.next()
            elif not existingids:
                url = importer.post_item_with_body(categoryid=CAT_ID, title=file.title[i], content=restrict_body_new)
                message = file.title[i] + " item created"
                bar.next()
            else:
                message = file.title[i] + " matches multiple items"
                url = "item numbers " + str(existingids)
                bar.next()

            print(message)
            print(url)

    elif "seqp" == str(MODE):
        for i in file.index:
            # create html entry for the sequencing primer
            seqprimer_body_new = create_body_seqprimer(file.iloc[i])
            # check if the primer already exists based on sequence
            try:
                seq1 = file.iloc[i, ]["Primer_sequence"]
            except KeyError:
                print('\033[31m' + "ERROR: Could not find Primer_sequence in submitted table, "
                                   "\nplease check Readme.md for further details" + '\x1b[0m')
                exit(1)

            exist = importer.get_id(seq1)
            if not exist:
                url = importer.post_item_with_body(categoryid=CAT_ID, title=file.title[i], content=seqprimer_body_new)
                bar.next()
                message = file.title[i] + " item created"
            elif len(exist) == 1:
                message = file.title[i] + " item exists nothing done"
                url = "item number " + str(exist)
                bar.next()
            else:
                message = file.title[i] + " primer matches multiple items"
                url = "item numbers " + str(exist)
                bar.next()
            print(message)
            print(url)

    elif "qpcr" == str(MODE):
        for i in file.index:
            primer_body_new = create_body_qpcr_primers(file.iloc[i])

            try:
                seqfwd = file.iloc[i, ]["Seq_fwd"]
                seqrev = file.iloc[i, ]["Seq_rev"]
            except KeyError:
                print('\033[31m' + "ERROR: Could not find Seq_fw or Seq_rw in submitted table, "
                                   "\nplease check Readme.md for further details" + '\x1b[0m')
                exit(1)

            a = np.array(importer.get_id(seqfwd))
            b = np.array(importer.get_id(seqrev))

            try:
                existingids = np.intersect1d(a, b)
            except TypeError as e:
                existingids = []

            if not existingids:
                url = importer.post_item_with_body(categoryid=CAT_ID, title=file.title[i], content=primer_body_new)
                message = file.title[i] + " has been created"
                bar.next()
            elif len(existingids) == 1:
                url = importer.patch_item(item_id=int(existingids), body=primer_body_new, title=file.title[i])
                message = file.title[i] + " has been found in database; patch applied"
                bar.next()
            else:
                message = file.title[i] + " more than one primer pair match"
                url = "item numbers" + str(existingids)

            print(message)
            print(url)

    elif "cons" == str(MODE):
        for i in file.index:

            cons_body_new = create_body_consumables(file.iloc[i, :])

            try:
                supp = file.iloc[i, ]["Supplier"]
                nume = file.iloc[i, ]["No"]
            except KeyError:
                print('\033[31m' + "ERROR: Could not find Supplier or No in submitted table, "
                                   "\nplease check Readme.md for further details" + '\x1b[0m')
                exit(1)

            a = np.array(importer.get_id(supp))
            b = np.array(importer.get_id(nume))
            try:
                existingids = np.intersect1d(a, b)
            except TypeError as e:
                existingids = []

            if len(existingids) == 1:
                message = file.title[i] + " has been found in database; nothing done"
                url = "item number " + str(existingids)
                bar.next()
            elif not existingids:
                url = importer.post_item_with_body(categoryid=int(CAT_ID), title=file.title[i], content=cons_body_new)
                message = file.title[i] + " has been created"
                bar.next()
            else:
                message = file.title[i] + " more than one item match Supplier and OrderNumber"
                url = "item numbers " + str(existingids)
            print(message)
            print(url)

    bar.finish()

    print('\033[92m' + "----------------------------" + '\x1b[0m')
    print('\033[92m' + "          Success!          " + '\x1b[0m')
    print('\033[92m' + "----------------------------" + '\x1b[0m')

    exit(0)
