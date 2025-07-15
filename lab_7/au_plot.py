import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = "/Users/seyeong/Desktop/lab7/d_pdos.dat"

# 데이터 로드 (공백과 주석 처리 가능)
data = np.loadtxt(file_path, comments="#")

# 데이터 확인
print(f"Data shape: {data.shape}")
print(f"First 5 rows:\n{data[:5]}")

# Energy (column 1) 및 d 오비탈 PDOS (column 2)
E = data[:, 0]   # 원본 에너지 값 (eV)
d_DOS = data[:, 1]  # d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy = -0.3568  # eV

# 그래프 설정
plt.figure(figsize=(8, 6))
plt.plot(E, d_DOS, label="d orbital PDOS", color="green", linewidth=1.5)
plt.axvline(x=fermi_energy, color='black', linestyle='--', label="Fermi level")

# 라벨 및 타이틀 설정
plt.xlabel("Energy (eV)", fontsize=12)
plt.ylabel("PDOS (states/eV)", fontsize=12)
plt.title("PDOS (d orbital) without Fermi-Level Alignment", fontsize=14)
plt.legend()
plt.grid()

# 그래프 저장 및 표시
plt.savefig("PDOS_d_orbital_no_alignment.png", dpi=300)
plt.show()
