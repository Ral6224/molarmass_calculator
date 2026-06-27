"""
化学式相对质量计算器
输入化学式（如 H2SO4, CaCO3, NaOH），计算相对分子质量或相对原子质量。
"""

# 常用相对原子质量（中学化学常用值）
ATOMIC_MASS = {
    "H": 1,    "He": 4,   "Li": 7,    "Be": 9,    "B": 11,
    "C": 12,   "N": 14,   "O": 16,    "F": 19,    "Ne": 20,
    "Na": 23,  "Mg": 24,  "Al": 27,   "Si": 28,   "P": 31,
    "S": 32,   "Cl": 35.5,"Ar": 40,   "K": 39,    "Ca": 40,
    "Sc": 45,  "Ti": 48,  "V": 51,    "Cr": 52,   "Mn": 55,
    "Fe": 56,  "Co": 59,  "Ni": 59,   "Cu": 64,   "Zn": 65,
    "Ga": 70,  "Ge": 73,  "As": 75,   "Se": 79,   "Br": 80,
    "Kr": 84,  "Rb": 85.5,"Sr": 88,   "Y": 89,    "Zr": 91,
    "Nb": 93,  "Mo": 96,  "Tc": 98,   "Ru": 101,  "Rh": 103,
    "Pd": 106.4,"Ag": 108,"Cd": 112,  "In": 115,  "Sn": 119,
    "Sb": 122, "Te": 128, "I": 127,   "Xe": 131,  "Cs": 133,
    "Ba": 137, "La": 139, "Ce": 140,  "Pr": 141,  "Nd": 144,
    "Pm": 147, "Sm": 150, "Eu": 152,  "Gd": 157,  "Tb": 159,
    "Dy": 162.5,"Ho": 165,"Er": 167,  "Tm": 169,  "Yb": 173,
    "Lu": 175, "Hf": 178.5,"Ta": 181, "W": 184,   "Re": 186,
    "Os": 190, "Ir": 192, "Pt": 195,  "Au": 197,  "Hg": 201,
    "Tl": 204, "Pb": 207, "Bi": 209,  "Po": 210,  "At": 210,
    "Rn": 222, "Fr": 223, "Ra": 226,  "Ac": 227,  "Th": 232,
    "Pa": 231, "U": 238,  "Np": 237,  "Pu": 244,  "Am": 243,
}


def parse_formula(formula: str) -> list[tuple[str, int]]:
    """解析化学式，返回 [(元素符号, 原子数量), ...]"""
    result = []
    i = 0
    n = len(formula)
    while i < n:
        # 读取元素符号（大写字母开头，可选一个小写字母）
        if not formula[i].isupper():
            raise ValueError(f"第{i+1}位应为元素符号（大写字母开头）: '{formula[i]}'")

        elem = formula[i]
        i += 1
        while i < n and formula[i].islower():
            elem += formula[i]
            i += 1

        # 读取下标数字
        count_str = ""
        while i < n and formula[i].isdigit():
            count_str += formula[i]
            i += 1

        count = int(count_str) if count_str else 1
        result.append((elem, count))

    return result


def calc_mass(formula: str) -> float:
    """计算化学式的相对质量"""
    elements = parse_formula(formula)
    total = 0.0
    detail_parts = []

    for elem, count in elements:
        if elem not in ATOMIC_MASS:
            raise ValueError(f"未收录元素 '{elem}' 的原子量")
        mass = ATOMIC_MASS[elem]
        total += mass * count
        detail_parts.append(f"{elem}({mass})×{count}" if count > 1 else f"{elem}({mass})")

    # 单原子直接返回
    if len(elements) == 1 and elements[0][1] == 1:
        is_int = total == int(total)
        return total if not is_int else int(total)

    detail = " + ".join(detail_parts)
    print(f"  计算过程: {detail} = {total}")
    return total if total != int(total) else int(total)


def main():
    print("=" * 50)
    print("  化学式相对质量计算器")
    print("  支持元素: " + " ".join(ATOMIC_MASS.keys()))
    print("  示例: H2O, H2SO4, CaCO3, NaOH, NaCl")
    print("=" * 50)

    while True:
        try:
            formula = input("\n请输入化学式 (输入 q 退出): ").strip()
            if formula.lower() == "q":
                print("再见！")
                break
            if not formula:
                continue

            mass = calc_mass(formula)
            print(f"  {formula} 的相对质量 = {mass}")

        except ValueError as e:
            print(f"  错误: {e}")
        except Exception:
            print("  输入格式有误，请重试。")


if __name__ == "__main__":
    main()
