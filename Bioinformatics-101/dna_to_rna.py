def dna_to_rna():
  print("Small python program to convert DNA sequence into RNA sequence")
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

    #Converting DNA to RNA
    rna_sequence = dna_sequence.replace('T','U')
        
    print(rna_sequence)

if __name__ == "__main__":
    dna_to_rna()