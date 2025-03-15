### Task1. dictionary >>> trying to output two highest score among students.. 



students = {
    "Alice": 45,
    "Bob": 78,
    "Charlie": 52,
    "David": 33
}

for name, score in students.items():
    if score > 50: 
        print(name, score)