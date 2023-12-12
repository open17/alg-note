import random

def generate_test_case(n):
    operations = []
    nums = set()

    for _ in range(n):
        opt = random.randint(1, 6)
        if opt == 1:
            x = random.randint(-10**7, 10**7)
            nums.add(x)
            operations.append((opt, x))
        elif opt == 2:
            if nums:
                x = random.choice(list(nums))
                nums.remove(x)
                operations.append((opt, x))
        else:
            if opt == 3 or opt == 4:
                if nums:
                    x = random.randint(1, len(nums))
                    operations.append((opt, x))
                else:
                    continue
            else:
                x = random.randint(-10**7, 10**7)
                operations.append((opt, x))

    return operations

def write_test_case(file_path, test_case):
    with open(file_path, 'w') as file:
        file.write(str(len(test_case)) + '\n')
        for opt, x in test_case:
            file.write(str(opt) + ' ' + str(x) + '\n')

test_case = generate_test_case(random.randint(1, 10))
write_test_case('testcase.txt', test_case)