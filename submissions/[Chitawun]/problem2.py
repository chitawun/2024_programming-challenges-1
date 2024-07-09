import string

def is_pangram(s):
    # แปลงสตริงเป็นตัวพิมพ์เล็กและลบอักขระที่ไม่ใช่ตัวอักษร
    s = ''.join(char.lower() for char in s if char.isalpha())
    # ตรวจสอบว่ามีตัวอักษรทุกตัวในภาษาอังกฤษหรือไม่
    return set(s) == set(string.ascii_lowercase)

def find_longest_word(s):
    # แยกคำและหาคำที่ยาวที่สุด
    words = s.split()
    return max(words, key=len) if words else ""

def pangram_longest_word(input_string):
    if is_pangram(input_string):
        longest_word = find_longest_word(input_string)
        return f"เป็น Pangram และคำที่ยาวที่สุดคือ: {longest_word}"
    else:
        return "ไม่เป็น Pangram"

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    test_strings = [
        "The quick brown fox jumps over the lazy dog",
        "Pack my box with five dozen liquor jugs",
        "This is not a pangram",
        "Waltz, nymph, for quick jigs vex Bud"
    ]

    for s in test_strings:
        print(f"สตริง: '{s}'")
        print(pangram_longest_word(s))
        print()
