import numpy as np

# 파일 로드 (예: "pt.d_pdos.dat" 파일)
file_path = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/Aud_pdos.dat"
data = np.loadtxt(file_path, comments="#")

energy = data[:, 0]  # 첫 번째 열: 에너지 (eV)
pdos = data[:, 1]    # 두 번째 열: d 오비탈 PDOS 값

# 페르미 에너지를 0 eV로 설정 (이전에 shift되었는지 확인)
fermi_level = 0.0

# Weighted Average 방식으로 d-band center 계산
numerator = np.sum(energy * pdos)
denominator = np.sum(pdos)

d_band_center = numerator / denominator

print(f"d-band center: {d_band_center:.3f} eV")
