def pair_product(numbers: list[int], target: int) -> tuple[int, int]:
    prev = {}
    result: tuple[int, int] = (-1, -1)

    for num_index, num in enumerate(numbers):
        complement = target/num
        if complement in prev:
            result = (prev[complement], num_index)
            break

        prev[num] = num_index

    return result
