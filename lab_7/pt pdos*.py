import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path_pt = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/Pt.d_pdos.dat"

# 데이터 로드
data_pt = np.loadtxt(file_path_pt, comments="#")

# Energy (column 1) 및 d 오비탈 PDOS (column 2)
E_pt = data_pt[:, 0]   # Pt 에너지 값 (eV)
d_DOS_pt = data_pt[:, 1]  # Pt d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy_pt = -0.3707  # Pt Fermi energy (eV)

# Fermi 레벨 기준으로 정렬
E_aligned_pt = E_pt - fermi_energy_pt

# 그래프 설정 (x축과 y축을 바꿔서)
plt.figure(figsize=(8, 6))
plt.plot(d_DOS_pt, E_aligned_pt, label="Pt d orbital PDOS", color="blue", linewidth=1.5)
plt.axhline(y=0, color='black', linestyle='--', label="Fermi level (E_F)")

# 라벨 및 타이틀 설정
plt.ylabel("Energy - E_F (eV)", fontsize=12)
plt.xlabel("PDOS (states/eV)", fontsize=12)
plt.title("PDOS (d orbital) - Pt", fontsize=14)
plt.legend()
plt.grid()

# 그래프 저장 및 표시
plt.savefig("Pt_Aligned_PDOS.png", dpi=300)
plt.show()