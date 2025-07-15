import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path = "/Users/seyeong/Desktop/lab7/pt.d_pdos.dat"

# 데이터 로드 (공백과 주석 처리 가능)
data = np.loadtxt(file_path, comments="#")

# 데이터 확인
print(f"Data shape: {data.shape}")
print(f"First 5 rows:\n{data[:5]}")

# Energy (column 1) 및 d 오비탈 PDOS (column 2)
E = data[:, 0]   # 에너지 값 (eV)
d_DOS = data[:, 1]  # d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy = -0.3707  # eV

# Fermi 레벨 기준으로 정렬
E_aligned = E - fermi_energy

# 그래프 설정
plt.figure(figsize=(8, 6))
plt.plot(E_aligned, d_DOS, label="d orbital PDOS", color="green", linewidth=1.5)
plt.axvline(x=0, color='black', linestyle='--', label="Fermi level (E_F)")

# 라벨 및 타이틀 설정
plt.xlabel("Energy - E_F (eV)", fontsize=12)
plt.ylabel("PDOS (states/eV)", fontsize=12)
plt.title("Fermi-Level Aligned PDOS (d orbital)", fontsize=14)
plt.legend()
plt.grid()

# 그래프 저장 및 표시
plt.savefig("Aligned_PDOS_d_orbital.png", dpi=300)
plt.show()
