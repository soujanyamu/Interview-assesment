# Interview-assesment

Flow Log Parser

Flow Log Parser is a Python-based utility designed to process network flow logs, map them to predefined tags based on port-protocol combinations, and generate detailed reports.
This tool is useful for analyzing network traffic and obtaining insights into port usage and tag distribution.

Features

Tag Mapping: Maps destination ports and protocols to user-defined tags using a lookup table.

Log Analysis: Processes network flow logs in version 2 format to:

Count occurrences of port/protocol combinations.

Count tag occurrences based on lookup table mappings.

Report Generation: Outputs the results in a structured CSV file for further analysis.

Project Structure

FlowLogParser.py: The main script for processing logs and generating reports.

lookup.csv: The lookup table containing port, protocol, and tag mappings.

flow_logs.txt: Sample input file containing flow log data.

output.csv: The output file with analysis results.

Requirements
Python 3.6 or newer

Required Modules: collections, csv

Usage Instructions:

1. Prepare the Lookup Table (lookup.csv)
Ensure your lookup table includes the following columns: dstport,protocol,tag

Example: dstport,protocol,tag

80,tcp,HTTP
443,tcp,HTTPS
25,tcp,SMTP

2. Prepare the Flow Logs (flow_logs.txt)
   
      Each flow log entry should follow this format:
   
    2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK

   Note: Only logs with version 2 are processed.

 3. Run the Script

      Execute the script to process the logs and generate the output: python FlowLogParser.py

4.   View the Results

The script generates an output file (output.csv) containing two sections:

Tag Counts and Port/Protocol Counts

Example Workflow

Place lookup.csv and flow_logs.txt in the same directory as FlowLogParser.py.

Run the script: python FlowLogParser.py and Open output.csv to view the results.




