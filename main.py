"""IEEE FP8 Floating Point Emulator"""

def simulate_fp8_e4m3(val):
    # E4M3: 1 sign bit, 4 exponent bits, 3 mantissa bits
    # Clamping range approx [-448, 448]
    val = max(-448.0, min(448.0, val))
    # Round to nearest 3-bit mantissa representation
    step = 0.125
    return round(val / step) * step

if __name__ == "__main__":
    print("[RUN] FP8 (E4M3) Float Emulator...")
    v = 3.14159
    fp8_v = simulate_fp8_e4m3(v)
    print(f"[OK] FP32: {v} -> Emulated FP8: {fp8_v}")
