#!/usr/bin/env python3

import xml.etree.ElementTree  as ET
import argparse
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description='Merge JUnit XML files')
parser.add_argument('directory', metavar='<input directory>', help='Input Directory')
parser.add_argument('--output', required=True, help='Output File')

args = parser.parse_args()

path = Path(args.directory)

if not path.exists():
    print('directory path does not exist')
    sys.exit(1)

if not path.is_dir():
    print('directory path is not a directory')
    sys.exit(1)

output = Path(args.output)

if output.exists():
    print('output file already exists. will not overwrite')
    sys.exit(1)

mergedXML = ET.Element('testsuites')

for xml in path.glob('*.xml'):
    tree = ET.parse(xml)
    root = tree.getroot()
    for testsuite in root.iterfind('testsuite'):
        mergedXML.append(testsuite)

ET.ElementTree(mergedXML).write(output, encoding='utf-8', xml_declaration=True)
