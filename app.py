def tambah(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input harus berupa angka")
    return a + b
