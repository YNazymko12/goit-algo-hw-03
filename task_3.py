def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f'Move disk 1 from {source} to {target}')
        return
    hanoi(n-1, source, auxiliary, target)
    print(f'Move disk {n} from {source} to {target}')
    hanoi(n-1, auxiliary, target, source)

def main():
    try:
        n = int(input("Enter the number of disks for the Tower of Hanoi: "))
        hanoi(n, 'A', 'C', 'B')
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of disks.")

if __name__ == "__main__":
    main()