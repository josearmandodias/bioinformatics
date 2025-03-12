def count_nucleotides():
  print("Small python program to count numbers of nucleotides in DNA sequence")
  print("If you want to exit, type 'q'\n")

  while True:
    #Getting DNA sequence from  user
    dna_sequence=input("Enter a DNA sequence (A, T, C, G):")

    if dna_sequence.lower() == "q":
      print("Exiting...")
      break
    
    #Converting given sequence to uppercase
    dna_sequence = dna_sequence.upper()

    #Checking if the given DNA sequence is valid
    valid_bases = set('ATCG')

    #Checking if given sequence contains only DNA valid letters
    if not set(dna_sequence).issubset(valid_bases):
      print("Invalid sequence. Please try again.")
      continue

    #Couting numbers of nucleotides in DNA sequence
    a_count=dna_sequence.count('A')
    t_count=dna_sequence.count('T')
    c_count=dna_sequence.count('C')
    g_count=dna_sequence.count('G')
        
    print(f"A count =  {a_count}\nT count = {t_count}\nC count = {c_count}\nG count = {g_count}")

if __name__ == "__main__":
    count_nucleotides()