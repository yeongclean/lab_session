import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정
file_path_au = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/Aud_pdos.dat"

# 데이터 로드
data_au = np.loadtxt(file_path_au, comments="#")

# Energy (column 1) 및 d 오비탈 PDOS (column 2)
E_au = data_au[:, 0]   # Au 에너지 값 (eV)
d_DOS_au = data_au[:, 1]  # Au d 오비탈 PDOS 값

# Fermi Energy 설정
fermi_energy_au = -0.3568  # Au Fermi energy (eV)

# Fermi 레벨 기준으로 정렬
E_aligned_au = E_au - fermi_energy_au

# 그래프 설정 (x축과 y축을 바꿔서)
plt.figure(figsize=(8, 6))
plt.plot(d_DOS_au, E_aligned_au, label="Au d orbital PDOS", color="green", linewidth=1.5)
plt.axhline(y=0, color='black', linestyle='--', label="Fermi level (E_F)")

# 라벨 및 타이틀 설정
plt.ylabel("Energy - E_F (eV)", fontsize=12)
plt.xlabel("PDOS (states/eV)", fontsize=12)
plt.title("PDOS (d orbital) - Au", fontsize=14)
plt.legend()
plt.grid()

# 그래프 저장 및 표시
plt.savefig("Au_Aligned_PDOS.png", dpi=300)
plt.show()