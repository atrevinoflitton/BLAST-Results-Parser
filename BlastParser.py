"""
Program author name: Analia Treviño-Flitton
- This function opens and reads in a file with the results from a local BLASTx search. It parses the document for the
  Best Hit, the E-value, and  the Identities then saves them to a text document.
"""

def blast_parser(file):
    # Regex for query
    import re


    ## Open & Read
    with open(file, 'r') as f:
        blast_file = f.read()


    re_query = r"Query=\s(\w+)"
    query = re.findall(re_query, blast_file)

    # Regex for BestHit
    re_best = r"(>\w+.+\w+.+\s+\w+.+\w.+)"
    best = re.findall(re_best, blast_file)
    best_list = []

    # Trim over shoot
    for i in range(len(best)):
        list_item = re.sub(r"(\n\s+Length.+\d)", "", (best[i]))
        best_list.append(list_item)


    # Regex for E-val
    re_eval = r"(\d[e].\d+)"
    e_val = re.findall(re_eval, blast_file)
    # Only keep the 1st of 4 returned
    e_val = (e_val[0::4])


    # Regex for IDs
    re_id = r"Identities\s.\s(\d+.\d+\s.\d+..)"
    iden = re.findall(re_id, blast_file)


    # Write output file
    out_file = open("blastxParse_results.txt", 'w')
    out_file.write("Summary of Blastx Results\n\n")

    for i in (range(0, (len(query)))):
        formatting = query[i], "\tBest Hit: " + best_list[i], "\n\nE-Value: " + e_val[i], "\t\tIdentities: " + iden[i], "\n\n\n\n"
        for x in formatting:
            out_file.write(str(x))


    out_file.write("Written by Analia Treviño-Flitton\n\n")

    out_file.close()


x = "BlastResults.txt"
blast_parser(x)





def user_blast_parser():
    ## Regex for query
    import re


    ## User Input
    file_name = str(input("Please enter the name of the BLASTx results file you would like to parse:"))
    out_file_name = str(input("Please name the file you would like to save the results to including file extension "))


    ## Open & Read
    with open(file_name, 'r') as f:
        blast_file = f.read()


    re_query = r"Query=\s(\w+)"
    query = re.findall(re_query, blast_file)


    # Regex for BestHit (lowest E-val)
    re_best = r"(>\w+.+\w+.+\s+\w+.+\w.+)"
    best = re.findall(re_best, blast_file)
    best_list = []

    # Trim over shoot
    for i in range(len(best)):
        list_item = re.sub(r"(\n\s+Length.+\d)", "", (best[i]))
        best_list.append(list_item)


    # Regex for E-val
    re_eval = r"(\d[e].\d+)"
    e_val = re.findall(re_eval, blast_file)
    # Only keep the 1st of 4 returned
    e_val = (e_val[0::4])


    # Regex for IDs
    re_id = r"Identities\s.\s(\d+.\d+\s.\d+..)"
    iden = re.findall(re_id, blast_file)


    # Write output file
    out_file = open(out_file_name, 'w')
    out_file.write("Summary of Blastx Results\n\n")

    for i in (range(0, (len(query)))):
        formatting = query[i], "\tBest Hit: " + best_list[i], "\n\nE-Value: " + e_val[i], "\t\tIdentities: " + iden[i], "\n\n\n\n"
        for x in formatting:
            out_file.write(str(x))

    out_file.write("Written by Analia Treviño-Flitton\n\n")
    out_file.close()



user_blast_parser()
