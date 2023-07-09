def multiply_and_save_results(file1_name, file2_name, result_file_name):
    with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2, open(result_file_name, 'w') as result_file:
        pairs = file1.readlines()
        names = file2.readlines()

        max_length = max(len(pairs), len(names))

        for i in range(max_length):
            pair = pairs[i % len(pairs)].strip()
            name = names[i % len(names)].strip()

            try:
                num1, num2 = map(float, pair.split('|'))
            except ValueError:
                continue

            product = num1 * num2

            if product < 0:
                result_file.write(f"{name.lower()}|{abs(product):.2f}\n")
            else:
                result_file.write(f"{name.upper()}|{round(product)}\n")

# # Пример использования
# file1_name = "random_pairs.txt"
# file2_name = "pseudonyms.txt"
# result_file_name = "results.txt"
# multiply_and_save_results(file1_name, file2_name, result_file_name)
