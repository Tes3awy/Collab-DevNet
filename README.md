![Cisco DevNet](https://img.shields.io/badge/Cisco-DevNet-blue)
[![Tested on Python 3.6+](https://img.shields.io/badge/Python%203.6+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads)
![Language](https://img.shields.io/github/languages/top/Tes3awy/Collab-DevNet)
![Repo Size](https://img.shields.io/github/repo-size/Tes3awy/Collab-DevNet)
[![Issues Open](https://img.shields.io/github/issues/Tes3awy/Collab-DevNet)](https://github.com/Tes3awy/Collab-DevNet/issues)
![Releases Download](https://img.shields.io/github/downloads/Tes3awy/Collab-DevNet/total)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/Tes3awy/Collab-DevNet)](https://github.com/Tes3awy/Collab-DevNet/commits/main)
![Last Commit](https://img.shields.io/github/last-commit/Tes3awy/Collab-DevNet)
[![Release Date](https://img.shields.io/github/release-date/Tes3awy/Collab-DevNet)](https://github.com/Tes3awy/Collab-DevNet/releases)
[![License](https://img.shields.io/github/license/Tes3awy/Collab-DevNet)](https://github.com/Tes3awy/Collab-DevNet/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# Cisco DevNet for Collaboration

## Netmiko, AXL, and Requests Exercises DevNet for Collaboration

- In `netmiko` folder, you will find ten Python exercises, `config-ex7.txt` file, a `requirements.txt` file, and an explanation of each exercise.

- In `axl` folder, you will find nine Python exercises, a `requirements.txt` file, and an explanation of each exercise.

- In `requests` folder, you will find four Python exercises, a `requirements.txt` file, and an explanation of each exercise.

## How to use?

1. `Clone` this repo or `Download ZIP` by clicking on <img src="assets/code-button.png" alt="Code Button" title="Button" width="100"/> up above.
   _(Alternativley, you can click on Releases on the right hand side and download the latest release)_

2. Once downloaded, extract the ZIP file and `cd` into `axl`, `netmiko` or `requests` folder.

3. Open `axl`, `netmiko`, or `requests` folder in VSCode.

4. Open `requirements.txt` file and if any of the libraries is not installed on your PC, run the following command in the PowerShell terminal within VSCode:

```powershell
path_to\folder> pip install -r requirements.txt --user ↵
```

5. Explore each `exercise*.py` file. _**(where **\*** is the number of the exercise)**_

6. Run any Python exercise by typing the following command in PowerShell terminal in VSCode:

```powershell
path_to\folder> python exercise*.py ↵
```

## Libraries Documentation Links

Examples in `netmiko` and `requests` folder uses some Python libraries. These libraries are:

1. Netmiko **v3.4.0** (Multi-vendor library to simplify Paramiko SSH connections to network devices) [Documentation Link](https://github.com/ktbyers/netmiko/blob/develop/README.md).
2. NTC Templates **v2.1.0** (TextFSM templates for parsing show commands of network devices) [Documentation Link](https://github.com/networktocode/ntc-templates).
3. XlsxWriter **v1.4.3** (XlsxWriter is a Python module for creating Excel XLSX files) [Documentation Link](https://xlsxwriter.readthedocs.io/).
4. Pandas **v1.2.5** (Data Analysis Library) [Documentation Link](https://pandas.pydata.org/docs/).
5. Openpyxl **v3.0.7** (A Python library to read/write Excel 2010 xlsx/xlsm files) [Documentation Link](https://openpyxl.readthedocs.io/en/stable/).
6. Requests **v2.22.0** (HTTP Requests) [Documentation Link](https://docs.python-requests.org/en/master/).
7. ciscoaxl **v0.158** (Cisco CUCM AXL Library. Simple to use.) [Documentation Link](https://github.com/PresidioCode/ciscoaxl).
