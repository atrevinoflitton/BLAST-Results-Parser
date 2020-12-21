# BLAST-Results-Parser
A program complete with a GUI to parse a BLASTx results file, ideal for report summaries. 
The GUI allows you to add addition comments to the parse results and save as a new file.

* Searches for the Best Hit, E-value and Identities

*Format assumes the results are from a local BLASTx search*

Two versions of the function:

* *blast_parser(file)*: The function is hard-coded with the file : "BlastResults.txt" 
and saves the results as: "blastxParse_results.txt"

* *user_blast_parser()*: Prompts the user for the file name and allows the user to name the output file


<dl>
  <dt> Required files for program </dt>
  
  <dd>

--- 
BlastParser.py
* Uses one function to open, read, parse, and write the output file
---

BlastResults.txt
* Test file with various Blast results
---
</dt>
