def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_sum_combinations(arr, target_sum):
    def backtrack(start, current_combination, current_sum):
        if is_prime(current_sum) and current_sum <= target_sum:
            result.append(current_combination[:])
        
        for i in range(start, len(arr)):
            if current_sum + arr[i] > target_sum:
                break
            current_combination.append(arr[i])
            backtrack(i + 1, current_combination, current_sum + arr[i])
            current_combination.pop()

    arr.sort()  # เรียงลำดับอาร์เรย์เพื่อเพิ่มประสิทธิภาพ
    result = []
    backtrack(0, [], 0)
    return result

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    arr = [2, 3, 5, 7, 11]
    target_sum = 15

    combinations = find_prime_sum_combinations(arr, target_sum)
    print(f"ค่าผสมที่มีผลรวมเป็นจำนวนเฉพาะ (ไม่เกิน {target_sum}):")
    for combo in combinations:
        print(f"{combo} (ผลรวม = {sum(combo)})")
